import os, tempfile, re
import gradio as gr
from rembg import remove
from PIL import Image, ImageColor

# CPU only
os.environ["ORT_PROVIDERS"] = "CPUExecutionProvider"

def normalize_color(c: str) -> str:
    """Convert 'rgba(r,g,b,a)' to '#rrggbb', or pass through hex."""
    c = c.strip()
    if c.startswith("rgba"):
        nums = [float(x) for x in re.findall(r"[\d\.]+", c)]
        r, g, b = map(int, nums[:3])
        return f"#{r:02x}{g:02x}{b:02x}"
    return c

def change_background_and_save(img: Image.Image, color: str):
    """Remove bg, composite over colored background, save PNG."""
    fg = remove(img).convert("RGBA")
    hexcol = normalize_color(color)
    rgb = ImageColor.getrgb(hexcol)
    bg = Image.new("RGBA", fg.size, rgb + (255,))
    out = Image.alpha_composite(bg, fg)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    out.save(tmp.name, "PNG")
    tmp.close()
    return out, tmp.name

css = """
h2, p { text-align:center; }
#controls-row { margin-top:1rem; margin-bottom:1rem; }
#swatch-red,#swatch-blue,#swatch-white {
  width:24px; height:24px; border:none; margin-right:8px; cursor:pointer;
}
#swatch-red { background:#DB1514; }
#swatch-blue{ background:#0090FF; }
#swatch-white{ background:#FFFFFF; border:1px solid #ccc; }
#change-btn { width:100%; }
.footer { text-align:center; margin-top:2rem; color:#666; font-size:0.9rem; }
.social-icons a { margin:0 .5rem; text-decoration:none; color:inherit; }
"""

with gr.Blocks(css=css, title="Change Background Color") as demo:
    gr.Markdown("## CHANGE BACKGROUND COLOR")
    gr.Markdown("Upload a photo, pick a background color, then download the result.")

    with gr.Row():
        inp = gr.Image(label="Upload Photo", type="pil")
        out = gr.Image(label="Result", interactive=False)

    with gr.Row(elem_id="controls-row"):
        with gr.Column(scale=1):
            gr.Markdown("**Default Colors**")
            red_btn   = gr.Button("", elem_id="swatch-red")
            blue_btn  = gr.Button("", elem_id="swatch-blue")
            white_btn = gr.Button("", elem_id="swatch-white")
        with gr.Column(scale=1):
            gr.Markdown("**Pick a Color**")
            picker = gr.ColorPicker(value="#DB1514")
        with gr.Column(scale=1):
            gr.Markdown("**Or enter hex**")
            manual = gr.Textbox(value="#DB1514", placeholder="#RRGGBB")

    change_btn   = gr.Button("✏️ Change Background", elem_id="change-btn", interactive=False)
    download_btn = gr.DownloadButton("⬇️ Download PNG", visible=True)

    # Enable the Change button once an image is uploaded
    inp.change(lambda _: gr.update(interactive=True), inp, change_btn)

    # swatches set the picker
    red_btn.click(lambda: "#DB1514", None, picker)
    blue_btn.click(lambda: "#0090FF", None, picker)
    white_btn.click(lambda: "#FFFFFF", None, picker)

    # manual textbox drives the picker too
    manual.change(lambda h: h or "#DB1514", manual, picker)

    # perform the work and hook up output & download
    change_btn.click(
        fn=change_background_and_save,
        inputs=[inp, picker],
        outputs=[out, download_btn],
    )

    gr.HTML("""
      <div class="footer">
        Made by Salman Alfarisi • 2025<br>
        <span class="social-icons">
          <a href="https://github.com/salmanalfarisi11" target="_blank">GitHub</a> |
          <a href="https://www.instagram.com/faris.salman111/" target="_blank">Instagram</a> |
          <a href="https://id.linkedin.com/in/salmanalfarisi11" target="_blank">LinkedIn</a>
        </span>
      </div>
    """)

if __name__ == "__main__":
    demo.launch()

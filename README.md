# 🖼️ Change Background Color App

A lightweight Gradio web app to remove the background of any image and replace it with a user-chosen solid color. Simply upload your photo, pick from default swatches, use the color picker or enter a HEX code, then download your finalized PNG.

[![Live Demo on Hugging Face](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-orange?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/salman555/Change-Background-Color)
![Visitor Count](https://profile-counter.glitch.me/salmanalfarisi11/count.svg)


---

## 📑 Table of Contents

1. [Features](#features)  
2. [Project Structure](#project-structure)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Running Locally](#running-locally)  
6. [Usage](#usage)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Author & Credits](#author--credits) 

---

## ✨ Features

- **Automatic Background Removal**  
  Leverages [rembg](https://github.com/danielgatis/rembg) under the hood to strip away backgrounds with a single click.

- **Multiple Color Selection Modes**  
  - **Default Swatches** (Red `#DB1514`, Blue `#0090FF`, White `#FFFFFF`)  
  - **Interactive Color Picker**  
  - **Manual HEX Input**

- **Live Preview**  
  See your original and transformed images side by side before downloading.

- **Instant Download**  
  Export your result as a transparent-background PNG that you can immediately drop into Word, PowerPoint, or any design tool.

<p align="center">
  <img src="assets/demo.png" alt="Demo Screenshot" width="600">
</p>

---

## 📁 Project Structure

```
background-editor/
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---


---

## ⚙️ Prerequisites

- Python 3.8 or higher  
- `git`  
- A terminal / command prompt  

---

## 🔧 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/salmanalfarisi11/Change-Background-Color-App.git
   cd remove-bg-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running Locally

Launch the app on your machine:
   ```bash
   python app.py
   ```
By default it will start on http://127.0.0.1:7860/. Open that URL in your browser to access the interface.

## 🎯 Usage

1. **Upload Photo** via the left panel.  
2. **Choose a Color**:  
   - Click a default swatch  
   - Use the color picker  
   - Or enter a HEX code manually  
3. Click **Change Background**  
4. Preview your result on the right  
5. Click **Download PNG** to save  


## 🤝 Contributing
Contributions, bug reports and feature requests are welcome!

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🖋️ Author & Credits

Developed by **[Salman Alfarisi](https://github.com/salmanalfarisi11)** © 2025  
- GitHub: [salmanalfarisi11](https://github.com/salmanalfarisi11)  
- LinkedIn: [salmanalfarisi11](https://linkedin.com/in/salmanalfarisi11)  
- Instagram: [faris.salman111](https://instagram.com/faris.salman111)  

Built with ❤️ and Gradio
Feel free to ⭐ the repo and share feedback!


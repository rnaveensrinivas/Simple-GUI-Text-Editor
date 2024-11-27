# Notepad Application

A simple **Notepad-like application** built with **PyQt5** that allows users to create, edit, save, and open text files. 
## Features

- **Open Files**: Open `.txt` and `.py` files directly into the editor.
- **Save Files**: Save the current text to a specified file location.
- **Font Size Adjustment**: Change the font size to 12pt, 18pt, or 24pt using menu options.
- **Close Confirmation**: Prompts the user to save their work before exiting the application.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## Prerequisites

Ensure you have Python installed on your system. You will also need the PyQt5 library and Qt Designer.

### Install PyQt5
```bash
pip install PyQt5
```
### Install Qt Designer 
You can install it from this [link]([url](https://build-system.fman.io/qt-designer-download)).
Note: Qt Designer is not needed for running the application. It is for modifying the UI.

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/notepad-pyqt5.git
   cd notepad-pyqt5
   ```
2. Run the application:
   ```bash
   python notepad.py
   ```

---

## File Structure

```
.
├── editor.ui        # User interface file created using Qt Designer
├── notepad.py       # Main Python script containing the application code
└── README.md        # Project documentation
```

---

## Usage

1. **Open Files**:
   - Click `File -> Open` in the menu bar.
   - Choose a `.txt` or `.py` file to open.

2. **Save Files**:
   - Click `File -> Save` in the menu bar.
   - Specify the file name and location to save the file.

3. **Adjust Font Size**:
   - Use the menu options under `Font Size` to switch between `12pt`, `18pt`, and `24pt`.

4. **Exit**:
   - When closing the application, a confirmation dialog will appear asking if you'd like to save your work.

---

## Screenshots

![image](https://github.com/user-attachments/assets/b6faab4b-f46b-42ca-909d-0a72ff8ed164)

---

## Acknowledgements

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Qt Designer](https://www.qt.io/qt-features-libraries-apis-tools-and-ide)
- [Tutorial using which I created this project](https://www.youtube.com/watch?v=mFdGV8C9o1k)

---

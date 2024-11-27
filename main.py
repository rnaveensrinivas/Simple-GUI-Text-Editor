from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton, QApplication, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import uic 

'''
QMainWindow: The main window class that supports menus, toolbars, and status bars.
QFileDialog: Provides dialog boxes for file operations like opening or saving files.
QPushButton: Represents a clickable button widget.
QApplication: Manages the GUI application's control flow and main settings.
QMessageBox: Used to display dialog boxes for user interaction, such as confirmations.
QFont: Allows for font customization (e.g., family, size).
uic: User Interface Compiler - Enables loading of .ui files created in Qt Designer.
'''

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.setWindowTitle("Notepad")

        '''
        <addaction name="action12pt"/>
        <addaction name="action18pt"/>
        <addaction name="action24pt"/>
        When the above are triggered we connect it with change_size method
        ?? Why are we passing lambda function to connect?
        '''
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))

        '''
        <addaction name="actionOpen"/>
        <addaction name="actionSave"/>
        '''
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

        self.show()

    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Consolas", size))

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py)", options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);; All Files (*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event):
        if self.plainTextEdit.toPlainText() != "":
            # only if there is some content within the note, we ping the user before closing
            dialog = QMessageBox()
            dialog.setText("Do you want save your work?")
            dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole) # 0
            dialog.addButton(QPushButton("No"), QMessageBox.NoRole) # 1
            dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole) # 2

            answer = dialog.exec_()

            if answer == 0:
                self.save_file()
                event.accept()
            elif answer == 2:
                event.ignore()

def main():
    app = QApplication([])
    MyGUI()
    app.exec_() # starts the application's event loop, hence GUI remains responsive

if __name__ == '__main__':
    main()
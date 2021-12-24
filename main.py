from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pdfplumber

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PDF Text Dumper'
        self.width = 500
        self.height = 105
        self.sourceFileDir = ''
        self.destFolderDir = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        # fixed size
        self.setFixedHeight(self.height)
        self.setFixedWidth(self.width)

        # UI Components #
        # select source file - label
        self.label_srcfile = QLabel('Selected Source File:', self)
        self.label_srcfile.move(5, 5)

        # select source file diaglog box - button
        self.selectFileButton = QPushButton(self)
        self.selectFileButton.setText('Select File')
        self.selectFileButton.move(5, 25)
        self.selectFileButton.clicked.connect(self.selectPDF_clicked)
             
        # select outfile location - label
        self.label_outfile = QLabel('Selected Output Folder:', self)
        self.label_outfile.move(5, 55)

        # select source file diaglog box - button
        self.selectFileButton = QPushButton(self)
        self.selectFileButton.setText('Select Output Folder')
        self.selectFileButton.move(5, 75)
        self.selectFileButton.clicked.connect(self.selectOutput_clicked)

        # extract text - button
        self.extractButton = QPushButton(self)
        self.extractButton.setText('Extract Text')
        self.extractButton.move(415, 75)
        self.extractButton.clicked.connect(self.extractButton_clicked)

        self.show()

    def TextExtractedUI(self):
        message = QMessageBox()
        message.setWindowTitle('Text Extracted')
        message.setText('Text has been extracted to output_text.txt')
        message.exec_()

    def selectPDF_clicked(self, arg2):
        self.sourceFileDir = QFileDialog.getOpenFileName(self, 'Select PDF File', '/home/', 'PDF Files (*.pdf)')
        self.label_srcfile.setText(f'Selected File: {self.sourceFileDir[0]}')
        self.label_srcfile.adjustSize()

    def selectOutput_clicked(self, arg2):
        self.destFolderDir = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.label_outfile.setText(f'Output Directory: {self.destFolderDir}')
        self.label_outfile.adjustSize()

    def extractButton_clicked(self, arg2):
        # make sure file and output directory are selected
        if self.sourceFileDir == '':
            raise NotImplementedError('FILE NOT SELECTED')
        if self.destFolderDir == '':
            raise NotImplementedError('OUTPUT FOLDER NOT SELECTED')


        with pdfplumber.open(self.sourceFileDir[0]) as pdf:
            outFile = open(f'{self.destFolderDir}/output_text.txt', 'w+')
            for page in pdf.pages:
                outFile.write(page.extract_text())
            outFile.close()

        self.TextExtractedUI()
        

if __name__ == '__main__':
    # execute the program
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

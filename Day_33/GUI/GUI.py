# PyQt5 intrdoduction           #   (python -m pip install PyQt5)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)                                    #(x, y, width, height)
        self.setWindowIcon(QIcon("Day_33/GUI/pic.jpg"))


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()        PyQt5.QtWidgets
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()






# *********************************************************

# PyQt5 QLabels


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: blue")
        label.setStyleSheet("color : #f0a351; "
                            "background-color: #00a7e7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline")
        
        # label.setAlignment(Qt.AlignTop)       #VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom)       #VERTICALLY Bottom
        # label.setAlignment(Qt.AlignVCenter)       #VERTICALLY Center
        
        # label.setAlignment(Qt.AlignRight)       # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter)       # HORIZONTALLY Center
        # label.setAlignment(Qt.AlignLeft)       # HORIZONTALLY Left

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)       # Center & Top
        # label.setAlignment(Qt.AlignHCenter  |  Qt.AlignBottom)     # center & bottom
        # label.setAlignment(Qt.AlignHCenter   | Qt.AlignVCenter)   # center & Center

        label.setAlignment(Qt.AlignCenter)          # CENTER


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()


# *********************************************************

# PyQt5 Images


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)


        label = QLabel(self)
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("Day_33/GUI/pic.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                           (self.height() - label.height()) // 2, 
                           label.width(), 
                           label.height())


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()



# *********************************************************


# PyQt5 Layouts


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: pink;")

        # vbox = QVBoxLayout()
        
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # central_widget.setLayout(vbox)


        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)

        # central_widget.setLayout(hbox)


        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 2)

        central_widget.setLayout(grid)


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()





# *********************************************************



# PyQt5 buttons


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px,")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")


    def on_click(self):
        # print("Button Clicked!")
        # self.button.setText("Clicked!")
        # self.button.setDisabled(True)

        self.label.setText("Goodbye")


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()



# ***********************************************************************************


# PyQt5 buttons


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(0 , 0, 500, 100 )
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        # if state == 2:
        if state == Qt.Checked:
            print("you like food")
        else:
            print("you DO NOT like food")

        # print(state)
        # print("You like food")

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()



# *******************************************************************************************


# PyQt5 radio buttons


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-store", self)
        self.radio5 = QRadioButton("Online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        # print("You selected something")
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()



# **************************************************************************************

# PyQt5 LineEdit

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial")
        
        self.line_edit.setPlaceholderText("Enter your name")

        self.button.clicked.connect(self.submit)

    
    def submit(self):
        # print("You clicked the button")
        text = self.line_edit.text()
        print(f"Hello {text}")


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()




# ********************************************************

#  PyQt5 setStyleSheet()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: red;
                background-color: #ff4747;
            }
            QPushButton#button2{
                background-color: green;
            }
            QPushButton#button3{
                background-color: blue;
            }
                           
            QPushButton#button1:hover{
                background-color: pink;
            }
            QPushButton#button2:hover{
                background-color: yellow;
            }
            QPushButton#button3:hover{
                background-color: orange;
            }
            
        """)

       
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
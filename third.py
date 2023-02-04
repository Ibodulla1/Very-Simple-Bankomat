from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QListWidget, QMainWindow, QLineEdit, QMessageBox, QInputDialog



class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.Main_Widget = QWidget()
        self.msg = QMessageBox()


        
        self.lst = ["Kit-Kat", "Metro", "Mars", "Bautin", "Twix"]

        self.Dict_lists = {
            "Kit-Kat":5,
            "Metro" : 10,
            "Mars" : 3,
            "Bautin":4,
            "Twix":3,
        }



        self.QList_W = QListWidget()
        self.QList_W.addItems(self.lst)

        self.Enter = QLineEdit()
        self.Enter.setStyleSheet("background-color:black;color:white")
        self.Enter.setPlaceholderText("Enter the Number...")




        self.Start_BTN = QPushButton("BUY")
        self.Start_BTN.clicked.connect(self.buy)
        self.Add_BTN = QPushButton("ADD")
        self.Add_BTN.clicked.connect(self.add)
        

        self.v_lay = QVBoxLayout()

        self.v_lay.addWidget(self.QList_W)
        self.v_lay.addStretch()
        self.v_lay.addWidget(self.Enter)
        self.v_lay.addStretch()
        self.v_lay.addWidget(self.Start_BTN)
        self.v_lay.addWidget(self.Add_BTN)

        self.setLayout(self.v_lay)


    def buy(self)->None:
       if self.Enter.text().isdigit():
        index = self.QList_W.currentRow()
        product = self.lst[index]
        product = product.split()[0]

        if self.Dict_lists[product] == 0:
            self.QList_W.takeItem(index)





        if self.Dict_lists[product] >= int(self.Enter.text()):
            self.Dict_lists[product] -= int(self.Enter.text())

            if self.Dict_lists[product] == 0:
                self.QList_W.takeItem(index)

            self.msg.setText(f"You Buy {product}\n\nWe have {self.Dict_lists[product]} of {product} left")   
            self.msg.show()
            self.msg.exec_()
            self.Enter.clear()



        elif self.Dict_lists[product] < int(self.Enter.text()): 
            self.msg.setText(f"We have {self.Dict_lists[product]} of {product} left")   
            self.msg.show()
            self.msg.exec_()
            self.Enter.clear()





       elif not self.Enter.text().isdigit():
        self.Enter.setPlaceholderText("You did not enter a number")
        self.Enter.setStyleSheet("background-color:black ; color:red; ")



    def add(self):

        text, ok = QInputDialog.getText(self,"Add New Product","e.g(product name number)")

        if text and ok is not None:

            text = text.split()
            num = text[1]
            text = text[0]
            self.Dict_lists[text] = int(num)

            if text not in self.lst:
                self.lst.append(text)
                self.QList_W.clear()
                self.QList_W.addItems(self.lst)





if __name__ == "__main__":
    app = QApplication([])
    Main_Window = Main()
    Main_Window.show()
    Main_Window.setWindowTitle("Bankomat")
    Main_Window.setGeometry(700,300,300,300)
    app.exec_()

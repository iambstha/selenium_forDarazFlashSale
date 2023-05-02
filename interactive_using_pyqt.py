from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daraz Flash Sale Searcher")
        self.setGeometry(100, 100, 400, 200)

        # Create a label for the search box
        self.search_label = QLabel("Search item in Daraz Flash Sale: ")

        # Create a search box for entering the item name
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Enter the item name")
        self.search_box.returnPressed.connect(self.findComponents)

        # Create a search button to start the search
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.findComponents)

        # Add the search label, search box and search button to a horizontal layout
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_box)
        search_layout.addWidget(self.search_button)

        # Create a label to display the search results
        self.result_label = QLabel("Search results:")
        self.result_label.setAlignment(Qt.AlignCenter)

        # Add the result label to a vertical layout
        result_layout = QVBoxLayout()
        result_layout.addWidget(self.result_label)

        # Add the search and result layouts to a vertical layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addLayout(result_layout)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Set up the Selenium web driver
        opt = Options()
        # opt.add_argument('headless')
        opt.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.daraz.com.np/")

    def findComponents(self):
        item = self.search_box.text()

        try:
            # Find and click the link to the flash sale
            text_box = self.driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[3]/div[2]/div[1]/a")
            text_box.click()

            # Find all the sale titles in the flash sale and check if the item is in any of them
            flash_element = self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]")
            sale_element = flash_element.find_elements(by=By.CLASS_NAME, value="sale-title")

            # Create a list to store the matching sale titles
            matching_sales = []

            for sale in sale_element:
                if item in sale.text:
                    matching_sales.append(sale.text)

            # Update the result label with the matching sale titles
            if matching_sales:
                self.result_label.setText("Search results: \n\n" + "\n\n".join(matching_sales))
            else:
                self.result_label.setText("No matching sale titles found.")
        except:
            QMessageBox.critical(self, "Error", "An error occurred while searching for the item.")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

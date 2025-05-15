import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from login1 import Ui_UI_Login
from signup import Ui_Signup
from Manager_window import Ui_MainWindow
from Type_window import Ui_Type
from home import Ui_Home
from PyQt5.QtGui import QIcon
from Database import cls_login


class MainWindow:
    def __init__(self):
        # Khởi tạo đối tượng cls_login để tương tác với database
        self.db = cls_login()
        self.solannhapsai = 0
        self.original_id = None
        self.current_image_path = None

        # Khởi tạo cửa sổ đăng nhập (Login)
        self.main_win = QMainWindow()
        self.uic = Ui_UI_Login()
        self.uic.setupUi(self.main_win)
        self.uic.cb_show.stateChanged.connect(self.showhide_pw)
        self.uic.pb_login.clicked.connect(self.dangnhap)
        self.uic.lb_to_signup.linkActivated.connect(self.open_signup)
        self.uic.exit.clicked.connect(self.close_application)

        # Khởi tạo cửa sổ đăng ký (Signup)
        self.signup_win = QMainWindow()
        self.signup_uic = Ui_Signup()
        self.signup_uic.setupUi(self.signup_win)
        self.signup_uic.pb_signup.clicked.connect(self.dangky)
        self.signup_uic.lk_login.linkActivated.connect(self.open_login)
        self.signup_uic.cb_show_2.stateChanged.connect(self.showhide_pw_signup)
        self.signup_uic.exit.clicked.connect(self.close_application)

        # Khởi tạo cửa sổ trang chủ (Home)
        self.home_win = QMainWindow()
        self.home_uic = Ui_Home()
        self.home_uic.setupUi(self.home_win)
        self.home_uic.manager.clicked.connect(self.enter_manager)
        self.home_uic.btn_logout_home.clicked.connect(self.back_to_login)
        self.home_uic.btn_.clicked.connect(self.close_application)
        self.home_uic.contact.clicked.connect(self.contact)

        # Khởi tạo cửa sổ quản lý CPU (Manager)
        self.manager_win = QMainWindow()
        self.manager_uic = Ui_MainWindow()
        self.manager_uic.setupUi(self.manager_win)
        self.manager_uic.pb_add.clicked.connect(self.add_cpu)
        self.manager_uic.pb_modi.clicked.connect(self.modify_cpu)
        self.manager_uic.pb_delete.clicked.connect(self.delete_cpu)
        self.manager_uic.pb_cancel.clicked.connect(self.clear_inputs)
        self.manager_uic.pb_findcompa.clicked.connect(self.search_cpu)
        self.manager_uic.pb_picture.clicked.connect(self.select_picture)
        self.manager_uic.btn_logout.clicked.connect(self.logout)
        self.manager_uic.btn_logout_2.clicked.connect(self.close_application)
        self.manager_uic.table.selectionModel().selectionChanged.connect(self.on_selection_change)
        self.manager_uic.btn_type.clicked.connect(self.open_type_window)
        self.manager_uic.pb_home.clicked.connect(self.back_to_home)
        self.manager_uic.cb_compa.currentIndexChanged.connect(self.update_processor_list)
        self.manager_uic.cb_sort.currentIndexChanged.connect(self.sort_data)

        # Khởi tạo cửa sổ quản lý loại CPU (Type)
        self.type_win = QMainWindow()
        self.type_uic = Ui_Type()
        self.type_uic.setupUi(self.type_win)
        self.type_uic.pb_addprocess.clicked.connect(self.add_processor)
        self.type_uic.pb_change_processor.clicked.connect(self.update_processor)
        self.type_uic.pb_deleteprocess.clicked.connect(self.delete_processor)
        self.type_uic.pb_cancel_processor.clicked.connect(self.clear_processor_inputs)
        self.type_uic.pb_exit_pro.clicked.connect(self.close_application)
        self.type_uic.pb_back_to_Manager.clicked.connect(self.back_to_manager)
        self.type_uic.table_processor.selectionModel().selectionChanged.connect(self.on_process_selection_change)
        self.load_combo_boxes()  # Tải dữ liệu cho combobox khi khởi tạo

    # Login
    def show(self):
        self.main_win.show()

    def dangnhap(self):
        UN = self.uic.le_us.text().strip()
        PW = self.uic.le_pw.text().strip()
        if not UN or not PW:
            QMessageBox.warning(self.main_win, "Error", "Please enter full username and password! ")
            return False
        rs = self.db.check(UN, PW)

        if len(rs) > 0:
            QMessageBox.information(self.main_win, "Success", "Login successful!")
            self.main_win.hide()
            self.home_win.show()
            self.load_data()
            return True
        else:
            self.solannhapsai += 1
            solanconlai = 3 - self.solannhapsai
            QMessageBox.warning(self.main_win, "Error",
                                f"Incorrect username or password!\nYou have {solanconlai} attempt left")

        if self.solannhapsai == 3:
            QMessageBox.warning(self.main_win, "Locked", "You are banned")
            self.uic.pb_login.setEnabled(False)
            return False

    def showhide_pw(self, a):
        if a == QtCore.Qt.CheckState.Checked:
            self.uic.le_pw.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.uic.le_pw.setEchoMode(QtWidgets.QLineEdit.Password)

    # Signup
    def open_signup(self):
        self.main_win.hide()
        self.signup_win.show()

    def dangky(self):
        nus = self.signup_uic.le_nus_2.text()
        npw = self.signup_uic.le_npw_2.text()
        if not nus or not npw:
            QMessageBox.warning(self.signup_win, "Error", "Please enter username and password!")
            return
        if self.db.insert(nus, npw):
            QMessageBox.information(self.signup_win, "Success", "Register successful!")
            self.signup_win.hide()
            self.main_win.show()
        else:
            QMessageBox.warning(self.signup_win, "Error", "Username already exist !")

    def showhide_pw_signup(self, a):
        if a == QtCore.Qt.CheckState.Checked:
            self.signup_uic.le_npw_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.signup_uic.le_npw_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def open_login(self):
        self.signup_win.hide()
        self.main_win.show()

    # home
    def enter_manager(self):
        self.home_win.hide()
        self.manager_win.show()
        self.clear_inputs()

    def back_to_login(self):
        self.home_win.hide()
        self.main_win.show()
        self.clear_inputs()

    def contact(self):
        QMessageBox.information(self.home_win, "Contact",
                                "Author: Tran Tien Anh\nMss: 0023411112\nPhone: 0815883548 \n ")

    # Manager
    def load_combo_boxes(self):
        self.manager_uic.cb_compa.clear()
        self.manager_uic.cb_compa.addItem("Not selected")
        self.manager_uic.cb_compa.addItem(QIcon("image/intel.png"), "Intel")
        self.manager_uic.cb_compa.addItem(QIcon("image/amd.png"), "Amd")

        self.manager_uic.cb_process.clear()
        self.manager_uic.cb_process.addItem("Not selected")
        self.update_processor_list()

    def update_processor_list(self):
        self.manager_uic.cb_process.clear()
        self.manager_uic.cb_process.addItem("Not selected")

        company = self.manager_uic.cb_compa.currentText()
        processors = self.db.fetch_processors()
        if company == "Not selected":
            for processor in processors:
                self.manager_uic.cb_process.addItem(processor[1])  # Use Name_Processors
        else:
            company_low = company.lower()
            for processor in processors:
                processor_name = processor[1]
                processor_name_lower = processor_name.lower()
                if company_low == "amd" and "ryzen" in processor_name_lower:
                    self.manager_uic.cb_process.addItem(processor_name)
                elif company_low == "intel" and "core" in processor_name_lower:
                    self.manager_uic.cb_process.addItem(processor_name)

    def set_default_image(self):
        self.manager_uic.label_4.setPixmap(QtGui.QPixmap(":/hinh/image/image (1).png"))
        self.manager_uic.label_4.setScaledContents(True)

    def select_picture(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self.manager_win, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_name:
            pixmap = QtGui.QPixmap(file_name)
            self.current_image_path = file_name
            self.manager_uic.lineEdit.setText(file_name)
            self.manager_uic.label_4.setPixmap(pixmap)
            self.manager_uic.label_4.setScaledContents(True)
        else:
            self.current_image_path = None
            self.manager_uic.lineEdit.clear()
            self.set_default_image()

    def is_valid_number(self, value):
        try:
            number = float(value)
            return number >= 0
        except ValueError:
            return False

    def format_price(self, price):
        try:
            return "{:,.0f}".format(float(price)).replace(",", ".")
        except (ValueError, TypeError):
            return str(price)

    def load_data(self):
        try:
            rows = self.db.fetch_all()
            self.manager_uic.table.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                for col_idx, data in enumerate(row_data):
                    if col_idx == 2:  # Cột giá
                        self.manager_uic.table.setItem(row_idx, col_idx, QTableWidgetItem(self.format_price(data)))
                    else:
                        self.manager_uic.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.critical(self.manager_win, "Error", f"Failed to load data: {str(e)}")

    def add_cpu(self):
        id = self.manager_uic.le_id.text().strip()
        name = self.manager_uic.le_name.text().strip()
        price = self.manager_uic.le_price.text().strip()
        company = self.manager_uic.cb_compa.currentText()
        processor = self.manager_uic.cb_process.currentText()
        status = "Full Box" if self.manager_uic.rd_full.isChecked() else "No Box"


        if not id or not name or not price or company == "Not selected" or processor == "Not selected":
            QMessageBox.warning(self.manager_win, "Warning", "Please fill in all field!")
            return

        cleaned_price = price.replace(".", "")
        if not self.is_valid_number(cleaned_price):
            QMessageBox.warning(self.manager_win, "Error", "Price must be a valid number (111222 or 111.222)!")
            return
        float_price = float(cleaned_price)
        formatted_price = self.format_price(float_price)
        self.manager_uic.le_price.setText(formatted_price)

        image_data = None
        if self.current_image_path:
            import os
            if not os.path.isfile(self.current_image_path):
                QMessageBox.warning(self.manager_win, "Error", "Selected image file does not exist!")
                return
            max_size = 10 * 1024 * 1024
            if os.path.getsize(self.current_image_path) > max_size:
                QMessageBox.warning(self.manager_win, "Error", "Image size exceed 10MB!")
                return
            with open(self.current_image_path, "rb") as file:
                image_data = file.read()
        else:
            reply = QMessageBox.question(
                self.manager_win,
                "No Image Selected",
                "You haven't selected an image. Do you want to continue without image?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if reply == QMessageBox.No:
                return

        try:
            if self.db.add_cpu(id, name, float_price, company, processor, status, image_data):
                QMessageBox.information(self.manager_win, "Success", "CPU added successfully!")
                self.load_data()
                self.clear_inputs()
            else:
                QMessageBox.warning(self.manager_win, "Error", "CPU with this ID already exists!")
        except Exception as e:
            QMessageBox.critical(self.manager_win, "Error", f"Failed to add CPU: {str(e)}")

    def modify_cpu(self):
        selected_row = self.manager_uic.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.manager_win, "Warning", "Please select a CPU to modify!")
            return

        if not self.original_id:
            QMessageBox.warning(self.manager_win, "Error", "Original ID not set. Please select a CPU again!")
            return

        ID = self.manager_uic.le_id.text().strip()
        name = self.manager_uic.le_name.text().strip()
        price = self.manager_uic.le_price.text().strip()
        company = self.manager_uic.cb_compa.currentText()
        processor = self.manager_uic.cb_process.currentText()
        status = "Full Box" if self.manager_uic.rd_full.isChecked() else "No Box"


        if not ID or not name or not price or company == "Not selected" or processor == "Not selected":
            QMessageBox.warning(self.manager_win, "Warning", "Please fill in all fields, including ID!")
            return

        cleaned_price = price.replace(".", "")
        if not self.is_valid_number(cleaned_price):
            QMessageBox.warning(self.manager_win, "Error", "Price must be a valid number (e.g., 111222 or 111.222)!")
            return
        float_price = float(cleaned_price)
        formatted_price = self.format_price(float_price)
        self.manager_uic.le_price.setText(formatted_price)

        image_data = None
        if self.current_image_path:
            import os
            if not os.path.isfile(self.current_image_path):
                QMessageBox.warning(self.manager_win, "Error", "Selected image file does not exist!")
                return
            max_size = 10 * 1024 * 1024
            if os.path.getsize(self.current_image_path) > max_size:
                QMessageBox.warning(self.manager_win, "Error", "Image size exceeds 10MB!")
                return
            with open(self.current_image_path, "rb") as file:
                image_data = file.read()
        else:
            image_data = self.db.get_image(self.original_id)

        try:
            self.db.update_cpu(self.original_id, ID, name, float_price, company, processor, status, image_data)
            QMessageBox.information(self.manager_win, "Success", "CPU updated successfully!")
            self.load_data()
            self.clear_inputs()
        except Exception as e:
            QMessageBox.critical(self.manager_win, "Error", f"Failed to update CPU: {str(e)}")

    def delete_cpu(self):
        """Hàm xóa CPU"""
        selected_row = self.manager_uic.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.manager_win, "Warning", "Please select a CPU to delete!")
            return

        id = self.manager_uic.table.item(selected_row, 0).text()
        name = self.manager_uic.table.item(selected_row, 1).text()
        reply = QMessageBox.question(self.manager_win, "Confirm Delete",
                                     f"Are you sure you want to delete CPU with ID {id} and Name {name}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                self.db.delete_cpu(id)
                QMessageBox.information(self.manager_win, "Success", "CPU deleted successfully!")
                self.load_data()
                self.clear_inputs()
            except Exception as e:
                QMessageBox.critical(self.manager_win, "Error", f"Failed to delete CPU: {str(e)}")

    def search_cpu(self):
        """Hàm tìm kiếm CPU"""
        ID = self.manager_uic.le_id.text().strip() or None
        name = self.manager_uic.le_name.text().strip() or None
        company = self.manager_uic.cb_compa.currentText()
        processor = self.manager_uic.cb_process.currentText()

        if not ID and not name and company == "Not selected" and processor == "Not selected":
            QMessageBox.warning(self.manager_win, "Warning",
                                "Please enter at least one search condition (ID, Name, Company, or Processor)!")
            return

        try:
            rows = self.db.search_cpu(ID, name, company, processor)
            if not rows:
                QMessageBox.information(self.manager_win, "No Results", "No CPU found !")
                self.manager_uic.table.setRowCount(0)
                return

            self.manager_uic.table.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                for col_idx, data in enumerate(row_data):
                    if col_idx == 2:  # Cột giá
                        self.manager_uic.table.setItem(row_idx, col_idx, QTableWidgetItem(self.format_price(data)))
                    else:
                        self.manager_uic.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.critical(self.manager_win, "Error", f"Failed to search CPUs: {str(e)}")

    def sort_data(self):
        """Hàm sắp xếp dữ liệu CPU"""
        sort_option = self.manager_uic.cb_sort.currentText()

        if sort_option == "No Sort":
            self.load_data()
            return
        elif sort_option == "Sort by ID":
            sort_column = "ID"  # Sửa thành tên cột chính xác trong bảng
        elif sort_option == "Sort by Name":
            sort_column = "Name"  # Sửa thành tên cột chính xác trong bảng
        elif sort_option == "Sort by Price":
            sort_column = "Price"  # Sửa thành tên cột chính xác trong bảng
        else:
            return

        try:
            rows = self.db.sort_cpu(sort_column)
            if not rows:
                QMessageBox.information(self.manager_win, "No Results", "No CPUs found!")
                self.manager_uic.table.setRowCount(0)
                return

            self.manager_uic.table.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                for col_idx, data in enumerate(row_data):
                    if col_idx == 2:  # Cột giá
                        self.manager_uic.table.setItem(row_idx, col_idx, QTableWidgetItem(self.format_price(data)))
                    else:
                        self.manager_uic.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.critical(self.manager_win, "Error", f"Failed to sort CPUs: {str(e)}")

    def on_selection_change(self):
        selected_row = self.manager_uic.table.currentRow()
        if selected_row >= 0:
            id = self.manager_uic.table.item(selected_row, 0).text()
            name = self.manager_uic.table.item(selected_row, 1).text()
            price = self.manager_uic.table.item(selected_row, 2).text()
            company = self.manager_uic.table.item(selected_row, 3).text()
            processor = self.manager_uic.table.item(selected_row, 4).text()
            status = self.manager_uic.table.item(selected_row, 5).text()


            self.original_id = id
            self.manager_uic.le_id.setText(id)
            self.manager_uic.le_name.setText(name)
            self.manager_uic.le_price.setText(price)
            self.manager_uic.cb_compa.setCurrentText(company)
            self.manager_uic.cb_process.setCurrentText(processor)

            if status == "Full Box":
                self.manager_uic.rd_full.setChecked(True)
                self.manager_uic.rd_no.setChecked(False)
            elif status == "No Box":
                self.manager_uic.rd_full.setChecked(False)
                self.manager_uic.rd_no.setChecked(True)
            else:

                self.manager_uic.rd_full.setChecked(True)  # Giá trị mặc định nếu Status không hợp lệ
                self.manager_uic.rd_no.setChecked(False)

            image_data = self.db.get_image(id)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image_data) if image_data else self.set_default_image()
            self.manager_uic.label_4.setPixmap(pixmap)
            self.manager_uic.label_4.setScaledContents(True)
            self.manager_uic.lineEdit.setText("Image loaded from database" if image_data else "")
            self.current_image_path = None

    def clear_inputs(self):
        """Hàm xóa dữ liệu nhập trên giao diện quản lý"""
        self.manager_uic.le_id.clear()
        self.manager_uic.le_name.clear()
        self.manager_uic.le_price.clear()
        self.manager_uic.cb_compa.setCurrentIndex(0)
        self.manager_uic.cb_process.setCurrentIndex(0)
        self.manager_uic.rd_full.setChecked(True)
        self.manager_uic.rd_no.setChecked(False)
        self.manager_uic.lineEdit.clear()
        self.set_default_image()
        self.current_image_path = None
        self.original_id = None
        self.uic.le_pw.clear()
        self.uic.le_us.clear()
        self.manager_uic.cb_sort.setCurrentIndex(0)
        self.load_data()

    def back_to_home(self):
        """Hàm quay lại trang chủ"""
        reply = QMessageBox.question(self.manager_win, "Confirm Return to Home",
                                     "Are you sure you want to return to Home?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.manager_win.hide()
            self.clear_inputs()
            self.home_win.show()

    def logout(self):
        """Hàm đăng xuất"""
        reply = QMessageBox.question(self.manager_win, "Confirm Logout",
                                     "Are you sure you want to logout?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.manager_win.hide()
            self.clear_inputs()
            self.main_win.show()

    # type
    def open_type_window(self):
        """Hàm mở cửa sổ quản lý loại CPU"""
        self.manager_win.hide()
        self.type_win.show()
        self.load_processors()

    def load_processors(self):
        """Hàm tải danh sách bộ xử lý"""
        try:
            rows = self.db.fetch_processors()
            self.type_uic.table_processor.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                self.type_uic.table_processor.setItem(row_idx, 0, QTableWidgetItem(str(row_data[0])))
                self.type_uic.table_processor.setItem(row_idx, 1, QTableWidgetItem(str(row_data[1])))
        except Exception as e:
            QMessageBox.critical(self.type_win, "Error", f"Failed to load processors: {str(e)}")

    def add_processor(self):
        """Hàm thêm bộ xử lý"""
        name_processor = self.type_uic.le_processorname.text().strip()
        if not name_processor:
            QMessageBox.warning(self.type_win, "Warning", "Please enter the processor name!")
            return
        try:
            if self.db.add_processor(name_processor):
                QMessageBox.information(self.type_win, "Success", "Processor added successfully!")
                self.load_processors()
                self.clear_processor_inputs()
                self.load_combo_boxes()
            else:
                QMessageBox.warning(self.type_win, "Error", "Processor with this name already exists!")
        except Exception as e:
            QMessageBox.critical(self.type_win, "Error", f"Failed to add processor: {str(e)}")

    def update_processor(self):
        """Hàm sửa bộ xử lý"""
        if not self.original_processor_id:
            QMessageBox.warning(self.type_win, "Warning", "Please select a processor to modify!")
            return
        name_processor = self.type_uic.le_processorname.text().strip()
        if not name_processor:
            QMessageBox.warning(self.type_win, "Warning", "Please enter the processor name!")
            return
        try:
            if self.db.update_processor(self.original_processor_id, name_processor):
                QMessageBox.information(self.type_win, "Success", "Processor updated successfully!")
                self.load_processors()
                self.clear_processor_inputs()
                self.load_combo_boxes()
            else:
                QMessageBox.warning(self.type_win, "Error", "Processor with this name already exists!")
        except Exception as e:
            QMessageBox.critical(self.type_win, "Error", f"Failed to update processor: {str(e)}")

    def delete_processor(self):
        """Hàm xóa bộ xử lý"""
        if not self.original_processor_id:
            QMessageBox.warning(self.type_win, "Warning", "Please select a processor to delete!")
            return
        reply = QMessageBox.question(self.type_win, "Confirm Delete",
                                     f"Are you sure you want to delete processor with ID {self.original_processor_id}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                self.db.delete_processor(self.original_processor_id)
                QMessageBox.information(self.type_win, "Success", "Processor deleted successfully!")
                self.load_processors()
                self.clear_processor_inputs()
                self.load_combo_boxes()
            except Exception as e:
                QMessageBox.critical(self.type_win, "Error", f"Failed to delete processor: {str(e)}")

    def clear_processor_inputs(self):
        """Hàm xóa dữ liệu nhập trên giao diện Type"""
        self.type_uic.le_processor_id.clear()
        self.type_uic.le_processorname.clear()
        self.type_uic.le_processor_id.setPlaceholderText("Auto-generated ID")
        self.original_processor_id = None

    def on_process_selection_change(self):
        selected_row = self.type_uic.table_processor.currentRow()
        if selected_row >= 0:
            self.original_processor_id = self.type_uic.table_processor.item(selected_row, 0).text()
            self.type_uic.le_processor_id.setText(self.original_processor_id)
            self.type_uic.le_processorname.setText(self.type_uic.table_processor.item(selected_row, 1).text())

    def back_to_manager(self):
        self.type_win.hide()
        self.manager_win.show()
        self.clear_inputs()
        self.load_combo_boxes()

    def close_application(self):
        reply = QMessageBox.question(self.manager_win, "Confirm Exit","Are you sure you want to exit the application?",
        QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()


# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
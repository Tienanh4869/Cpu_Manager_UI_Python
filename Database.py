from pyodbc import Binary, connect

class cls_login:
    def __init__(self):
        self.conn = connect(
            "Driver={SQL Server};"
            "Server=MY-LAPPPP\\DATA;"
            "Database=Dangnhap;"
            "Trusted_Connection=yes;"
        )
        self.cursor = self.conn.cursor()

    # Kiểm tra đăng nhập
    def check(self, username, password):
        self.cursor.execute("SELECT * FROM LOGIN WHERE UN = ? AND PW = ?", (username, password))
        return self.cursor.fetchall()

    # Thêm tài khoản
    def insert(self, username, password):
        self.cursor.execute("SELECT * FROM LOGIN WHERE UN = ?", (username,))
        if len(self.cursor.fetchall()) > 0:
            return False
        self.cursor.execute("INSERT INTO LOGIN (UN, PW) VALUES (?, ?)", (username, password))
        self.conn.commit()
        return True

    # Thêm CPU
    def add_cpu(self, id, name, price, company, processor, status, image_data):
        self.cursor.execute("SELECT * FROM Manager WHERE ID = ?", (id,))
        if len(self.cursor.fetchall()) > 0:
            return False
        self.cursor.execute(
            "INSERT INTO dbo.Manager (ID, Name, Price, Company, Processor, Status, Picture) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (id, name, price, company, processor, status, Binary(image_data) if image_data else None)
        )
        self.conn.commit()
        return True

    # Cập nhật CPU
    def update_cpu(self, original_id, id, name, price, company, processor, status, image_data):
        if id != original_id:
            self.cursor.execute("SELECT * FROM Manager WHERE ID = ?", (id,))
            if len(self.cursor.fetchall()) > 0:
                return False
        self.cursor.execute(
            "UPDATE Manager SET ID = ?, Name = ?, Price = ?, Company = ?, Processor = ?, Status = ?, Picture = ? WHERE ID = ?",
            (id, name, price, company, processor, status, Binary(image_data) if image_data else None, original_id)
        )
        self.conn.commit()
        return True

    # Xóa CPU
    def delete_cpu(self, id):
        self.cursor.execute("DELETE FROM Manager WHERE ID = ?", (id,))
        self.conn.commit()
        return True

    # Lấy tất cả CPU
    def fetch_all(self):
        self.cursor.execute("SELECT ID, Name, Price, Company, Processor, Status FROM dbo.Manager")
        return self.cursor.fetchall()

    # Lấy ảnh CPU
    def get_image(self, id):
        self.cursor.execute("SELECT Picture FROM Manager WHERE ID = ?", (id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    # Tìm CPU
    def search_cpu(self, id=None, name=None, company=None, processor=None):
        query = "SELECT ID, Name, Price, Company, Processor, Status FROM Manager WHERE 1=1"
        params = []
        if id:
            query += " AND ID = ?"
            params.append(id)
        if name:
            query += " AND Name LIKE ?"
            params.append(f"%{name}%")
        if company and company != "Not selected":
            query += " AND Company = ?"
            params.append(company)
        if processor and processor != "Not selected":
            query += " AND Processor = ?"
            params.append(processor)

        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    # Sắp xếp CPU
    def sort_cpu(self, sort_column):
        query = f"SELECT ID, Name, Price, Company, Processor, Status FROM Manager ORDER BY {sort_column}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # Lấy danh sách bộ xử lý
    def fetch_processors(self):
        self.cursor.execute("SELECT ID_Processors, Name_Processors FROM Type_Processors")
        return self.cursor.fetchall()

    # Thêm bộ xử lý
    def add_processor(self, name_processor):
        self.cursor.execute("SELECT * FROM Type_Processors WHERE Name_Processors = ?", (name_processor,))
        if len(self.cursor.fetchall()) > 0:
            return False
        self.cursor.execute("INSERT INTO Type_Processors (Name_Processors) VALUES (?)", (name_processor,))
        self.conn.commit()
        return True

    # Cập nhật bộ xử lý
    def update_processor(self, original_id, name_processor):
        self.cursor.execute("SELECT * FROM Type_Processors WHERE Name_Processors = ? AND ID_Processors != ?", (name_processor, original_id))
        if len(self.cursor.fetchall()) > 0:
            return False
        self.cursor.execute("UPDATE Type_Processors SET Name_Processors = ? WHERE ID_Processors = ?", (name_processor, original_id))
        self.conn.commit()
        return True

    # Xóa bộ xử lý
    def delete_processor(self, id_processor):
        self.cursor.execute("DELETE FROM Type_Processors WHERE ID_Processors = ?", (id_processor,))
        self.conn.commit()
        return True

    # Đóng kết nối
    def __del__(self):
        self.conn.close()
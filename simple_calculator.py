import tkinter as tk
from tkinter import messagebox

class MayTinh:
    """
    Lớp MayTinh quản lý toàn bộ giao diện và logic của ứng dụng máy tính đơn giản.
    """
    def __init__(self, master):
        """
        Khởi tạo cửa sổ chính và các thành phần GUI.
        master: đối tượng cửa sổ Tkinter gốc (root).
        """
        self.master = master # Lưu trữ đối tượng cửa sổ chính
        master.title("Máy tính") # Đặt tiêu đề cửa sổ
        master.geometry("300x330") # Đặt kích thước cửa sổ
        master.resizable(False, False) # Không cho phép thay đổi kích thước cửa sổ

        # Cấu hình các cột để chúng giãn nở đều khi cửa sổ được thay đổi kích thước
        master.grid_columnconfigure(0, weight=1) #
        master.grid_columnconfigure(1, weight=1) #

        # --- Tạo và sắp xếp các thành phần GUI bằng Grid ---

        # Hàng 0: Label "Số thứ nhất" và Entry nhập số thứ nhất
        tk.Label(master, text="Số thứ nhất:").grid(row=0, column=0, padx=5, pady=5, sticky="w") #
        self.entry_num1 = tk.Entry(master, width=20) #
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5, sticky="ew") #

        # Hàng 1: Label "Số thứ hai" và Entry nhập số thứ hai
        tk.Label(master, text="Số thứ hai:").grid(row=1, column=0, padx=5, pady=5, sticky="w") #
        self.entry_num2 = tk.Entry(master, width=20) #
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5, sticky="ew") #

        # Hàng 2 & 3: Các Radiobutton để chọn phép toán
        self.operation_var = tk.StringVar(value="+") # Giá trị mặc định là '+'

        tk.Radiobutton(master, text="Cộng (+)", variable=self.operation_var, value="+").grid(row=2, column=0, padx=5, pady=2, sticky="w") #
        tk.Radiobutton(master, text="Trừ (-)", variable=self.operation_var, value="-").grid(row=2, column=1, padx=5, pady=2, sticky="w") #
        tk.Radiobutton(master, text="Nhân (×)", variable=self.operation_var, value="*").grid(row=3, column=0, padx=5, pady=2, sticky="w") #
        tk.Radiobutton(master, text="Chia (÷)", variable=self.operation_var, value="/").grid(row=3, column=1, padx=5, pady=2, sticky="w") #

        # Hàng 4: Nút "Tính"
        self.button_calculate = tk.Button(master, text="Tính", command=self.calculate, width=15, height=2) #
        self.button_calculate.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew") #

        # Hàng 5: Nút "Reset"
        self.button_reset = tk.Button(master, text="Reset", command=self.reset_fields, width=15, height=2) #
        self.button_reset.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew") #

        # Hàng 6: Label hiển thị kết quả
        self.label_result = tk.Label(master, text="Kết quả", font=("Helvetica", 12, "bold"), fg="blue", bg="lightgray", padx=10, pady=10) #
        self.label_result.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="ew") #

    def calculate(self):
        """
        Đọc giá trị từ các ô nhập liệu, thực hiện phép toán đã chọn
        và hiển thị kết quả trên Label. Bắt các lỗi ValueError và ZeroDivisionError.
        """
        try:
            num1_str = self.entry_num1.get() #
            num2_str = self.entry_num2.get() #

            if not num1_str or not num2_str: #
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ cả hai số.") #
                return

            num1 = float(num1_str) #
            num2 = float(num2_str) #
            operation = self.operation_var.get() #

            result = 0
            if operation == "+": #
                result = num1 + num2 #
            elif operation == "-": #
                result = num1 - num2 #
            elif operation == "*": #
                result = num1 * num2 #
            elif operation == "/": #
                if num2 == 0: #
                    raise ZeroDivisionError("Không thể chia cho số 0!") #
                result = num1 / num2 #
            else:
                messagebox.showerror("Lỗi", "Vui lòng chọn một phép toán.") #
                return

            self.label_result.config(text=f"Kết quả = {result}") #

        except ValueError: #
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.") #
            self.label_result.config(text="Kết quả: Lỗi nhập liệu!") #
        except ZeroDivisionError as e: #
            messagebox.showerror("Lỗi", str(e)) #
            self.label_result.config(text="Kết quả: Lỗi chia 0!") #


    def reset_fields(self):
        """
        Xóa nội dung của cả hai ô nhập liệu và đặt lại nhãn kết quả.
        """
        self.entry_num1.delete(0, tk.END) #
        self.entry_num2.delete(0, tk.END) #
        self.label_result.config(text="Kết quả") #
        self.operation_var.set("+") #

# Khởi tạo cửa sổ Tkinter gốc
root = tk.Tk()

# Tạo một thể hiện của lớp MayTinh, truyền cửa sổ gốc vào
my_calculator = MayTinh(root)

# Chạy vòng lặp sự kiện chính của Tkinter
root.mainloop() #

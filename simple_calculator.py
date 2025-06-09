import tkinter as tk
from tkinter import messagebox

class MayTinh: 
    # Lớp MayTinh quản lý toàn bộ giao diện và logic của ứng dụng máy tính đơn giản.
    def __init__(self, master):

        # Khởi tạo cửa sổ chính và các thành phần GUI.
        # master: đối tượng cửa sổ Tkinter gốc (root).
        self.goc = master # gốc Lưu trữ đối tượng cửa sổ chính 
        self.goc.title("May Tinh") 
        self.goc.geometry("300x330") 
        self.goc.resizable(False, False) # Không cho phép thay đổi kích thước cửa sổ
        self.goc.configure(bg="#30e8db") # Đặt màu nền cho cửa sổ chính

        # Cấu hình các cột để chúng giãn nở đều khi cửa sổ được thay đổi kích thước
        self.goc.grid_columnconfigure(0, weight=1) 
        self.goc.grid_columnconfigure(1, weight=1) 

        # --- Tạo và sắp xếp các thành phần GUI bằng Grid ---

        # Hàng 0: Label "Số thứ nhất" và Entry nhập số thứ nhất
        tk.Label(self.goc, text="So thu nhat:").grid(row=0, column=0, padx=5, pady=5, sticky="w") #
        self.so1 = tk.Entry(self.goc, width=20) 
        self.so1.grid(row=0, column=1, padx=5, pady=5, sticky="ew") 

        # Hàng 1: Label "Số thứ hai" và Entry nhập số thứ hai
        tk.Label(self.goc, text="So thu hai:").grid(row=1, column=0, padx=5, pady=5, sticky="w") #
        self.so2 = tk.Entry(self.goc, width=20) 
        self.so2.grid(row=1, column=1, padx=5, pady=5, sticky="ew") 

         # Hàng 2 & 3: Các Radiobutton để chọn phép toán
        self.phep_toan = tk.StringVar(value="+") 

        tk.Radiobutton(self.goc, text="Cong (+)", variable=self.phep_toan, value="+").grid(row=2, column=0, padx=5, pady=2, sticky="w") 
        tk.Radiobutton(self.goc, text="Tru (-)", variable=self.phep_toan, value="-").grid(row=2, column=1, padx=5, pady=2, sticky="w") 
        tk.Radiobutton(self.goc, text="Nhan (x)", variable=self.phep_toan, value="*").grid(row=3, column=0, padx=5, pady=2, sticky="w") 
        tk.Radiobutton(self.goc, text="Chia (:)", variable=self.phep_toan, value="/").grid(row=3, column=1, padx=5, pady=2, sticky="w") 

        # Hàng 4: Nút "Tính"
        tk.Button(self.goc, text="Tinh", command=self.tinh, width=15, height=2).grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew") 
        
        # Hàng 5: Nút "Reset"
        tk.Button(self.goc, text="Reset", command=self.dat_lai, width=15, height=2).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew") 

        # Hàng 6: Label hiển thị kết quả
        self.ket_qua = tk.Label(self.goc, text="Ket qua", font=("Helvetica", 12, "bold"), fg="blue", bg="lightgray", padx=10, pady=10) 
        self.ket_qua.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="ew") #

    def tinh(self): 
        # Đọc giá trị từ các ô nhập liệu, thực hiện phép toán đã chọn
        # và hiển thị kết quả trên Label. Bắt các lỗi ValueError và ZeroDivisionError
        try:
            so1_str = self.so1.get() 
            so2_str = self.so2.get() 

            if not so1_str or not so2_str: 
                messagebox.showerror("Loi", "Vui long nhap day du ca hai so.") #
                return

            num1 = float(so1_str) #
            num2 = float(so2_str) #
            phep = self.phep_toan.get() # Phép toán (operation_var)

            kq = 0 # kết quả 
            if phep == "+": 
                kq = num1 + num2 
            elif phep == "-": 
                kq = num1 - num2 
            elif phep == "*": 
                kq = num1 * num2 
            elif phep == "/": 
                if num2 == 0: 
                    raise ZeroDivisionError("Khong the chia cho so 0!") 
                kq = num1 / num2 
            else:
                messagebox.showerror("Loi", "Vui long chon mot phep toan.") 
                return

            self.ket_qua.config(text=f"Ket qua = {kq}") 

        except ValueError: 
            messagebox.showerror("Loi", "Vui long nhap so hop le.") 
            self.ket_qua.config(text="Ket qua: Loi nhap lieu!") 
        except ZeroDivisionError as e: 
            messagebox.showerror("Loi", str(e)) 
            self.ket_qua.config(text="Ket qua: Loi chia 0!") 


    def dat_lai(self):  
        # Xóa nội dung của cả hai ô nhập liệu và đặt lại nhãn kết quả.
        self.so1.delete(0, tk.END) 
        self.so2.delete(0, tk.END) 
        self.ket_qua.config(text="Ket qua") 
        self.phep_toan.set("+") 

# Khởi tạo cửa sổ Tkinter gốc
cua_so_goc = tk.Tk() 

# Tạo một thể hiện của lớp MayTinh, truyền cửa sổ gốc vào
may_tinh_cua_toi = MayTinh(cua_so_goc)  

# Chạy vòng lặp sự kiện chính của Tkinter
cua_so_goc.mainloop() #

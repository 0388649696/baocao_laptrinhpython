import tkinter as tk
from tkinter import messagebox

def calculate():
    """
    Đọc giá trị từ các ô nhập liệu, thực hiện phép toán đã chọn
    và hiển thị kết quả trên Label. Bắt các lỗi ValueError và ZeroDivisionError.
    """
    try:
        # Lấy giá trị từ các ô Entry
        num1_str = entry_num1.get()
        num2_str = entry_num2.get()

        # Kiểm tra xem ô nhập có rỗng không
        if not num1_str or not num2_str:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ cả hai số.")
            return

        num1 = float(num1_str)
        num2 = float(num2_str)
        operation = operation_var.get()

        result = 0
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Không thể chia cho số 0!")
            result = num1 / num2
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn một phép toán.")
            return

        # Cập nhật kết quả lên Label
        label_result.config(text=f"Kết quả = {result}")

    except ValueError:
        # Bắt lỗi khi chuyển đổi sang float không thành công
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
        label_result.config(text="Kết quả: Lỗi nhập liệu!") # Đặt lại nhãn khi lỗi
    except ZeroDivisionError as e:
        # Bắt lỗi chia cho 0
        messagebox.showerror("Lỗi", str(e))
        label_result.config(text="Kết quả: Lỗi chia 0!") # Đặt lại nhãn khi lỗi
    except Exception as e:
        # Bắt các lỗi không mong muốn khác
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi không mong muốn: {e}")
        label_result.config(text="Kết quả: Lỗi!") # Đặt lại nhãn khi lỗi

def reset_fields():
    """
    Xóa nội dung của cả hai ô nhập liệu và đặt lại nhãn kết quả.
    """
    entry_num1.delete(0, tk.END) # Xóa từ đầu đến cuối
    entry_num2.delete(0, tk.END) # Xóa từ đầu đến cuối
    label_result.config(text="Kết quả") # Đặt lại văn bản nhãn kết quả
    operation_var.set("+") # Đặt lại phép toán mặc định là cộng

# 1. Khởi tạo cửa sổ chính của ứng dụng
root = tk.Tk()
root.title("Máy tính")
root.geometry("300x330") # Đặt kích thước cửa sổ để dễ nhìn hơn
root.resizable(False, False) # Không cho phép thay đổi kích thước cửa sổ

# 2. Tạo các thành phần giao diện và sắp xếp bằng Grid

# Cấu hình các cột để chúng giãn nở đều khi cửa sổ được thay đổi kích thước
# (Mặc dù resizable(False, False) nhưng đây là một thực hành tốt)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Hàng 0: Label "Số thứ nhất" và Entry nhập số thứ nhất
tk.Label(root, text="Số thứ nhất:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_num1 = tk.Entry(root, width=20) # Thêm width để có kích thước ban đầu
entry_num1.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Hàng 1: Label "Số thứ hai" và Entry nhập số thứ hai
tk.Label(root, text="Số thứ hai:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_num2 = tk.Entry(root, width=20)
entry_num2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Hàng 2 & 3: Các Radiobutton để chọn phép toán
# Biến để lưu trữ phép toán đã chọn
operation_var = tk.StringVar(value="+") # Giá trị mặc định là '+'

# Các nút Radio (được sắp xếp trên 2 hàng, mỗi hàng 2 nút)
tk.Radiobutton(root, text="Cộng (+)", variable=operation_var, value="+").grid(row=2, column=0, padx=5, pady=2, sticky="w")
tk.Radiobutton(root, text="Trừ (-)", variable=operation_var, value="-").grid(row=2, column=1, padx=5, pady=2, sticky="w")
tk.Radiobutton(root, text="Nhân (×)", variable=operation_var, value="*").grid(row=3, column=0, padx=5, pady=2, sticky="w")
tk.Radiobutton(root, text="Chia (÷)", variable=operation_var, value="/").grid(row=3, column=1, padx=5, pady=2, sticky="w")

# Hàng 4: Nút "Tính"
button_calculate = tk.Button(root, text="Tính", command=calculate, width=15, height=2)
button_calculate.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

# Hàng 5: Nút "Reset"
button_reset = tk.Button(root, text="Reset", command=reset_fields, width=15, height=2)
button_reset.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Hàng 6: Label hiển thị kết quả
label_result = tk.Label(root, text="Kết quả", font=("Helvetica", 12, "bold"), fg="blue", bg="lightgray", padx=10, pady=10)
label_result.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

root.mainloop()
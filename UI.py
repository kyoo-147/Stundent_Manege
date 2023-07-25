from tkinter import simpledialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk
from QuanLySinhVien import QuanLySinhVien

class QuanLySinhVienApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chương trình quản lí học sinh")
        self.geometry("500x400")
        self.qlsv = QuanLySinhVien()

        self.create_widgets()


    def create_widgets(self):
        background_image_path = r"C:\Users\Admin\Downloads\QuanLySinhVien\QuanLySinhVien\main\unnamed.jpg"  # Thay đổi đường dẫn đến hình ảnh nền của bạn
        background_image = Image.open(background_image_path)
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_photo, background = "#FAF053") 
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.frame_menu = tk.Frame(self)
        self.frame_menu.pack(pady=10)

        self.label_menu = tk.Label(self.frame_menu, text="DANH SÁCH", font=("Arial", 16, "bold"),background = "#FAF053")
        self.label_menu.pack()

        self.button_them = tk.Button(self.frame_menu, text="1. Thêm học sinh", command=self.them_sinh_vien,background = "#FAF053")
        self.button_them.pack()

        self.button_cap_nhat = tk.Button(self.frame_menu, text="2. Cập nhập học sinh với ID", command=self.cap_nhat_sinh_vien, background = "#FAF053")
        self.button_cap_nhat.pack()

        self.button_xoa = tk.Button(self.frame_menu, text="3. Xóa học sinh với ID", command=self.xoa_sinh_vien, background = "#FAF053")
        self.button_xoa.pack()

        self.button_tim_kiem = tk.Button(self.frame_menu, text="4. Tìm kiếm học sinh theo tên", command=self.tim_kiem_sinh_vien,background = "#FAF053")
        self.button_tim_kiem.pack()

        self.button_sap_xep_gpa = tk.Button(self.frame_menu, text="5. Sắp xếp học sinh theo điểm trung bình", command=self.sap_xep_gpa,background = "#FAF053")
        self.button_sap_xep_gpa.pack()

        self.button_sap_xep_ten = tk.Button(self.frame_menu, text="6. Sắp xếp học sinh theo tên", command=self.sap_xep_ten,background = "#FAF053")
        self.button_sap_xep_ten.pack()

        self.button_sap_xep_id = tk.Button(self.frame_menu, text="7. Sắp xếp học sinh theo ID", command=self.sap_xep_id,background = "#FAF053")
        self.button_sap_xep_id.pack()

        self.button_hien_thi = tk.Button(self.frame_menu, text="8. Hiển thị danh sách học sinh", command=self.hien_thi_danh_sach,background = "#FAF053")
        self.button_hien_thi.pack()

        self.button_thoat = tk.Button(self.frame_menu, text="0. Thoát", command=self.quit,background = "#FAF053")
        self.button_thoat.pack()

    def them_sinh_vien(self):
        self.qlsv.nhapSinhVien()
        messagebox.showinfo("Thông Báo", "Thêm học sinh thành công!")

    def cap_nhat_sinh_vien(self):
        if self.qlsv.soLuongSinhVien() > 0:
            ID = int(simpledialog.askstring("Cập nhập thông tin học sinh", "Nhập ID:"))
            self.qlsv.updateSinhVien(ID)
        else:
            messagebox.showinfo("Thông Báo", "Danh sách học sinh trống!")

    def xoa_sinh_vien(self):
        if self.qlsv.soLuongSinhVien() > 0:
            ID = int(simpledialog.askstring("Xóa học sinh", "Nhập ID:"))
            if self.qlsv.deleteById(ID):
                messagebox.showinfo("Thông Báo", f"Học sinh có ID = {ID} đã bị xóa.")
            else:
                messagebox.showinfo("Thông Báo", f"Học sinh có ID = {ID} không tồn tại.")
        else:
            messagebox.showinfo("Thông Báo", "Danh sách học sinh trống!")

    def tim_kiem_sinh_vien(self):
        if self.qlsv.soLuongSinhVien() > 0:
            name = simpledialog.askstring("Tìm kiếm học sinh theo tên", "Nhập tên để tìm kiếm:")
            searchResult = self.qlsv.findByName(name)
            self.qlsv.showSinhVien(searchResult)
        else:
            messagebox.showinfo("Thông Báo", "Danh sách học sinh trống!")

    def sap_xep_gpa(self):
        if self.qlsv.soLuongSinhVien() > 0:
            self.qlsv.sortByDiemTB()
            self.qlsv.showSinhVien(self.qlsv.getListSinhVien())
        else:
            messagebox.showinfo("Thông Báo", "Danh sách học sinh trống!")

    def sap_xep_ten(self):
        if self.qlsv.soLuongSinhVien() > 0:
            self.qlsv.sortByName()
            self.qlsv.showSinhVien(self.qlsv.getListSinhVien())
        else:
            messagebox.showinfo("Thông Báo", "Danh sách học sinh trống!")

    def sap_xep_id(self):
        if self.qlsv.soLuongSinhVien() > 0:
            self.qlsv.sortByID()
            self.qlsv.showSinhVien(self.qlsv.getListSinhVien())
        else:
            messagebox.showinfo("Thong bao", "Danh sách học sinh trống!")

    def hien_thi_danh_sach(self):
        if self.qlsv.soLuongSinhVien() > 0:
            self.qlsv.showSinhVien(self.qlsv.getListSinhVien())
        else:
            messagebox.showinfo("Thông Báo", "Danh sách học sinh trống!")

if __name__ == "__main__":
    app = QuanLySinhVienApp()
    app.mainloop()

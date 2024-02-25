import socket
from tkinter import *
from tkinter.font import BOLD
from tkcalendar import *
#mở cmd và nhập
#pip install tkcalendar
def delete5():
    screen5.destroy()
def removeinfor():
    global type
    type = 'Menu2'

    client.sendall(type.encode(FORMAT))
    client.recv(1024)

    global screen6
    screen6=Toplevel(screen5)
    screen6.geometry("700x300")
    screen6.title("Kết quả xóa đặt phòng")

    name1=name.get()
    hotel=clicked.get()
    sl1=num1.get()
    sl2=num2.get()
    sl3=num3.get()
    stay=str(ent.get_date())
    leave=str(ent1.get_date())
    
    client.sendall(name1.encode(FORMAT))
    client.recv(1024)

    client.sendall(hotel.encode(FORMAT))
    client.recv(1024)

    client.sendall(sl1.encode(FORMAT))
    client.recv(1024)

    client.sendall(sl2.encode(FORMAT))
    client.recv(1024)

    client.sendall(sl3.encode(FORMAT))
    client.recv(1024)

    client.sendall(stay.encode(FORMAT))
    client.recv(1024)

    client.sendall(leave.encode(FORMAT))
    client.recv(1024)

    Label(screen6,text=" ").grid(row=0,column=0)
    Label(screen6,text=" ").grid(row=1,column=0)

    check=client.recv(1024).decode(FORMAT)
    client.sendall(check.encode(FORMAT))

    if (check == '1'):
        Label(screen6,text="Xóa đặt phòng thành công !!!",font=("Calibri",20)).grid(row=2,column=1)
    elif (check == '0'):
        Label(screen6,text="Xóa đặt phòng không thành công !!!",font=("Calibri",20)).grid(row=2,column=1)

    Label(screen6,text=" ").grid(row=16,column=0)
    Button(screen6,text="Xác nhận",height="2",width="20",font=("Calibri",9),command=delete5).grid(row=16,column=1)

    screen6.mainloop()

def remove():
    global name
    global clicked
    global num1
    global num2
    global num3
    global ent
    global ent1

    name = StringVar()

    global screen5
    screen5=Toplevel(root)
    screen5.geometry("600x600")
    screen5.title("Xóa đặt phòng")

    Label(screen5,text=" ").grid(row=0,column=0)
    Label(screen5,text=" ").grid(row=1,column=0)

    Label(screen5,text="XÓA ĐẶT PHÒNG ",font=("Calibri",20)).grid(row=2,column=1)
    Label(screen5,text=" ").grid(row=3,column=0)

    Label(screen5,text="Tên khách hàng:",font=("Calibri",12)).grid(row=4,column=0)
    Entry(screen5,textvariable=name).grid(row=4,column=1)
    Label(screen5,text=" ").grid(row=5,column=0)

    Label(screen5,text="Tên / Mã khách sạn:",font=("Calibri",12)).grid(row=6,column=0)
    List1=['Hong Trang','Phuong Loan','Minh Tuan']
    clicked=StringVar()
    clicked.set(List1[0])
    drop=OptionMenu(screen5,clicked,*List1)
    drop.grid(row=6,column=1)

    Label(screen5,text="Loại phòng cần đặt:",font=("Calibri",12)).grid(row=8,column=0)
    Label(screen5,text="Deluxe:",font=("Calibri",12)).grid(row=8,column=1)
    #Entry(screen3,textvariable=num1).grid(row=8,column=2)
    List2=['0','1','2']
    num1=StringVar()
    num1.set(List2[0])
    drop=OptionMenu(screen5,num1,*List2)
    drop.grid(row=8,column=2)

    Label(screen5,text="Suite:",font=("Calibri",12)).grid(row=9,column=1)
    #Entry(screen3,textvariable=num2).grid(row=9,column=2)
    List2=['0','1','2']
    num2=StringVar()
    num2.set(List2[0])
    drop=OptionMenu(screen5,num2,*List2)
    drop.grid(row=9,column=2)

    Label(screen5,text="Standard:",font=("Calibri",12)).grid(row=10,column=1)
    #Entry(screen3,textvariable=num3).grid(row=10,column=2)
    List2=['0','1','2']
    num3=StringVar()
    num3.set(List2[0])
    drop=OptionMenu(screen5,num3,*List2)
    drop.grid(row=10,column=2)

    Label(screen5,text="Chọn ngày vào ở:",font=("Calibri",12)).grid(row=11,column=0)
    ent=DateEntry(screen5)
    ent.grid(row=11,column=1)

    Label(screen5,text=" ").grid(row=12,column=0)
    Label(screen5,text="Chọn ngày rời đi:",font=("Calibri",12)).grid(row=13,column=0)
    ent1=DateEntry(screen5)
    ent1.grid(row=13,column=1)
    Label(screen5,text=" ").grid(row=14,column=0)

    Label(screen5,text=" ").grid(row=17,column=0)
    Button(screen5,text="Xác nhận",height="2",width="20",font=("Calibri",9),command=removeinfor).grid(row=17,column=1)

    screen5.mainloop()
def book():
    def del1():
        screen1.destroy()
    global khachsan
    global ngayo
    global ngaydi
    global songay
    khachsan=clicked.get()
    ngaydi=ent1.get_date()
    ngayo=ent.get_date()
    if ngaydi>ngayo:
        ngayo1=str(ngayo)
        ngaydi1=str(ngaydi)
        client.sendall(type.encode(FORMAT))
        client.recv(1024)
        print(" ")
        print("Client send type:"+type)
        client.sendall(khachsan.encode(FORMAT))
        client.recv(1024)
        print("Client send Khách Sạn:"+khachsan)
        client.sendall(ngayo1.encode(FORMAT))
        client.recv(1024)
        print("Client send Ngày ở:"+ngayo1)
        client.sendall(ngaydi1.encode(FORMAT))
        client.recv(1024)
        print("Client send Ngày đi:"+ngaydi1)
        print(" ")
        screen2.destroy()
        roominf(khachsan)
    elif ngayo>=ngaydi:
        global screen1
        screen1=Toplevel(screen2)
        screen1.geometry("300x150")
        screen1.title("Notification")
        Label(screen1,text="",).pack()
        Label(screen1,text="Ngày đi trước ngày ở! Bạn hãy chọn lại!",font=("Calibri",11)).pack()
        Button(screen1,text="OK",command=del1).pack()

def saveinfor():
    def del1():
        screen1.destroy()
    def del2():
        screen6.destroy()
    def del3():
        screen7.destroy()
    name1=name.get()
    hotel=clicked.get()
    sl1=num1.get()
    sl2=num2.get()
    sl3=num3.get()
    stay=str(ent.get_date())
    leave=str(ent1.get_date())
    note1=note.get()
    if not note.get():
        note1="Khong co"
    day=str((ent1.get_date()-ent.get_date()).days)
    if leave>stay and name.get() and (sl1!='0' or sl2!='0' or sl3!='0'):
        global type
        type='DatPhong'
        client.sendall(type.encode(FORMAT))
        client.recv(1024)
        client.sendall(name1.encode(FORMAT))
        client.recv(1024)

        client.sendall(hotel.encode(FORMAT))
        client.recv(1024)

        client.sendall(sl1.encode(FORMAT))
        client.recv(1024)

        client.sendall(sl2.encode(FORMAT))
        client.recv(1024)

        client.sendall(sl3.encode(FORMAT))
        client.recv(1024)

        client.sendall(stay.encode(FORMAT))
        client.recv(1024)

        client.sendall(leave.encode(FORMAT))
        client.recv(1024)

        client.sendall(day.encode(FORMAT))
        client.recv(1024)
    
        client.sendall(note1.encode(FORMAT))
        client.recv(1024)
        
        total=client.recv(1024).decode(FORMAT)
        client.sendall(total.encode(FORMAT))

        

        global screen4
        screen4=Toplevel(screen3)
        screen4.geometry("750x300")
        screen4.title("Kết quả đặt phòng")

        Label(screen4,text=" ").grid(row=0,column=0)
        Label(screen4,text=" ").grid(row=1,column=0)
        Label(screen4,text="Đặt phòng thành công !!!",font=("Calibri",20)).grid(row=2,column=1)

        Label(screen4,text="Tổng chi phí thuê phòng cần thanh toán là: "+str(total)+" VND ",font=("Calibri",20)).grid(row=3,column=1)

        Label(screen4,text=" ").grid(row=16,column=0)
        Button(screen4,text="Xác nhận",height="2",width="20",font=("Calibri",9),command=delete3).grid(row=16,column=1)
    elif leave<=stay or (not name.get()) or (sl1=='0' and sl2=='0' and sl3=='0'):
        if leave<=stay:
            screen1=Toplevel(screen3)
            screen1.geometry("300x150")
            screen1.title("Notification")
            Label(screen1,text="",).pack()
            Label(screen1,text="Ngày đi trước ngày ở! Bạn hãy chọn lại!",font=("Calibri",11)).pack()
            Button(screen1,text="OK",command=del1).pack()
        if not name.get():
            screen6=Toplevel(screen3)
            screen6.geometry("300x150")
            screen6.title("Notification")
            Label(screen6,text="",).pack()
            Label(screen6,text="Bạn không nhập tên!",font=("Calibri",11)).pack()
            Button(screen6,text="OK",command=del2).pack()
        if sl1=='0' and sl2=='0' and sl3=='0':
            screen7=Toplevel(screen3)
            screen7.geometry("300x150")
            screen7.title("Notification")
            Label(screen7,text="",).pack()
            Label(screen7,text="Bạn chưa nhập số lượng phòng!",font=("Calibri",11)).pack()
            Button(screen7,text="OK",command=del3).pack()  
def order():
    global note
    global name
    global clicked
    global num1
    global num2
    global num3
    global ent
    global ent1
    
    note = StringVar()
    name = StringVar()

    global screen3
    screen3=Toplevel(root)
    screen3.geometry("600x600")
    screen3.title("Đặt phòng")
    
    Label(screen3,text=" ").grid(row=0,column=0)
    Label(screen3,text=" ").grid(row=1,column=0)

    Label(screen3,text="THÔNG TIN ĐẶT PHÒNG ",font=("Calibri",20)).grid(row=2,column=1)
    Label(screen3,text=" ").grid(row=3,column=0)

    Label(screen3,text="Tên khách hàng:",font=("Calibri",12)).grid(row=4,column=0)
    Entry(screen3,textvariable=name).grid(row=4,column=1)
    Label(screen3,text=" ").grid(row=5,column=0)

    Label(screen3,text="Tên / Mã khách sạn:",font=("Calibri",12)).grid(row=6,column=0)
    List1=['Hong Trang','Phuong Loan','Minh Tuan']
    clicked=StringVar()
    clicked.set(List1[0])
    drop=OptionMenu(screen3,clicked,*List1)
    drop.grid(row=6,column=1)

    Label(screen3,text="Loại phòng cần đặt:",font=("Calibri",12)).grid(row=8,column=0)
    Label(screen3,text="Deluxe:",font=("Calibri",12)).grid(row=8,column=1)
    #Entry(screen3,textvariable=num1).grid(row=8,column=2)
    List2=['0','1','2']
    num1=StringVar()
    num1.set(List2[0])
    drop=OptionMenu(screen3,num1,*List2)
    drop.grid(row=8,column=2)

    Label(screen3,text="Suite:",font=("Calibri",12)).grid(row=9,column=1)
    #Entry(screen3,textvariable=num2).grid(row=9,column=2)
    List2=['0','1','2']
    num2=StringVar()
    num2.set(List2[0])
    drop=OptionMenu(screen3,num2,*List2)
    drop.grid(row=9,column=2)

    Label(screen3,text="Standard:",font=("Calibri",12)).grid(row=10,column=1)
    #Entry(screen3,textvariable=num3).grid(row=10,column=2)
    List2=['0','1','2']
    num3=StringVar()
    num3.set(List2[0])
    drop=OptionMenu(screen3,num3,*List2)
    drop.grid(row=10,column=2)

    Label(screen3,text="Chọn ngày vào ở:",font=("Calibri",12)).grid(row=11,column=0)
    ent=DateEntry(screen3)
    ent.grid(row=11,column=1)

    Label(screen3,text=" ").grid(row=12,column=0)
    Label(screen3,text="Chọn ngày rời đi:",font=("Calibri",12)).grid(row=13,column=0)
    ent1=DateEntry(screen3)
    ent1.grid(row=13,column=1)
    Label(screen3,text=" ").grid(row=14,column=0)

    Label(screen3,text="Ghi chú:",font=("Calibri",12)).grid(row=15,column=0)
    Entry(screen3,textvariable=note).grid(row=15,column=1)
    Label(screen3,text=" ").grid(row=16,column=0)

    Label(screen3,text=" ").grid(row=17,column=0)
    Button(screen3,text="Xác nhận",height="2",width="20",font=("Calibri",9),command=saveinfor).grid(row=17,column=1)

    screen3.mainloop()

def hotellist():
    global screen2
    screen2=Toplevel(root)
    screen2.geometry("600x250")
    root.title("E-Booking")
    list=[]
    item=None
    type='Menu1'
    client.sendall(type.encode(FORMAT))
    client.recv(1024)
    print("Client send:"+type)
    print("Danh sách khách sạn Server đã gửi:")
    item=client.recv(1024).decode(FORMAT)
    while(item!="end"):
        list.append(item)
        print("Client received:"+item)
        client.sendall(item.encode(FORMAT))
        item=client.recv(1024).decode(FORMAT)
    print(" ")
    lst=[('     STT','      Khách Sạn'),('1','Hồng Trang'),('2','Phương Loan'),('3','Minh Tuấn')]
    rows=len(lst)
    columns=len(lst[1])
    for i in range(rows):
        for j in range(columns):
            e=Entry(screen2,width=20,font=('Arial',16))
            e.grid(row=i,column=j)
            e.insert(0,lst[i][j])
    Label(screen2,text=" ").grid()        
    Button(screen2,text='Back',heigh="3",width="30",command=delete2).grid()

def roominf(string):
    loaiphong=[]
    mota=[]
    giaphong=[]
    room=[]
    print("CÁC PHÒNG CÒN TRỐNG:")
    print(" ")
    item=client.recv(1024).decode(FORMAT)
    while(item!="end"):
        room.append(item)
        print("Client received Phòng:"+item)
        client.sendall(item.encode(FORMAT))
        loaiphong1=client.recv(1024).decode(FORMAT)
        client.sendall(loaiphong1.encode(FORMAT))
        loaiphong.append(loaiphong1)
        print("Client receive loại phòng trên:"+loaiphong1)
        mota1=client.recv(1024).decode(FORMAT)
        client.sendall(mota1.encode(FORMAT))
        mota.append(mota1)
        print("Client receive mô tả của phòng trên:"+mota1)
        giaphong1=client.recv(1024).decode(FORMAT)
        client.sendall(giaphong1.encode(FORMAT))
        giaphong.append(giaphong1)
        print("Client receive giá phòng trên:"+giaphong1)
        print(" ")
        item=client.recv(1024).decode(FORMAT)
    global screen2
    screen2=Toplevel(root)
    screen2.geometry("700x450")
    screen2.title("E-Booking")
    Label(screen2,text=" ").grid(row=0,column=0)
    Label(screen2,text="Khách sạn "+string,font=("Calibri",15)).grid(row=1,column=2)
    e=Entry(screen2, width=15,font=('Calibri',13))
    e.grid(row=2,column=0)
    e.insert(0, "Phòng")
    e=Entry(screen2, width=15,font=('Calibri',13))
    e.grid(row=2,column=1)
    e.insert(0, "Loại Phòng")
    e=Entry(screen2, width=15,font=('Calibri',13))
    e.grid(row=2,column=2)
    e.insert(0, "Mô Tả")
    e=Entry(screen2, width=15,font=('Calibri',13))
    e.grid(row=2,column=3)
    e.insert(0, "Giá Phòng")
    rows=len(room)
    columns=4
    for i in range(rows):
        for j in range(columns):
            e=Entry(screen2, width=15,font=('Calibri',13))
            e.grid(row=i+3,column=j)
            if j==0:
                e.insert(0, room[i])
            elif j==1:
                e.insert(0,loaiphong[i])
            elif j==2:
                e.insert(0,mota[i])
            elif j==3:
                e.insert(0,giaphong[i])
    Button(screen2,text="Đặt Phòng",height="2",width="20",command=delete22).grid(row=10,column=2)
    
def delete22():
    screen2.destroy()
    order()

def booking():
    
    global type
    type='Menu3'
    global screen2
    screen2=Toplevel(root)
    screen2.geometry("500x450")
    screen2.title("E-Booking")
    Label(screen2,text=" ").grid(row=0,column=0)
    Label(screen2,text=" ").grid(row=1,column=0)

    Label(screen2,text="ĐẶT PHÒNG KHÁCH SẠN",font=("Calibri",20)).grid(row=2,column=1)
    Label(screen2,text=" ").grid(row=3,column=0)

    global ent
    global ent1
    Label(screen2,text="Chọn ngày vào ở:",font=("Calibri",12)).grid(row=4,column=0)
    ent=DateEntry(screen2)
    ent.grid(row=4,column=1)
    Label(screen2,text=" ").grid(row=5,column=0)
    Label(screen2,text="Chọn ngày rời đi:",font=("Calibri",12)).grid(row=6,column=0)
    ent1=DateEntry(screen2)
    ent1.grid(row=6,column=1)
    Label(screen2,text=" ").grid(row=7,column=0)

    Label(screen2,text="Khách sạn:",font=("Calibri",12)).grid(row=8,column=0)
    List1=['Hồng Trang','Phương Loan','Minh Tuấn']
    global clicked
    clicked=StringVar()
    clicked.set(List1[0])
    drop=OptionMenu(screen2,clicked,*List1)
    drop.grid(row=8,column=1)

    Label(screen2,text=" ").grid(row=9,column=0)
    Button(screen2,text="Xác nhận",height="2",width="20",font=("Calibri",9),command=book).grid(row=10,column=1)
def exit():
    global type
    type="Exit"
    client.sendall(type.encode(FORMAT))
    client.recv(1024)
    root.destroy()
def menu():
    resetAll()
    Label(root,text="Welcome to E-Booking",width="300",height="3",font=("Calibri",34)).pack()
    Label(root,text=" ").pack()
    Button(text="DANH SÁCH CÁC KHÁCH SẠN",height="3",width="30",command=hotellist).pack()
    Label(root,text=" ").pack()
    Button(text="THÔNG TIN ĐẶT PHÒNG",height="3",width="30",command=remove).pack()
    Label(root,text=" ").pack()
    Button(text="TRA CỨU",height="3",width="30",command=booking).pack()
    Label(root,text=" ").pack()
    Button(text="THOÁT",height="3",width="30",command=exit).pack()

def resetAll():
    canvas.destroy()

def delete2whensuccess():
    screen2.destroy()
    screen1.destroy()

def delete2():
    screen2.destroy()
    
def delete3():
    screen3.destroy()

def delete4():
    screen4.destroy()

def notidangky(string):
    global screen2
    screen2=Toplevel(screen1)
    screen2.title("Notification")
    screen2.geometry("150x100")
    Label(screen2,text=string).pack()
    if string=="Đăng ký thất bại":
        Button(screen2,text="OK",command=delete2).pack()
    elif string=="Đăng ký thành công":
        Button(screen2,text="OK",command=delete2whensuccess).pack()

def getuser():
    taikhoan=username.get()  
    matkhau=password.get()
    sobank=bankact.get()
    global type
    type='Dang Ky'
    client.sendall(type.encode(FORMAT))
    client.recv(1024)

    client.sendall(taikhoan.encode(FORMAT))
    client.recv(1024)
    client.sendall(matkhau.encode(FORMAT))
    client.recv(1024)
    client.sendall(sobank.encode(FORMAT))
    client.recv(1024)
    cone=client.recv(1024).decode(FORMAT)
    client.sendall(cone.encode(FORMAT))
    if cone=='thanhcong':
        notidangky("Đăng ký thành công")
        #Label (screen1,text="Registration Sucess",fg="green", font=("Calibri",11) ).pack()
    elif cone=='thatbai':
        notidangky("Đăng ký thất bại")

def register():
    global screen1
    screen1=Toplevel(root)
    screen1.title("Đăng Ký")
    screen1.geometry("400x350")

    global username 
    username= StringVar()
    global password 
    password=StringVar()
    global bankact 
    bankact= StringVar()

    Label(screen1,text="Tài Khoản").pack()
    Entry(screen1,textvariable=username).pack()
    Label(screen1,text="Mật Khẩu").pack()
    Entry(screen1,textvariable=password).pack()
    Label(screen1,text="Số thẻ ngân hàng").pack()
    Entry(screen1,textvariable=bankact).pack()
    Button(screen1,text="Đăng ký",height="1",width="15",command=getuser).pack()
    Label(screen1,text=" ").pack()
    Label(screen1,text="-Tài khoản gồm ít nhất 5 ký tự: a-z, 0-9",font=("Calibri",9,BOLD)).pack()
    Label(screen1,text=" ").pack()
    Label(screen1,text="-Mật khẩu gồm ít nhất 3 ký tự",font=("Calibri",9,BOLD)).pack()
    Label(screen1,text=" ").pack()
    Label(screen1,text="-Mã thẻ ngân hàng gồm 10 ký số 0 - 9",font=("Calibri",9,BOLD)).pack()


def delete2whensuccessdn():
    screen2.destroy()
    screen1.destroy()
    menu()

def notidangnhap():
    global screen2
    screen2=Toplevel(screen1)
    screen2.title("Thông báo")
    screen2.geometry("150x100")
    Label(screen2,text="Đăng nhập thành công").pack()
    Button(screen2,text="OK",command=delete2whensuccessdn).pack()
def notidangnhapthatbai():
    global screen2
    screen2=Toplevel(screen1)
    screen2.title("Thông báo")
    screen2.geometry("150x100")
    Label(screen2,text="Tài khoản không tồn tại").pack()
    Button(screen2,text="OK",command=delete2).pack()

def checkuser():
    taikhoan1=username1.get()  
    matkhau1=password1.get()
    global type
    type='Dang Nhap'
    client.sendall(type.encode(FORMAT))
    client.recv(1024)
    print(" ")
    print("Client send type:"+type)
    client.sendall(taikhoan1.encode(FORMAT))
    client.recv(1024)
    print("Client send taikhoan:"+taikhoan1)
    client.sendall(matkhau1.encode(FORMAT))
    client.recv(1024)
    print("Client send matkhau:"+matkhau1)
    print(" ")
    #notidangnhap()
    
    cone=client.recv(1024).decode(FORMAT)
    client.sendall(cone.encode(FORMAT))
    if cone=='1':
        #notidangky("Registration Success")
        notidangnhap()
    elif cone=='0':
        notidangnhapthatbai()
    

def login():
    global type
    type='Dang Nhap'
    global screen1
    screen1=Toplevel(root)
    screen1.title("Login")
    screen1.geometry("400x350")

    global username1
    username1=StringVar()
    global password1
    password1=StringVar()

    Label(screen1,text="Tài Khoản").pack()
    Entry(screen1,textvariable=username1).pack()
    Label(screen1,text="Mật Khẩu").pack()
    Entry(screen1,textvariable=password1).pack()
    Label(screen1,text=" ").pack()
    Button(screen1,text="Đăng Nhập",height="1",width="15",command=checkuser).pack()

def mainscreen():
    global root
    root = Tk()
    root.geometry("600x550")
    root.title("E-Booking")
    global canvas
    canvas = Canvas(root)
    canvas.pack()
    Label(canvas,text="Welcome to E-Booking",width="300",height="3",font=("Calibri",30)).pack()
    Label(canvas,text=" ").pack()
    Button(canvas,text="Đăng nhập",height="3",width="30",command=login).pack()
    Label(canvas,text=" ").pack()
    Button(canvas,text="Đăng ký",height="3",width="30", command=register).pack()
    root.mainloop()

HOST = "127.0.0.1"  # IP adress server
PORT = 65432        # port is used by the server
FORMAT="utf8"
global client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
try:
    client.connect(server_address)
    print("Client connect to server with port: " + str(PORT))
    mainscreen()
except:
    client.close()
    print("Error!!!")
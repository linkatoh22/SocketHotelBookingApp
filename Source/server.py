import socket
import json
import threading
import os, sys
from datetime import timedelta
from datetime import datetime

def dangky(taikhoan,matkhau,banknum):
    kitu=0
    so=0
    global loiten, loimk,loibank
    error=0
    for c in taikhoan:
        if c.isdigit()==False and c.islower()==False:
            print("Loi! Ten dang nhap khong duoc co ky tu dac biet va viet hoa")
            error+=1
            break
        elif c.isdigit()==True:
            so+=1
        else:
            kitu+=1
    if so<1:
        print("Loi! Ten dang nhap phai co it nhat 1 chu so")
        error+=1
    if kitu<1:
        print("Loi! Ten dang nhap phai co it nhat 1 chu cai viet thuong")
        error+=1
    if len(taikhoan)<5:
        print("Loi! Ten dang nhap phai co it nhat 5 ki tu")
        error+=1
    if len(matkhau)<3:
        print("Mat khau phai co it nhat 3 ky tu")
        error+=1
    for c in banknum:
        if c.isdigit()==False:
            error+=1
            print("Ma the ngan hang phai la so")
            break
    if len(banknum)!=10:
        error+=1
        print("Ma the ngan hang phai co 10 chu so")
    if error==0:
        print("Dang ky thanh cong!")
        return True
    else:
        print("TAI KHOAN KHONG HOP LE!")
        return False


HOST = "127.0.0.1"  # IP adress server
PORT = 65432        # port is used by the server
FORMAT="utf8"

def handleClient(conn, addr):
    type=conn.recv(1024).decode(FORMAT)
    conn.sendall(type.encode(FORMAT))
    print("Server receive:"+type)
    while True:
        if type=='Dang Ky':
            taikhoan=conn.recv(1024).decode(FORMAT)
            conn.sendall(taikhoan.encode(FORMAT))
            matkhau=conn.recv(1024).decode(FORMAT)
            conn.sendall(matkhau.encode(FORMAT))
            sobank=conn.recv(1024).decode(FORMAT)
            conn.sendall(sobank.encode(FORMAT))
            if dangky(taikhoan,matkhau,sobank)==True:
                cone='thanhcong'
                type='success'
                conn.sendall(cone.encode(FORMAT))
                conn.recv(1024)
                newinfor = {'tai khoan':taikhoan, 'matkhau':matkhau, 'sobank':sobank}

                listinfor = []
                listinfor.append(newinfor)
                    
                if (os.stat("user.json").st_size == 0) == False:
                    f = open('user.json','r')
                
                    # returns JSON object as
                    # a dictionary

                    infor1 = str(newinfor)

                    infor1 = json.loads(f.read())
                            
                    # Iterating through the json
                    # list
                    for i in infor1:
                        print(i)
                        infor = i
                        listinfor.append(infor)
                        # Closing file
                        f.close()

                userinfor = json.dumps(listinfor,indent=4)
                file = open("user.json","w")
                file.write(userinfor)
                file.close()
            else:
                cone='thatbai'
                conn.sendall(cone.encode(FORMAT))
                conn.recv(1024)


            type=conn.recv(1024).decode(FORMAT)
            conn.sendall(type.encode(FORMAT))

        if type=='Dang Nhap':

            taikhoan=conn.recv(1024).decode(FORMAT)
            conn.sendall(taikhoan.encode(FORMAT))
            print("Server receive tai khoan:"+taikhoan)
            matkhau=conn.recv(1024).decode(FORMAT)
            conn.sendall(matkhau.encode(FORMAT))
            print("Server receive mat khau:"+matkhau)
            
            newinfor=({"tai khoan": "baohanh1","matkhau": "abc123","sobank": "1234567890"})    
            searchinfor={"tai khoan": taikhoan,"matkhau": matkhau} 
            
            kt = 1
            listinfor = []
                
            if (os.stat("user.json").st_size == 0) == False:
                f = open('user.json','r')
            
                data1 = str(newinfor)

                data1 = json.loads(f.read())

                for i in data1:
                    data = i
                    listinfor.append(data)
                        
                for i in data1:
                    print(i)
                            
                    if (searchinfor["tai khoan"] == i["tai khoan"] and searchinfor["matkhau"] == i["matkhau"]):
                        kt = 1
                        break
                    else:
                        kt = 0
                    
                f.close()

            else:
                kt = 0
            print(kt)
            
            conn.sendall(str(kt).encode(FORMAT))
            conn.recv(1024)
            
            type=conn.recv(1024).decode(FORMAT)
            conn.sendall(type.encode(FORMAT))

        if type=='Menu1':
            list=["Hồng Trang","Phương Loan","Minh Tuấn"]
            for item in list:
                conn.sendall(item.encode(FORMAT))
                conn.recv(1024)
            msg="end"
            conn.sendall(msg.encode(FORMAT))
            type=conn.recv(1024).decode(FORMAT)
            conn.sendall(type.encode(FORMAT))

        if type=='Menu2':
            print("Server received type:"+type)

            check = 1

            name1 = conn.recv(1024).decode(FORMAT)
            conn.sendall(name1.encode(FORMAT))
            print("Server receive name: "+name1)

            hotel = conn.recv(1024).decode(FORMAT)
            conn.sendall(hotel.encode(FORMAT))
            print("Server receive hotel: "+hotel)
            
            sl1 = conn.recv(1024).decode(FORMAT)
            conn.sendall(sl1.encode(FORMAT))
            print("Server receive sl1: "+sl1)

            sl2 = conn.recv(1024).decode(FORMAT)
            conn.sendall(sl2.encode(FORMAT))
            print("Server receive sl2: "+sl2)

            sl3 = conn.recv(1024).decode(FORMAT)
            conn.sendall(sl3.encode(FORMAT))
            print("Server receive sl3: "+sl3)
            
            stay = conn.recv(1024).decode(FORMAT)
            conn.sendall(stay.encode(FORMAT))
            print("Server receive stay: "+stay)

            leave = conn.recv(1024).decode(FORMAT)
            conn.sendall(leave.encode(FORMAT))
            print("Server receive leave: "+leave)

            newdata=({"name": "baohanh","hotel": "Hong Trang","Deluxe": "0","Suite": "2","Standard": "0","ngay o lai": "2022-07-14","ngay roi di": "2022-07-15","total": "7000000","note": "X","time": "14/07/2022/22/29/59"})    
            deletedata = {'name': name1, 'hotel': hotel, 'Deluxe': sl1, 'Suite': sl2, 'Standard': sl3, 'ngay o lai': stay, 'ngay roi di': leave}

            listdata = []
            dem = 0
                
            if (os.stat("infor.json").st_size == 0) == False:
                f = open('infor.json','r')
            
                data1 = str(newdata)

                data1 = json.loads(f.read())

                for i in data1:
                    data = i
                    listdata.append(data)
                        
                for i in data1:
                    print(i)
                    dem += 1
                            
                    if (deletedata["name"] == i["name"] and deletedata["hotel"] == i["hotel"] and deletedata["Deluxe"] == i["Deluxe"] and deletedata["Suite"] == i["Suite"] and deletedata["Standard"] == i["Standard"] and deletedata["ngay o lai"] == i["ngay o lai"] and deletedata["ngay roi di"] == i["ngay roi di"]):
                        check = 1
                        t2 = i["time"].split('/')

                        y2 = int(t2[2])
                        m2 = int(t2[1])
                        d2 = int(t2[0])
                        h2 = int(t2[3])
                        mi2 = int(t2[4])
                        s2 = int(t2[5])

                        now1 = datetime.now() # lấy thời gian ở hiện tại

                        dt_string1 = now1.strftime("%d/%m/%Y/%H/%M/%S") # ép kiểu string cho thời gian ở hiện tại

                        t1 = dt_string1.split('/')

                        y1 = int(t1[2])
                        m1 = int(t1[1])
                        d1 = int(t1[0])
                        h1 = int(t1[3])
                        mi1 = int(t1[4])
                        s1 = int(t1[5])

                        t1 = datetime(year = y1, month = m1, day = d1, hour = h1, minute = mi1, second = s1)
                        t2 = datetime(year = y2, month = m2, day = d2, hour = h2, minute = mi2, second = s2)
                        t3 = t1 - t2
                        sec = t3.total_seconds()

                        if (int(sec) <= 86400):

                            print(dem)
                            listdata.pop(dem-1)

                            userinfor = json.dumps(listdata,indent=4)
                            file = open("infor.json","w")
                            file.write(userinfor)
                            file.close()
                            break
                        else:
                            check = 0
                    else:
                        check = 0

                f.close()

            else:
                check = 0

            conn.sendall(str(check).encode(FORMAT))
            conn.recv(1024)
        
            type=conn.recv(1024).decode(FORMAT)
            conn.sendall(type.encode(FORMAT))

        if type=='Menu3':
            print("Server receive Type:"+type)
            khachsan=conn.recv(1024).decode(FORMAT)
            conn.sendall(khachsan.encode(FORMAT))
            print("Server receive khách sạn:"+khachsan)
            ngayo=conn.recv(1024).decode(FORMAT)
            conn.sendall(ngayo.encode(FORMAT))
            print("Server receive ngày ở:"+ngayo)
            ngaydi=conn.recv(1024).decode(FORMAT)
            conn.sendall(ngaydi.encode(FORMAT))
            print("Server receive ngày đi:"+ngaydi)
            if(khachsan=='Hồng Trang'):
                filetxt= open("Hồng Trang.txt","r")
                filecontent=filetxt.read()
                room=filecontent.split(" ")
                filetxt.close()
            elif(khachsan=='Phương Loan'):
                filetxt= open("Phương Loan.txt","r")
                filecontent=filetxt.read()
                room=filecontent.split(" ")
                filetxt.close()
            elif(khachsan=='Minh Tuấn'):
                filetxt= open("Minh Tuấn.txt","r")
                filecontent=filetxt.read()
                room=filecontent.split(" ")
                filetxt.close()
            for item in room:
                conn.sendall(item.encode(FORMAT))
                conn.recv(1024)
                if "A" in item:
                    loaiphong="Deluxe"
                    mota="60m^2"
                    giaphong="4.500.000 VND"
                    conn.sendall(loaiphong.encode(FORMAT))
                    conn.recv(1024)
                    conn.sendall(mota.encode(FORMAT))
                    conn.recv(1024)
                    conn.sendall(giaphong.encode(FORMAT))
                    conn.recv(1024)
                if "B" in item:
                    loaiphong="Suite"
                    mota="50m^2"
                    giaphong="3.500.000 VND"
                    conn.sendall(loaiphong.encode(FORMAT))
                    conn.recv(1024)
                    conn.sendall(mota.encode(FORMAT))
                    conn.recv(1024)
                    conn.sendall(giaphong.encode(FORMAT))
                    conn.recv(1024)
                if "C" in item:
                    loaiphong="Standard"
                    mota="30m^2"
                    giaphong="2.500.000 VND"
                    conn.sendall(loaiphong.encode(FORMAT))
                    conn.recv(1024)
                    conn.sendall(mota.encode(FORMAT))
                    conn.recv(1024)
                    conn.sendall(giaphong.encode(FORMAT))
                    conn.recv(1024)
                print("Server send:"+item)
            msg="end"
            conn.sendall(msg.encode(FORMAT))

            type=conn.recv(1024).decode(FORMAT)
            conn.sendall(type.encode(FORMAT))

        if type=='DatPhong':
            name1 = conn.recv(1024).decode(FORMAT)
            conn.sendall(name1.encode(FORMAT))
            print("Server receive name: "+name1)

            hotel = conn.recv(1024).decode(FORMAT)
            conn.sendall(hotel.encode(FORMAT))
            print("Server receive hotel: "+hotel)
            
            sl1 = conn.recv(1024).decode(FORMAT)
            conn.sendall(sl1.encode(FORMAT))
            print("Server receive sl1: "+sl1)

            sl2 = conn.recv(1024).decode(FORMAT)
            conn.sendall(sl2.encode(FORMAT))
            print("Server receive sl2: "+sl2)

            sl3 = conn.recv(1024).decode(FORMAT)
            conn.sendall(sl3.encode(FORMAT))
            print("Server receive sl3: "+sl3)
            
            stay = conn.recv(1024).decode(FORMAT)
            conn.sendall(stay.encode(FORMAT))
            print("Server receive stay: "+stay)

            leave = conn.recv(1024).decode(FORMAT)
            conn.sendall(leave.encode(FORMAT))
            print("Server receive leave: "+leave)

            day = conn.recv(1024).decode(FORMAT) #day la ngay di tru cho ngay o nha ba
            conn.sendall(day.encode(FORMAT))
            print("Server receive day: "+day)

            note1 = conn.recv(1024).decode(FORMAT)
            conn.sendall(note1.encode(FORMAT))
            print("Server receive note: "+note1)

            total1 = (int(sl1)*4500000 + int(sl2)*3500000 + int(sl3)*2500000)*int(day)
            total = str(total1)
            conn.sendall(total.encode(FORMAT))
            print("Server receive total: "+total)

            now = datetime.now() # lấy thời gian ở hiện tại
            print("now =", now)  # in ra thời gian đó

            dt_string = now.strftime("%d/%m/%Y/%H/%M/%S") # ép kiểu string cho thời gian ở hiện tại
            print("Ngay va gio hien tai =", dt_string)	  # in ra thời gian đã được ép kiểu string

            newdata = ({'name': name1, 'hotel': hotel, 'Deluxe': sl1, 'Suite': sl2, 'Standard': sl3, 'ngay o lai': stay, 'ngay roi di': leave,'total': total, 'note': note1, 'time':dt_string})
            listdata = []
            listdata.append(newdata)

            if (os.stat("infor.json").st_size == 0) == False:
                f = open('infor.json','r')
    
                # returns JSON object as
                # a dictionary

                data1 = str(newdata)

                data1 = json.loads(f.read())
                
                # Iterating through the json
                # list
                for i in data1:
                    data = i
                    listdata.append(data)
                # Closing file
                f.close()

            userinfor = json.dumps(listdata,indent=4)
            file = open("infor.json","w")
            file.write(userinfor)
            file.close()

            type=conn.recv(1024).decode(FORMAT)
            conn.sendall(type.encode(FORMAT))

        if type=='Exit':
            print(addr,"is Disconnected!")
            type=None
            s.close()
            break
        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Server Side:",HOST, PORT)
print("Waiting for Client:")

nClient = 0
while (nClient < 10):
    try:
        conn,addr=s.accept() #addr là địa chỉ của client
        thr = threading.Thread(target=handleClient, args=(conn,addr)) 
        thr.daemon = True
        thr.start()
    except:
        print("Error")
    nClient += 1

s.close()
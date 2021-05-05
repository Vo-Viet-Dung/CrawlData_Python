import pymongo

# Cấu hình kết nối localhost
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# Tạo cơ sở dữ liệu
mydb = myclient["mydatabase"]
# Tạo bảng admin
adminCol = mydb["admin"]
# Tạo bảng news
newsCol = mydb["news"]
content = "\xe1 Ngày 28-3, Phòng cảnh sát quản lý hành chính về trật tự xã hội Công an TP.HCM (PC06) ra thông báo tạm dừng việc tiếp nhận hồ sơ cấp căn cước công dân (CCCD) gắn chip điện tử tại trụ sở của phòng ở địa chỉ số 459 Trần Hưng Đạo, phường Cầu Kho (quận 1, TP.HCM) kể từ ngày 29-3-2021. Việc trở lại tiếp nhận hồ sơ cấp CCCD tại trụ sở PC06 sẽ thông báo sau.Lý do của việc tạm dừng tiếp nhận hồ sơ là để tăng cường nguồn lực cho Công an TP Thủ Đức và các quận, huyện."
title = "\xe1 TP.HCM: Từ ngày 29-3, chỉ nhận hồ sơ cấp CCCD gắn chip tại công an quận, huyện và TP Thủ Đức"
a = content.encode()
b = title.encode()
admin = {"name": "Vo Viet Dung", "username": "admin", "password": "12345678"}
firstNews = {"title": a,
             "content": b}
x = adminCol.insert_one(admin)
y = newsCol.insert_one(firstNews)
print(a.decode())
print(b.decode())

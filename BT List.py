l = [1,2,5,3,4,"8","-5"]
#1 Duyệt và in ra giá trị của từng phần tử trong List.
for i in l:
    print(i)

#2 In ra tổng giá trị các phần tử trong List.
sum = 0
for i in range(len(l)):
    l[i] = int(l[i])
    sum += l[i]
print("Tong gia tri cac phan tu cua list la", sum)

#3 In ra độ dài của List.
print("Do dai cua list la", len(l))

#4 In ra giá trị của phần tử có giá trị lớn nhất, nhỏ nhất trong List.
print("Gia tri nho nhat la", min(l))
print("Gia tri lon nhat la", max(l))

#5 Sắp xếp List, sau đó in ra List sau khi đã sắp xếp.
l.sort()
print(l)

#6 Xóa phần tử có chỉ số là 2 trong List.
del(l[2])
print(l)

#7 Xóa toàn bộ List.
del l
print(l)
def nhap_toa_do(name):
    diem = []
    diem.append(int(input("Nhập hoành độ x của {}: ".format(name))))
    diem.append(int(input("Nhập tung độ y của {}: ".format(name))))
    return diem

def di_chuyen(tot):
    key = input("Nhập hướng đi của tốt (a: trái, d: phải, w: lên, s: xuống): ")
    if tot[0] > 0 and tot[0] < 5:
        if (key == 'a'):
            tot[0] -= 1
        if (key == 'd'):
            tot[0] += 1
    elif tot[0] == 0:
        if (key == 'a'):
            tot[0] = 5
        if (key == 'd'):
            tot[0] = 1
    elif tot[0] == 5:
        if (key == 'a'):
            tot[0] = 4
        if (key == 'd'):
            tot[0] = 0

    if tot[1] > 0 and tot[1] < 5:
        if (key == 'w'):
            tot[1] -= 1
        if (key == 's'):
            tot[1] += 1
    elif tot[1] == 0:
        if (key == 'w'):
            tot[1] = 5
        if (key == 's'):
            tot[1] = 1
    elif tot[1] == 5:
        if (key == 'w'):
            tot[1] = 4
        if (key == 's'):
            tot[1] = 0

    print("vị trí của tốt: ", tot)
    return tot

vua = nhap_toa_do("vua")
tot = nhap_toa_do("tot")
print("vị trí của vua: ", vua)
print("vị trí của tốt: ", tot)

while (tot[0] != vua[0] or tot[1] != vua[1]):
    tot = di_chuyen(tot)
print("Bạn đã đến đích")
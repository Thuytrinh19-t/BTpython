class GiangVien:
    def __init__(self):
        self.ma = input().strip()
        self.ten = input().strip()
        self.luong_co_ban = int(input().strip())
        self.he_so = input().strip()
    
    def tinh_thu_nhap(self):
        if self.he_so == 'A':
            hs = 1.5
        elif self.he_so == 'B':
            hs = 1.2
        else:
            hs = 1.0
        return self.luong_co_ban * hs * 250000
    
    def out(self):
        if self.he_so == 'A':
            hs = 1.5
        elif self.he_so == 'B':
            hs = 1.2
        else:
            hs = 1.0
        print(f"{self.ma} {self.ten} {hs} {int(self.tinh_thu_nhap())}")

gv = GiangVien()
gv.out()

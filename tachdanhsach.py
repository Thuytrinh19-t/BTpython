def tach_danh_sach(danh_sach, k):
    if k <= 0 or k >= len(danh_sach):
        return "INVALID"
    
    ket_qua = []
    for i in range(0, len(danh_sach), k):
        danh_sach_con = danh_sach[i:i+k]
        ket_qua.append(danh_sach_con)
    
    return ket_qua

def main():
    so_bo_test = int(input())
    for _ in range(so_bo_test):
        line = input().strip()
        while '  ' in line:  
            line = line.replace('  ', ' ')
        danh_sach = list(map(int, line.split()))
        
        k = int(input())
        
        ket_qua = tach_danh_sach(danh_sach, k)
        
        if ket_qua == "INVALID":
            print("INVALID")
        else:
            print(' '.join([str(ds) for ds in ket_qua]))

if __name__ == "__main__":
    main()
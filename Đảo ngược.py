count=int(input())
while count>0:
    s=input()
    lst=s.split()
    lst_new=[]
    for item in lst:
        new_item=item[::-1]
        lst_new.append(new_item)
    new_string="".join(new_item)
    print(new_string)
    count-=1
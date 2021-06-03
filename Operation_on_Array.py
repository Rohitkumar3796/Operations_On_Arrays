import array
# class array.array(typecode[,initializer])('i' is a typecode and i means integer
arr=array.array('i',[1,2,3,4,5])
while True:
    print("1 is for print numbers ")
    print("2 is for add number")
    print("3 is for delete number")
    print("4 is for delete number by index")
    print("5 is for exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        for i in arr:
            print(i)
    elif choice==2:
        val=int(input("enter the number"))
        arr.append(val)
        print(arr)
    elif choice==3:
        value=arr.pop() #pop is use to delete element from list by index or without index (it deletes last added value)
        print(value,"the last item is deleted")
        print(arr)
    elif choice==4:
        del_no_ind=int(input("enter the number u want to delete from the list:"))
        value1=arr.pop(del_no_ind)
        print(value1,'the elemnet u entered is deleted')
        print(arr)
    elif choice==5:
        exit()  
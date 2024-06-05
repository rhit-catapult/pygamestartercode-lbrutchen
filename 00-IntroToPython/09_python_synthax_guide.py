def main():
    #Lily Brutchen
    print("python Syntax guide")
    variables()
    loops()
    sequences()
def variables():
    print("--------variables--------")
    x=7
    b="bob"
    print(x+3)
    print(b*3)
    print(type(x))
    print(type(b))
def strings():
    print("----strings-----")
    str1 = "Can't"
    str2 ='Dave'
    str3 ='''can use' or " or even seprate line'''
    print(str1)
    print(str2)
    print(str3)
    str4= f"x exauls {x}. Fun."
    print(str4)
def loops():
    x=0
    while True:
        x=x+1
        if x>5:
            break
    print(f"x is eqaul to {x}")
    for k in range(5):
        print(k)
    total=0
    for k in range(1,101):
        total= total+k
    print(total)
    total=1
    for k in range(1,101):
        total= total*k
    print(total)
def sequences():
    print("-------sequences-")
    my_list=[4,5,6,7]
    print(my_list)
    my_list[2]=99
    print(my_list)
    my_list.append(1000)
    print(my_list)
    print(f"the lenght of the list is {len(my_list)}")
    for k in range(len(my_list)):
        my_list[k]+=10
    print(my_list)
    product=1
    for k in range(len(my_list)):
       product=product*my_list[k]
    print(product)
main()
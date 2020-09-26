TempStr = input()
if eval(TempStr)==0:
    print("Hello World")
elif eval(TempStr)>0:
    string="Hello World"
    st = '';
    for i in range(len(string)):
        if (i+1)%2 != 0:
            st = st+string[i];
            if len(string) == (i+1):
                print(st);
        else :
            st = st+string[i];
            print(st);
            st = '';
else:
    string="Hello World"
    for i in range(len(string)):
        print(string[i]);

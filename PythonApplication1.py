#First time using python
print("1.Add");
print("2. Subtract");
print("3. Multiply");
print("4. Divide");
print("5. Exit Program");
choice=int(input("enter your choice:"));
if (choice>=1 and choice<=4):
        print("Enter two numbers: ");
num1=int(input());
num2=int(input());
if choice==1:
    res=num1+num2;
print("Result = ",res);
if choice==2:
    res=num1+num2;
print("result = ",res);

#I made some changes
print("Success! Project pushed to github.");
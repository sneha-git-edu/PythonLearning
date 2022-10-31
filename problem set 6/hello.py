name=input('enter your name :')
with open("hello.txt" , "a") as file :
    file.write(f'hello,{name}\n')


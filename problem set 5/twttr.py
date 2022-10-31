def main():
    text = input('input: ')
    print('output:',shorten(text))

def shorten(text):
    for i in text :
        if i in ('A','E','I','O','U','a','e','i','o','u'):
            text = text.replace(i,'')
    return text.lower()

if __name__ == "__main__":
    main()
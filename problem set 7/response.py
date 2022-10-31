from validator_collection import validators, checkers 
def main():
    print(validation(input("What's your email address? ").strip()))

def validation(s):
    try:

        if validators.email(s) :
            return 'valid'
    except  :
        return 'invalid'
if __name__ == "__main__":
    main()
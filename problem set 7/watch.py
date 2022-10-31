import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    links = re.compile(r"https?://(www\.)?youtube\.com/.+/[a-z0-9]+")
    link = links.search(s)
    link = link.group()
    match = re.sub(r"(www\.)?youtube\.com/.+",r"youtu.be", link)
    return match

                           

    






if __name__ == "__main__":
    main()
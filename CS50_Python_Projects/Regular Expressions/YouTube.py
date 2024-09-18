# converterer en html søgeadresse til en kortere der kan ses på youtube

import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # input example: <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
    # output example: https://youtu.be/xvFZjo5PgG0
    # [^>]+ matches any characters that are not >, ensuring we are within the iframe tag. (da den lukkes med iframe>)
    URL = re.search(r'<iframe[^>]+src="https?://www\.youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if URL:
        video_id = URL.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return "Invalid Input"
  

       


if __name__ == "__main__":
    main()
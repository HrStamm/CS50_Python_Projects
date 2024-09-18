# Working 9-5
# Omskriver AM og PM til militær-tid (digitalt ur)
# input eksempel 9:00 AM to 5:00 PM eller 9 AM to 5 PM

import re

def main():
    print(convert(input("Hours: "))) 

def convert(s):
    # laver en regular expression til timerne som skal være 0-24 
    # 2[0-4] matches numbers from 20 to 24.
    # 1[0-9] matches numbers from 10 to 19.
    # [0-9] matches single-digit numbers from 0 to 9.
    # sammme princip med minutterne som skal være 0-59
    # ?: er en non capturing group 
    # \s* er en whitespace 
    
    hours = r"(2[0-3]|1[0-9]|0?[0-9])(:[0-5][0-9])?"
    pattern = rf"^\s*{hours}\s*(AM|PM)\s*to\s*{hours}\s*(AM|PM)\s*$"
    time = re.search(pattern, s, re.IGNORECASE)
    
    # sætter de forskelligfe elementer i inputtet lig de tilhørende grupper
    # hvis minut tallet ikke eksitere i inputtet sættes det lig 00
    if time:
        start_hour = int(time.group(1))
        start_minute = time.group(2) if time.group(2) else ":00"
        start_period = time.group(3).upper()
        
        end_hour = int(time.group(4))
        end_minute = time.group(5) if time.group(5) else ":00"
        end_period = time.group(6).upper()

        # konverter til 24 timers periode 
        if start_period == "AM":
            if start_hour == 12:
                start_hour = 0
        elif start_period == "PM":
            if start_hour != 12:
                start_hour += 12

        # konverter til 24 timers periode 
        if end_period == "AM":
            if end_hour == 12:
                end_hour = 0
        elif end_period == "PM":
            if end_hour != 12:
                end_hour += 12
        
        # returner stringen 
        return f"{start_hour:02}{start_minute} to {end_hour:02}{end_minute}"

    else:
        return "Invalid input"
    


if __name__ == "__main__":
    main()
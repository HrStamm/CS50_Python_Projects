from Twitter import shorten 

def test_string():
    assert shorten("Hello") == "Hll"
    assert shorten("Just testing my Twitter") == "Jst tstng m Twttr"
    assert shorten("aeuOiIA") == ""

def test_digits():
    assert shorten("999") == "999"



    

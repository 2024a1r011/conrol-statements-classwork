# Write a python program to detect whether a comment is spam or not . A comment should be treated as sapm if it contains any of these keywords : "make a lot of money" ,"buy now","subscribe this" , or "click this"

mssg = input("Enter a message : ")

if "make a lot of money" in mssg or "buy now" in mssg or "subscribe this" in mssg or "click this" in mssg:
    print("its a spam message")
else:
    print("Not a spam ")
try:
    print("try") 
    print(10/0)
except ZeroDivisionError:
    print("exception captured in except block")
finally:
    print("finally")


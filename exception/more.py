try:
    file = open("file.txt", "r")
    info = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    
    

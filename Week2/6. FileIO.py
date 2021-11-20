with open("input.txt","r") as fileInput:
    # Reading whole document at once
    st=fileInput.read()
    print(st)
    
    # Reading line by line
    for line in fileInput:
        print("NewLine : ",line)
    
    fileInput.close()
largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num.lower() == 'done':
        break
    else:
        try:
            num = int(num)
            if largest == None:
                largest = num
            else:
                if num > largest:
                    largest = num
                else: None
            if smallest == None:
                smallest = num
            else:
                if num < smallest:
                    smallest = num
                else: None
        except:
            print 'Invalid input'

print 'Maximum is', largest
print 'Minimum is', smallest
largest = None
smallest = None
while True:
    num = input('enter a number')
    if num == 'done':
        break
    try:
        sum = [int(num)]
        for i in sum:
            if smallest is None:
                smallest = i
                if largest is None:
                    largest = i
            elif i < smallest:
                smallest = i
            else:
                largest = i
    except:
        print('Invalid input')
    
            
print('Maximum', largest)           
print('Minimum',smallest)


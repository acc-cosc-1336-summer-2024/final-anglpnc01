#write functions here, don't add input('') statements here!

def create_multiplication_table(total = 10): #total of 10x10 by default!!
    #2_D list

    list = []
    
    for i in range(1, total + 1):
        
        row = [i * j for j in range(1, total + 1)] #from 1 to 'total'
        
        list.append(row)
    
    return list

def display_multiplication_table(list):

    for row in list:

        print(" ".join(f"{num:4}" for num in row))



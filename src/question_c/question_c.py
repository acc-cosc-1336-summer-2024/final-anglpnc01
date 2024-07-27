#write functions here, don't add input('') statements here!
#design a program that asks a user for 5 numbers and displays the following statistics
#lowest, highest, total, average
#print the results for every entry

def list_of_numbers():

    numbers = []
    print('Please enter 5 numbers: ') #ensure that 5 numbers is the maximum!!

    while len(numbers) < 5:

        try:
            number = float(input(f'Number {len(numbers) + 1}: '))
            numbers.append(number)

        except ValueError:
            print('Invalid, try again')

    return numbers

def display_stats(numbers): #display for the given list of numbers

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers) #5??

    print("\nStats!: ")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of numbers: {total}")
    print(f"Average of numbers: {average:.2f}")

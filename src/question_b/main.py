from question_b import create_multiplication_table, display_multiplication_table

def main():

    while True:
    
        new_table = create_multiplication_table()

        display_multiplication_table(new_table)

        user_input = input("Do you want to view the table again? (yes/no): ").strip().lower()

        if user_input not in ['yes', 'y']:
            print("Exiting...")
            exit()

main()
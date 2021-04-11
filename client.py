import db

print("\nClient Command Line Interface for PostgreSQL database")
user_input = ""
while user_input.lower() != "exit":
    user_input = input("\nAdd to database [add], view database [view], or exit [exit]: ")
    if user_input.lower() == "add":
        db.main()
    elif user_input.lower() == "view":
        db.print_table()
    elif user_input.lower() != "exit":
        print("Invalid Command, Try Again.")
print("Exiting Program...")

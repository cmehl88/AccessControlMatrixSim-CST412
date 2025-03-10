"""
Carson Mehl
Assignment 3
Prof. Bui
11/4/2024
Description/How to run: This assignment was to simulate the creation and upkeep of
a Capabilities (the rows are subjects) ACM (Access Control Matrix) where The users,
files, and the rights to the files that those users have can be first loaded, then
added or removed. When running the program, you're first presented with the menu
of options to choose from and the first option will always be 1, loading the initial
acm list from a given text file. From there it can be printed, updated, and Evaluated
in any order on after initially being loaded by given a chosen filename.
"""

acm = {} # The ACM structure by Capabilties (Subjects)

def main():
    while True:
        # The menu with the options
        print("\nInput a number for the option you want below.")
        print("Menu:")
        print("1. Load the input entries")
        print("2. Print current ACM")
        print("3. Update ACM entries from a file")
        print("4. Evaluate access requests from a file")
        print("5. Quit the program")
        choice = input("Enter your number option: ")

        # Collect file name input with option chosen
        if choice == "1":
            filepath = input("Enter the filename for ACM entries: ")
            load_acm_entries(filepath)
        elif choice == "2":
            print_acm()
        elif choice == "3":
            filepath = input("Enter the filename for ACM updates: ")
            update_acm_entries(filepath)
        elif choice == "4":
            filepath = input("Enter the filename for access requests: ")
            evaluate_the_requests(filepath)
        elif choice == "5":
            print("Completed")
            break
        else:
            print("\nInvalid choice. Make sure it's only a number 1-5, Please try again.") # Error option

# Prints current ACM onto console, each user indented
def print_acm():
    for subject, permissions in acm.items():
        print(f"{subject}:")
        for obj, rights in permissions.items():
            print(f"  {obj}: {rights}")
    print()

# Loads ACM entries from the specified file
def load_acm_entries(filepath):
    global acm 
    acm.clear()  # First clear any existing entries from before
    # Using a try catch to force correct file names 
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    subject, obj, rights = line.split(',')
                    if subject not in acm:
                        acm[subject] = {}
                    acm[subject][obj] = acm[subject].get(obj, '') + rights  # Concatenate rights if they exist
        print("\nACM entries loaded.")
    
    except FileNotFoundError: # The output message for incorrect filename
        print(f"\nError: The file '{filepath}' is not found. Please make sure the file is in the folder with the other txt's\nAlong with to add the extension.")

def update_acm_entries(filepath):
    # Updates the ACM entries based on changes made from the sample-update-acm-entires file
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                action, subject, obj, right = line.split(',')
                
                # If the action is to add
                if action == "add":
                    if subject not in acm:
                        acm[subject] = {}
                    # Check if the object already exists for the subject
                    if obj in acm[subject]:
                        if right not in acm[subject][obj]:
                            acm[subject][obj] += right  # Add the new right
                            print(f"add,{subject},{obj},{right}: Successfully Updated.")
                        else:
                            print(f"add,{subject},{obj},{right}: Already exists.")
                    else:
                        acm[subject][obj] = right  # If it doesn't exist then create it
                        print(f"add,{subject},{obj},{right}: Successfully Updated.")
                
                # If the action is to remove
                elif action == "remove":
                    if subject in acm and obj in acm[subject] and right in acm[subject][obj]:
                        # Remove the right
                        acm[subject][obj] = acm[subject][obj].replace(right, '')
                        # Clean up empty entries
                        if not acm[subject][obj]:
                            del acm[subject][obj]
                        print(f"remove,{subject},{obj},{right}: Successfully Updated.")
                    else:
                        print(f"remove,{subject},{obj},{right}: Invalid Update. Entry Not Found.")

# Output whether to Permit or Deny from the given sample-requests.txt file/Whatever file you input
def evaluate_the_requests(filepath):
    # Evaluates the access requests and checks if each one is PERMIT or DENY
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip() # lets remove any extra spaces
            if line:
                subject, obj, right = line.split(',') 
                # If it's in the list then permit, if not then deny
                if subject in acm and obj in acm[subject] and right in acm[subject][obj]:
                    print(f"{subject},{obj},{right}: PERMIT")
                else:
                    print(f"{subject},{obj},{right}: DENY")
    print("-------------------------------")                
    print("Evaluation Complete.")

# Lets run the program!
main()



user_choice = input("Rock, Paper, or Scissors? (r/p/s)").lower()
choices = ('r','s','p')

if user_choice not in choices:
    print("Invalid Choice")
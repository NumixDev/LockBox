import json


# loads the JSON file
def load_passwords():
  with open("passwords.json", "r") as f:
    passwords = json.load(f)
  return passwords


# list accounts of JSON file
def list_accounts(passwords):
  print("Accounts registred:")
  for account in passwords:
    print(account)


# clones Password
def clone_password(account, passwords):
  if account in passwords:
    password = passwords[account]
    print(f"Password of '{account}' : {password}")
  else:
    print(f"The account '{account}' was not found")


# main Loop
def main_loop():
  passwords = load_passwords()
  while True:
    command = input("Load a command (list, clone-{account name}, exit): ")
    if command == "list":
      list_accounts(passwords)
    elif command.startswith("clone-"):
      account = command[6:]
      clone_password(account, passwords)
    elif command == "exit":
      break
    else:
      print("Is not a vaild command.")


# starter main
if __name__ == "__main__":
  main_loop()

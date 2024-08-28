#FirstProgram.py
#Name:
#Date:
#Assignment:

def main():
  #print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
  name = input("What is you name? ")
  #print(name)
  #Use the user's name in the program.
  print("hello", name)
  #Ask the user for their age.
  age = input("What is your age? ")
  #print(age)
  #Tell the user what year they were born in.
  age = int(age)
  born = 2024 - age
  print("You were born in", born)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

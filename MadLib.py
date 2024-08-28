#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("noun me,(person place or thing) ")
  noun2 = input("again ")
  noun3 = input("and again ")
  adj1 = input("an adjective this time ")
  noun5 = input("nvm, one more time ")
  noun6 = input("last time ")
  #Print the story with the user supplied words.
  print("This morning, I woke up and put on my", noun1 , ". Next, I brushed my", noun2 , ". After that, I walked to", noun3 , ". It was", adj1 , ". Next, I went to", noun5 ,"I ended my day at", noun6)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

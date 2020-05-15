# CPE 101 Lab 4
# Name:
# Section:

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      show_table(table_size, first, get_increment())
      table_size = get_table_size()

# Obtain a valid table size from the user
# none --> int
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))

   while (size) < 0:
      print ("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))
      
   return size;

# Obtain the first table entry from the user 
# none --> int
def get_first():
   first = int(input("Enter the value of the first number in the table: "))
   while first < 0:
      print("First number must be non-negative.")
      print(first)
      
   return first;

# Display the table of power5
# int, int, int  --> int (the total of the power)
def show_table(size, first, increment):
   print ("A power5 table of size %d will appear here starting with %d." % (size, first))
   print ("Number  Power5")
   

   # Insert Loop Here
   total = 0
   for n in range(first, first + size*increment, increment):
       power = n ** 5
       print("%-6d  %d" % (n,power))
       total += power
   print("\nThe sum of power5 is " + str(total) + "\n")

# the purpose of this function is get the increment between rows to put it in the show_table function
# none  --> int
def get_increment():
   increment = int (input("Enter the increment between rows: "))
   while increment < 0:
      print("Increment must be non-negative.")
      print(increment)
   return increment;

if __name__ == "__main__":
   main()

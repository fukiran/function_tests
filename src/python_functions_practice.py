def return_10():
    return 10

# def test_return_10(self):
      # return_10_result = return_10()
      # self.assertEqual( 10, return_10_result )

def add(num1, num2):
    return num1 + num2
    
# def test_add(self):
    #  add_result = add( 1, 2 )
    #  self.assertEqual( 3, add_result )

def subtract(num1, num2):
    return num1 - num2

# def test_subtract(self):
      # subtract_result = subtract( 10, 5 )
      # self.assertEqual( 5, subtract_result )

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return str(string_1) + str(string_2)

def add_string_as_number(num1, num2):
    return int(num1) + int(num2)

def number_to_full_month_name(num):
    if (num == 1):
          return "January"
    elif (num == 3):
        return "March"
    elif (num == 9):
        return "September"

def number_to_short_month_name(num):
    if (num == 1):
          return "Jan"
    elif (num == 4):
          return "Apr"
    elif (num == 10):
          return "Oct"

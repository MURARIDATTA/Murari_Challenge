# Murari_Challenge-
This function determines whether a given credit card number is valid based on specific rules.
It returns "Valid" if the number meets all the rules, otherwise "Invalid".
   *It checks right away if there are spaces in the number and marks it as "Invalid" if there are.
   *The number should begin with '4', '5', or '6'. If not, it's immediately considered "Invalid".
   *Removes any hyphens to make it easier to check the rest of the rules.
   *The number should be exactly 16 digits long and should contain only numbers after removing hyphens.
   *If the original number had hyphens, the function checks that they were used to divide the number into groups of four digits.
   *It checks for sequences where the same digit repeats four or more times in a row.
   
has_four_consecutive_identical_digits(number):This function looks for any part of the number where the same digit shows up four or more times in a row.

Main Function:  It reads credit card numbers from the input, skips the first line (usually the number count), and then uses the validation function on each credit card number to check if it's valid.

When you run this script, you can feed it credit card numbers through the command line or from a file. It reads all input at once, breaks it into lines, and processes each line (except for the first one). It then prints out "Valid" or "Invalid" based on each number's validity.

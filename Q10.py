card_number_input = input("Please enter the credit card number to check: ")

cleaned_number = ""
for character in card_number_input:
    if character.isdigit():
        cleaned_number = cleaned_number + character

digits = []
for digit_char in cleaned_number:
    digits.append(int(digit_char))

number_of_digits = len(digits)
for i in range(number_of_digits - 2, -1, -2):
    doubled_digit = digits[i] * 2

    if doubled_digit > 9:
        doubled_digit = doubled_digit - 9

    digits[i] = doubled_digit

total_sum = sum(digits)

if total_sum % 10 == 0:
    print("\nResult: This credit card number is VALID.")
else:
    print("\nResult: This credit card number is INVALID.")
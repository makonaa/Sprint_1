def digit_root(num:int):
    num_len = len(str(num))
    #checks that number is longer than one digit
    while num_len > 1:
        num_sum = 0

        #gets the sum of the number's digits
        for i in range(num_len):
            num_sum += num % 10
            num //= 10

        #variables are overwritten with new values for further checks
        num = num_sum
        num_len = len(str(num))
    print(f'digital root is {num}')

digit_root(889987)
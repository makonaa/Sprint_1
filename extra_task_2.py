
def digit_root():
    num = int(input ('number:'))
    num_len = len(str(num))
    while num_len > 1:
        num_sum = 0

        for i in range(num_len):
            num_sum += num % 10
            num //= 10

        num = num_sum
        num_len = len(str(num))
    print(f'digital root is {num}')

digit_root()
input_string = input()
result = 0
digits = str("0 1 2 3 4 5 6 7 8 9").split()
op = str()
nums = []
for ch in input_string:
    if ch == "+" or ch == "*":
        op = ch
    elif ch in digits:
        nums.append(int(ch))

if op == "+":
    for i in nums:
        result += i
elif op == "*" and len(nums) != 0:
    result = 1
    for i in nums:
        result *= i

print(result)
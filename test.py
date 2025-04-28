'''
print("hello world");

firstNumber = 12;
secondNumber = 89;

sum = firstNumber + secondNumber;

print("Calculated number: ", sum);

secondNumber = "abc"
print("Length : ", len(secondNumber));
print(5*5)
print(16/5)
print(16%5)
print(15+5)
print(15-5)
print(10**2)

value1 = "Hello"
value2 = "Sumit"

finalValue = value1 + value2

print(finalValue)

print("first index "+finalValue[0])
print("0-4 index "+finalValue[:4])
print("0-4 index "+finalValue[7:])
print("0-4 index "+finalValue[-3])
print("0-4 index "+finalValue[4:9])
print("0-4 index "+finalValue[2:9:3])
print("0-4 index "+finalValue[::-1])
print("0-4 index "+finalValue[::-3])

print("Value {}".format(finalValue))
print("Value {} of {} & {}".format(finalValue, value1, value2))
print(f"This is the text {finalValue}")

n = 1890/17
print("Number is {num:1.3f}".format(num=n))

my_list = ["string", 1, "sumt", 1.59]

print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[:-1])
print(my_list.pop())
my_list.append("hahaha")
print(my_list)


my_dict = {}
print(my_dict)
my_dict['monday'] = 1
print(my_dict)
my_dict = {'monday': 1, 'tuesday': 2, 'wednesday': 3}
print(my_dict)
print(my_dict['monday'])

my_dict['tuesday'] = 8
print(my_dict)

my_dict = {"key1" : "hello", "key2" : [1,2,3,4,5],  "key3": {'monday': 1, 'tuesday': 2, 'wednesday': 3}}

my_dict["key2"][-3] = 9
print(my_dict)
print("key1" in my_dict)
print("key134" in my_dict)



my_set = set()
my_set.add(1)
my_set.add(3)
my_set.add(3)
print(my_set)

my_set = set([11,33,22,11,33,22])
print(my_set)

print(11 in my_set)



my_stack = []
my_stack.append(123)
my_stack.append(23)
print(my_stack.pop())
my_stack.append(231)
my_stack.append(False)
my_stack.append(545)
my_stack.append("hello")
my_stack.append(True)
my_stack.append("sumit")
print(my_stack)
print("Peek - {}".format(my_stack[-1]))
print(len(my_stack))


my_qeque = []
my_qeque.append(123)
my_qeque.append(23)
print(my_qeque)
my_qeque.pop(0)
print(my_qeque)
my_qeque.append(231)
my_qeque.append(False)
my_qeque.append(545)
my_qeque.append("hello")
my_qeque.append(True)
my_qeque.append("sumit")
print(my_qeque)
print(my_qeque[0])
print(my_qeque)

val = "mulad"
num1 = 10
num2 = 15

if val == "add":
    print(num1 + num2)
elif val == "sub":
    print(num2 - num1)
elif val == "div":
    print(num2/num1)
else:
    print(num1 * num2)

newVal = 25 if val == "add" else "new value"
print(newVal)


val = [1,4,6,2]

for i in val:
    print(i)

for index in range(10):
    print(f"range: {index}")

for index, item in enumerate(val):
    print("Index {}, value {}".format(index, item))

f = 0
while f < 5:
    print(f)
    f += 1
else:
    print("Value is equal to 5")

my_list1 = [1,2,3,4,5]
my_list2 = ['a','d','a','2']
my_list3 = [True, False]

for a, b, c in zip(my_list1, my_list2, my_list3):
    print(a,b,c)

print(3 in my_list1)

my_listCombo = [word for word in "this is sumit's code!"]
print(my_listCombo)
my_listCombo1 = [x for x in range(0,17) if x % 2 == 0]
print(my_listCombo1)
my_listCombo2 = [x if x%2 == 0 else  "ODD" for x in range(0,17)]
print(my_listCombo2)

def print_numbers(number):
    for n in number:
        print(n)

print_numbers([1,4,5,7])

def sum_numbers(number):
    sum = 0
    for n in number:
        sum += n
    
    return sum

print(sum_numbers([1,4,5,7]))

def find_number_with_index(numbers, number):
    index = 0;
    for n in numbers:
        if n == number:
            return (index, number)
        index += 1
    
    return (-1, number)

print(find_number_with_index([1,4,5,7], 4))
print(find_number_with_index([1,4,5,7], 14))
'''

lambda_list = [1, 2,4,5,6]

def even_or_not(num: int) -> bool:
    return True if num % 2 == 0  else False

new_lambda_list = map(even_or_not, lambda_list)
print(list(new_lambda_list))

print(list(filter(even_or_not, lambda_list)))
print(list(filter(lambda num: num % 2 == 0 , lambda_list)))

def hello(val: int):
    print(val)

hello("12")


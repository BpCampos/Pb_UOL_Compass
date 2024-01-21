# Python

## **What is Python?**

- Is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.
- To run a program in python we just need to write in the terminal: python <programName>.py
- Python is a interpreted language, unlike C that is a compiled language

- **`Compilation`** – the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an *.exe* file if the code is intended to be run under MS Windows) containing the machine code. Now you can distribute the file worldwide; the program that performs this translation is called a **compiler** or **translator**.

- **`Interpretation`** – you (or any user of the code) can translate the source program each time it has to be run. The program performing this kind of transformation is called an **interpreter**, as it interprets the code every time it is intended to be executed. It also means that you cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.

## **Python built in functions**

[Built-in Functions](https://docs.python.org/3/library/functions.html)

- Python cares about `indentation`, so we cannot put the start of an equation in one line and the next in another for example

```python
#Print Hello World in Python
print('Hello World')
```

- The `print()` function has two keyword arguments that you can use for your purposes. The first is called end.

```python
#By default the 'end' key word comes implicitly with '\n' that jumps to another line. In this case when the print function reaches the end it does jump to another line
print("My name is", "Python.", end=" ")
print("Monty Python.")
```

- As you can see, the `end` keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments.
- The default behavior reflects the situation where the end keyword argument is **implicitly** used in the following way: `end="\n"`.
- We said previously that the `print()` function separates its outputted arguments with spaces. This behavior can be changed too.
- The **keyword argument** that can do this is named `sep` (as in *separator*).

```python
print("My", "name", "is", "Monty", "Python.", sep="-")
#The output: My-name-is-Monty-Python
```

- To get a user input in python we can import `get_string()` from C, or use the built in input function from python

```python
answer = get_string("What's your name?")
print("hello, " + answer)
```

- Another way to print anything is using `f` inside the print function alongside with `{answer}`
- We need a `already created variable` to allocate into the interpolation
- Or we can use the `.format(<value>)`

```python
answer = 'Bruno'
#By using f, we can use the answer variable inside the string
print(f "hello, {answer}") #This is called interpolation

print("hello, {}".format('Bruno')) #Another way to use interpolation
```

- We can `comment` in our code using `#` as shown in the examples above
- types of variables in python
  - `boolean` → **True/False**
  - `float` → **1.2**
  - `integer` → **12**
  - `string` → **‘something’** or **“something”**
- `set()` in python set is a collection of values without duplicates
- `.lower()` convert all values to lowercase

```python
#The value in the variable will be converted to lowercase
variable.lower()
```

-

## Operators

- **All python operators:**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/51282dd0-38dd-4009-bfbb-3f8d4cadedd6/a2290bbb-e0cc-494b-860b-92ea8ec3b79e/Untitled.png)

- The `**` operator is the **exponential** so 2e3 or 2 \*\* 3 means 2 in the power of 3

**Remember**: It's possible to formulate the following rules based on this result:

- when **both** **`**`\*\* arguments are integers, the result is an integer, too;
- when **at least one** **`**`\*\* argument is a float, the result is a float, too.
- **`The result produced by the division operator is always a float`**
- A **`//`** (double slash) sign is an **integer division** operator. It differs from the standard **`/`** operator in two details:
  - Its result lacks the fractional part ‒ it's absent (for integers), or is always equal to zero (for floats); this means that **the results are always rounded down**;
  - It conforms to the *integer vs. float rule*. and it is basically `Math.floor()` from Javascript
- A **`unary`** operator is an operator with only one operand, e.g., -1, or +3.
- A **`binary`** operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.
- The **binding** of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression.
- Most of Python's operators have `left-sided binding`, which means that the calculation of the expression is conducted from `left to right`.
- The result clearly shows that **the `exponentiation operator` uses `right-sided binding`**.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/51282dd0-38dd-4009-bfbb-3f8d4cadedd6/852a1082-d963-4ddd-a2ab-dec9ee3315d2/Untitled.png)

## Conditionals in Python:

```python
if x < y:
		print("x is less than y")
else:
		print("x is not less than y")
```

- Using if and else together, we got something like this:

```python
if x < y:
		print("x is less than y")
elif x > y:
		print("x is greater than y")
else:
		print("x is equal to y")
```

- We can use `range()` alongside with `if` to check if a value is in a certain range

```python
def faixa_etaria(idade):
	if 0 <= idade < 18:
		return 'Menor de idade'
	elif idade in range(18, 50)
		return 'Adulto'
```

## Ternary Operators

- ‘My clothes are ‘ + `(’wet.’ if is_raining else ‘dry.’)`
- We use the `if` in the same line as the result of the condition
- `biggest_number = a if (a > b) else b`

## Match case

- Used when we would have many `if/else` cases, instead we use `match`

```python
def get_dia_semana(dia):
    match dia:
        case 1:
            return 'Domingo'
        case 2:
            return 'Segunda'
        case 3:
            return 'Terça'
        case 4:
            return 'Quarta'
        case 5:
            return 'Quinta'
        case 6:
            return 'Sexta'
        case 7:
            return 'Sabado'
        case _:
            return '** inválido **'



if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
```

## Variables

```python
#In python you don't need to add the type or the semicolon
counter = 0
#To increase the value of counter
counter = counter + 1
#or
counter += 1
```

- The name of the variable must not be any of Python's reserved words

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/51282dd0-38dd-4009-bfbb-3f8d4cadedd6/5c4a1d95-aa48-4aab-91a0-d9abb1de5f4d/Untitled.png)

- They are called **`keywords`** or (more precisely) **reserved keywords**. They are reserved because **you mustn't use them as names**: neither for your variables, nor functions, nor any other named entities you want to create.
- Python offers a more convenient way of doing the swap of two variables:

```python
variable_1 = 1
variable_2 = 2
#Variable 1 will now variable 2 valeu and vice versa
variable_1, variable_2 = variable_2, variable_1
```

## Interaction with user

- \***\*The `input()` function is able to read data entered by the user and to return the same data to the running program.**
- the **result of the `input()` function is a `string`**. A string containing all the characters the user enters from the keyboard. It is not an integer or a float
- **`Type casting` → Python offers two simple functions to specify a type of data and solve this problem ‒ here they are: `int()` and `float()`.**
- The `*` (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a **replication operator, it multiplies the string repeating it by number you passed**
- **Ex: 5 _ "2" (or "2" _ 5) gives "22222" (not 10!)**
- We can turn numbers into strings using `str()` as well
- `Strings` are **immutable**, we cannot assign another value to a character in a string

## Making decisions

- To ask the question if two values are equal, you use the `==` (equal equal) operator.
- The `!=` (not equal to) operator compares the values of two operands, too. Here is the difference: if they are equal, the result of the comparison is False. If they are not equal, the result of the comparison is True.
- **Conditionally executed statements have to be indented**. This creates a very legible structure, clearly demonstrating all possible execution paths in the code.

```python
if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
	feed_the_sheepdogs()#This one is not indented and does belong to the if block
```

- The way to assemble subsequent *`if-elif-else`* statements is sometimes called a **cascade**.
- `else` is always the **last branch of the cascade**, regardless of whether you've used `elif` or not;
- `else` is an **optional** part of the cascade, and may be omitted;

## Loops

```python
#Using while
i = 0
while i < 3:
		print("car")
		i += 1

#Using for
for i in [0,1,2]:
		print("hello, world")

#Another way of writing this would be
for i in range(3):
		print("hello, world")
```

- Python does not have arrays, it has `lists` and we can use the function `range` to create that list for us
- For an infinite loop, we can use `while True:` with a capital T in true
- If you want to execute **more than one statement inside one while loop**, you must (as with `if`) **`indent`** all the instructions in the same way;

```python
odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
```

- the *`for`* keyword opens the for loop; note – there's no condition after it; you don't have to think about conditions, as they're checked internally, without any intervention;
- We can get the `index` of the iterable values by using `enumerate()` → `**for position, name in enumerate(<iterable>)**`
- the `range()` function (this is a very special function) is responsible for generating all the desired values of the control variable; in our example, the function will create (we can even say that it will **feed** the loop with) subsequent values from the following set: 0, 1, 2 .. 97, 98, 99; note: in this case, the `range()` function starts its job from 0 and finishes it one step (one integer number) before the value of its argument;
- The `range()` function invocation may be equipped with two or even three arguments, not just one
- **`range(start, stop, step)`**
- These two instructions are:
  - `break` – exits the loop immediately, and unconditionally ends the loop's operation; the program begins to execute the nearest instruction after the loop's body;
  - `continue` – behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.

```python
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue #This will skip the print of the inside the loop 3
    print("Inside the loop.", i)
print("Outside the loop.")
```

- Additions, which don't improve the language's expressive power, but only simplify the developer's work, are sometimes called **`syntactic candy`**, or `syntactic sugar`.

## and / or - **logical operators**

- **logical operators**
- `and` is called a **conjunction**
- `or` is called a **disjunction**
- For `True` **and** `False` we get → `False`
- For `True` **or `False`** we get **→ `True`**
- `not` is the opposite of what is passed: `not True` = `False` and vice-versa
- Here are all of the **bit operators**:
  - `&` (ampersand) ‒ bitwise conjunction;
  - `|` (bar) ‒ bitwise disjunction;
  - `~` (tilde) ‒ bitwise negation;
  - `^` (caret) ‒ bitwise exclusive or (xor).
- The difference in the operation of the logical and bit operators is important: **the logical operators do not penetrate into the bit level of its argument**. They're only interested in the final integer value.

---

- We can use arrays to check if conditions, `if s in [”Y”, “y”]` , this will check if s is either `Y` or `y`
- Python support OOP(Object Oriented Programming) paradigm

## **Lists**

```python
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.
```

- The value inside the brackets which selects one element of the list is called an **`index`**, while the operation of selecting an element from the list is known as **`indexing`**.
- Using the `len()` function we can grab the length of a list. The same with `.length` from Javascript
- We can reverse the list with `reversed()`
- Or use `list.reverse()`
- To remove elements of a list → `del` - *`del* numbers[1]` . Note that this is a instruction and not a function
- You can delete de whole list by calling `del` and the list name
- A **method is a specific kind of function** ‒ it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.
- **A typical method invocation usually looks like this:**

```python
#The name of the method is preceded by the name of the data which owns the method
result = data.method(arg)
#Example
list.append(value) #Add elements into a list
list.insert(location, value)
```

- A new element may be added to the `end` of the existing list: `list.append(value)`
- Instead of append, we can use the `+` to add elements to the end of the list
- The insert() method is a bit smarter ‒ it can add a new element **at any place in the list**, not only at the end: `list.insert(location, value)`
- When you insert a value, all the others jump one index to the `right`
- To see if a value is in the list, we can use the `in` or `not in`

```python
list = [1,2,3,'car', 4.15]

'car' in list # True
1 not in list # False
```

-

## Operations on lists

- The assignment: **_list_2 = list_1_** copies the name of the array, not its contents. In effect, the two names (list*1 and list_2) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa. If the values in the \*\*\_list_1*** changes, the values in the **_list_2_\*\* will change as well
- A `slice` is an element of Python syntax that allows you to **make a brand new copy of a list, or parts of a list**.

```python
list_1 = [1]
list_2 = list_1[:] #This [:] creates another list for list_2
list_1[0] = 2
print(list_2) #The result will be ' 1 '
```

- The `[:]` actually copies the list's contents, not the list's name, and produce a new list
- Another representation of `slice`

```python
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)#This will print [8,6]
```

- the new list will start at **_index 1 and go to index 3 - 1(it’s always end - 1)_**
- If you omit the `start` in your `slice` like `numbers[::]`, it is assumed that you want to get a slice beginning at the element with index 0.
- We can use a third parameter in `slice` to jump through the numbers or characters → `numbers[::2]`, it will get the numbers in the list skipping one place

```python
numbers = '123456789'
new_numbers = numbers[::2]
print(new_numbers) #Output: 13579
```

- Using `del` with `slice` removes the elements from the list and does not create another list

```python
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)#Result: [10, 4, 2]
```

- Python offers two very powerful operators, able to **look through the list in order to check whether a specific value is stored inside the list or not**.
- elem `in` my_list / elem `not in` my_list

```python
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)#False
print(5 not in my_list)#True
print(12 in my_list)#True
```

## **List comprehensions**

- A list comprehension is actually a list, but **created on-the-fly during program execution, and is not described statically**

```python
row = [WHITE_PAWN for i in range(8)]
squares = [x ** 2 for x in range(10)]#Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

- It can be created with `conditionals`

```python
double_even = [i * 2 for i in range(10) if i % 2 == 0]

print(double_even)
```

- Lets create a `two dimensional list`

```python
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
```

- The `board` variable is now a **two-dimensional array**. It's also called, by analogy to algebraic terms, a **matrix**.
- Within the same line as the list comprehension, we have `generators` that work similarly to the lists but gives the result on demand

```python
generator = (i ** 2 for i in range(10) if i % 2 == 0)

print(next(generator)) # Output: 0
print(next(generator)) # Output: 4
```

- You need to call `next` for the next value to appear. This method consumes much `less memory` than the `list comprehension`

## Functions

- **\*if a piece of code becomes so large that reading and understating it may cause a problem, consider dividing it into separate, smaller problems, and implement each of them in the form of a separate function**.\*
- This decomposition continues until you get a set of short functions, easy to understand and test.
- This is what the simplest function definition looks like:

```python
def function_name(): function_body
```

- It always starts with the **keyword `def`** (for *define*)
- next after def goes the **name of the function** (the rules for naming functions are exactly the same as for naming variables)
- after the function name, there's a place for a pair of **parentheses**
- the line has to be ended with a **colon `:`**
- **You mustn't invoke a function which is not known at the moment of invocation.**
- Remember - Python reads your code from top to bottom. It's not going to look ahead in order to find a function you forgot to put in the right place ("right" means "before invocation".)
- **`Parameterized functions` →** *def* *function*(parameter):
- **_It's legal, and possible, to have a variable named the same as a function's parameter._**

```python
def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)
```

- Another way of passing arguments is by `keyword`

```python
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
```

- the values passed to the parameters are preceded by the target parameters names, followed by the `=` sign. The position doesn't matter here
- We cannot pass `positional arguments` after `keyword arguments`

```python
def sum(a,b):
		return a + b

sum(a = 3, 2) #This will trigger an error
sum(a = 3, b= 2) #This works
```

- A function may have a `return` inside it. the `return` can be empty or extended with an expression
- Don't forget this: if a function doesn't return a certain value using a return expression clause, it is assumed that it **implicitly returns `None`**.

```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12

def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None
```

- Using `*` or `**` with a function, it’s possible to pass a `tuple`, in the case of, one `*` or a `dictionary` using `**`. This is called `args` e `kwargs`

```python
random_tuple = (4,2,8,7)

def sum(*numbers): # *numbers is a tuple
		sum = 0
		for n in numbers:
			sum += n
		return sum

#Packing
sum((1,3)) # Output: 4
#Unpacking
sum(random_tuple) # Output: 21
```

- Passing a `tuple` to a function like the example above is called `packing`. If we created a variable with a `tuple` before initializing the function and used the variable when calling the function instead of creating a tuple, it’s called `unpacking`
- For `dictionary` we have

```python
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')

#The way to pass information is not like a traditional dictionary
resultado_f1(primeiro='L. hamilton', segundo='M. Verstappen')
```

- A **variable existing outside a function has scope inside the function's body**.

```python
def my_function():
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function() # var = 2
print(var) #var = 1
```

- In the example above, if the function doesn’t have the variable `var`, it will use the var created outside
- If we want python to change the value of the variable that is outside the function, we need to add the keyword `global` to the variable inside the function(keeping in mind that they need to have the same name)
- `FIBONACCI FUNCTION`

  ```python
  def fib(n):
      if n < 1:
          return None
      if n < 3:
          return 1

      elem_1 = elem_2 = 1
      the_sum = 0
      for i in range(3, n + 1):
          the_sum = elem_1 + elem_2
          elem_1, elem_2 = elem_2, the_sum
      return the_sum

  for n in range(1, 10):  # testing
      print(n, "->", fib(n))
  ```

- **`Recursion` → I**s a **technique where a function invokes itself**

## Tuples / Dictionaries / sets

- `tuple` → I**s an immutable sequence type**. It can behave like a list, but it can't be modified
- **`tuples` prefer to use parenthesis,** although it's also **possible to create a tuple just from a set of values separated by commas**

```python
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
```

- You can create tuples with single values but it needs to end with a comma, because it needs to be different from normal variables. E.g. `one_element_tuple_2 = 1.,`
- You can’t assign new values to a position in a tuple e.g. `tuple_1[2] = 45,`
- The **`dictionary`** is another Python data structure. It's **not a sequence** type (but can be easily adapted to sequence processing) and it is **mutable**.

```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary["cat"]) # Output: 'chat'
```

- `Dictionary` is a set of **key-value** pairs
- To access a value of a dictionary, use `dictonary[value]`
- We can use the `in` / `not in` operators to check if a `KEY` exists inside a dictionary, it only works for `keys`, not values
- To access the keys inside a dictionary we can use `dictionary.keys()`
- You can use `.values()` instead of keys to the values
- The method `items()` return tuples **where each tuple is a `key-value pair`**
- To change a value of a key inside a dictionary, we need to use `nameOfTheDicitionary[<OldValue>] = newValue` e.g. `dictionary['cat'] = 'minou’`
- To add a new pair of key value to a dictionary, you can create a key and value that don’t exist already `dictionary['swan'] = 'cygne’`
- You can also insert an item to a dictionary by using the `update()` method → `dictionary.update({"duck": "canard"})`
- To remove a key, you can use de _`del`_ method → *`del* dictionary['dog']`
- Tuples are **immutable**, which means you cannot change their elements (you cannot **append** tuples, or **modify**, or **remove tuple elements**).
- Using `for` with `dictionary`

```python
product = {'name':'pen', 'price': 10, 'imported': True, 'stock': 793}

for key in product:
		print(key) # Ex: name

for value in product.values():
		print(value) # Ex: pen

for key, value in products.items():
		print(key, '=', value) # name = pen
```

- A `set` is a collection of values that cannot be duplicate and don’t have a set order inside the set

```python
set = {1,2,3,4, True, 'Maria', 19.32}
```

## Exceptions

- Similarly to javascript `try/catch`, the python language has `try/except` that let’s you run the code and try to work with possible errors

```python
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except:
    print('I do not know what to do.')
```

## Open/Close outside files

- Using methods like `open()` - `close()` - `write()` - `read()` we can go inside a file, get information from another file and use it inside our own

```python
arquivo = open('palavras.txt', 'r')# the 'r' means to read the file passed before it
arquivo.close()#It's necessary to close the file after using it
```

- `file.read()` → Used to read the file information and set it’s content into a variable if needed
- `file.readlines()` → Return all lines in the file, as a `list` where each line is an item in the list object
- If we use a `for` in the variable containing the `file read`, we get each character of the words inside the file. For this we need to use the function `splitlines()` alongside the variable containing the file content

```python
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print(registro)
```

- It’s not needed to use `file.read()` if we want to use the file content via streaming i.e. read line by line from the opened file. We can use the `for loop` with variable containing the `open(<file>)`
- We don’t need to close the file if function open starts with the `with` keyword. The file automatically close

```python
with open('file.csv') as file:
		for content in file:
			print(content)
```

- Using `csv.reader(<file>)` makes it easier to get the content from the file

## Spread operator

- In Python we can use `*` to work as a spread operator, like the `. . .` in Javascript

```python
numbers = [1, 2, 3, 4, 5, 6]

new_list = ['A', True, *numbers, 24]

print(new_list) # ['A', True, 1, 2, 3, 4, 5, 6, 24]
```

## Built-in-Functions

- To create or define a function in python, we need to use the word `def` follow by the function name
  ```python
  def main():
  	for i in range(3):
  		meow()
  ```
- To convert strings into numbers in Python, we use the `int()` function
- Inside the function `print()` there are other values we can pass that changes the way that the will occur
  ```python
  #Using end, we can make the '#' be printed in a line instead of a column, and the content inside the end will appear beside the first argument printed
  print('#', end='')
  ```
- The `sum()` function in Python display the sum of the numbers inside an array, while the `len()` function gets the length of the array. Using this, we can the average of an array of numbers

  ```python
  scores = [72, 73, 33]

  averge = sum(scores) / len(scores)
  print(f"Average: {average}")
  ```

- `append()` only works with lists and insert values in the end of a list, like `push()` in Javascript arrays
  ```python
  #To insert the value 2 in an array
  scores = []
  scores.append(2)
  ```
- `upper()` → turns the string into uppercase
  ```python
  word = 'car'
  word.upper()#CAR
  ```
- `strip()` → Remove spaces at the beginning and at the end of the string
- `min(<lista>)` → Return the lowest value in a list as long as the list contains only numeric values
- `title()` → Changes every fist letter in a word to upper case
- `type()` → Show the type of the variable passed as a parameter
- We can see all built in functions for certain types of data using `dir()` e.g. `dir(float)`
- `split()` → Can be used with a `string` to separate the characters into a list according to a parameter e.g. `‘nice day’.split() → [’nice’, ‘day’]`. If we do not pass a parameter, the `split` will count the blank spaces

---

## Import

- Python code in one module gains access to the code in another module by the process of importing it. The `import` statement is the most common way of invoking the import machinery, but it is not the only way.
- We can have our own modules by simply creating a file ended in `.py`, then defining a function for example and now we can import that function

```python
import teste #'teste' is a file I created that has the function 'ola'

teste.ola('Bruno')
```

- If the module file you created is in the same directory as the file importing it, the term `from` is not needed, however if it is in another directory, we need `from <directory_name> import <module>`
- To make a `directory` become a `package` we need to include a file called `__init__.py`
- `Decimal()` → module that let us work with float numbers without having an enormous number of decimal places. The number inside the Decimal function need have ‘**quotation marks’**

```python
from decimal import *

a = Decimal('23') * 3 #The result will have only 2 decimal places
```

- Other function that we can get with `decimal` is `getcontext`, that let us precise the amount decimal places

```python
Decimal(1) / Decimal(7) # 0.1428571...

getcontext().prec = 4
Decimal(1) / Decimal(7) # 0.1429
```

## Functional programming

### First class functions

- `zip` → Takes two lists and `merge them` together forming pairs with the `[0] value` from the **first list** with `[0] value` from the **second** e so on

### Lambda functions

- `Anonymous function`

```python
a = [1, 2, 3]
m = list(map(lambda i: i * 2, a))

print(m) # [2,4,6]
```

- `map` here works just like javascript. The use of `lambda` is essencial
- The `i` is the variable that will loop through the list or dictionary or tuple
- `filter` works the same way as in javascript

```python
carros = [
    {'marca': 'Honda', 'velocidade': 200},
    {'marca': 'Toyota', 'velocidade': 180},
    {'marca': 'Jaguar', 'velocidade': 250},
    {'marca': 'Mercedes', 'velocidade': 270},
]

a = filter(lambda c: c['velocidade'] > 200, carros)

print(list(a)) # [{'marca': 'Jaguar', 'velocidade': 250}, {'marca': 'Mercedes', 'velocidade': 270}]
```

- `reduce` works the same way as in javascript

```python
from functools import reduce

carros = [
    {'marca': 'Honda', 'velocidade': 200},
    {'marca': 'Toyota', 'velocidade': 180},
    {'marca': 'Jaguar', 'velocidade': 250},
    {'marca': 'Mercedes', 'velocidade': 270},
]
# Sum all cars speed
a = reduce(lambda velocidade, c: velocidade + c['velocidade'], carros, 0)

print(a) # 900
```

## PIP - Python Package Index

- Package manager for Python, much like NPM for Javascript
- `pip3 install <package_name>` → To install a package
- `pip3 uninstall <package_name>` → To uninstall
- `pip3 list` → Show a list of packages installed
- `pip3 list --outdated` → Check if there’s any outdated library
- `pip3 install --upgrade <package_name>` → Upgrade package

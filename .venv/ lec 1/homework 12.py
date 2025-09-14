def say_hi(name, age):
    return f"Hello, My name is {name} and I'm {age} years old"

assert say_hi ('Alex', 31) == "Hello, My name is Alex and I'm 31 years old", 'Test1'
assert say_hi('Frank', 36) == "Hello, My name is Frank and I'm 36 years old", 'Test2'
print('OK')

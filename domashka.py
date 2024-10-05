#1.Функция с параметрами по умолчанию:
def print_params(a=1, b="строка", c=True):
    print(f"a = {a}, b = {b}, c = {c}")

print_params()
print_params(5)
print_params(b=25)
print_params(c=[1, 2, 3])
#2.Распаковка параметров:
def print_params(a=1, b="строка", c=True):
    print(f"a = {a}, b = {b}, c = {c}")

values_list = [1, 'строка', True]
values_dict = {"a": 2, "b": "строчка но отличается", "c": False}
#3.Распаковка + отдельные параметры:
print_params(*values_list)
print_params(**values_dict)

def print_params(a=1, b="строка", c=True):
    print(f"a = {a}, b = {b}, c = {c}")

values_list_2 = [54.32, "Строка"]

print_params(*values_list_2, 42)
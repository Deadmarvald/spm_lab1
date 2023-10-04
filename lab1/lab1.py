memory = [] 
history = []  

decimal = int(input("Введіть скільки десяткових розрядів після коми показувати: "))
max_history_size = int(input("Введіть скільки обчислень зберігати у історії: "))

while True:
    try:
        while True:
            memory_operator = (input("Для відновлення результату натисніть R. Для перегляду історії натисніть H, для переходу на калькулятор введіть K: "))
            if memory_operator not in ['R', 'H', 'K']:
                raise ValueError("Недійсна функція. Введіть одину із цих: R (відновити), H (історія).")

            if memory_operator == 'K':
                break

            if memory_operator == 'H':
                print("\nІсторія обчислень:")
                for item in history:
                    print(f"{item}\n")
                continue
            elif memory_operator == 'R':
                print("\nрезультат збережених обчислень:")
                for item in memory:
                        print(f"{item}\n")
            else:
                print("Пам'ять порожня.")
                continue


        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, √, %,): ")

        if operator not in ['+', '-', '*', '/','^', '√', '%']:
            raise ValueError("Недійсний оператор. Введіть один із +, -, *, /, ^, √, %")

        if operator != '√':
            num2 = float(input("Введіть друге число: "))

        result = 0

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль недопустимо.")
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        elif operator == '√':
            result = num1 ** 0.5
        elif operator == '%':
            result = num1 % num2

        result = round(result, decimal)

        save_operator = (input("Хочете зберегти результат?(y/n): "))
        if save_operator.lower() == 'y':
            memory.append(f"{num1} {operator} {num2} = {result}")

        if len(history) >= max_history_size:
            del history[0]

        history.append(f"{num1} {operator} {num2} = {result}")

        print(f"Результат: {result}")

    except ValueError as e:
        print(f"Помилка: {e}")
    except ZeroDivisionError as e:
        print(f"Помилка: {e}")

    choice = input("Бажаєте виконати ще одне обчислення?(y/n): ")
    if choice.lower() != 'y':
        break


    # M (зберегти), R (відновити), H (історія).
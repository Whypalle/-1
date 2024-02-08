import datetime


def create_todo_list():
    # Получаем текущую дату
    today = datetime.date.today().strftime("%Y-%m-%d")

    # Создаем файл с текущей датой в качестве имени
    filename = f"{today}_todo_list.txt"
    file = open(filename, "w")

    # Записываем задачи пользователя в файл
    print("Введите свои задачи (для окончания ввода введите 'q'): ")
    while True:
        task = input()
        if task == "q":
            break
        else:
            file.write(task + "\n")

    # Закрываем файл
    file.close()
    print(f"Файл {filename} успешно создан!")


# Вызываем функцию для создания TO-DO листа
create_todo_list()

import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('autoservice.db')
cursor = conn.cursor()

# Создание таблицы для клиентов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        address TEXT
    )
''')

# Создание таблицы для записей на ремонт
cursor.execute('''
    CREATE TABLE IF NOT EXISTS repairs (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        date_time TEXT,
        problem TEXT,
        car_make TEXT,
        car_model TEXT,
        car_year INTEGER,
        car_plate TEXT,
        FOREIGN KEY(client_id) REFERENCES clients(id)
    )
''')

# Функция для добавления нового клиента
def add_client():
    name = input("Введите ФИО клиента: ")
    phone = input("Введите номер телефона клиента: ")
    address = input("Введите адрес клиента: ")

    cursor.execute("INSERT INTO clients (name, phone, address) VALUES (?, ?, ?)", (name, phone, address))
    conn.commit()
    print("Клиент успешно добавлен")

# Функция для записи на ремонт
def add_repair():
    client_id = int(input("Введите ID клиента: "))
    date_time = input("Введите дату и время записи на ремонт (гггг-мм-дд чч:мм): ")
    problem = input("Введите описание проблемы/работы: ")
    car_make = input("Введите марку автомобиля: ")
    car_model = input("Введите модель автомобиля: ")
    car_year = int(input("Введите год выпуска автомобиля: "))
    car_plate = input("Введите номерной знак автомобиля: ")

    cursor.execute("INSERT INTO repairs (client_id, date_time, problem, car_make, car_model, car_year, car_plate) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (client_id, date_time, problem, car_make, car_model, car_year, car_plate))
    conn.commit()
    print("Запись на ремонт успешно добавлена")

# Функция для вывода всех клиентов
def show_clients():
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    print("Список клиентов:")
    for client in clients:
        print(client)

# Функция для вывода всех записей на ремонт
def show_repairs():
    cursor.execute("SELECT * FROM repairs")
    repairs = cursor.fetchall()
    print("Список записей на ремонт:")
    for repair in repairs:
        print(repair)

# Основное меню программы
while True:
    print("\nМеню:")
    print("1. Добавить клиента")
    print("2. Добавить запись на ремонт")
    print("3. Показать список клиентов")
    print("4. Показать список записей на ремонт")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_client()
    elif choice == '2':
        add_repair()
    elif choice == '3':
        show_clients()
    elif choice == '4':
        show_repairs()
    elif choice == '5':
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

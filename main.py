class Bus:
    def __init__(self, bus_id, bus_number, capacity):
        self.bus_id = bus_id
        self.bus_number = bus_number
        self.capacity = capacity

    def update_bus(self, new_id=None, new_number=None, new_capacity=None):
        if new_id:
            self.bus_id = new_id
        if new_number:
            self.bus_number = new_number
        if new_capacity:
            self.capacity = new_capacity
        print(f"Автобус {self.bus_id} обновлен.")

    def read_bus(self):
        info = (
            f"Автобус ID: {self.bus_id}\n"
            f"Номер автобуса: {self.bus_number}\n"
            f"Вместимость: {self.capacity} мест"
        )
        print(info)
        return info

    def __str__(self):
        return f"Автобус {self.bus_id}: Номер - {self.bus_number}, Вместимость - {self.capacity}"


class Passenger:
    def __init__(self, passenger_id, name, age):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age

    def update_passenger(self, new_id=None, new_name=None, new_age=None):
        if new_id:
            self.passenger_id = new_id
        if new_name:
            self.name = new_name
        if new_age:
            self.age = new_age
        print(f"Пассажир {self.passenger_id} обновлен.")

    def read_passenger(self):
        info = (
            f"Пассажир ID: {self.passenger_id}\n"
            f"Имя: {self.name}\n"
            f"Возраст: {self.age}"
        )
        print(info)
        return info

    def __str__(self):
        return f"Пассажир {self.passenger_id}: Имя - {self.name}, Возраст - {self.age}"


class ShowInterface:
    def __init__(self):
        self.buses = {}
        self.passengers = {}

    def check_bus_class(self):
        print("\nПроверка работы класса Bus:")
        bus = Bus(1, "A123", 50)
        bus.read_bus()

        print("\nОбновляем автобус:")
        bus.update_bus(new_id=2, new_number="B456", new_capacity=60)
        bus.read_bus()

        print("\nИспользуем __str__ метод:")
        print(bus)

    def check_passenger_class(self):
        print("\nПроверка работы класса Passenger:")
        passenger = Passenger(101, "Иван Иванов", 30)
        passenger.read_passenger()

        print("\nОбновляем пассажира:")
        passenger.update_passenger(new_id=102, new_name="Петр Петров", new_age=35)
        passenger.read_passenger()

        print("\nИспользуем __str__ метод:")
        print(passenger)

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Проверить работу класса Bus")
            print("2. Проверить работу класса Passenger")
            print("3. Выход")

            try:
                choice = input("Выберите действие (1-3): ")

                # Проверка, что choice является числом
                choice = int(choice)

                if choice == 1:
                    self.check_bus_class()
                elif choice == 2:
                    self.check_passenger_class()
                elif choice == 3:
                    print("Выход из программы...")
                    break
                else:
                    print("Неверный выбор! Пожалуйста, выберите действие от 1 до 3.")
            except ValueError:
                print("Ошибка! Пожалуйста, введите число от 1 до 3.")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")


# Запуск интерфейса
interface = ShowInterface()
interface.run()

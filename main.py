class Bus:
    def __init__(self, bus_id, bus_number, capacity):
        self.bus_id = bus_id
        self.bus_number = bus_number
        self.capacity = capacity

    def update_bus(self, new_id, new_number, new_capacity):
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


class ShowInterface:
    def __init__(self):
        self.buses = {}

    def check_bus_class(self):
        print("\nПроверка работы класса Bus:")
        bus1 = Bus(1, "A123", 50)
        bus1.read_bus()

        print("\nОбновляем автобус:")
        bus1.update_bus(new_id=2, new_number="B456", new_capacity=60)
        bus1.read_bus()

        print("\nИспользуем __str__ метод:")
        print(bus1)

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Проверить работу класса Bus")
            print("2. Допишу")
            print("3. Выход")

            try:
                choice = input("Выберите действие (1-ага): ")

                # Проверка, что choice является числом
                choice = int(choice)

                if choice == 1:
                    self.check_bus_class()
                elif choice == 2:
                    print("Ща допишу")
                elif choice == 3:
                    print("Выход из программы...")
                    break
                else:
                    print("Неверный выбор! Пожалуйста, выберите действие от 1 до ага.")
            except ValueError:
                print("Ошибка! Пожалуйста, введите число от 1 до 3.")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")


# Запуск интерфейса
interface = ShowInterface()
interface.run()

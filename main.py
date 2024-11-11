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
 
class Ticket:
    def __init__(self,ticket_id):
        self.ticket_id = ticket_id

    def update_ticketid(self,ticket_id=None):
        self.ticket_id = ticket_id

    def read_ticket(self):
        info = (
            f"Номер билета: {self.ticket_id}\n"
        )
        print(info)
        return info

    def ticket_to_bus(self, bus_id):
        return str(self.ticket_id)[:2] == str(bus_id)[:2]

class Route:
    def __init__(self,route_id):
        self.route_id = route_id
    
    def update_routeid(self,route_id=None):
        self.route_id = route_id

    def read_route(self):
        info = (
            f"Номер маршрута: {self.route_id}\n"
        )
        print(info)
        return info

    def route_to_bus(self, bus_id):
        return str(self.route_id)[:2] == str(bus_id)[:2]

class Payment:
    def __init__(self,pay_way,amount):
        self.pay_way = pay_way
        self.amount = amount

    def update_payway(self,pay_way=None):
        self.pay_way = pay_way
    
    def update_amount(self,amount=None):
        self.amount = amount

    def read_payment(self):
        info = (
            f"Способ оплаты: {self.pay_way}\n"
            f"Сумма оплаты: {self.amount}\n"
        )
        print(info)
        return info
    





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

    def check_ticket_id(self):
        print("\nПроверка работы класса Ticket:")
        ticket = Ticket(123456)
        ticket.read_ticket()

        print("\nОбновляем билет")

        ticket.update_ticketid(ticket_id=133712)
        ticket.read_ticket()
        if(ticket.ticket_to_bus(133)):
            print("Hell yea")
        else:
            print("Oops")

    def check_route_id(self):
        print("\nПроверка работы класса Route:")
        route = Route(1212444)
        route.read_route()

        print("\nОбновляем маршрут")

        route.update_routeid(route_id=1919334)
        route.read_route()
        if(route.route_to_bus(191)):
            print("Hell yea")
        else:
            print("Oops")

    def check_payment(self):
        print("\n Проверка работы класса Payment")
        payment = Payment("Sberbank",1362)
        payment.read_payment()

        print("\n Обновляем данные по платежу")

        payment.update_amount(8579)
        payment.update_payway("T-Bank")
        payment.read_payment()
        if(payment.amount>=1000):
            print("Hell yea")
        else:
            print("Oops")

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Проверить работу класса Bus")
            print("2. Проверить работу класса Passenger")
            print("3. Проверить работу класса Ticket")
            print("4. Проверить работу класса route")
            print("5. Проверить работу класса Payment")
            print("6. Завершить программу")

            try:
                choice = input("Выберите действие (1-6): ")

                choice = int(choice)

                if choice == 1:
                    self.check_bus_class()
                elif choice == 2:
                    self.check_passenger_class()
                elif choice == 3:
                    self.check_ticket_id()
                elif choice == 4:
                    self.check_route_id()
                elif choice == 5:
                    self.check_payment()
                elif choice == 6:
                    print("Программа завершена")
                    break
                else:
                    print("Неверный выбор! Пожалуйста, выберите действие от 1 до 6.")
            except ValueError:
                print("Ошибка! Пожалуйста, введите число от 1 до 6.")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")


interface = ShowInterface()
interface.run()

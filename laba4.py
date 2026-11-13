class Printer:
    category: str = "Офісна техніка"
    warranty_months: int = 12


    def __init__(self, name="Невідомо", print_speed=0, price=0.0, status="Готовий"):
        self.__name = name              
        self.__print_speed = print_speed  
        self.__price = price             
    
        self._status = status


    def get_name(self) -> str:
        return self.__name
    def set_name(self, name: str):
        self.__name = name

    def get_print_speed(self) -> int:
        return self.__print_speed
    def set_print_speed(self, print_speed: int):
        self.__print_speed = print_speed

    def get_price(self) -> float:
        return self.__price
    def set_price(self, price: float):
        self.__price = price

    def get_status(self) -> str:
        return self._status
    def set_status(self, status: str):
        self._status = status

  
    def __str__(self) -> str:
        return (f"Принтер '{self.__name}', швидкість: {self.__print_speed} стор/хв, "
                f"ціна: {self.__price} грн, статус: {self._status}")


    def __repr__(self) -> str:
        return f"Printer(name='{self.__name}', print_speed={self.__print_speed}, price={self.__price}, status='{self._status}')"

  
    def __del__(self):
        print(f"[Деструктор] Об'єкт принтера '{self.__name}' видалено з пам'яті.")


def main():
    printer1 = Printer()
    printer2 = Printer("HP LaserJet Pro M404dn", 38, 9499.00, "В роботі")
    printer3 = Printer("Canon Pixma G3411", 9, 6299.50, "Очікування")

    printers = [printer1, printer2, printer3]


    print("=== ІНФОРМАЦІЯ ПРО ОБ'ЄКТИ КЛАСУ 'ПРИНТЕР' ===\n")
    for p in printers:
        print("--- Об'єкт принтера ---")
        print(f"Назва: {p.get_name()}")
        print(f"Швидкість друку: {p.get_print_speed()} стор/хв")
        print(f"Ціна: {p.get_price()} грн")
        print(f"Статус: {p.get_status()}")
        print(f"Категорія: {p.category}")
        print(f"Гарантія: {p.warranty_months} місяців")
        print(f"Рядкове представлення: {p}")
        print(f"Офіційне представлення: {p!r}")
        print()

if __name__ == "__main__":
    main()


"""1. Вивчити поняття модифікаторів видимості, конструкторів та деструкторів мови Python
2. Написати файл для представлення сутності з таблиці за допомогою класу мови Python.
3. Поля, вказані в таблиці, мають бути приватними.
4. Для кожного приватного поля слід реалізувати методи доступу до даних (наприклад для поля name – get_name())
5. Перевизначити методи __str__ та __repr__.
6. Для кожного класу слід додати 2 публічні поля, одне з яких має бути числового типу, а друге – стрічкового.
7. Для кожного класу слід створити конструктор по замовчуванню та конструктор, котрий приймає та виконує ініціалізацію всіх 
                                                                           приватних та захищених полів.
8. Для кожного класу слід оголосити та реалізувати деструктор.
9. Написати main метод, в якому здійснити ініціалізацію 3 об’єктів заданого класу та реалізувати виведення значень всіх полів."""

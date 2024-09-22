class Frame:
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes or {}

    def get_attribute(self, attribute_name):
        return self.attributes.get(attribute_name, "Атрибут не знайдено")

    def set_attribute(self, attribute_name, value):
        self.attributes[attribute_name] = value

    def find_in_subframes(self, attribute_name, value):
        results = []
        for subframe in self.get_attribute("Працівники"):
            if subframe.get_attribute(attribute_name) == value:
                results.append(subframe)
        return results

    def __repr__(self):
        return f"{self.name}: {self.attributes}"

viddil_kadriv = Frame("Відділ кадрів", {
    "Керівник": "Олена Іванова",
    "Кількість працівників": 3,
    "Контактна інформація": {
        "Адреса": "вул. Київська, 10",
        "Телефон": "+380501234567",
        "Email": "hr@company.com"
    }
})

pratsivnyk1 = Frame("Працівник", {
    "Ім'я": "Іван",
    "Прізвище": "Петров",
    "Посада": "Менеджер",
    "Вік": 30,
    "Стаж роботи": 5,
    "Заробітна плата": 15000
})

pratsivnyk2 = Frame("Працівник", {
    "Ім'я": "Анна",
    "Прізвище": "Сидоренко",
    "Посада": "Бухгалтер",
    "Вік": 45,
    "Стаж роботи": 20,
    "Заробітна плата": 20000
})

pratsivnyk3 = Frame("Працівник", {
    "Ім'я": "Марія",
    "Прізвище": "Коваленко",
    "Посада": "Юрист",
    "Вік": 35,
    "Стаж роботи": 10,
    "Заробітна плата": 18000
})

viddil_kadriv.set_attribute("Працівники", [pratsivnyk1, pratsivnyk2, pratsivnyk3])

print(viddil_kadriv.get_attribute("Контактна інформація"))
print(viddil_kadriv.find_in_subframes("Посада", "Менеджер"))
print(viddil_kadriv.find_in_subframes("Заробітна плата", 18000))
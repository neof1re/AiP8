countries = {"Бутан": "Тхимпху","Мадагаскар": "Антананариву","Исландия": "Рейкьявик","Новая Зеландия": "Веллингтон","Перу": "Лима","Лихтенштейн": "Вадуц"}
print("Все страны и столицы:")
for country, capital in countries.items():
    print(f"- {country}: {capital}")
print("\n")
country_name = input("\nВведите название страны: ")
if country_name in countries:
    print(f"Столица {country_name}: {countries[country_name]}")
else:
    print("Страна не найдена")
print("\n")
print("в) Отсортировано по названию стран (по алфавиту):")
for country in sorted(countries):
    print(f"- {country}: {countries[country]}")
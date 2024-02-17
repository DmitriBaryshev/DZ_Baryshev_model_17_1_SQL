# Заданеи на SQL
# Задание 1
import sqlite3

conn = sqlite3.connect('SQL_zad_1.db')
cursor = conn.cursor()

# Отображение всех овощей с калорийностью меньше указанной калорийности
calories_threshold = 19
cursor.execute("SELECT * FROM Dima WHERE Тип='овощ' AND Калорийность < ?", (calories_threshold,))
print("Овощи с калорийностью меньше", calories_threshold)
for row in cursor.fetchall():
    print(row)
print("")
# Отображение всех фруктов с калорийностью в указанном диапазоне
min_calories = 31
max_calories = 70
cursor.execute("SELECT * FROM Dima WHERE Тип='Фрукт' AND Калорийность BETWEEN ? AND ?", (min_calories, max_calories))
print("Фрукты с калорийностью от", min_calories, "до", max_calories)
for row in cursor.fetchall():
    print(row)
print("")
# Отображение всех овощей с указанным словом в названии
search_word = 'Морковь'
cursor.execute("SELECT * FROM Dima WHERE Тип='овощ' AND название LIKE ?", ('%' + search_word + '%',))
print("Овощи с названием содержащим слово", search_word)
for row in cursor.fetchall():
    print(row)
print("")
# Отображение всех овощей и фруктов с указанным словом в кратком описании
search_word_description = 'лежит'
cursor.execute("SELECT * FROM Dima WHERE Краткое_описание LIKE ?", ('%' + search_word_description + '%',))
print("Овощи и фрукты с описанием содержащим слово", search_word_description)
for row in cursor.fetchall():
    print(row)
print("")
# Показать все овощи и фрукты, у которых цвет желтый или красный
colors = ['желтый', 'красный']
cursor.execute("SELECT * FROM Dima WHERE Цвет IN ({})".format(','.join('?' for _ in colors)), colors)
print("Овощи и фрукты с цветом желтый или красный")
for row in cursor.fetchall():
    print(row)
print("")
# Задание 2
# Показать количество овощей
cursor.execute("SELECT COUNT(*) FROM Dima WHERE Тип='овощ'")
print("Количество овощей:", cursor.fetchone()[0])
print("")
# Показать количество фруктов
cursor.execute("SELECT COUNT(*) FROM Dima WHERE Тип='Фрукт'")
print("Количество фруктов:", cursor.fetchone()[0])
print("")
# Показать количество овощей и фруктов заданного цвета (например, желтого)
color = 'желтый'
cursor.execute("SELECT COUNT(*) FROM Dima WHERE Цвет=?", (color,))
print("Количество овощей и фруктов цвета", color, ":", cursor.fetchone()[0])
print("")
# Показать количество овощей и фруктов каждого цвета
cursor.execute("SELECT Цвет, COUNT(*) FROM Dima GROUP BY Цвет")
print("Количество овощей и фруктов каждого цвета:")
for row in cursor.fetchall():
    print(row)
print("")
# Показать цвет с минимальным количеством овощей и фруктов
cursor.execute("SELECT Цвет, COUNT(*) FROM Dima GROUP BY Цвет ORDER BY COUNT(*) ASC LIMIT 1")
print("Цвет с минимальным количеством овощей и фруктов:", cursor.fetchone()[0])
print("")
# Показать цвет с максимальным количеством овощей и фруктов
cursor.execute("SELECT Цвет, COUNT(*) FROM Dima GROUP BY Цвет ORDER BY COUNT(*) DESC LIMIT 1")
print("Цвет с максимальным количеством овощей и фруктов:", cursor.fetchone()[0])
print("")
# Показать минимальную калорийность овощей и фруктов
cursor.execute("SELECT MIN(Калорийность) FROM Dima")
print("Минимальная калорийность овощей и фруктов:", cursor.fetchone()[0])
print("")
# Показать максимальную калорийность овощей и фруктов
cursor.execute("SELECT MAX(Калорийность) FROM Dima")
print("Максимальная калорийность овощей и фруктов:", cursor.fetchone()[0])
print("")
# Показать среднюю калорийность овощей и фруктов
cursor.execute("SELECT AVG(Калорийность) FROM Dima")
print("Средняя калорийность овощей и фруктов:", cursor.fetchone()[0])
print("")
# Показать фрукт с минимальной калорийностью
cursor.execute("SELECT * FROM Dima WHERE Тип='Фрукт' ORDER BY Калорийность ASC LIMIT 1")
print("Фрукт с минимальной калорийностью:", cursor.fetchone())
print("")
# Показать фрукт с максимальной калорийностью
cursor.execute("SELECT * FROM Dima WHERE Тип='Фрукт' ORDER BY Калорийность DESC LIMIT 1")
print("Фрукт с максимальной калорийностью:", cursor.fetchone())

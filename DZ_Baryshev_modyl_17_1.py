# Заданеи на SQL
import sqlite3

conn = sqlite3.connect('SQL_zad_1.db')
cursor = conn.cursor()

# Отображение всей информации из таблицы
cursor.execute("SELECT * FROM Dima")
for row in cursor.fetchall():
    print(row)
print("")
# Отображение всех овощей
cursor.execute("SELECT * FROM Dima WHERE Тип='овощ'")
for row in cursor.fetchall():
    print(row)
print("")
# Отображение всех фруктов
cursor.execute("SELECT * FROM Dima WHERE Тип='Фрукт'")
for row in cursor.fetchall():
    print(row)
print("")
# Отображение всех названий овощей и фруктов
cursor.execute("SELECT название FROM Dima")
for row in cursor.fetchall():
    print(row[0])
print("")
# Отображение всех уникальных цветов
cursor.execute("SELECT DISTINCT Цвет FROM Dima")
for row in cursor.fetchall():
    print(row[0])
print("")
# Отображение фруктов конкретного цвета
cursor.execute("SELECT * FROM Dima WHERE Тип='Фрукт' AND Цвет='красный'")
for row in cursor.fetchall():
    print(row)
print("")
# Отображение овощей конкретного цвета
cursor.execute("SELECT * FROM Dima WHERE Тип='овощ' AND Цвет='черный'")
for row in cursor.fetchall():
    print(row)

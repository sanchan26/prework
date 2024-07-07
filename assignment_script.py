import sqlite3

def db_connection(database):
    conn = sqlite3.connect(database)
    return conn


def finder(conn, search_string):
    cursor = conn.cursor()
    sql_search = "SELECT name, marks FROM students WHERE name LIKE ? COLLATE NOCASE"
    cursor.execute(sql_search, ('%' + search_string + '%',))
    results = cursor.fetchall()
    return results


database = 'assignment.db' 
conn = db_connection(database)

while True:
    search_string = input("Enter a search string: ").strip()
    if not search_string:
        print("Please enter a search string")
        continue

    results = finder(conn, search_string)
    
    if results:
        total = 0
        for name, marks in results:
            print(f"Name: {name}, Marks: {marks}")
            total += marks
        
        avg = total / len(results) if results else 0
        print(f"Total Marks: {total}")
        print(f"Average Marks: {avg:.2f}")
    else:
        print("No matching records found.")

    break

conn.close()

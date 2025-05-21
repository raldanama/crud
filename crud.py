import sqlite3
#crud prueba 555555556676676676
def connect_db():
    conn = sqlite3.connect("uninpahu.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            codigo TEXT PRIMARY KEY,
            nombre TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insertar_estudiante():
    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO estudiantes (codigo, nombre) VALUES (?, ?)", (codigo, nombre))
        conn.commit()
        print("Estudiante insertado.")
    except sqlite3.IntegrityError:
        print("Error: ya existe un estudiante con ese código.")
    conn.close()

def ver_estudiantes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    for row in cursor.fetchall():
        print(f"Código: {row[0]} | Nombre: {row[1]}")
    conn.close()

def actualizar_estudiante():
    codigo = input("Ingrese código del estudiante a actualizar: ")
    nuevo_nombre = input("Ingrese nuevo nombre: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE estudiantes SET nombre = ? WHERE codigo = ?", (nuevo_nombre, codigo))
    if cursor.rowcount == 0:
        print("No se encontró el estudiante.")
    else:
        print("Estudiante actualizado.")
    conn.commit()
    conn.close()

def eliminar_estudiante():
    codigo = input("Ingrese código del estudiante a eliminar: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE codigo = ?", (codigo,))
    if cursor.rowcount == 0:
        print("No se encontró el estudiante.")
    else:
        print("Estudiante eliminado.")
    conn.commit()
    conn.close()

def menu():
    create_table()
    while True:
        print("\n1. Insertar\n2. Ver\n3. Actualizar\n4. Eliminar\n5. Salir")
        opcion = input("Elija una opción: ")
        if opcion == "1":
            insertar_estudiante()
        elif opcion == "2":
            ver_estudiantes()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()

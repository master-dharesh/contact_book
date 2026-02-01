import sqlite3

# Connect to database
connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    name TEXT PRIMARY KEY,
    phone TEXT
)
""")
connection.commit()


def add_contact():
    name = input("Enter name: ").lower()
    phone = input("Enter phone number: ")

    try:
        cursor.execute(
            "INSERT INTO contacts (name, phone) VALUES (?, ?)",
            (name, phone)
        )
        connection.commit()
        print("Contact added successfully!")
    except sqlite3.IntegrityError:
        print("Contact already exists.")


def view_contacts():
    cursor.execute("SELECT name, phone FROM contacts")
    rows = cursor.fetchall()

    if not rows:
        print("No contacts found.")
    else:
        for name, phone in rows:
            print(name.title(), ":", phone)


def search_contact():
    name = input("Enter name to search: ").lower()

    cursor.execute(
        "SELECT phone FROM contacts WHERE name = ?",
        (name,)
    )
    result = cursor.fetchone()

    if result:
        print(name.title(), ":", result[0])
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").lower()

    cursor.execute(
        "DELETE FROM contacts WHERE name = ?",
        (name,)
    )

    if cursor.rowcount > 0:
        connection.commit()
        print("Contact deleted.")
    else:
        print("Contact not found.")


while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

# Close database
connection.close()

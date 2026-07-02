# PRODIGY_WD_03
# Contact Management System

A simple **Contact Management System** built using **Python**. This application allows users to store and manage contact information through a command-line interface. Contact data is saved in a **JSON file**, ensuring that information remains available even after the program is closed.

## 📌 Features

* Add new contacts
* View all saved contacts
* Edit existing contacts
* Delete contacts
* Store data permanently using a JSON file
* Easy-to-use menu-driven interface

## 🛠 Technologies Used

* Python 3
* JSON (for data storage)
* OS Module (for file handling)

## 📂 Project Structure

```text
Contact-Management-System/
│
├── contact_management.py
├── contacts.json
└── README.md
```

## 🚀 How to Run the Project

1. Make sure **Python 3** is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in your terminal or command prompt.
4. Run the following command:

```bash
python contact_management.py
```

## 📋 Menu Options

When the program starts, you will see the following menu:

```text
====== Contact Management System ======

1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
```

Choose the desired option by entering its corresponding number.

## 💾 Data Storage

All contacts are stored in a file named **contacts.json**.

Each contact contains:

* Name
* Phone Number
* Email Address

Example:

```json
[
    {
        "Name": "John Doe",
        "Phone": "1234567890",
        "Email": "john@example.com"
    }
]
```

## 📚 Python Concepts Used

* Functions
* Lists
* Dictionaries
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`while`, `for`)
* File Handling
* JSON Data Storage
* Exception Handling (`try`, `except`)
* CRUD Operations (Create, Read, Update, Delete)

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

* Building a menu-driven Python application
* Managing data using JSON files
* Performing CRUD operations
* Organizing code using functions
* Implementing persistent data storage
* Handling user input and exceptions

## 👨‍💻 Author

**Tashaffur Ellahi**

Software Development Intern


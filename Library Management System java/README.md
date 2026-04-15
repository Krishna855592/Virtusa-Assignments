# Library-Management-System-Virtusa-Assignment-Java

## 1. Overview
This project is a simple console based **Library Management System** developed using core java technologies. The purpose of this system is to manage books,users and basic library operations like issuing and returning books. The system helps in reducing manual work by keeping track of book records and user transactions

## 2. Project Objectives
- To manage books, users, and transactions efficiently
- To track issued and returned books
- To reduce manual effort in library operations
- To provide a simple and easy-to-use system

## 3. Features
### 3.1 Book Management
- Add new books to the library
- Remove existing books
- Update book details such as title and author
- Display the list of all available books
### 3.2 User Management
- Register new users
- Prevent duplicate user IDs to maintain data integrity
- Display all registered users
### 3.3 Book Transactions
- Issue books to users
- Return issued books
- Prevent issuing books that are already issued
- Restrict issuing books to non-registered users
### 3.4 Due Date and Fine
- Automatically assigns a due date (7 days from the issue date)
- Calculates fine for late returns (₹10 per day)
- Utilizes Java `LocalDate` for accurate date handling
### 3.5 Search Functionality
- Search books by title
- Search books by author
- Supports case-insensitive and partial matching for better usability
### 3.6 Data Storage
- Stores data using text files:
  - `books.txt`
  - `users.txt`
- Automatically loads data when the program starts

## 4. Technologies Used
• Core Java<br>
• OOP Concepts:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o Classes and Objects<br>
&nbsp;&nbsp;&nbsp;&nbsp;o Encapsulation<br>
• Collections:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o ArrayList<br>
• File Handling:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o BufferedReader<br>
&nbsp;&nbsp;&nbsp;&nbsp;o BufferedWriter<br>
• Java Time API:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o LocalDate<br>
&nbsp;&nbsp;&nbsp;&nbsp;o ChronoUnit 

## 5. Project Structure
• model package:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o Book.java<br>
&nbsp;&nbsp;&nbsp;&nbsp;o User.java<br>
• service package:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o LibraryService.java<br>
• main package:<br>
&nbsp;&nbsp;&nbsp;&nbsp;o Main.java

**Note:** All these files are organized under `src/com/library/` directory, followed by their respective packages (main, model, service).

## 6. Screenshots
### 6.1 Main Menu  
![Main Menu](screenshots/main-menu.png)
### 6.2 Add Book  
![Add Book](screenshots/add-book.png)
### 6.3 Show All Books  
![Show All Books](screenshots/show-all-books.png)
### 6.4 Search Book (By Title / Author)  
![Search Book](screenshots/search-by-author-or-title-example.png)
### 6.5 Issue Book  
![Issue Book](screenshots/issue-book.png)
### 6.6 Return Book (With Fine)  
![Return Book](screenshots/return-book.png)

## 7. How to Run

1. Open the project in any Java IDE (Eclipse, IntelliJ, or VS Code)  
2. Run the Main.java file  
3. Use the menu options displayed in the console














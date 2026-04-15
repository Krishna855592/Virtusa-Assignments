package com.library.service;

import com.library.model.Book;
import com.library.model.User;

import java.io.*;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;

public class LibraryService {
    private ArrayList<Book> books;
    private ArrayList<User> users;
    public LibraryService(){
        books=new ArrayList<>();
        users=new ArrayList<>();
        loadBooksFromFile();
        loadUsersFromFile();

    }

    //adding book
    public void addBook(Book book){
        if(bookExists(book.getId())){
            System.out.println("Book Already Exists");
            return;
        }
        books.add(book);
        saveAllBooksToFile();
        System.out.println("Book is Added Successsfully");
    }

    private boolean bookExists(int id){
        for(Book b:books){
            if(b.getId()==id){
                return true;
            }
        }
        return false;
    }

    private void saveAllBooksToFile(){
        try{
            BufferedWriter writer=new BufferedWriter(new FileWriter("books.txt"));
            for(Book b:books){
                writer.write(
                        b.getId() + "," +
                            b.getTitle() + "," +
                            b.getAuthor() + "," +
                            b.isIssued() + "," +
                            b.getIssuedToUserId() + "," +
                                (b.getIssueDate()==null?"null": b.getIssueDate()) + "," +
                                (b.getDueDate()==null?"null":b.getDueDate())

                );
                writer.newLine();
            }
            writer.close();
        } catch(IOException e){
            System.out.println("Error in Saving Book");
        }
    }

//    private void saveToFile(Book b) {
//        try{
//            BufferedWriter writer=new BufferedWriter(new FileWriter("books.txt",true));
//            writer.write(b.getId() + "," + b.getTitle() + "," + b.getAuthor());
//            writer.newLine();
//            writer.close();
//        } catch(IOException e){
//            System.out.println("Error in Saving Book");
//        }
//
//    }

    //adding users
    public void addUser(User user){
        if(userExists(user.getUserId())){
            System.out.println("user already exists");
            return;
        }
        users.add(user);
        saveUserToFile(user);
        System.out.println("User is Added Successfully");

    }

    private void saveUserToFile(User u) {
        try{
            BufferedWriter writer=new BufferedWriter(new FileWriter("users.txt",true));
            writer.write(u.getUserId() + "," + u.getName());
            writer.newLine();
            writer.close();
        } catch (IOException e){
            System.out.println("Error in saving users");
        }

    }

    //display books
    public void showAllBooks(){
        if (books.isEmpty()){
            System.out.println("There are no books");
            System.out.println("Please add some books");
            return;
        }
        for(Book b:books){
            b.displayBook();
        }
    }

    //search the book by title
    public void searchBookByTitle(String title){
        boolean found =false;
        for(Book b:books){
            if(b.getTitle().equalsIgnoreCase(title)){
                b.displayBook();
                found=true;

            }
        }
        if(!found){
            System.out.println("Book is not found");

        }

    }

    //search book by author
    public void searchBookByAuthor(String author){
        boolean found=false;
        for(Book b:books){
            if(b.getAuthor().equalsIgnoreCase(author)){
                b.displayBook();
                found=true;

            }
        }
        if(!found){
            System.out.println("There are no books for this author");
        }
    }

    //issuing book to user
    public void issueBook(int bookid,int userid){
        if(!userExists(userid)){
            System.out.println("user doesn't exists");
            return;
        }
        for(Book b:books){
            if(b.getId()==bookid){
                if(b.isIssued()){
                    System.out.println("Book is already issued");
                    return;
                }
                b.setIssued(true);
                b.setIssuedToUserId(userid);
                //b.setIssueDate(LocalDate.now());
                LocalDate issueDate=LocalDate.now();
                LocalDate dueDate=issueDate.plusDays(7);
                b.setIssueDate(issueDate);
                b.setDueDate(dueDate);
                saveAllBooksToFile();
                System.out.println("book is issued successfully on: "+LocalDate.now());
                System.out.println("book due date is: "+dueDate);

                return;
            }
        }
        System.out.println("Book not found");

    }
//helper function so we should not add book if user doesn't exist
    private boolean userExists(int userId){
        for(User u:users){
            if(u.getUserId()==userId){
                return true;
            }
        }
        return false;
    }


    //return the book
    public void returnBook(int bookid){
        for(Book b:books){
            if(b.getId()==bookid){
                if(!b.isIssued()){
                    System.out.println("Book is not issued");
                    return;
                }

                LocalDate returnDate=LocalDate.now();
                //long daysTaken= ChronoUnit.DAYS.between(b.getIssueDate(),returnDate);
                long lateDays=ChronoUnit.DAYS.between(b.getDueDate(),returnDate);
                long allowedDays=7; // library only allowes 7 days
                long fine=0;
                //this handles if user returns book before due date
                if(lateDays<0){
                    lateDays=0;
                }
                if(lateDays>0){
                    fine=lateDays*10;
                }

//                if(daysTaken>allowedDays){
//                    fine=(daysTaken-allowedDays)*10; //10 rupees fine
//
//                }


//                int extraDays=daysTaken-b.getDueDays();
//                int fine=0;

//                if(extraDays>0){
//                    fine=extraDays*10;  //assuming fine is 10 rupees per day
//
//                }
                b.setIssued(false);
                b.setIssuedToUserId(-1);
                b.setIssueDate(null);
                b.setDueDate(null);
                saveAllBooksToFile();
                System.out.println("Book Returned on: "+ returnDate);
                System.out.println("Days Taken: "+lateDays);
                System.out.println("Book is returned successfully");

                System.out.println(fine > 0 ? "your fine is " + fine : "There is no fine to you");
                return;
            }
        }
        System.out.println("Book not found");

    }
    private void loadBooksFromFile(){
        try{
            BufferedReader reader = new BufferedReader(new FileReader("books.txt"));
            String line;

            while((line= reader.readLine())!=null){
                String[] data= line.split(",");

                int id=Integer.parseInt(data[0]);
                String title=data[1];
                String author=data[2];

                Book book =new Book(id,title,author);
                boolean isIssued=Boolean.parseBoolean(data[3]);
                int userId=Integer.parseInt(data[4]);
                book.setIssued(isIssued);
                book.setIssuedToUserId(userId);

                if(!data[5].equals("null")){
                    book.setIssueDate(java.time.LocalDate.parse(data[5]));
                }
                if(!data[6].equals("null")){
                    book.setDueDate(java.time.LocalDate.parse(data[6]));
                }
                books.add(book);

            }
            reader.close();
        }
        catch (IOException e){
            System.out.println("no previous book data found");
        }
    }

    private void loadUsersFromFile(){
        try{
            BufferedReader reader = new BufferedReader(new FileReader("users.txt"));
            String line;
            while((line= reader.readLine())!=null){
                String[] data= line.split(",");

                int id=Integer.parseInt(data[0]);
                String name=data[1];

                User user=new User(id,name);
                users.add(user);

            }
            reader.close();
        }
        catch (IOException e){
            System.out.println("no previous book data found");
        }

    }

    public void showAllUsers(){
        if(users.isEmpty()){
            System.out.println("no users available");
            return;
        }
        for(User user: users){
            user.displayUser();
        }
    }

    public void removeBook(int bookId){
        for(Book book:books){
            if(book.getId()==bookId){
                if(book.isIssued()){
                    System.out.println("Book is issued cannot remove it");
                    return;
                }
                books.remove(book);
                saveAllBooksToFile();
                System.out.println("Books removed Successfully");
                return;

            }
        }
        System.out.println("Book Not Found");
    }

    public void updateBook(int bookId,String newTitle,String newAuthor){
        for(Book b:books){
            if(b.getId()==bookId){
                b.setTitle(newTitle);
                b.setAuthor(newAuthor);

                saveAllBooksToFile();

                System.out.println("Books is updated Successfully");
                return;
            }
        }
        System.out.println("Book not Found");
    }

}

package com.library.main;

import com.library.model.Book;
import com.library.model.User;
import com.library.service.LibraryService;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {


        Scanner sc=new Scanner(System.in);
        LibraryService library=new LibraryService();

        while(true){
            System.out.println("\n=====Library Menu=======");
            System.out.println("1.Add Book");
            System.out.println("2.Register User");
            System.out.println("3.Show All Books");
            System.out.println("4.Search Book by Title");
            System.out.println("5.Search Book by Author");
            System.out.println("6.Issue Book");
            System.out.println("7.Return Book");
            System.out.println("8.Show all users");
            System.out.println("9.Remove Book");
            System.out.println("10.Update Book");
            System.out.println("11.Exit");

            System.out.print("enter you choice: ");
            int choice=sc.nextInt();
            sc.nextLine();

            switch (choice){

                case 1:
                    System.out.print("Enter Book id: ");
                    int bid=sc.nextInt();
                    sc.nextLine();
                    System.out.print("Enter Book Title: ");
                    String title=sc.nextLine();

                    System.out.print("Enter Author Name: ");
                    String author=sc.nextLine();

                    Book b =new Book(bid,title,author);
                    library.addBook(b);
                    break;
                case 2:
                    System.out.print("Enter user Id: ");
                    int userid=sc.nextInt();
                    sc.nextLine();
                    System.out.print("Enter Name: ");
                    String name=sc.nextLine();

                    User u=new User(userid,name);
                    library.addUser(u);
                    break;
                case 3:
                    library.showAllBooks();
                    break;
                case 4:
                    System.out.print("Enter the title by which you want to search: ");
                    String searchtitle=sc.nextLine();
                    library.searchBookByTitle(searchtitle);
                    break;
                case 5:
                    System.out.print("Enter the Author name by which you want to search: ");
                    String searchAuthor=sc.nextLine();
                    library.searchBookByAuthor(searchAuthor);
                    break;
                case 6:
                    System.out.print("Enter the book id: ");
                    int issuebookid=sc.nextInt();

                    System.out.print("Enter the user id: ");
                    int issueuserid=sc.nextInt();

//                    System.out.print("Enter the no of days: ");
//                    int issuedays=sc.nextInt();

                    library.issueBook(issuebookid,issueuserid);
                    break;
                case 7:
                    System.out.print("Enter the book id: ");
                    int returnbookid=sc.nextInt();

//                    System.out.print("Enter the days taken: ");
//                    int daystaken=sc.nextInt();

                    library.returnBook(returnbookid);
                    break;
                case 8:
                    library.showAllUsers();
                    break;
                case 9:
                    System.out.print("Enter Book id to remove: ");
                    int removeId=sc.nextInt();
                    library.removeBook(removeId);
                    break;
                case 10:
                    System.out.print("Enter Book id to update: ");
                    int updateId=sc.nextInt();
                    sc.nextLine();
                    System.out.print("Enter new Title: ");
                    String newTitle=sc.nextLine();

                    System.out.print("Enter new Author:");
                    String newAuthor=sc.nextLine();

                    library.updateBook(updateId,newTitle,newAuthor);
                    break;
                case 11:
                    System.out.println("Exiting.....");
                    return;

                default:
                    System.out.println("Invalid choice");

            }
        }
    }
}



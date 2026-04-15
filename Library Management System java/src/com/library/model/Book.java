package com.library.model;

import java.time.LocalDate;

public class Book {

    private int id;
    private String title;
    private String author;
    private boolean isissued;

    //adding which user has taken book and duedays
    private int issuedToUserId;
    private int dueDays;

    private LocalDate issueDate;

    private LocalDate dueDate;

    public Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isissued=false; // at initialising the book is not issued
        this.issuedToUserId=-1;
        this.dueDays=0;
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public boolean isIssued() {
        return isissued;
    }

    //setter method for isissued
    public void setIssued(boolean issued){
        this.isissued=issued;
    }
    //writing the display book method
    public void displayBook(){
        System.out.println("Book id: "+ id);
        System.out.println("Book title: "+title);
        System.out.println("Book Author: "+author);
        System.out.println("Book availability: "+(!isissued?"Available":"Not Available"));
        System.out.println("------------------------------");

    }

    public int getIssuedToUserId(){
        return issuedToUserId;
    }

    public void setIssuedToUserId(int userId){
        this.issuedToUserId=userId;

    }

    public int getDueDays() {
        return dueDays;
    }

    public void setDueDays(int days) {
        this.dueDays = days;
    }

    public LocalDate getIssueDate(){
        return issueDate;

    }
    public void setIssueDate(LocalDate date){
        this.issueDate=date;
    }

    public void setTitle(String newtitle){
        this.title=newtitle;
    }

    public void setAuthor(String newAuthor){
        this.author=newAuthor;
    }

    public LocalDate getDueDate(){
        return dueDate;
    }

    public void setDueDate(LocalDate dueDate){
        this.dueDate=dueDate;
    }


}

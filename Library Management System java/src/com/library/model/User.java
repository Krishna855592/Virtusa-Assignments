package com.library.model;

public class User {
    private int userId;
    private String name;

    public User(int userId, String name) {
        this.userId = userId;
        this.name = name;
    }


    public int getUserId() {
        return userId;
    }

    public String getName() {
        return name;
    }
    //displaying the user details
    public void displayUser(){
        System.out.println("User Id: "+ userId);
        System.out.println("User Name: "+ name);
        System.out.println("--------------");

    }
}

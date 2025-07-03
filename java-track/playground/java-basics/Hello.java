// Hello.java

import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {

        String animal1 = "Lion";
        String animal2 = "Elephant";
        System.out.println("Before swapping, Animal1 = " + animal1 + " and Animal2 = " + animal2);

    }

}

class Vehicle {
    void start() {
        System.out.println("Engine starts");
    }
}

class Car extends Vehicle {
    @Override
    void start() { // ❌ Cannot override final method
        System.out.println("Car starts");
    }
}
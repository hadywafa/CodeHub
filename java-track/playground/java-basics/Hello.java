// Hello.java

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Hello {
    public static void main(String[] args) {

        var list1 = new ArrayList<Integer>();
        list1.add(10);
        list1.add(20);
        list1.add(1, 15); // Insert at index
        list1.remove(0); // Remove by index
        System.out.println(list1); // [Orange, Banana]
        // ------------------------------------
        LinkedList<String> list2 = new LinkedList<>();
        list2.add("Apple");
        list2.addFirst("Orange");
        list2.addLast("Banana");
        list2.remove("Apple");
        System.out.println(list2); // [Orange, Banana]
        // ------------------------------------
        System.out.println();
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
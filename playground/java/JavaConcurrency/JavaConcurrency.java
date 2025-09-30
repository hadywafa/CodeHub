import java.util.*;

public class JavaConcurrency {

    public static void main(String[] args) throws InterruptedException {

        Set<Employee> set = new TreeSet<>();
        set.add(new Employee(101, "Raj"));
        set.add(new Employee(100, "Sara"));
        set.add(new Employee(100, "Ahmed")); // Duplicate
        System.out.println(set); // Sorted by ID
    }

}

class Employee implements Comparable<Employee> {
    int id;
    String name;

    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int compareTo(Employee other) {
        return this.id - other.id;
    }

    public String toString() {
        return id + " : " + name;
    }
}

class HwHelper {

    // 💤 Reusable sleep helper
    public static void sleep(long ms) {
        try {
            Thread.sleep(ms);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt(); // Best practice
            System.err.println("Sleep interrupted");
        }
    }
}
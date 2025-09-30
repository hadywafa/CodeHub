# 🧱 What Does **"Java is Object-Oriented"** Mean?

> 🧠 Java is **Object-Oriented** because everything in Java is built around **objects and classes**, using the principles of **OOP (Object-Oriented Programming)**.

This means:

- Java organizes code using **real-world objects**
- You **model data + behavior** together
- Your app becomes more **modular, reusable, and easier to maintain**

---

## 🧠 Core Principles of OOP (The Big 4️⃣)

| Principle         | What It Means                               | Real-Life Analogy                                            |
| ----------------- | ------------------------------------------- | ------------------------------------------------------------ |
| **Encapsulation** | Hide internal data; expose only needed info | Like a remote control — you use buttons, not circuits        |
| **Abstraction**   | Show only essential features, hide details  | Like driving a car — you don’t need to know engine internals |
| **Inheritance**   | One class inherits features of another      | Like a Dog class inheriting from Animal                      |
| **Polymorphism**  | One interface, many implementations         | Like a USB port used by a mouse, keyboard, or phone          |

Let’s see each one, with examples 👇

---

## 🔐 1. **Encapsulation**

### 💡 Idea: Bundle data + behavior, and hide private internals

```java
public class BankAccount {
    private double balance; // hidden

    public void deposit(double amount) {
        balance += amount;
    }

    public double getBalance() {
        return balance;
    }
}
```

✅ The `balance` is private — you **can’t access it directly**, only through `getBalance()` or `deposit()`.

---

## 🧽 2. **Abstraction**

### 💡 Idea: Expose what’s needed, hide the messy stuff.

```java
abstract class Animal {
    abstract void makeSound();
}

class Dog extends Animal {
    void makeSound() {
        System.out.println("Woof!");
    }
}
```

✅ The user just calls `makeSound()` — doesn’t need to know what’s happening inside.

---

## 🧬 3. **Inheritance**

### 💡 Idea: Reuse existing class behavior.

```java
class Vehicle {
    void start() {
        System.out.println("Vehicle started");
    }
}

class Car extends Vehicle {
    void honk() {
        System.out.println("Beep beep!");
    }
}
```

✅ `Car` **inherits** `start()` from `Vehicle` — no need to rewrite it.

---

## 🦾 4. **Polymorphism**

### 💡 Idea: One method, different behaviors (via override or interfaces)

```java
class Animal {
    void makeSound() {
        System.out.println("Some sound");
    }
}

class Cat extends Animal {
    void makeSound() {
        System.out.println("Meow");
    }
}

class Dog extends Animal {
    void makeSound() {
        System.out.println("Woof");
    }
}
```

```java
Animal a = new Dog();
a.makeSound();  // Woof

a = new Cat();
a.makeSound();  // Meow
```

✅ Same method call (`makeSound()`), but different outcomes. 🔁

---

## 📦 Everything is an Object (Mostly)

- All Java code lives inside **classes**
- Every object is an **instance of a class**
- Even the `main()` method must be inside a class!

```java
public class Hello {
    public static void main(String[] args) {
        Person p = new Person();
        p.sayHi();
    }
}
```

---

## ⚠️ BUT… Is Java _Fully_ Object-Oriented?

🧠 Not 100% pure:

- Java has **primitive types** like `int`, `char`, `boolean`, which are **not objects**
- But Java gives **wrapper classes** like `Integer`, `Boolean`, etc., to treat them like objects when needed

---

## ✅ Summary

✔️ Java is **Object-Oriented** because it follows all OOP principles:

| ✅ Feature          | ✅ Supported in Java                     |
| ------------------- | ---------------------------------------- |
| Encapsulation       | ✅ Yes (access modifiers)                |
| Abstraction         | ✅ Yes (abstract classes, interfaces)    |
| Inheritance         | ✅ Yes (extends, super)                  |
| Polymorphism        | ✅ Yes (method override, interfaces)     |
| Everything in class | ✅ Yes (even main method needs a class!) |

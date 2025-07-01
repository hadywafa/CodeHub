# **C# Structs vs. Classes – What’s the Difference? 🚀**

When diving deep into **C#**, one of the first questions that comes up is: **Should I use a struct or a class?** While they seem similar, the differences **matter**—especially when it comes to **performance, memory, and behavior**. Let’s break it down **with your structured learning style**.

---

## **1. Memory Allocation – Heap vs. Stack 📍**

✅ **Structs** are stored **on the stack**, meaning they are lightweight and automatically cleaned up when they go out of scope.  
✅ **Classes** are stored **on the heap**, meaning they require **garbage collection** to free up memory.

🔹 **Example:**

```csharp
struct MyStruct { public int Value; }
class MyClass { public int Value; }

MyStruct s1 = new MyStruct { Value = 10 };
MyStruct s2 = s1; // Full copy is created

MyClass c1 = new MyClass { Value = 10 };
MyClass c2 = c1; // Only reference is copied
```

**🚀 Key takeaway:** Structs are **copied**, while classes are **referenced**, affecting performance in large applications.

---

## **2. Copy Behavior – Value vs. Reference**

🔹 **Structs are value types**, meaning **each instance holds its own data**.  
🔹 **Classes are reference types**, meaning **multiple instances can point to the same object in memory**.

🔹 **Example:**

```csharp
struct PointStruct { public int X, Y; }
class PointClass { public int X, Y; }

PointStruct p1 = new PointStruct { X = 5, Y = 10 };
PointStruct p2 = p1; // Copy created (separate memory)

PointClass p3 = new PointClass { X = 5, Y = 10 };
PointClass p4 = p3; // Both share the same memory
p4.X = 20; // p3.X also changes!
```

🚀 **Key takeaway:** If data **must not be altered elsewhere**, **use a struct**. If it should be **shared**, **use a class**.

---

## **3. Performance – When Should You Use Each?**

✅ **Use structs for** small, frequently used objects (e.g., points, coordinates, lightweight models).  
✅ **Use classes for** complex objects that require reference behavior (e.g., large data models, services).

📌 **Structs are great when:**

- You **don’t need inheritance**.
- The object is **small & frequently used**.
- You want **faster performance with stack allocation**.

📌 **Classes are great when:**

- You need **inheritance** or **polymorphism**.
- Objects **must be shared** among different parts of the app.
- The object **is large & needs heap allocation**.

---

## **4. Can Structs Hold Methods, Properties, and Events?**

✅ **Methods** – Structs can define instance methods just like classes.  
✅ **Properties** – You can create `get` and `set` properties inside a struct.  
✅ **Events** – Structs can declare events and event handlers.  
✅ **Constructors** – Structs **can** have parameterized constructors, but **cannot** define explicit default constructors.

🔹 **Example of a Struct with Methods, Properties, and Events:**

```csharp
struct Button
{
    public string Label { get; set; }
    public event Action OnClick;  // Struct can have events!

    public Button(string label)
    {
        Label = label;
        OnClick = null;
    }

    public void Click()
    {
        OnClick?.Invoke();  // Struct method executing an event
    }
}
```

🚀 **Key takeaway:** Structs are **not just plain data holders**—they can **execute logic**, **handle events**, and **encapsulate behavior**, just like classes.

---

## **5. Limitations of Structs vs. Classes 🚨**

Even though structs can have methods and events, they are more restricted than classes:  
❌ **No inheritance** – Structs **cannot inherit** from other structs or classes.  
❌ **No explicit default constructor** – You **cannot** define a **parameterless constructor** manually.  
❌ **No destructors** – Structs do **not support finalizers** (`~StructName()`).

🔹 **Example of What Structs Cannot Do:**

```csharp
struct MyStruct
{
    public int X;

    // ❌ ERROR: Structs cannot have a parameterless constructor.
    public MyStruct()
    {
        X = 0;
    }
}
```

🚀 **Key takeaway:** If you need **inheritance, lifecycle management, or complex behavior**, use a **class** instead.

---

## **6. When Should You Use a Struct vs. a Class?**

✅ **Use a struct when:**

- The object is **small & lightweight** (e.g., points, colors, coordinates).
- You don’t need **inheritance** or **complex logic**.
- You want **fast memory allocation on the stack**.

✅ **Use a class when:**

- You need **polymorphism and inheritance**.
- The object **must be shared** across different parts of the app.
- You require **explicit constructors** and memory control.

---

## **7. Real-World Examples – Where to Use Structs vs. Classes?**

🔹 **Use a struct for small data models:**

```csharp
struct Coordinates
{
    public int X { get; set; }
    public int Y { get; set; }
}
```

🔹 **Use a class for business logic & complex objects:**

```csharp
class UserProfile
{
    public string Name { get; set; }
    public string Email { get; set; }
}
```

**🚀 Key takeaway:** Structs **are efficient**, but classes **offer flexibility**.

## **Final Verdict – Struct or Class? 🔥**

If **performance matters**, **use structs**.  
If **complexity and flexibility matter**, **use classes**.

# ☕ What Does **Java is Portable** Mean?

> 🧳 **Portability** in Java means: _Write your code once, run it anywhere (WORA)._

Java is designed to be **platform-independent**, which means Java programs can run on any device or operating system that has a **Java Virtual Machine (JVM)** — without needing to change your code!

---

## 🔄 Why is Java Portable?

### 🧱 1. **Java Code Compiles to Bytecode**

- When you compile Java code:

  ```java
  javac Hello.java
  ```

  It generates **`Hello.class`** (this is **bytecode** 🧩 — a platform-independent format).

- Bytecode is **not machine code**, but an intermediate format understood by the JVM.

---

### 💻 2. **JVM Handles Platform Differences**

- Every platform (Windows, Linux, Mac, etc.) has its own version of the **JVM**.
- The JVM takes the **same bytecode** and **runs it on any OS**.

📦 Think of Java bytecode like a universal package, and the JVM as a local delivery guy who knows your city’s roads (OS) and delivers it perfectly.

---

## 💡 Simple Example

### Code:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Compile once:

```bash
javac Hello.java
```

### Run on:

- 🪟 Windows: `java Hello`
- 🐧 Linux: `java Hello`
- 🍏 macOS: `java Hello`

✔️ No code change needed.

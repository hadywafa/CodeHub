# 🚦 Learning Path: Multi-threading, Async, and Parallelism in C\

_💡 Ordered topics to become an execution model pro!_

---

## ✅ **Phase 1: Foundation – Execution Models**

> Understand the **core differences** between these three models

### Topics

1. 🧵 What is Multi-threading vs Concurrency vs Parallelism?
2. 🧠 CPU-bound vs I/O-bound workloads — why it matters
3. ⚠️ When to use: thread vs task vs async vs parallel

---

## 🧵 **Phase 2: Multi-threading in C#**

> Learn how to create and control threads manually
> Focus on low-level threading for CPU-bound workloads

### Topics

1. 🔨 Creating threads using `Thread` class
2. 🧼 Thread lifecycle, `Start()`, `Join()`, `Abort()` (deprecated)
3. 🔄 Thread synchronization:

   - `lock`, `Monitor`, `Mutex`, `Semaphore`

4. ⚠️ Race conditions, deadlocks, and thread safety
5. 🪵 Thread-safe collections

---

## 🔃 **Phase 3: ThreadPool & Tasks**

> Move to .NET's modern way of using threads efficiently (managed pool)

### Topics

1. 🔄 `ThreadPool.QueueUserWorkItem` — basics
2. 🚀 `Task` vs `Task<T>` vs `ValueTask<T>`
3. 🧵 `Task.Run()` vs creating threads manually
4. ⚠️ Unobserved exceptions in tasks
5. 🧠 Task scheduling and thread pool starvation

---

## 🌀 **Phase 4: Asynchronous Programming (async/await)**

> Ideal for I/O-bound apps like file/network/database operations

### Topics

1. 🔄 Synchronous vs Asynchronous code
2. 🧑‍💻 How `async` and `await` work internally
3. 🧵 Does async use threads? (spoiler: not always!)
4. ⛓️ `ConfigureAwait(false)` and SynchronizationContext
5. ⚠️ Common async mistakes (blocking with `.Result`, `.Wait()`)

---

## 🧮 **Phase 5: Parallel Programming in C#**

> True multi-core CPU usage for compute-heavy workloads

### Topics

1. 🧠 What is parallelism vs concurrency
2. ⚙️ `Parallel.For`, `Parallel.ForEach`, `Parallel.Invoke`
3. ⚠️ Controlling degree of parallelism
4. 🧯 Cancellation, exceptions in parallel loops
5. 🧩 When _not_ to use parallelism (e.g., I/O-bound)

---

## 🤖 **Phase 6: Advanced Patterns and Real-World Usage**

### Topics

1. 🔀 Async streams (`IAsyncEnumerable<T>`)
2. 🕸️ Producer-consumer with `BlockingCollection`
3. 🧵 Thread-safe singletons & `Lazy<T>`
4. 🧰 Background services and hosted workers (ASP.NET Core)
5. 🧭 Choosing the right model for your use case

---

## 🎓 Bonus Deep Dives (Optional But Powerful)

| Topic                   | Purpose                                     |
| ----------------------- | ------------------------------------------- |
| 🔎 TaskScheduler        | Control how tasks are scheduled             |
| 🧹 ThreadPool internals | How threads are created, reused, and killed |
| 🧬 ValueTask vs Task    | Performance tuning for high-throughput APIs |
| 🔄 PLINQ                | Parallel LINQ for data processing           |

---

## ✅ Final Sequence

```text
1. Concepts: Threads vs Tasks vs Async
2. Manual Multi-threading
3. ThreadPool + Tasks
4. Async/Await
5. Parallel Programming
6. Real-world Patterns
```

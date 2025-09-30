# 🧭 Your Personalized Interview Prep Focus Guide

## ✅ **1. Core Strength Refresh (Just polish!)**

Spend \~20% of your time here (because you’re already good at it)

| Topic                      | What to Review                           | Resources                           |
| -------------------------- | ---------------------------------------- | ----------------------------------- |
| ✅ .NET OOP + SOLID        | Class design, interfaces, DI, clean code | Your own past projects or tutorials |
| ✅ REST API Design         | Route naming, versioning, filters        | Rebuild a TMF-style endpoint        |
| ✅ Entity Framework Basics | Code First, LINQ, migrations             | Review old EF projects              |

---

## 🔥 **2. Weakness Fix (High priority!)**

Spend \~40% here

| Topic                   | Focus Area                            | Fix Strategy                                                      |
| ----------------------- | ------------------------------------- | ----------------------------------------------------------------- |
| 🧨 DB Optimization      | EF query tuning, N+1 problem, indexes | Practice `.AsNoTracking()`, logging SQL, execution plans          |
| 🧨 Parallel Programming | Task, async/await, Parallel.For, TPL  | Build a sample app that fetches 10 URLs in parallel               |
| 🧨 Queues (RabbitMQ)    | Pub/Sub, producer-consumer in C#      | Use Docker to run RabbitMQ locally; write 1 producer + 1 consumer |

---

## 📦 **3. Python & AI Integration (Just enough to impress)**

Spend \~20%

| Goal                    | Action                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------ |
| Basic Python fluency    | Write a small Flask API or script that reads data and posts to your .NET backend                 |
| AI integration demo     | Learn how Python scripts could do AI tasks (e.g., NLP or scoring model), then call them via HTTP |
| Bonus: mention Azure ML | Learn the concept of hosting models as endpoints                                                 |

---

## ☁️ **4. Azure + DevOps + TMF + Microservices (Pro-level topics)**

Spend \~20%

| Focus Area         | How to Cover Quickly                                                            |
| ------------------ | ------------------------------------------------------------------------------- |
| TMF APIs + OpenAPI | Create a Swagger doc, follow TMF pattern (GET /resource/{id})                   |
| Azure DevOps CI/CD | Study a YAML build + release pipeline                                           |
| Microservices      | Know containerization, Kubernetes basics, Azure Functions, API Gateway concepts |
| Message Brokers    | Compare Azure Service Bus vs RabbitMQ just in concept                           |

---

## 🧩 Suggested Study Flow (If you want exact timing)

| Day      | AM                   | PM                    | Night                     |
| -------- | -------------------- | --------------------- | ------------------------- |
| 🗓️ Day 1 | EF & DB optimization | Parallel programming  | Python basics             |
| 🗓️ Day 2 | RabbitMQ + TMF API   | Microservices & Azure | Practice system design Q  |
| 🗓️ Day 3 | DevOps & Pipelines   | Mock interview Q\&A   | Review cheat sheet & rest |

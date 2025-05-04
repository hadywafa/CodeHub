# 🎯 ASP.NET Core API – Senior-Level Interview Topics with Q\&A

## 1️⃣ **Request Pipeline & Middleware**

**Q: What is middleware in ASP.NET Core?**
**A:** Middleware is a component that handles HTTP requests and responses. It runs in a pipeline where each component can modify the request, response, or short-circuit the request.
**Follow-up:** “I can create custom middleware by implementing `InvokeAsync(HttpContext context)` and registering it with `app.UseMiddleware<T>()`.”

---

## 2️⃣ **Routing – Attribute vs Convention**

**Q: What's the difference between Attribute Routing and Convention Routing?**
**A:** Attribute routing defines routes directly on actions using `[Route]`, giving fine control. Convention routing uses a global pattern (e.g. `{controller}/{action}`) set in `UseEndpoints`.

---

## 3️⃣ **Model Binding & Validation**

**Q: How does model binding work in ASP.NET Core?**
**A:** It maps data from HTTP requests (route, query, form, body) to action parameters. For validation, we use `[Required]`, `[Range]`, or custom `IValidatableObject`, and check `ModelState.IsValid`.

---

## 4️⃣ **Dependency Injection & Lifetimes**

**Q: What are the service lifetimes in ASP.NET Core?**
**A:**

- `Transient`: New instance every time.
- `Scoped`: One per HTTP request.
- `Singleton`: One for the app's lifetime.
  Used via constructor injection.

---

## 5️⃣ **Global Error Handling**

**Q: How do you handle exceptions globally in ASP.NET Core?**
**A:** Use `app.UseExceptionHandler()` in `Program.cs` to redirect to a custom error endpoint. Optionally, use `ExceptionFilter` for MVC or `ProblemDetails` for API-friendly responses.

---

## 6️⃣ **Authentication & Authorization**

**Q: How does ASP.NET Core handle authentication and authorization?**
**A:** AuthN uses `UseAuthentication()` and tokens (e.g., JWT), while AuthZ uses `UseAuthorization()` and `[Authorize]`, role-based or policy-based. Configured in `AddAuthentication()` and `AddAuthorization()`.

---

## 7️⃣ **Filters (Action, Exception, etc.)**

**Q: What is the use of filters in ASP.NET Core?**
**A:** Filters add logic before/after controller actions. Types: `ActionFilter`, `ExceptionFilter`, `ResultFilter`, `ResourceFilter`. Useful for cross-cutting concerns like logging, auth, error handling.

---

## 8️⃣ **Versioning**

**Q: How do you version an API in ASP.NET Core?**
**A:** Add `Microsoft.AspNetCore.Mvc.Versioning` and configure in `Startup`. Support versioning by URL, query string, or headers using `[ApiVersion("1.0")]`.

---

## 9️⃣ **Swagger/OpenAPI**

**Q: How do you enable Swagger in ASP.NET Core?**
**A:** Use `Swashbuckle.AspNetCore`. Add `AddSwaggerGen()` in services and `UseSwagger()` + `UseSwaggerUI()` in the pipeline. It auto-generates OpenAPI docs from controllers and XML comments.

---

## 🔟 **Asynchronous APIs**

**Q: Why use async/await in API controllers?**
**A:** To free up threads while waiting for I/O (e.g., DB, HTTP). Improves scalability. Always use `Task<IActionResult>` with `await`.

---

## 🔐 Bonus: Clean Architecture Question

**Q: How do you organize a scalable API project?**
**A:** I follow Clean Architecture:

- **Controllers** in API layer
- **Business logic** in Services
- **Interfaces** for abstractions
- **Repositories** for data access
  I use **DI** for separation of concerns and **DTOs** to decouple entities from the API.

---

## 📦 Bonus: Unit of Work + Repository

**Q: Why and when do you use the Unit of Work and Repository patterns?**
**A:** Repository abstracts data access logic. Unit of Work manages transaction consistency across multiple repositories. Useful for complex domains and testing.

---

## 💾 Bonus: Entity Framework Core

**Q: How do you handle transactions in EF Core?**
**A:** Use `DbContext.Database.BeginTransaction()` or `IDbContextTransaction`. Also, use `SaveChanges()` or `SaveChangesAsync()` to persist.

---

## 📍 What You Should Memorize Before the Interview

| Area             | What to Know                            |
| ---------------- | --------------------------------------- |
| Middleware       | Custom, pipeline order                  |
| Routing          | Attribute vs convention                 |
| Model Validation | DataAnnotations, `ModelState.IsValid`   |
| DI Lifetimes     | Transient / Scoped / Singleton          |
| Auth             | JWT, policies, `[Authorize]`            |
| Filters          | `ActionFilter`, `ExceptionFilter`       |
| Swagger          | `AddSwaggerGen`, UI                     |
| Error Handling   | `UseExceptionHandler`, `ProblemDetails` |
| Versioning       | `[ApiVersion]`, config strategies       |
| Async            | `Task<IActionResult>`, `await`          |
| EF Core          | DbContext, UoW, migration, async        |

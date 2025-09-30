# 🎯 ASP.NET Core MVC – Senior Interview Questions with Model Answers

---

## 🌐 1. **MVC Architecture**

**Q1: What is the MVC pattern and how does ASP.NET Core implement it?**
**A:** MVC stands for **Model-View-Controller**. ASP.NET Core separates responsibilities:

- **Model**: Represents business/data logic
- **View**: UI template (Razor)
- **Controller**: Handles requests and returns responses (View or JSON)

---

**Q2: Difference between ASP.NET MVC (pre-Core) and ASP.NET Core MVC?**
**A:** ASP.NET Core MVC is:

- Cross-platform
- Unified with Web API
- Lightweight, modular, and middleware-based
- Supports DI, Razor Pages, Tag Helpers

---

## 🚦 2. **Routing**

**Q3: How does routing work in ASP.NET Core MVC?**
**A:** Routing maps URLs to controller actions.

- **Convention-based routing**: Defined in `UseEndpoints()`
- **Attribute routing**: `[Route("products/{id}")]`

---

**Q4: What happens if both routing types are used?**
**A:** **Attribute routing takes precedence**. If none match, falls back to conventional routes if configured.

---

## 📥 3. **Model Binding & Validation**

**Q5: How does model binding work?**
**A:** It automatically maps request data (query string, form, route, body) to action parameters or models.

---

**Q6: How do you validate models in MVC?**
**A:** Use `[Required]`, `[Range]`, etc.
In controller:

```csharp
if (!ModelState.IsValid) return View(model);
```

---

## 🔐 4. **Filters**

**Q7: What are filters in ASP.NET Core MVC?**
**A:** Filters allow code execution **before/after** controller actions. Types:

- `AuthorizationFilter`
- `ActionFilter`
- `ResultFilter`
- `ExceptionFilter`

Used for **logging**, **error handling**, **auth**, **caching**, etc.

---

**Q8: How do you create a custom action filter?**
**A:** Inherit from `ActionFilterAttribute` and override `OnActionExecuting()` / `OnActionExecuted()`. Register globally or via `[ServiceFilter]`.

---

## 🧩 5. **View & Razor Engine**

**Q9: What is Razor syntax?**
**A:** Razor is a templating syntax for writing C# code in `.cshtml` views.
E.g., `@Model.Name`, `@foreach`, `@{ var x = 1; }`

---

**Q10: What are Tag Helpers?**
**A:** Tag Helpers allow you to use server-side logic with **HTML-like syntax**.
E.g.,

```html
<form asp-action="Login">
  <input asp-for="Username" />
</form>
```

---

## ⚙️ 6. **Controller & Action Results**

**Q11: What return types can a controller action have?**
**A:**

- `IActionResult` or `ActionResult<T>`
- `ViewResult`, `JsonResult`, `RedirectResult`, etc.

---

**Q12: What is the difference between ViewResult and PartialViewResult?**
**A:** `ViewResult` renders full view, `PartialViewResult` returns only a view fragment (for AJAX or nested rendering).

---

## 🧱 7. **Dependency Injection**

**Q13: How is DI used in MVC?**
**A:** Controllers get dependencies injected via constructor. Services are registered in `Program.cs` using:

```csharp
services.AddScoped<IMyService, MyService>();
```

---

## 🛑 8. **Error Handling**

**Q14: How do you handle exceptions in ASP.NET Core MVC?**
**A:**

- Use `UseExceptionHandler()` middleware
- Use `ExceptionFilter`
- Return `ProblemDetails` in APIs

---

## 🎯 9. **Authentication & Authorization**

**Q15: How is user authentication handled in MVC?**
**A:** Via:

- ASP.NET Identity
- Cookies
- External providers (Google, Facebook)
- `[Authorize]` attributes on controllers or actions

---

## 🧪 10. **Testing & Maintainability**

**Q16: How do you unit test a controller in MVC?**
**A:**

- Mock dependencies using Moq
- Call the action method directly
- Assert the `ViewResult`, `Model`, or `RedirectToAction`

---

**Q17: How do you make an MVC app scalable and testable?**
**A:** By:

- Using SOLID principles
- Abstracting logic into Services
- Following Clean Architecture
- Using dependency injection

---

## ⚡ Bonus Senior-Level Questions

**Q18: How would you implement a custom HTML helper?**
**A:** Create a static method returning `IHtmlContent`. E.g.,

```csharp
public static class MyHelpers
{
    public static IHtmlContent LabelWithColon(this IHtmlHelper html, string name)
    {
        return html.Label(name + ":");
    }
}
```

---

**Q19: What's the difference between Razor Pages and MVC?**
**A:**

- Razor Pages use **page-based model**, no controllers
- Good for simple UIs
- MVC is **controller-based**, better for large apps

---

**Q20: What’s new in ASP.NET Core MVC 6/7/8?**
**A:**

- Minimal APIs
- Endpoint filters
- Improved model binding
- Output caching
- Integration with OpenTelemetry and gRPC

---

## ✅ Need a printable cheatsheet or mock interview based on this?

Let me know and I can generate one instantly for your preparation. Want to dive deeper into any specific MVC topic?

# 🎯 Razor Pages – Senior .NET Interview Questions with Answers

---

## 🧱 1. **Razor Pages Basics**

**Q1: What is Razor Pages in ASP.NET Core?**
**A:** Razor Pages is a **page-centric** web framework in ASP.NET Core that follows the **MVVM** pattern (loosely), where each `.cshtml` file has an associated `.cshtml.cs` PageModel (C# class). It's simpler than MVC for basic CRUD and form-based web UIs.

---

**Q2: Razor Pages vs MVC – What's the difference?**
**A:**

| Aspect     | Razor Pages                          | MVC (Model-View-Controller)        |
| ---------- | ------------------------------------ | ---------------------------------- |
| Structure  | Page-based (`/Pages`)                | Controller + View folders          |
| Complexity | Simpler, fewer files                 | More setup, great for complex apps |
| Routing    | Folder-based routing                 | Attribute or conventional routing  |
| Best for   | CRUD, admin panels, simple workflows | Large, modular applications        |

---

## 🧭 2. **Routing & Page Discovery**

**Q3: How does routing work in Razor Pages?**
**A:** Razor Pages use **convention-based routing**. Each page in the `Pages` folder maps to its path:

`/Pages/Account/Login.cshtml` → `/Account/Login`

You can override it with `[@page "/custom-url"]`.

---

**Q4: Can you have route parameters in Razor Pages?**
**A:** Yes, via the `@page` directive:

```razor
@page "/product/{id:int}"
```

This binds `id` to the `PageModel` property.

---

## 💼 3. **PageModel Class & Handlers**

**Q5: What is the role of the PageModel in Razor Pages?**
**A:** It acts like a **ViewModel + Controller**, containing:

- Request handling logic (`OnGet`, `OnPost`)
- Bound properties for form data
- Services injected via constructor

---

**Q6: What are page handler methods?**
**A:**

| Handler          | Description                            |
| ---------------- | -------------------------------------- |
| `OnGet()`        | Runs on GET requests                   |
| `OnPost()`       | Runs on POST requests                  |
| `OnPostDelete()` | Runs on form post to `?handler=Delete` |

Each handler maps to HTTP methods and optional `handler` query values.

---

**Q7: How do you create multiple POST handlers?**
**A:** Use named handlers:

```csharp
public IActionResult OnPostSave() { }
public IActionResult OnPostDelete() { }
```

And in Razor:

```html
<button asp-page-handler="Save">Save</button> <button asp-page-handler="Delete">Delete</button>
```

---

## ✅ 4. **Model Binding & Validation**

**Q8: How is data bound in Razor Pages?**
**A:** Razor Pages uses `[BindProperty]` to bind form fields to `PageModel` properties:

```csharp
[BindProperty]
public Product MyProduct { get; set; }
```

Model validation uses the same `[Required]`, `[Range]`, etc., and is checked via `ModelState.IsValid`.

---

## 🔒 5. **Security**

**Q9: How do you restrict access to a Razor Page?**
**A:**

- Use `[Authorize]` on `PageModel`
- Or apply globally in `Startup.cs`

```csharp
[Authorize(Roles = "Admin")]
public class IndexModel : PageModel { ... }
```

---

## 🔄 6. **Redirects & Navigation**

**Q10: How do you redirect in Razor Pages?**
**A:**

```csharp
return RedirectToPage("/Dashboard");
return RedirectToPage("Edit", new { id = 1 });
```

---

## 🧪 7. **Partial Pages, Layouts, and Reuse**

**Q11: How do you reuse HTML in Razor Pages?**
**A:** Use:

- `_Layout.cshtml` for shared layout
- `_ViewStart.cshtml` for default layout
- `Partial Views` or `Tag Helpers` for reusable fragments

```razor
@await Html.PartialAsync("_ProductCard", product)
```

---

## ⚙️ 8. **Advanced**

**Q12: How do you inject services in Razor Pages?**
**A:** Use constructor injection in `PageModel`:

```csharp
private readonly IProductService _service;
public IndexModel(IProductService service) => _service = service;
```

---

**Q13: Can Razor Pages be used with APIs?**
**A:** No, Razor Pages is designed for **HTML-based web UIs**. For REST APIs, use **Controllers** or **Minimal APIs**.

---

## 🔥 9. **Bonus Senior-Level**

**Q14: How do you test Razor Pages?**
**A:**

- Use `WebApplicationFactory<T>` for **integration tests**
- Mock services and validate response content and model state
- Test handlers (`OnGet`, `OnPost`) as regular methods

---

**Q15: Can you use Razor Pages and MVC together?**
**A:** Yes. They share the same middleware and can coexist. You can have `/Pages` for Razor and `/Controllers` for API or complex routing.

---

## ✅ Final Tip

If you say this in your interview, it’ll impress them:

> “I prefer Razor Pages for admin panels and form-heavy UIs where I want minimal plumbing. But for complex business logic and API-first apps, I still lean toward the MVC controller pattern.”

---

Would you like a **cheat sheet** summarizing both **MVC vs Razor Pages** interview questions? Or shall we dive into **Blazor**, **Minimal APIs**, or **real-world Razor Pages use cases** next?

# 🧠 YAML Explained

## 🏁 1. What is YAML?

**YAML** = _YAML Ain’t Markup Language_
A human-friendly, indentation-based data format used in:

- Kubernetes manifests 🧩
- CI/CD pipelines (GitHub Actions, Azure Pipelines, etc.)
- Config files (Docker Compose, Ansible, etc.)

✅ **Goal:** readable, minimal syntax
❌ **No curly braces or commas** like JSON

```yaml
# Example
app:
  name: "My WebApp"
  version: 1.0
  debug: true
```

Equivalent JSON:

```json
{
  "app": {
    "name": "My WebApp",
    "version": 1.0,
    "debug": true
  }
}
```

---

## 🧩 2. YAML = 3 Building Blocks

| Type         | Description                               | Example      |
| ------------ | ----------------------------------------- | ------------ |
| **Scalar**   | Single value (string, number, bool, etc.) | `count: 10`  |
| **Sequence** | Ordered list (like JSON array)            | `- apple`    |
| **Mapping**  | Key-value pairs (like JSON object)        | `name: Sara` |

Example combo 👇

```yaml
person:
  name: Sara
  age: 30
  hobbies:
    - painting
    - hiking
    - reading
```

---

## ✍️ 3. Indentation Rules

- Use **spaces only**, never tabs 🚫
- 2 spaces per level (standard)
- Indentation defines structure (like Python)

Bad ❌

```yaml
name: Sara
 age: 30
```

Good ✅

```yaml
name: Sara
age: 30
```

---

## 💬 4. Comments

Use `#` for inline or full-line comments.

```yaml
# Full line comment
timeout: 30 # Inline comment
```

✅ JSON does **not** support comments!

---

## 🧷 5. Strings in YAML

There are 4 styles — memorize them like this:

| Type              | Syntax          | When to use               |     |
| ----------------- | --------------- | ------------------------- | --- |
| **Plain**         | `name: Sara`    | Safe text (no symbols)    |     |
| **Single quoted** | `'I''m Sara'`   | No escape sequences       |     |
| **Double quoted** | `"Line\nBreak"` | Escape characters allowed |     |
| **Block scalars** | `|`or`>`        | Multi-line text           |

Examples 👇

```yaml
plain: hello
single: "it's ok"
double: "value\nwith escape"
```

---

## 🧱 6. Block Scalars (Multiline Texts)

Use when writing long strings (e.g., paragraphs, scripts).

```yaml
literal: | # Keep line breaks exactly
  line1
  line2 stays
  line3 too

folded: > # Fold lines into a single string (spaces)
  This is a long
  paragraph folded
  into one line.
```

💡 Memory Trick:

- `|` → keeps lines _as-is_
- `>` → folds lines _together_

### 🧠 Chomp Indicators:

| Type        | Syntax | Effect                  |
| ----------- | ------ | ----------------------- |
| **Strip**   | `>-`   | Remove trailing newline |
| **Keep**    | `>+`   | Keep extra newlines     |
| **Default** | `>`    | Keep one newline        |

```yaml
folded-strip: >-
  Hello
  World
```

---

## ⚙️ 7. Lists (Sequences)

```yaml
fruits:
  - apple
  - mango
  - banana
```

Inline style (JSON-like):

```yaml
fruits: [apple, mango, banana]
```

JSON Equivalent:

```json
{ "fruits": ["apple", "mango", "banana"] }
```

---

## 🔑 8. Dictionaries (Mappings)

```yaml
user:
  name: John
  role: admin
  active: true
```

Inline (Flow Style):

```yaml
user: { name: John, role: admin, active: true }
```

---

## 🧬 9. Anchors and Aliases

Anchors (`&`) and aliases (`*`) let you **reuse** YAML blocks like variables.
You can also **merge** values using `<<:`.

```yaml
# Database configuration anchor
database_config: &db_config
  host: localhost
  port: 5432
  username: myuser
  password: secret
  database: mydatabase

# Development environment
development:
  <<: *db_config
  pool_size: 10
  debug: true

# Production environment
production:
  <<: *db_config
  pool_size: 50
  debug: false
```

🧩 **Explanation:**

- `&db_config` → defines a reusable **anchor**
- `*db_config` → refers (alias) to that block
- `<<:` → **merge key**, merges key-value pairs from the aliased map

✅ Saves duplication
✅ Great for environments or shared configs

Equivalent JSON ❌ → Not possible (no anchors)

---

## 🪄 10. Tags and Data Types

Explicitly declare or override a data type using `!!`.

```yaml
str_num: !!str 123 # string, not number
real_num: !!float "3.14"
is_active: !!bool "true"
date: !!timestamp 2025-10-17
nothing: !!null ""
```

Custom type example:

```yaml
color: !RGB [255, 0, 0]
```

🧠 Useful when a parser guesses wrong (e.g., `"no"` becomes false in YAML 1.1)

---

## 🔁 11. Merge Multiple Documents

Use `---` to start new YAML documents and `...` to end (optional).

```yaml
---
env: dev
replicas: 1
---
env: prod
replicas: 5
```

🧠 Common in Kubernetes where one file defines multiple manifests.

---

## 💡 12. Complex Keys

You can use multi-line or structured keys with `?`.

```yaml
? |
  multi line key
: this is the value
```

Or use a list as a key:

```yaml
[apple, banana]: fruits combo
```

---

## 🧮 13. Sets and Null Values

YAML supports sets and nulls too.

```yaml
letters: !!set
  A: null
  B: null
  C: null
```

```yaml
missing_value: null
also_missing: ~
empty:
```

---

## 🧰 14. YAML vs JSON — Quick Battle

| Feature            | YAML                  | JSON                   |     |
| ------------------ | --------------------- | ---------------------- | --- |
| Syntax             | Indentation-based     | Braces + commas        |     |
| Comments           | ✅ Yes (`#`)          | ❌ No                  |     |
| Multi-line strings | ✅ `|`/`>`            | ❌ Must escape `\n`    |
| Anchors / Reuse    | ✅ `&` / `*`          | ❌ Not supported       |     |
| Readability        | 🥇 Human-friendly     | Good, but noisy        |     |
| Tooling            | Configs (DevOps, K8s) | APIs, data interchange |     |
| JSON subset        | ✅ JSON ⊂ YAML 1.2    | ❌ YAML ⊃ JSON         |     |

---

## 🧮 15. Same Example (YAML vs JSON)

**YAML!**

```yaml
app:
  name: ShopEasy
  version: 1.2
  features:
    - login
    - checkout
  flags:
    debug: false
    beta: true
```

**JSON!**

```json
{
  "app": {
    "name": "ShopEasy",
    "version": 1.2,
    "features": ["login", "checkout"],
    "flags": { "debug": false, "beta": true }
  }
}
```

---

## ⚠️ 16. Common YAML Pitfalls

| Mistake                   | Fix                               |
| ------------------------- | --------------------------------- |
| ❌ Using tabs             | Use spaces (2 or 4)               |
| ❌ Misaligned indentation | Keep consistent levels            |
| ❌ Colons inside strings  | Quote them `"key: value"`         |
| ❌ Wrong boolean style    | Use lowercase `true/false`        |
| ❌ Leading zeros          | Quote if you mean string `"007"`  |
| ❌ Dangling `-`           | Every list item must have content |

---

## 🧠 17. YAML 1.1 vs YAML 1.2 (Traps!)

| Example | YAML 1.1 | YAML 1.2       |
| ------- | -------- | -------------- |
| `yes`   | true     | "yes" (string) |
| `on`    | true     | "on" (string)  |
| `off`   | false    | "off" (string) |
| `no`    | false    | "no" (string)  |

Always prefer YAML 1.2 standard → use `true` / `false`.

---

## 🧩 18. YAML Flow Styles (Inline Mode)

You can use JSON-like inline syntax for compactness.

```yaml
person: { name: "John", age: 30, city: "Dubai" }
hobbies: [swimming, chess, coding]
```

Mix block + flow freely:

```yaml
employees:
  - { name: "Sara", dept: "IT" }
  - { name: "Omar", dept: "Finance" }
```

---

## 🔥 19. YAML Best Practices (DevOps Edition)

✅ **Do**

- Keep consistent indentation
- Use anchors for shared configs
- Use comments to explain configs
- Quote strings that contain special characters
- Validate YAML with tools (`yamllint`, `yamllint .github/workflows/`)

❌ **Don’t**

- Mix tabs and spaces
- Overuse anchors in large files (can get confusing)
- Forget the difference between block (`|`) and folded (`>`) scalars

---

## 🧩 20. Quick Memorization Formula

**👉 YAML = .**

> Spaces + Colons + Dashes
>
> - Anchors + Comments + Blocks

---

## 🧭 21. YAML in Real Tools

| Tool                | YAML usage                            |
| ------------------- | ------------------------------------- |
| **Kubernetes**      | Pods, Deployments, Services           |
| **GitHub Actions**  | Workflows (`.github/workflows/*.yml`) |
| **Docker Compose**  | Multi-container definitions           |
| **Azure Pipelines** | CI/CD pipeline definitions            |
| **Ansible**         | Playbooks                             |
| **Terraform Cloud** | Variable and workspace configs        |

---

## 🧠 22. JSON ⊂ YAML (Subset Rule)

Every valid JSON is also valid YAML — meaning:

✅ You can copy-paste JSON into a YAML parser, and it’ll work.
❌ But not every YAML works in JSON (anchors, comments, etc.)

---

## 🚀 23. Final Quick Reference — “YAML in 1 Minute”

```yaml
# comment
name: "YAML 101"
count: 3
tags: [beginner, config]
multi-line: |
  hello
  world
nested:
  key: value
  list:
    - one
    - two
merged:
  <<: *alias
anchors: &alias
  key: val
```

---

Would you like me to create a **visual YAML vs JSON cheat sheet (1-page poster)** with all syntax, symbols, and memory hints (like arrows for indentation and diagrams for anchors)? It’s great for quick recall before DevOps or Azure pipeline exams.

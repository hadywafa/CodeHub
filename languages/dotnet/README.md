# 🗂️ Learning Path Order

## 1. **Unit Testing Fundamentals**

- xUnit basics (`Fact`, `Theory`)
- Arrange-Act-Assert pattern
- FluentAssertions (readable expectations)
- Mocking with Moq / NSubstitute
- Test data with AutoFixture & Bogus

👉 Goal: Get comfortable testing _logic in isolation_.

---

## 2. **Testing Console Apps**

- Testing pure functions
- Capturing console output (`Console.SetOut`)
- Dependency injection in console apps for testability

👉 Goal: Learn how even CLI utilities can be test-driven.

---

## 3. **Integration Testing (Web API)**

- `WebApplicationFactory` for in-process testing
- Using EF Core with SQLite in-memory vs InMemory provider
- Database reset with Respawn
- Stubbing external APIs (WireMock.Net)
- Real dependencies with Testcontainers

👉 Goal: Be confident your API works as a whole system.

---

## 4. **MVC & Razor Page Testing**

- Controller unit tests (with fake services)
- View rendering checks
- UI smoke tests with Playwright (E2E browser automation)

👉 Goal: See how MVC + UI can be validated beyond controllers.

---

## 5. **Contract Testing**

- Consumer-driven contracts with Pact.NET
- Generating Pact files and verifying them in provider CI

👉 Goal: Prevent breaking other teams who rely on your API.

---

## 6. **Advanced Test Styles**

- Snapshot/approval testing with Verify
- Approval testing for JSON, HTML, and emails
- Mutation testing with Stryker.NET

👉 Goal: Increase trust in your test suite, not just line coverage.

---

## 7. **Performance & Load Testing**

- BenchmarkDotNet (micro-benchmarks)
- k6 (API load testing)

👉 Goal: Catch slowdowns before your users do.

---

## 8. **Quality Gates & CI/CD Integration**

- Coverage reports with Coverlet + ReportGenerator
- Enforcing minimum coverage/mutation thresholds
- Adding tests to GitHub Actions / Azure Pipelines

👉 Goal: Automation: tests should run every PR, with reports visible to the team.

---

## 9. **Testing Philosophy & TDD**

- Test naming conventions (`Method_Scenario_Result`)
- Red-Green-Refactor cycle
- Testing smells (overspecified, brittle, too many mocks)
- Choosing the right balance in the testing pyramid

👉 Goal: Write tests that are maintainable and actually helpful.

---

⚡ My suggestion: spend **1 week per block**, starting with **Unit Tests → Console → API Integration → MVC/E2E**, then branch into advanced (contracts, mutation, performance, CI).

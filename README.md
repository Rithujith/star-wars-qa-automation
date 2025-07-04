# Star Wars App QA Automation

Automated UI and API testing suite for the [Star Wars React App](https://github.com/MindfulMichaelJames/star-wars), designed as part of a QA Engineer technical assessment.

---

## 🚀 Features

- **UI Automation**: Selenium-based end-to-end tests for sorting, movie details, and negative scenarios.
- **API Automation**: REST API validation using the public [SWAPI](https://swapi.dev).
- **CI/CD Integration**: Automated test execution via GitHub Actions on every push and pull request.
- **Reusable Architecture**: Page Object Model and utility helpers for maintainable, scalable tests.

---

## 🗂️ Project Structure

```
star-wars-qa-automation/
│
├── tests/
│   ├── ui/        # Selenium UI tests
│   ├── api/       # API validation tests
│   └── utils/     # Page objects & helpers
├── .github/
│   └── workflows/ # CI/CD pipeline
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🛠️ Setup & Usage

### 1. Clone Repositories

```sh
# Clone the QA automation repo
git clone https://github.com/Rithujith/star-wars-qa-automation.git

# Clone the Star Wars frontend app
git clone https://github.com/MindfulMichaelJames/star-wars.git
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Start the Star Wars App

In a separate terminal, run:

```sh
cd star-wars
npm install
npm run build   # For production mode
npm start       # Or use `npm run dev` for development mode
```
The app should be running at [http://localhost:3000](http://localhost:3000).

### 4. Run Tests

From the QA automation directory:

```sh
pytest
```
- To run only UI or API tests:
  - `pytest tests/ui`
  - `pytest tests/api`

---

## 🎯 Test Scenarios Covered

### UI Tests
- **Sort movies by Title** and assert the last movie is _The Phantom Menace_.
- **View _The Empire Strikes Back_** and check if the Species list contains _Wookie_.
- **Assert that Planets list for _The Phantom Menace_ does NOT contain _Camino_.**

### API Tests
- **Validate movies count** is 6.
- **Check director of the 3rd movie** is _Richard Marquand_.
- **Assert producers of the 5th movie** are NOT _Gary Kurtz, George Lucas_.

---

## 🧑‍💻 CI/CD

- All tests are automatically run on every push and pull request via [GitHub Actions](.github/workflows/ci.yml).
- Results are available in the **Actions** tab of your repo.

---

## 📝 Author

**Rithujith Roshan**

---

## 💡 Notes

- Requires [Google Chrome](https://www.google.com/chrome/) for Selenium UI tests.
- Make sure the frontend app is running before executing UI tests.
- For any issues or suggestions, feel free to open an issue or PR.

---

# Star Wars App QA Automation

This project contains automated UI and API tests for the [Star Wars App](https://github.com/MindfulMichaelJames/star-wars/tree/main), as part of a QA Engineer technical assessment.

## Features
- **UI Automation**: Selenium-based tests for movie sorting, details, and negative scenarios.
- **API Automation**: REST API tests for Star Wars movie data.
- **CI/CD**: Automated test execution via GitHub Actions.

## Project Structure
```
star-wars-qa-automation/
│
├── tests/
│   ├── ui/
│   ├── api/
│   └── utils/
├── .github/
│   └── workflows/
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup
1. Clone this repo and the Star Wars App repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests locally:
   ```bash
   pytest
   ```

## CI/CD
Tests run automatically on every push via GitHub Actions (`.github/workflows/ci.yml`).

## Author
[Your Name]

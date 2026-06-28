# Manual and Automated QA Project for the QA Bootcamp Website

In this project, a complete Quality Assurance (QA) process was carried out on the main functionality of the website: https://web-qa.dev.adalab.es/

The project was developed as a team using the Scrum agile methodology and BDD (Behavior-Driven Development) for test design before development, following testing best practices.

## Test Plan, Results, and Bug Reports: [View Test Plan]([https://bootcampqa-equipo2.atlassian.net/wiki/spaces/SCRUM/pages/294913/Plan+de+Pruebas+-+Web+Vida+Verde])

This document details the test plan, the functionalities tested, the results of the executed tests, and the bug reports.

## E2E Automation – Technologies

* Python 3.12+
* Playwright v1.48

## Automated Test Results

A continuous integration workflow has been configured with GitHub Actions to run the tests after every change and once a week at the end of each sprint.

You can check the latest test execution results and download the test report from the following link:

![Test Workflow](https://github.com/Bootcamp-QA/playwright-python-template/actions/workflows/playwright_tests.yml/badge.svg)

## Project Requirements

### Python 3.12

Download and install Python 3.12 from the official website:

https://www.python.org/downloads/

Make sure Python is added to the PATH during installation.

### Install Dependencies

Once Python is installed:

1. Clone this repository.
2. Navigate to the project folder.
3. Run the following commands in the terminal:

```bash
pip install -r requirements.txt
```

```bash
playwright install
```

### Run Tests Locally

Navigate to the project folder and run:

```bash
pytest --headed
```

Alternativelly you can use the folowing 

```bash
python -m pytest --headed
```

## Team Members

* Irene Arribas Méndez
* Anna Moreno Bonell
* Sara Posada Domínguez
* Florencia Raquel Posse



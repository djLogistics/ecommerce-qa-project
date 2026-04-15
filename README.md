# E-Commerce QA Automation Project

## Overview
This project demonstrates end-to-end testing of an e-commerce web application (SauceDemo) using both manual and automated testing techniques.

## Features Tested
- User login validation
- Product selection
- Add-to-cart functionality
- Cart verification

## Automation
- Built using Selenium WebDriver with Python
- Implemented explicit waits for dynamic elements
- Designed validation logic for pass/fail test outcomes
- Configured browser settings to disable password manager and security popups, ensuring stable test execution

## Project Structure
- tests/ → automation scripts
- docs/ → test plan and bug reports
- test-cases.xlsx → manual test cases

## Requirements
- Python 3.x
- Google Chrome

## Setup
pip install -r requirements.txt
pytest

## Test Coverage
- Login functionality (valid credentials)
- Add item to cart
- Cart validation

## Skills Demonstrated
- Page Object Model (POM) design pattern
- Test automation using Selenium WebDriver and pytest
- Writing reusable and maintainable test code
- Implementing explicit waits for reliable UI testing
- Debugging and resolving Selenium test failures
- Structuring a scalable QA automation framework
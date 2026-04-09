# AI Code Reviewer

AI Code Reviewer is a simple Streamlit-based web application that analyzes source code and provides instant feedback on bugs, performance, coding style, and security issues based on predefined static rules. The project also generates a basic refactored version of the submitted code and displays an overall quality score.

## Features

- Multi-language selection interface
- Code review based on static pattern checks
- Issue categorization into:
  - Bugs
  - Performance
  - Style
  - Security
- Quality score out of 100
- Optional refactored code output
- Clean dark-themed Streamlit interface

## Project Structure

```bash
.
├── app.py
├── reviewer.py
├── requirements.txt
└── README.md
```

## Files Description

### `app.py`
This is the main Streamlit application file. It handles:
- Page configuration
- Custom UI styling
- Sidebar settings
- Code input area
- Review button action
- Displaying results such as score, summary, detected issues, and refactored code

### `reviewer.py`
This file contains the backend logic for code analysis. It includes:
- Static rule-based checks for bugs, performance, style, and security
- Quality score calculation
- Refactored code generation
- Final review result packaging in dictionary form

## Requirements

- Python 3.8 or above
- pip

## Installation

1. Clone or download the project files.
2. Open the project folder in terminal.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Run the Streamlit app using:

```bash
streamlit run app.py
```

After running the command, Streamlit will open the application in your default web browser.

## Live Demo
[Open App](https://ai-code-reviewer-grwmcjzjo32dsxsgjufrvm.streamlit.app/)

AI Code Reviewer is a Streamlit-based web app that analyzes code for bugs, performance, style, and security issues.

## How It Works

1. Select the programming language from the sidebar.
2. Choose the review depth.
3. Enable or disable focus areas such as Bugs, Performance, Style, Security, and Refactor Code.
4. Paste your code into the text area.
5. Click **Review Code**.
6. View the generated score, summary, issue lists, and refactored code.

## Analysis Rules Used

The current implementation uses simple static pattern matching rules such as:

- Detecting debug print statements
- Detecting possible misuse of comparison operators
- Detecting hardcoded passwords
- Detecting use of `eval()`
- Detecting inefficient iteration patterns like `range(len(...))`
- Suggesting modularization for long code

## Output

The system returns:
- A score from 0 to 100
- A summary message
- Lists of issues in separate categories
- A refactored version of the code

## Limitations

- The project uses rule-based checks, not advanced AI or machine learning
- It does not perform deep semantic understanding of code
- The refactoring output is basic and not optimized for production use
- File upload support is not included yet

## Future Enhancements

- Integrate LLM APIs for smarter code understanding
- Add file upload support for source files
- Expand language-specific rule sets
- Add downloadable review reports
- Connect with GitHub repositories for automatic review

## Author

Minor Project — AI Code Reviewer

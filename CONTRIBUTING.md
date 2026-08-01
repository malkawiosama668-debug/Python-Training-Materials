# Contributing to the Python Training Program

First off, thank you for considering contributing to this repository! This guide is meant to be a living document, and community contributions are what keep the 60-Hour Python Training Program accurate, comprehensive, and useful for everyone learning programming, data science, and machine learning.

Whether you are fixing a typo in a practice module, adding a new script for a logic gate simulator, or sharing an updated deployment method for YOLO models, your help is appreciated.

## 📋 Table of Contents

* [How Can I Contribute?](#️-how-can-i-contribute)
* [Submission Workflow](#-submission-workflow)
* [Style Guide & Formatting](#-style-guide--formatting)
* [Keeping Your Fork Synced](#-keeping-your-fork-synced)
* [Code of Conduct](#-code-of-conduct)

---

## 🛠️ How Can I Contribute?

There are several ways you can contribute to this project:

* **Add New Practice Modules:** Have a great exercise for teaching Python fundamentals, a new data science dataset to explore, or a script for machine learning deployment? We want it.
* **Update Existing Content:** Python and its libraries evolve quickly. If a syntax is deprecated (e.g., in pandas or TensorFlow) or a setup guide is out of date, please submit an update.
* **Fix Formatting or Typos:** Clean, readable documentation and well-commented code are key for learners. Minor corrections are always welcome.
* **Suggest Topics:** If you don't have the time to write a module but want to request one, feel free to open an Issue.

---

## 🔄 Submission Workflow

To submit a contribution, please follow the standard GitHub Pull Request (PR) workflow:

1. **Fork the Repository:** Click the "Fork" button at the top right of the repository page.
2. **Clone Your Fork:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/python-training-program.git
    cd python-training-program
    ```

3. **Create a Branch:** Create a uniquely named branch for your feature or fix.

    ```bash
    git checkout -b add-yolo-deployment-module
    ```

4. **Make Your Changes:** Add or edit the Markdown or Python (`.py`) files in the appropriate directory (e.g., modules/machine-learning/).

5. **Commit Your Changes:** Write a clear, concise commit message.

    ```bash
    git commit -m "docs: add practice module for YOLO object detection"
    ```

6. **Push to Your Fork:**

    ```bash
    git push origin add-yolo-deployment-module
    ```

7. **Open a Pull Request:** Navigate to the original repository and click "Compare & pull request." Provide a brief description of what you added or fixed.

## 📝 Style Guide & Formatting

To keep the repository clean and easily scannable for students, please adhere to the following formatting guidelines when writing your files:

1. **File Naming**
    Use lowercase letters and hyphens for file names (or underscores for Python scripts if they need to be imported).
    * Good: logic_gate_simulator.py or 01-variables-basics.md
    * Bad: Logic Gate Simulator.py or 01 Variables.md

2. **Headings and Structure (for Markdown)**
    Start every new document with a single H1 (#) title, followed by a brief description of the lesson. Use H2 (##) and H3 (###) for subsequent sections.

3. **Code Blocks**
    Always use syntax highlighting for code blocks in documentation. Specify the language (e.g., python, bash, json).

    Example:

    ```python

    # Initialize the logic gate variables
    input_a = True
    input_b = False

    # Simulate an AND gate
    output = input_a and input_b
    print(f"AND Gate Output: {output}")
    ```

4. **Context is Key**
    When adding a new concept or code snippet, briefly explain what it does and why it is useful for the learner.
    * Good: `df.dropna(inplace=True)` — This removes any rows containing missing (NaN) values from the DataFrame, which is a crucial step in cleaning data before training a model.
    * Bad: Run `df.dropna()`.

5. **Categorization**
    Place your code or note in the most relevant folder. If you are adding a lesson on loops, it belongs in the fundamentals modules. If you are adding a computer vision script, it belongs in the machine learning section. If you are unsure where a file belongs, just place it in the root directory, and it can be moved during the PR review.

## 🔄 Keeping Your Fork Synced

Before creating a new branch or opening a pull request, please ensure your fork is up to date with the original repository to avoid merge conflicts.

1. **Add the upstream repository** (You only need to do this once):

    ```bash
    git remote add upstream https://github.com/AhmadAbukhuit/python-training-program.git
    ```

2. **Fetch and merge the latest updates:**

    ```bash
    # Download the latest changes from the original repo
    git fetch upstream

    # Ensure you are on your local main branch
    git checkout main

    # Merge the updates into your local main branch
    git merge upstream/main

    # Push the synced changes up to your GitHub fork
    git push origin main
    ```

## 🤝 Code of Conduct

This project is an open and welcoming environment designed to help people learn. Please be respectful, encouraging, and constructive in your PR descriptions, issue comments, and code reviews.

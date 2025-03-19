# AI AGENTIC Automation Project

This project automates website testing and interaction using AI and browser automation tools. It leverages Playwright for browser control, LangChain with Google Gemini for AI-driven task execution, and browser-use for seamless integration.

## Table of Contents

-   [Project Description](#project-description)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Configuration](#configuration)
-   [Testing](#testing)
-   [Contributing](#contributing)
-   [License](#license)

## Project Description

This project automates web UI testing by using an AI agent to follow a series of steps on a website. The agent uses the Google Gemini AI model to understand instructions and Playwright to interact with the browser. The results are stored in a JSON file for analysis.

Key features include:

-   Automated website navigation and interaction.
-   AI-driven task execution and validation.
-   Configuration management for API keys and settings.
-   Structured project layout for easy expansion and maintenance.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [your-repository-url]
    cd my-automation-project
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Usage

1.  **Configure API keys:**
    * Open `config/config.yaml` and replace `YOUR_GEMINI_API_KEY` with your actual Google Gemini API key.
    * Ensure the `website_url` is set to the correct website you wish to test.

2.  **Run the automation:**

    ```bash
    python src/main.py
    ```

3.  **View results:**
    * The results of the agent's run will be saved in `data/agentresults.json`.
    * The console will also display the final test result.

## Configuration

The project uses a `config/config.yaml` file to store configuration settings.

```yaml
gemini_api_key: "YOUR_GEMINI_API_KEY"
website_url: "[https://rahulshettyacademy.com/loginpagePractise/](https://rahulshettyacademy.com/loginpagePractise/)"
# llm-exchange-viewer

A desktop application for viewing single-prompt LLM exchanges (prompt, response, system prompt) that have been saved locally.

# Installation

In a Python3.11 environment, install the requirements from `requirements.txt`. Run `python main.py` to confirm installation.

- `python -m venv venv`
- `source venv/bin/activate` or `.\venv\Scripts\activate` (Windows)
- `python --version` (should be 3.11.x)
- `python main.py` (should launch GUI)

# Usage

This app assumes that you have local records of LLM exchanges in a specific format. Specifically, this app assumes you have at least one folder that contains the following kinds of files:
- `prompt.txt`
- `response.txt
- `system.txt`

Note that the names of the files don't need to match exactly, but the content should be present: prompt, response, and system prompt.

To run the app, activate the corresponding environment created in `Installation`, then run `python main.py`. The GUI will open. At the top, you will have the option to select a folder. This folder should contain at least the three kinds of files listed above. Once you have selected a folder, you have three dropdown menus: one to select the prompt file, one to select the response file, and one to select the system prompt file.

The prompt file will be displayed in plaintext in the upper text region. The response file will be displayed with rendered Markdown in the lower text region. To view the system prompt, click the button in the bottom right of the GUI.

To view a different LLM exchange, simply select a different folder, and modify the dropdowns accordingly to point to your prompt, response, and system prompt.

For questions or suggestions, please email `ariessunfeld@eworldes.com`.


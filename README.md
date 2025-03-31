# Selenium Stealth Interaction Test

This project is designed to test the detection of Selenium automation using undetected‑chromedriver by simulating human-like interactions on a detection site. The script retrieves values from `window.token` and `window.getAsyncToken()`, simulates natural typing behavior into the input fields, and then clicks the "Interaction Test" button. It attempts to bypass automation detection by disabling and overriding various browser features.

> **Disclaimer:**  
> No solution can guarantee 100% undetectability. This project employs several techniques to minimize automation fingerprints, but advanced detection systems may still detect the automation.

## Features

- **Human-like random wait times:** Simulates natural delays between actions.
- **Comprehensive Chrome options:** Disables features that could reveal automation.
- **ActionChains simulation:** Mimics human typing behavior.
- **Retrieval and injection of tokens:** Gets values from `window.token` and `window.getAsyncToken()` and inputs them into the webpage.
- **Interaction Test automation:** Clicks the "Interaction Test" button and prints the detection result.

## Requirements

- Python 3.8+
- [undetected‑chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
- [Selenium](https://www.selenium.dev/)

Install the required packages using pip:

```bash
pip install undetected-chromedriver selenium
```

## Usage

1. **Clone or download this repository.**
2. **Run the script:**  
   Execute the Python file (e.g., `python3 RUN_ME.py`).  
   The script will open a browser window, navigate to the detection site ([https://hmaker.github.io/selenium-detector/](https://hmaker.github.io/selenium-detector/)), simulate human input for the token values, click the "Interaction Test" button, and finally print the detection result to the console.

3. **Observe the result:**  
   The script will keep the browser open for a while (90 seconds) before closing so you can inspect the output.

## Code Overview

- **wait_random(min_time, max_time):**  
  A helper function that simulates human-like random wait times.
  
- **Main Function:**  
  - Configures a comprehensive list of Chrome options to disable automation-related features.
  - Launches the browser using undetected‑chromedriver.
  - Retrieves `window.token` and `window.getAsyncToken()` values via JavaScript.
  - Uses Selenium ActionChains to simulate natural typing into the input fields.
  - Clicks the "Interaction Test" button.
  - Prints the detection result.

## Limitations

- **Detection:**  
  Even with all these measures, there is no guarantee that the automation will be 100% undetectable. Modern detection methods are highly advanced and constantly evolving.
- **Performance:**  
  Extensive Chrome options and stealth techniques might affect the performance of the automated session.

## Contributing

If you have improvements or additional stealth techniques to share, feel free to open an issue or submit a pull request.

## License

This project is provided "as is" without any warranty. Use it at your own risk.


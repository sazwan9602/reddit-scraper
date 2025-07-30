# Reddit Scraper

## Installation
> **Note:** This project requires **Python 3.9** or above.
  
You can use **HTTPS** or **SSH** to clone the repository:

- **HTTPS:**
    ```bash
    git clone https://github.com/sazwan9602/reddit-scraper.git
    ```

- **SSH (optional):**
    ```bash
    git clone git@github.com:sazwan9602/reddit-scraper.git
    ```

Then navigate into the project directory:
    ```bash
    cd reddit-scraper
    ```
1. Create and activate a Python virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Scrape a Subreddit

Run the scraper and enter the subreddit name when prompted:
```bash
python scrape.py
```

### View the Data

Start the web server:
```bash
python main.py
```
Open your browser and go to: [http://127.0.0.1:5000/]

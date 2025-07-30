import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
)


adapter = HTTPAdapter(max_retries=retry_strategy)


session = requests.Session()
session.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
)
session.mount("http://", adapter)
session.mount("https://", adapter)


def get(url: str) -> dict | None:
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} {e.response.reason}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Check your network or the server.")
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")

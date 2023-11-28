# Selenium Testing Example
Welcome to my selenium testing example project! This project will grow over time as more test cases are added to it for testing different websites and their associated functionality.
## Setup
- Clone this repository to your local drive:
```
cd path/to/local/
git clone https://github.com/an0nan0nan0n/jr-duckduckgo-selenium-python.git
```
- Ensure Python version 3.11.4+ is installed: [Python Downloads](https://python.org/downloads) 
- Install project packages from [jr-duckduckgo-selenium-python/requirements.txt](https://github.com/an0nan0nan0n/jr-duckduckgo-selenium-python/blob/main/requirements.txt):
```
cd path/to/local/jr-duckduckgo-selenium-python/
python -m pip install -r requirements.txt
```
## Run Tests
- Use the following command to run all tests:
```
  python -m pytest -s -vv path/to/local/jr-duckduckgo-selenium-python/tests
```
- The `-s` flag was included to capture stdout so things like `print()` calls are captured in the output.
- The `-vv` flag was included to capture the maximum verbose output.
- There are more flags you can use in pytest when running tests using our `python -m pytest` approach. For a full list go here: https://docs.pytest.org/en/6.2.x/usage.html

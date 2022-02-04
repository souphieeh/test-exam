# Test Exam

## Exercise 1 (1 P.)

Fork the repository into your own github account.

## Exercise 2 (3 P.)

Change the `main.css` to match the following image

![index.png](index.png)

## Exercise 3 

Open the file `scrape.py` and implement the following behavior.

```python
from bs4 import BeatifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_ursids"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

bears = [elem.string for elem in soup.select('th[scope=row] a')]
print(bears)



```

## Exercise 4

Copy the code from the webscraper into `run.py`, add a button to run the
webscraping.

## Exericse 5

Create a new page that extends `base.html` and displays the results from the
Webscraping.

## Exericse 6

Create a pull request to upstream.

## Exercise 7

Create a new branch an implement an alternative design. Create another pull
request from this new branch.

# Test Exam
This is an example of what the next computer science exam will look like. The exam will be *open book*, which means that you may use any resources at your disposal: jupyter notebooks, the mini project files, the internet ...

**Communication with classmates or external persons is forbidden**

## Exercise 1 (Fork the Repo - 1 P.)

Fork the repository into your own github account.

## Exercise 2 (Some Styling - 3 P.)

Change the `main.css` to match the following image

![index.png](index.png)

## Exercise 3 (Write a Webscraper - 4 P.)

1. Go to the website 'https://www.w3schools.com/cssref/css_selectors.asp' and
   inspect the table elements. Which HTML/CSS tags do they have?
2. The middle entry in the table has a CSS class. What is it called?
3. Open the file `scrape.py` and read through the code.
3. Run the code and compare the newly created file `selectors.json` with the
   table on the website. What do you observe?
4. Rewrite the code as a function `my_scraper()` that does all three tasks: webscraping, filtering and writing to a json file.
5. Delete `selectors.json` and run the program in `scrape.py`; if
   everything works out you should see that file reappear. Copy the three
   functions to the `run.py` file. Make sure any required modules are loaded at
   the beginning.


## Exercise 4 (Integrating into Your Website - 4 P.)

1. Copy the code from `scrape.py` into `run.py` as indicated.
1. Add a page called `webscraping.html` to your website that extends `base.html`.
1. Add a link on this page that runs the webscraping function (i.e. when you click the link, the function my_scraper() is
   executed). You can test this by deleting the file `selectors.json` and
   clicking the link. The file should then be recreated. Hint: This link should lead to a new page - I called it `success.html`.


## Exericse 5 (Displaying your Results - 4 P.)

1. The page `css-selectors.html` extends `base.html` and displays the
   results from the webscraping.
1. Play around with the display. Perhaps use `choice` to show a random
   selector, or create a table that shows all results in your own style.


## Exericse 6 (Pull Request - 1 P.)

Create a pull request to upstream.

## Exercise 7 (Bonus 1: Create a new Design - 2 P.)

Create a new branch an implement an alternative design. Create another pull
request from this new branch.

## Exercise 8 (Bonus 2: Filtering - 3 P.)
Implement a filter function on your scraping results that only return selectors
which contain a single `:`. When finished create another pull request.

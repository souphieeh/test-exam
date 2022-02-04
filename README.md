# Test Exam

## Exercise 1 (Fork the Repo - 1 P.)

Fork the repository into your own github account.

## Exercise 2 (Some Styling - 3 P.)

Change the `main.css` to match the following image

![index.png](index.png)

## Exercise 3 (Write a Webscraper - 4 P.)

1. Go to the website 'https://www.w3schools.com/cssref/css_selectors.asp' and inspect the table elements. Which HTML/CSS tags do they have?

2. The middle entry in the table has a CSS class. What is it called?

3. Open the file `scrape.py` and implement the following.

- Change the source URL to the above website.
- Change the selector so that all the table entries are scraped.
- Change the output so that it writes to a text file 'output.json' instead of the console. You can use the code below as a guide.
```
# changes a list to the json format
output = json.dumps(selectors)

# writes to a json file
with open("output.json", "w") as file:
    file.write(output)
```

4. Test your code by running it using the run button. You should see a file called output.json in the left sidebar.


## Exercise 4 (Organize your Output - 3 P.)

Organize the output so that each row becomes its own json entry:
```
[
    {
        "selector": "first entry of first row",
        "example":  "second entry of first row",
        "example description": "third entry of first row",
    },

    {
        next row ...
    }
]
```

## Exercise 5

- Copy the code from the webscraper into `run.py' as the function 'my_scraper()'.
- Add a page called 'scraping.html' that extends the base template.
- Add a button (link) to this page that runs the webscraping function in the background (i.e. on  clicking the link the function my_scraper() is executed).
- Use the json to recreate the table from the website with your own styling.


## Exericse 6

Create a new page that extends `base.html` and displays the results from the
Webscraping.

## Exericse 7

Create a pull request to upstream.

## Exercise 8

Create a new branch an implement an alternative design. Create another pull
request from this new branch.

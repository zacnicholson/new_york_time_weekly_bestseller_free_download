New York Times Weekly Ebook Downloader

This script automates the download of the newest best sellers on the NYTs lists. To use this script, you must first sign up for a free account on https://singlelogin.app/registration.php. The account will give you 10 free downloads per day.

To use the script, follow these steps:

    Paste your username in line 40 of main.py
    Paste your password in line 42 of main.py
    Choose the list you want to download from the following options:
        Advice, How-To & Miscellaneous (https://www.nytimes.com/books/best-sellers/advice-how-to-and-miscellaneous/)
        Paperback Nonfiction (https://www.nytimes.com/books/best-sellers/paperback-nonfiction/)
        Paperback Trade Fiction (https://www.nytimes.com/books/best-sellers/trade-fiction-paperback/)
        Hardcover Nonfiction (https://www.nytimes.com/books/best-sellers/hardcover-nonfiction/)
        Hardcover Fiction (https://www.nytimes.com/books/best-sellers/hardcover-fiction/)
        Combined Print & E-Book Nonfiction (https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-nonfiction/)
        Combined Print & E-Book Fiction (https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-fiction/)
    Copy the URL of the chosen list and paste it into line 21 of main.py
    The script will download up to 10 books per day and rename them to remove the "(z-lib.org)" from the file name.
    By default, the script is set to run headless (chrome hidden). If you want to change this, edit line 11 of main.py.

Note: This script is current as of September 2021, and may not work with future updates to the NYTs website.

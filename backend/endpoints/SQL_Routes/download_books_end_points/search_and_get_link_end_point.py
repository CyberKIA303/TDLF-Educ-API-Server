import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import (APIRouter, HTTPException)
from . import (Book, Author, Book_Authors)
from fastapi.concurrency import run_in_threadpool
import requests

GetBookLinkRoute = APIRouter(prefix="/get_book_link", tags=["let be code and emortals"])

def search_book_online(title: str):
    urls = [
        {"type": "gutendex", "url": f"https://gutendex.com/books/?search={title}"}
    ]
    found: bool = False
    dns: str = None
    data: list = []
    for web in urls:
        if web["type"] == "gutendex":
            response = requests.get(web["url"]).json()
            books = response["results"]
            for book in books:
                formats = book["formats"]
                if "application/pdf" in formats:
                    book_title: str = book.get("title", "N/A")
                    authors: list = []
                    for author in book.get("authors", []):
                        authors.append(author.get("name", "N/A"))
                    url = formats.get("application/pdf", "")
                    pic_url = formats.get("image/jpeg", "")
                    check = Book.read_book_by("book_name", book_title)
                    trim = check["data"]
                    if not trim:
                        Book.create_book(book_title, url, pic_url)
                        for author in authors:
                            res = Author.read_author_by(author)
                            trim2 = res["data"]
                            if not trim2:
                                Author.create_author(author)
                            bid = Book.read_book_by("book_name", book_title)["data"][0]["book_id"]
                            aid = Author.read_author_by("author_name", author)["data"][0]["author_id"]
                            Book_Authors.create_book_authors(bid, aid)
                    found = True
                    break
            if found:
                dns = web["type"]
                break
        else:
            continue


@GetBookLinkRoute.post("/")
async def get_and_retrive_book_data(title: str):
    try:
        response = Book.read_book_by("book_name", title)
        print(response)
        print(type(response))
        check = response[0].get("data")
        check = False
        if not check:
            search_book_online(title)
            response = Book.read_book_by("book_name", title)
        return response
    except Exception as e:
        raise HTTPException(500, Exception)
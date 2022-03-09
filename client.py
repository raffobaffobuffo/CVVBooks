import requests
import json
from bs4 import BeautifulSoup

class Client:
    def __init__(self, uid, pwd):
        self.Session = requests.Session()
        isLogged = self.LogIn(uid, pwd)
        assert isLogged, "Log in failed"
        print(" * Logged to ClasseViva")

    def LogIn(self, uid, pwd):
        request = self.Session.post("https://web.spaggiari.eu/auth-p7/app/default/AuthApi4.php?a=aLoginPwd",
                data = {"uid": uid, "pwd": pwd})
        response = json.loads(request.content)["data"]["auth"]["loggedIn"]
        return response

    def GetBooks(self):
        result = list()
        content = BeautifulSoup(self.Session.get("https://web.spaggiari.eu/ldt/app/default/libri_studente.php").content, "html.parser")
        books = content.find_all("tr", class_="gen ado")
        for book in books:
            id = book.find_all("p", class_="open_sans_condensed darkgraytext font_size_12 bold margin_top_2")[1].text
            title = book.find_all("p", class_="open_sans_semibold darkgraytext font_size_16 bold")[0].text
            price = book.find_all("p", class_="open_sans_condensed darkgraytext font_size_14 bold")[0].text
            to_buy = book.find_all("p", class_="open_sans_condensed graytext font_size_13 margin_top_2")[0].find("strong").text
            link = f"https://www.amazon.it/s?k={id}"
            result.append({"id": id, "title": title, "price": price, "toBuy": to_buy,
                    "link": link})
        return result

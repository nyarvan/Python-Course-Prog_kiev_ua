def login(other_url):
    def authorization(func):
        login = "Ivan"
        password = "12344321"
        input_log = "Ivan"
        input_password = "12344321"
        def wrapper(*args, **kwargs):
            if login == input_log and password == input_password:
                return func(*args, **kwargs)
            else:
                return other_url
        return wrapper
    return authorization

@login("login.html")
def get_adress(url):
    return url

if __name__ == "__main__":
    url = "www.python.com"
    adress = get_adress(url)
    print(adress)
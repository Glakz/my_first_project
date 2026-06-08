example_url = "https://www.udemy.com/python-full-course"
 
class URL:
    def __init__(self, url):
        self.url = url
 
        if "://" in self.url:
            self.__protocol, remainder = self.url.split("://", 1)
        else:
            self.__protocol = None
            remainder = self.url
 
        if "/" in remainder:
            self.__domain, bread_crumbs = remainder.split("/", 1)
            self.__bread_crumbs = "/" + bread_crumbs if bread_crumbs else None
        else:
            self.__domain = remainder
            self.__bread_crumbs = None
 
    def get_protocol(self):
        return self.__protocol

    def is_secure(self):
        if self.__protocol == "https":
            return True
        elif self.__protocol == "http":
            return False

    def get_domain(self):
        return self.__domain
 
    def get_bread_crumbs(self):
        if self.__bread_crumbs == False:
            return "bread_crumbs not found"
        else:
            return self.__bread_crumbs
    # Добавьте метод just_domain, который удалит из объекта всю информацию о "хлебных крошках".
    def just_domain(self):
        if self.__bread_crumbs:
            # через срез
            self.url = self.url[:self.url.index(self.__bread_crumbs)]
            self.__bread_crumbs = None
        return self

    def __str__(self):
        return self.url

url = URL(example_url)
url.just_domain()
print(url)


    


class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Article author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Article magazine must be a Magazine instance")
        self._magazine = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if hasattr(self, "_title"):
            return
            # raise Exception("Article title cannot be changed")
        if not isinstance(new_title, str):
            raise Exception("Article title must be a string")
        if not (5 <= len(new_title) <= 50):
            raise Exception("Article title must be 5 – 50 characters long")
        
        self._title = new_title

        
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        if len(name) <= 0:
            raise Exception("Author name cannot be empty")
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            return
            raise Exception("Author name cannot be changed")
        self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Magazine name must be a string!")
        if not (2 <= len(new_name) <= 16):
            raise Exception("Magazine name must be 2–16 characters long")
        self._name = new_name
        
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise Exception("Magazine category must be a string and at least 1 character long")
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass


jay = Author("Rihanna")
print(jay.name)

# jay.name = "Callum Scott"
# print(jay.name) - Exception: Author name cannot be changed
vogue = Magazine(name="Vogue", category="Lifestyle")
print(vogue.name)
print(vogue.category)

# ariel = Magazine(name="a", category="Lifestyle") # Exception: Magazine name must be 2–16 characters long
# print(ariel.name) # Exception: Magazine name must be a string!

panda = Magazine(name="panda", category="Animals")
print(panda.category)
# panda.category = "" # Exception: Magazine category must be a string and at least 1 character long
# print(panda.category)

article1 = Article(jay, vogue, "Fashion and Culture")
print(article1.title)
# article1.title = "Another Title" #Exception: Article title cannot be changed
# print(article1.title)

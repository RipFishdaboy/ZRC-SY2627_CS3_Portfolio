class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        Publication.__init__(self, title, author)
        self.number_of_pages = number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.number_of_pages = number_of_pages
        else:
            print("Number of pages must be positive.")

    def get_number_of_pages(self):
        return self.number_of_pages

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        Publication.__init__(self, title, author)
        self.issue_number = issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.issue_number = issue_number
        else:
            print("Issue number must be positive.")

    def get_issue_number(self):
        return self.issue_number

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
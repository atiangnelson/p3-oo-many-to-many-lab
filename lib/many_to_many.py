class Author:
    
    def __init__(self,name:str):
        self.name=name
        self._contracts=[]
        self._books=[]


    def contracts(self):
        return self._contracts
    
    def books(self):
        return list ({contract.book for contract in self._contracts})
    
    def sign_contract(self, book, date: str, royalties: int):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)



class Book:
    def __init__(self,title:str):
        self.title=title
        self._contracts=[]


    def contracts(self):
        return self._contracts 

    def authors(self):
        return list({contract.author for contract in self._contracts})   
    
     



class Contract:
    all_contracts=[]

    def __init__(self,author,book,date:str,royalties:int):
        if not isinstance(author,Author):
            raise TypeError("Invalid author")
        self.author=author
        if not isinstance(book,Book):
            raise TypeError("Invalid book")
        self.book=book
        if not isinstance(date,str):
            raise TypeError("date must be a string")
        self.date=date
        if not isinstance(royalties,int):
            raise TypeError("Royalties must be an integer")
        self.royalties=royalties

        author._contracts.append(self)
        book._contracts.append(self)
        Contract.all_contracts.append(self)



    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    
    


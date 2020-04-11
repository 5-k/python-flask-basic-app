from data import books_data

def getValidBook(input):
    newBook = {
        'name': input['name'],
        'price': input['price'],
        'purchased_date': input['purchased_date']
    }
    return newBook

def GetNewId():
    idList = []
    for book in books_data:
        idList.append(book['id'])
    idList.sort()
    return idList.pop() + 1
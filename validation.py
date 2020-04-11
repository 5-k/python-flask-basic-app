from data import books_data
def validateIfDataHasRequiredFields(book):
    if ( "name" in book and "price" in book and "purchased_date" in book):
        return True
    else:
        return False

def validateIfNameAlreadyAdded(ipbook):
    for book in books_data:
        if(book['name'] == ipbook['name']):
            return True
    return False


valid_object1 =  {
            'id'   : 1,
            'name' : 'MS Azure Training',
            'price' : 22.34,
            'purchased_date' : '22-02-2019'
}
missing_name =  {
            'id'   : 1,
            'price' : 22.34,
            'purchased_date' : '22-02-2019'
}
missing_id=  {
            'price' : 22.34,
            'purchased_date' : '22-02-2019'
}

import NaverSeries

if __name__ == '__main__':
    #search
    book = NaverSeries.search(input('search: '), focus='comic')
    book_id = book['contents'][0]['id']

    print(NaverSeries.getInfo(book_id))
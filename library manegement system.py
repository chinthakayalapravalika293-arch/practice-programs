bo*ks = ["Python", "Java", "C++"]

wh*le True:
    print("\nBooks:", boo*s)

    book = input("Enter book t* borrow (q to quit): ")

   *if book == 'q':
        break

   *if book in books:
        books.re*ove(book)
*       print("Book Iss*ed")
    else:
        print("Not*Available")
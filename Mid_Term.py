class Star_Cinema:
    def __init__(self):
        self.__hall_list = []

    def entry_hall(self,hall):
        self.__hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__rows = rows
        self.__cols=cols
        self.__hall_no = hall_no
        self.__show_list =[]


    def entry_show(self, id, movie_name, time):
        showDetails = (id, movie_name, time)
        self.__show_list.append(showDetails)

        self.__seats[id]=[['0']*self.__cols for i in range(self.__rows)]

    def view_show_list(self):
        print(f"\n\tHall No. {self.hall_no}")
        for i in self.__show_list:
            print(f"Show ID : {i[0]}, Show Name : {i[1]}, Show Time : {i[2]}")

    

    def view_available_seats(self, id):
        if id in self.__seats:
            for i,row in enumerate(self.__seats[id],start=1):
                for j,columnNo in enumerate(row,start=1):
                    if columnNo=='0':
                        print(f"Row {i}, Seat {j}")

        else:
            print("Incorrect Show ID")


    def book_seats(self,id,orderedSeat):
        for show in self.__show_list:
            if show[0]==id:
                for seat in orderedSeat:
                    row,col=seat
                    if row in self.__seats and col<=self.__cols:
                        if self.__seats[id][row-1][col-1]=='0':
                            self.__seats[id][row-1][col-1]='1'
                            print("Booking Complete")
                        else:
                            print("Already booked")
                    else:
                        print("Seat number is invalid")
                return
            

star_cinema = Star_Cinema()
h1=Hall(10,10,1)
h1.entry_show(id=1,movie_name="Dune",time="4:00 PM")
h1.entry_show(id=2,movie_name="12th Fail",time="7:00 PM")
star_cinema.entry_hall(h1)


run=True
currentCompny=star_cinema

while run:
    print("1. View All Show Today")
    print("2. View Available __seats")
    print("3. Book Ticket")
    print("4. Exit")

    option=int(input("ENTER OPTION: "))
    if option==1:
        for hall in star_cinema._Star_Cinema__hall_list:
            hall.view_show_list()

    elif option==2:
        h1.view_available_seats(id=1)

    elif option==3:
        booking=int(input(print("Enter Show ID: ")))
        quantity=int(input("Enter Number of seat: "))
        ordered_seats=[]
        for i in range(quantity):
            row_number=int(input(print("Enter Row Number: ")))
            col_number=int(input(print("Enter Column Number: ")))
            ordered_seats.append((row_number,col_number))
        h1.book_seats(booking,orderedSeat=ordered_seats)

    elif option==4:
        run=False
    else:
        print("Invalid Option. Please Enter a Valid Option")


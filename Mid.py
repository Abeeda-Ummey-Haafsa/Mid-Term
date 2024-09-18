class StarCinema:
    #hallList = []
    def __init__(self) -> None:
        self.hallList = []

    def entryHall(self, hall):
        self.hallList.append(hall)

class Hall(StarCinema):
    def __init__(self, rows, cols, hallNo) -> None:
        self.rows = rows
        self.cols = cols
        self.__hallNo = hallNo # Private Attribute
        self._seats={} # Protected Attribute
        self.showList = []

    def entryShow(self, id, movieName, time):
        shows = (id, movieName, time)
        self.showList.append(shows)
        self._seats[id]=[['0']*self.cols for i in range(self.rows)]

    def viewShowList(self):
        for shows in self.showList:
            print(f'Show ID: {shows[0]} || Movie Name: {shows[1]} || Time: {shows[2]}')

    def viewAvailableSeats(self, id):
        if id in self._seats:
            for i, row in enumerate(self._seats[id]):
                for j, columnNo in enumerate(row):
                    if columnNo == '0':
                        print(f"Seat ({i+1}, {j+1})")
                    else:
                        print(f"Seat ({i+1}, {j+1}) is booked") 

    def bookSeats(self, orderedShowID, orderedSeats):
        # for showID in self.showList:
        #     if showID[0] == orderedShowID:
        if orderedShowID in self._seats:
            for seat in orderedSeats:
                row, col = seat
                row -= 1
                col -= 1
                if 0 <=row<self.rows and 0<=col<self.cols:
                    if self._seats[orderedShowID][row][col] == '0':
                        self._seats[orderedShowID][row][col] = '1'
                        print(f"Booking for Seat ({row+1}, {col+1}) is Completed")
                    else:
                        print(f"Seat ({row+1}, {col+1}) is already booked")
                else:
                    print(f"Seat ({row+1}, {col+1}) is invalid")
        else:
            print("Incorrect Show ID")


cinePlex = StarCinema()
hall1 = Hall(5, 5, 1)
hall2 = Hall(5, 5, 2)
cinePlex.entryHall(hall1)
cinePlex.entryHall(hall2)


hall1.entryShow(101, 'DUNE', '17/09/24 18:00')
hall1.entryShow(102, 'DARK', '17/09/24 20:00')
hall2.entryShow(103, '1984', '17/09/24 22:00')
hall2.entryShow(104, '1920', '17/09/24 17:00')


print("\t\t\t\t\t\tWELCOME TO STAR CINEMA")
#run = True
while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    option=int(input("ENTER OPTION: "))
    if option == 1:
        for availableHall in cinePlex.hallList:
            availableHall.viewShowList()

    elif option == 2:
        i = int(input("ENTER SHOW ID: "))
        #print("AVAILABLE SEATS FOR SHOW ID: ",i)
        track = False
        #To get access of the viewAvailableSeats() method
        #1st -> go to the hallList using cinePlex
        #2nd -> check each hall if they have similar show ID in showList
        for availableHall in cinePlex.hallList:
            for availableShows in availableHall.showList:
                if availableShows[0] == i:
                    track = True
                    availableHall.viewAvailableSeats(i)
                    break
            #break
        if track is False:
            print("WRONG SHOW ID !!!")

    elif option==3:
        desiredShowID=int(input("Enter Show ID: "))
        desiredTicket=int(input("Enter Number of Ticket: "))
        desiredSeats=[]
        track = False
        for i in range(desiredTicket):
            rowNo=int(input("Enter Row Number: "))
            colNo=int(input("Enter Column Number: "))
            desiredSeats.append((rowNo,colNo))
        for availableHall in cinePlex.hallList:
            for availableShows in availableHall.showList:
                if availableShows[0] == desiredShowID:
                    track = True
                    availableHall.bookSeats(desiredShowID, desiredSeats)
                    break
            #break
        if track is False:
            print("WRONG SHOW ID !!!")

    elif option == 4:
        print("GOODBYE!!!")
        break
    
    else:
        print("INVALID OPTION !!!")
        print("PLEASE ENTER A VALID OPTION :D")


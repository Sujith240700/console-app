import pickle
import time
class booking():
    def __init__(self,choice):
        self.choice=choice
        if self.choice == 'a' or self.choice == 'A':
            booking.list_all()
        elif self.choice == 'b' or self.choice == 'B':
            booking.availability_city()
        elif self.choice == 'c' or self.choice == 'C':
            booking.availability_technology()
        elif self.choice == 'd' or self.choice == 'D':
            booking.Purchase_ticket()
        elif self.choice == 'e' or self.choice == 'E':
            booking.Cancel_ticket()
        elif self.choice == 'f' or self.choice == 'F':
            print(booking.manage_conferences())

    @staticmethod
    def ch():
        print("""\n\ta. list all the conferences available from all cities by default (we should be able to list based on the city as well when we specify the city)\n
                    b. Check for the availability of the conference tickets in a particular city\n
                    c. Check for the availability of the conference based on the technology/domain (java, devops, docker, aws, etc.,)\n
                    d. Purchase the conference ticket max 2 per transaction\n
                    e. Cancel the conference ticket any time before 24 hours of the conference date\n
                    f. Manage conferences (add conference, delete, update conference details)""")
        choice = input()
        booking(choice)

    @staticmethod
    def Purchase_ticket():
        print("Please enter details to Purchase_ticket")
        name=input("Enter name")
        mail_id=input("Enter mail id")
        phone=input("Enter Phone number")
        try:
            with open('conferences','rb') as fp:
                loader=pickle.load(fp)
                for i in loader:
                    print(i)        
        except:
            print("No event found")
            booking.ch()
        book_conference=input("Enter Conference Name")
        number_of_tickets=int(input("number_of_tickets"))
        if number_of_tickets > 2:
            print("enter <= 2")
            booking.Purchase_ticket()
        
        with open('conferences','rb') as fp:
            b_loader=pickle.load(fp)
        temp_ls_book=[]
        for i in b_loader:
            if i[0] == book_conference:
                if int(i[3]) >= number_of_tickets:
                    i[3] = i[3]-number_of_tickets
                    temp_ls_book.append(i)
                else:
                    print("NO Tickets Available")
            else:
                temp_ls_book.append(i)
        with open('conferences','wb') as fp1:
            pickle.dump(temp_ls_book,fp1)
        

        try:
            with open('booking','rb') as fp:
                booking_loader=pickle.load(fp)
            tmp_book=[]
            for l in booking_loader:
                tmp_book.append(l)
            temp_booking_ls=[]
            temp_booking_ls.append(book_conference)
            temp_booking_ls.append(name)
            temp_booking_ls.append(mail_id)
            temp_booking_ls.append(phone)
            temp_booking_ls.append(list(time.localtime()))
            tmp_book.append(temp_booking_ls)

            with open('booking','wb') as fp1:
                pickle.dump(tmp_book,fp1)
        except Exception as e:
            print(e)
            temp_booking_ls,booking_loader,tmp_final=[],[],[]
            temp_booking_ls.append(book_conference)
            temp_booking_ls.append(name)
            temp_booking_ls.append(mail_id)
            temp_booking_ls.append(phone)
            temp_booking_ls.append(list(time.localtime()))
            booking_loader.append(temp_booking_ls)
            tmp_final.append(booking_loader)
            print("new",booking_loader)
            with open('booking','wb') as fp1:
                pickle.dump(tmp_final,fp1)
        
        
        finally:
            print("ticked booked")
            booking.ch()
        
    @staticmethod
    def Cancel_ticket():
        """tm_year=2021, tm_mon=1, tm_mday=17, tm_hour=9, tm_min=35, tm_sec=41, tm_wday=6, tm_yday=17, tm_isdst=0"""
        mail=input("Enter mail id")
        ph=input("Enter phone number")
        try:
            with open('booking','rb') as fp:
                booking_loader=pickle.load(fp)
            for k in booking_loader:
                print(k)
            time1=list(time.localtime())
            tmp_booked=[]
            for i in booking_loader:
                
                if i[2] == mail and i[3] == ph:
                    if i[-1][0] ==  time1[0]:
                        if i[-1][1] == time1[1]:
                            if abs(i[-1][2] - time1[2]) <= 1:
                                print("ticket cancelled")
                            else:
                                print("ticket not cancelled")
                        else:
                            print("ticket not cancelled")
                    else:
                        print("ticket not cancelled")
                else:
                    tmp_booked.append(i)
            else:
                print("Mail id or Phone number incorrect")
        except:
            print("No ticket booked")
        finally:
            with open('booking','wb') as fp1:
                pickle.dump(tmp_booked,fp1)
            booking.ch()
            


    @staticmethod
    def list_all():
        try:
            with open('conferences','rb') as fp:
                loader=pickle.load(fp)
                for i in loader:
                    print(i)
                return loader
        
        except:
            print("No event found")
            return "NULL"
        
        finally:
            booking.ch()
    
    @staticmethod
    def availability_technology():
        technology=input("Enter technology")
        print("---conference  technology seats date---")
        """[Data Scientist conference','20.20.2021','Python','50','cbe']"""
        try:
            with open('conferences','rb') as fp:
                loader=pickle.load(fp)
                for i in loader:
                    if i[-3] == technology:
                        print(i[0],i[-3],i[-2],i[1])
        except:
            print("No event found")
    
        finally:
            booking.ch()

    @staticmethod
    def availability_city():
        city=input("Enter city")
        print("---conference  seats  city date---")
        try:
            with open('conferences','rb') as fp:
                loader=pickle.load(fp)
                for i in loader:
                    if i[-1] == city:
                        print(i[0],i[-2],i[-1],i[1])
        
        except:
            print("No event found")
            return "NULL"
        
        finally:
            booking.ch()

    @staticmethod
    def manage_conferences():
        print("1.add conference \n 2.delete conference \n 3.update conference details \n 0 for back")
        number=int(input("Enter number"))
        if number == 0:
            booking.ch()
        if number == 1:
            print("Add conference")
            """[Data Scientist conference','20.20.2021','Python','50','cbe']"""
            try:
                with open('conferences','rb') as fp:
                    loader=pickle.load(fp)
                add_event=[]
                add_event.append(input("Conference name"))
                add_event.append(input("Conference Date"))
                add_event.append(input("Conference technology"))
                add_event.append(int(input("Conference seats")))
                add_event.append(input("Conference city"))
                loader.append(add_event)
                with open('conferences','wb') as fp1:
                    pickle.dump(loader,fp1)
            except:
                add_event=[]
                add_event.append(input("Conference name"))
                add_event.append(input("Conference Date"))
                add_event.append(input("Conference technology"))
                add_event.append(int(input("Conference seats")))
                add_event.append(input("Conference city"))
                templs=[]
                templs.append(add_event)
                with open('conferences','wb') as fp1:
                    pickle.dump(templs,fp1)
            finally:
                booking.manage_conferences()
        elif number == 2:
            print("Delete conferences")
            try:
                with open('conferences','rb') as fp:
                    loader=pickle.load(fp)
                for i in loader:
                    print(i)
                name=input("Enter conference name")
                templs=[]
                for i in loader:
                    if i[0] != name:
                        templs.append(i)
                with open('conferences','wb') as fp1:
                    pickle.dump(templs,fp1)
                    
            except:
                print("no data found")
            finally:
                booking.manage_conferences()
                
        elif number == 3:
            """[Data Scientist conference','20.20.2021','Python','50']"""
            print("update conferences")
            try:
                with open('conferences','rb') as fp:
                    loader=pickle.load(fp)
                print("1.conference name\n2. date,\n3. technology\n4.seats,\n5.city")
                num=int(input("Enter num"))
                if num == 1:
                    prev_c_name=input("Enter previous conference name")
                    new_name=input("Enter New conference name")
                    temp_ls=[]
                    for i in loader:
                        if i[0] != prev_c_name:
                            temp_ls.append(i)
                        else:
                            i[0] = new_name
                            temp_ls.append(i)
                    with open('conferences','wb') as fp1:
                        pickle.dump(temp_ls,fp1)
                elif num == 2:
                    prev_c_name=input("Enter conference name")
                    new_date=input("Enter New conference date")
                    temp_ls=[]
                    for i in loader:
                        if i[0] != prev_c_name:
                            temp_ls.append(i)
                        else:
                            i[1] = new_date
                            temp_ls.append(i)
                    with open('conferences','wb') as fp1:
                        pickle.dump(temp_ls,fp1)
                elif num == 3:
                    prev_c_name=input("Enter conference name")
                    new_Technology=input("Enter New Technology")
                    temp_ls=[]
                    for i in loader:
                        if i[0] != prev_c_name:
                            temp_ls.append(i)
                        else:
                            i[2] = new_Technology
                            temp_ls.append(i)
                    with open('conferences','wb') as fp1:
                        pickle.dump(temp_ls,fp1)
                elif num == 4:
                    prev_c_name=input("Enter conference name")
                    new_seats=int(input("Enter seats"))
                    temp_ls=[]
                    for i in loader:
                        if i[0] != prev_c_name:
                            temp_ls.append(i)
                        else:
                            i[3] = new_seats
                            temp_ls.append(i)
                    with open('conferences','wb') as fp1:
                        pickle.dump(temp_ls,fp1)
                elif num == 5:
                    prev_c_name=input("Enter conference name")
                    new_city=input("Enter new city name")
                    temp_ls=[]
                    for i in loader:
                        if i[0] != prev_c_name:
                            temp_ls.append(i)
                        else:
                            i[-1] = new_city
                            temp_ls.append(i)
                    with open('conferences','wb') as fp1:
                        pickle.dump(temp_ls,fp1)
            except:
                print("no data found")
            finally:
                booking.manage_conferences()
booking.ch()
from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None, all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, address2=None, phone2=None, bday=None, bmonth=None, byear=None,
                 title=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.all_phones_from_home_page = all_phones_from_home_page
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address2 = address2
        self.phone2 = phone2
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.title = title
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

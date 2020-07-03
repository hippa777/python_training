from model.contact import Contact
import random
import string
import os.path
import json
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone():
    symbols = string.digits
    first = random.randint(1, 9)
    return str(first) + ''.join([random.choice(symbols) * 8])


def random_email():
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(3, 7, 1))]) + "@" + "".join(
        [random.choice(symbols) for i in range(random.randrange(3, 7, 1))]) + "." + "".join(
        [random.choice(symbols) for i in range(random.randrange(3, 7, 1))])


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 15),
            lastname=random_string("lastname", 15), nickname=random_string("nickname", 10),
            company=random_string("company", 20), address=random_string("address", 20),
            home=random_phone(),
            mobile=random_phone(), work=random_phone(), fax=random_phone(), email=random_email(),
            email2=random_email(), email3=random_email(),
            address2=random_string("address2", 15)) for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

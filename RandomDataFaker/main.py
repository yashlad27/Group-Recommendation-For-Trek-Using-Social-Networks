from faker import Faker
import random
import pandas as pd
from random import randrange
from datetime import datetime


nr_of_trekkers = 10000
# time-stamp
# email, name, height, weight, age, gender, city, locality
# languages, college
# working profession, have you gone trekking
# preference of trek days
# no. of previous treks
# list of treks done
# difficulty of trek
# preferred location of trek
# food preferences

fake = Faker('de_DE')

trekkers = []

for customers_id in range(nr_of_trekkers):
    # creating time-stamp:
    d1 = datetime.strptime(f'1/1/2021', '%m/%d/%Y')
    d2 = datetime.strptime(f'12/31/2022', '%m/%d/%Y')
    transaction_date = fake.date_between(d1, d2)
    # create email:
    email = fake.ascii_email()
    # create trekkers name:
    name = fake.name()
    # create height:
    height = fake.random_int(160, 199)
    # create weight:
    weight = fake.random_int(50, 110)
    # create age:
    age = fake.random_int(0, 100)
    # create gender:
    gender = random.choice(["M", "F", "None"])
    # create city:
    city = random.choice(["Pune", "Mumbai", "Nashik", "Kolhapur", "Nagpur"])
    # create locality:
    locality = random.choice(["Sky-One", "Krishna Kamal", "Midori Towers", "24K-KPS", "Krishna Park", "Evergreen Society"])
    # create languages:
    languages = random.choice(["English", "Marathi", "Hindi", "Gujarati", "Urdu"])
    # create college:
    college = random.choice(["MIT-WPU", "SPPU", "MIT-ADT", "PCCOE", "PICT", "VIT"])
    # create profession:
    profession = random.choice(["accountant","actor","air traffic controller","architect","artist","attorney","banker",
                                    "bartender","barber","bookkeeper","builder","businessman","businessperson","butcher","carpenter",
                              "cashier","chef","coach","dental hygienist","dentist","designer","developer","dietician","doctor","economist","editor",
                              "electrician","engineer","farmer","fisherman","flight attendant","jeweler","judge","lawyer","mechanic",
                              "musician","nutritionist","nurse","optician","painter","pharmacist","photographer","physician","pilot",
                              "plumber","policeofficer",  "politician","professor","programmer","psychologist","receptionist","salesman",
                              "salesperson","secretary","singer","surgeon""teacher","therapist","translator","translator","undertaker",
                              "veterinarian","videographer","waiter","writer","Professors","Teachers","Actors","Clergy","Musicians",
                              "Philosophers","Visual Artists","Writers","Audiologists","Chiropractors","Dentists","Dietitians","Doctors",
                              "Medical Laboratory Scientists","Midwives","Nurses","Occupationaltherapists","Optometrists","Pathologists",
                              "Pharmacists","Physicaltherapists","Physicians","Psychologists","Speechlanguagepathologists","Accountants",
                              "Actuaries","Agriculturists","Architects","Economists","Engineers","Interpreters","Attorney","Advocates",
                              "Solicitors","Librarians","Statisticians","Surveyors","Urbanplanners","Humanresources","Firefighters","Judges",
                              "Militaryofficers","Policeofficers","Airtrafficcontrollers","Aircraftpilots","Seacaptains","Scientists",
                              "Astronomers","Biologists","Botanists","Ecologists","Geneticists","Immunologists","Pharmacologists","Virologists",
                              "Zoologists","Chemists","Geologists","Meteorologists","Oceanographers","Physicists","Programmers","Webdevelopers",
                              "Designers","Graphicdesigners","Webdesigners","Physicians","surgeons","Dentists","Veterinarians","Pharmacists",
                              "Chiropractors","Osteopaths","Optometrists","Opticians","RegisteredNurses","Licensedpracticalnurses","Dieticians",
                              "Physicaltherapists","Occupationaltherapists","Dentalhygienists","Clinicallabtechnicians","EMTspecialist","Speechpathologists",
                              "Physicianassistants","Paramedics"])
    # create YES/NO:
    gone_trekking = random.choice(["Y", "N"])
    # create preference of trek days:
    preferred_days = random.choice(["Friday", "Saturday", "Sunday", "Monday"])
    # create no. of treks done:
    num_treks = fake.random_int(0, 20)
    # list of treks done:
   # prev_treks = random.choice()
    # difficulty of treks:
    difficulty_trek = random.choice(["Beginner", "Intermediate", "Experienced"])
    # preferred location of treks:

    # food choice:
    food_choice = random.choice(["Non-Veg", "Veg", "Vegan"])

    trekkers.append([email, name, height, weight, age, gender, city, locality, languages, college, profession,
                     gone_trekking, preferred_days, num_treks, difficulty_trek])

trekkers_df = pd.DataFrame(trekkers, columns=['Email-ID', 'Name', 'Height', 'Weight', 'Age', 'Gender', 'City', 'Locality',
                                               'Languages', 'college', 'Profession', 'Have you gone Trekking', 'Preferred Days',
                                               'Number of Treks', 'Difficulty of Trek'])

pd.pandas.set_option('display.max_columns', None)
print(trekkers_df)
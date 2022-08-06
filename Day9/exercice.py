student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"   

#print(student_grades)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def Add_new_country(country_visited, cities_visited, times):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

Add_new_country(country_visited="Russia", times=2, cities_visited=["Moscow", "Saint Petersburg"])

#print(travel_log)

blind_auction = {}

exit = False
winner = ""
highest_bid = 0

while not exit:
    name = input("What is your name ? - ")
    bid = int(input("How bid you want : $"))

    blind_auction[name] = bid

    another_user = input("Another user : 'yes' or 'no' - ")
    print(blind_auction)

    if another_user != 'yes':
        exit = True

        for bid in blind_auction:
            if blind_auction[bid] > highest_bid:
                highest_bid = blind_auction[bid]
                winner = bid
        
        print(winner)
#importing csv file and making variables to store information in, such as auhtors and favorite movie
import csv
with open('/home/pi/VE/userreviews.csv', 'r', encoding= 'utf-8-sig') as userreviews:
    csv_reader = csv.reader(userreviews, delimiter=';')
    
    next(csv_reader, None)
    score = []
    authors = []
    score_kaoutar = 8.5
    favorite_movie = 'tangled'
    count = 0
    avg = 0
    sum = 0
    
    
    for i in csv_reader:
        if (i[0]) == favorite_movie:
            sum+=float(i[1])
            count = count+1
            author=i[2]
            authors.append(i[2])
            print(author)
            print('the reviewer gave this movie a: ' + (i[1]))
            print('the sum is: ' + str(sum))
            print('the count is: ' + str(count))

#computing the list of reviewers/authors wo have reviewed Tangled
print('The full list of authors who have seen and reviewed: ' + favorite_movie + ' is: ')
print(authors)

#computing the average score for Tangled compared to my own score for Tangled            
avg = sum/count
print('The average score of ' + favorite_movie + ' is: ' + str(avg))
print('Tangled was rated, compared to the score of Kaoutar: ' + str(avg-score_kaoutar))

with open('userreviews.csv', 'r', encoding= 'utf-8-sig') as userreviews:
    List1 = []
    List2= []
    csv_reader = csv.reader(userreviews, delimiter=';')
    for i in csv_reader:
        if (i[2]) in authors and float(i[1]) > float(avg):
            List1.extend([i[0],i[1],i[2]])
            List2.extend([List2])
            print(List1)
            List1 = []
            
            print('Reviewer: ' + i[2] + 'Score: ' + str(i[1]) + 'favorite_movie: ' + str(i[0]))
#creating csv file with the fields Movie, Userscore and Reviewer
fields = [['Movie', 'Userscore', 'Reviewer']]
file = open('moviesKaoutar.csv', 'w+', newline = '')
with file:
    write = csv.writer(file)
    write.writerows(fields)
    write.writerows(List2)
import csv

with open("movies.csv",encoding = 'utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster link")

with open("final.csv","a+",encoding = 'utf-8') as i:
    writer = csv.writer(i)
    writer.writerow(headers)

with open("posters.csv",encoding = 'utf-8') as j:
    reader1 = csv.reader(j)
    data1 = list(reader1)
    all_posters = data1[1:]

for k in all_movies:
    poster = any(k[8] in i for i in all_posters)
    if poster:
        for i in all_posters:
            if k[8]==i[0]:
                k.append(i[1])
                if len(k)==28:
                    with open("final.csv","a+",encoding = 'utf-8') as i:
                        writer = csv.writer(i)
                        writer.writerow(k)
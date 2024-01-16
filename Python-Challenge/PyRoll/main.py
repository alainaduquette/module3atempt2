import csv

with open("C:\\Users\\alain\\Documents\\Bootcamp\\Python Challenge\\Python-Challenge\\PyRoll\\Resources\\election_data.csv", "r") as file:
    header=file.readline() 
    my_reader = csv.reader(file, delimiter=",")
    candidate_dictionary = {}
    
    ballot_id = []

    for row in my_reader:
        candidate_name = row[2]
        if candidate_name not in candidate_dictionary.keys():
            candidate_dictionary[candidate_name] = 0
         
        candidate_dictionary[candidate_name] = candidate_dictionary[candidate_name] +1 
        ballot_id.append({'county':row[1], 'candidate':row[2]})
        
count = len(ballot_id)

total_percent = []

for votes_cast in candidate_dictionary.values():
    total_percent.append(round(((votes_cast / count)*100), 3))
#
total_percent_index=0

print("Election Resuluts")
print("------------------------------------------------")
print("Total Votes: " + str(count))
print("------------------------------------------------")
for candidate_name, votes_cast in candidate_dictionary.items():
   

    print(candidate_name +": " + str(total_percent[total_percent_index]) + "% " +"("+ str(votes_cast) +")")
    # print(f"{candidate_name}: 0% ({votes_cast})")
    total_percent_index=total_percent_index+1

print("------------------------------------------------")

print("Winner: " + max(candidate_dictionary, key=candidate_dictionary.get), max(candidate_dictionary.values()))
print("------------------------------------------------")

# Open a file in write mode ('w')
with open('C:\\Users\\alain\\Documents\\Bootcamp\\Python Challenge\\Python-Challenge\\PyRoll\\analysis\elecction_results.txt', 'w') as file:
    # Redirect the standard output to the file
    print("Election Resuluts", file=file)
    print("------------------------------------------------", file=file)
    print("Total Votes: " + str(count), file=file)
    print("------------------------------------------------", file=file)
    ##print(candidate_name +": " + str(total_percent[total_percent_index]) + "% " +"("+ str(votes_cast) +")", file=file)
    print("------------------------------------------------", file=file)
    print("Winner: " + max(candidate_dictionary, key=candidate_dictionary.get), max(candidate_dictionary.values()), file=file)
 
   







    





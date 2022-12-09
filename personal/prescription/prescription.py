data = """name: first1 first2 first3 m.i. last1 last2
age: 0 < x < 118
address: [(number street) or (blk# lot#)] (subd) brgy city province

drug deliverable[drug...] amt#
sig: instruction/code

esig
name + 'm.d.'
licenseno."""

data_dict = {
    "name": "name: first1 first2 first3 m.i. last1 last2",
    "age": "str(int age)",
    "address": "[(number street) or (blk# lot#)] (subd) brgy city province",
    "prescription": "drug deliverable[drug...] amt#",
    "instructions": "instruction/code",
    "e-sig": "png",
    "md_name": "name + md",
    "license_number": "str(license_number)"
}

print("Raw Data:", '\n')
print(data, '\n\n')

print("Formatted Data:", '\n')
for key in data_dict:
    print(f"{key}: {data_dict[key]}")


# run request for prescription in mssgr
# convo loop: send "name: " -> type name -> next... 
    # store in dict 
# per sent message from user -> compile in database as one string
# send total receipt to confirm
# ask if any changes
    # if yes -> send list of fields to change
        # they type field -> prompt input
    # resend receipt
    # if no, download dictionary

# get data(dict) from mssgr
# place in file
# read data from file
# print accordingly

# split data


# name
# age
# address
# drug-deliverable-amt
# sig
# esig
# name + md
# license no.
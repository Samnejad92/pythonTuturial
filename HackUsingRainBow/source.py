import hashlib
import csv
def hash_password(password):
    # Encode the password as bytes
    password_bytes = password.encode('utf-8')    
    # Use SHA-256 hash function to create a hash object
    hash_object = hashlib.sha256(password_bytes)    
    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()    
    return password_hash

def hash_password_hack(input_file_name, output_file_name):
    d=dict()
    c=dict()
    for i in range(1000,10000):
        d[hash_password(str(i))]=i
    with open(input_file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] in d.keys():
                print(row[0], d[row[1]])
                c[row[0]]= d[row[1]]
    with open(output_file_name, 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in c.items():
            writer.writerow([key, value])
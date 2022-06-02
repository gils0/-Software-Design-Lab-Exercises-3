# Function to display hashtable
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()

HashTable = [[] for _ in range(10)]


# Hashing Function to return
# key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


# Driver Code
insert(HashTable, 10, 'ED')
insert(HashTable, 25, 'Gills')
insert(HashTable, 20, 'Mara')
insert(HashTable, 9, 'Jay')
insert(HashTable, 21, 'Vonn')
insert(HashTable, 21, 'Noime')

display_hash(HashTable)








# Hash functions are one way and deterministic
class HashTable:
    def __init__(self, size=7):       # Recommended to work with prime numbers
        self.data_map = [None] * size     # Creates a list with 7 empty items

    # __ before method means it doesn't get called directly, only by other methods in the class
    def __hash(self, key):          # Mathematical function for hashing
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ': ', val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map[index])):
                # Gets the key [0] in the i list [i] in the box [index]
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]       # Return the value
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] != None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())

# my_hash_table.print_table()
# print(my_hash_table.get_item('bolts'))


# CHECK IF LISTS HAVE ITEMS IN COMMON

# Naive approach
def item_in_common_naive(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True       # Takes every value and puts it in the dictionary
    for j in list2:
        if j in my_dict:        # If j exists in the dictionary (list1)
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 7]
print(item_in_common(list1, list2))

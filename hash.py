class HashTable:
    def __init__(self):
        self.size = 32
        self.table = [[] for _ in range(self.size)]

    def hash_function1(self, key):
        return sum(ord(c) for c in key) % self.size

    def hash_function2(self, key):
        return ((1731 * sum(ord(c) for c in key) + 520123) % 524287) % self.size

    def hash_function3(self, key):
        return hash(key) % self.size

    def insert(self, key, hash_function):
        index = hash_function(key)
        self.table[index].insert(0, key)

    def delete(self, key, hash_function):
        index = hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def display(self):
        for i in range(self.size):
            print(f"Slot {i}: {self.table[i]}")

    def process_commands(self, hash_function, commands):
        for command in commands.split('\n'):
            if command.startswith('del '):
                key_to_delete = command[4:]
                self.delete(key_to_delete, hash_function)
            else:
                key_to_insert = command
                self.insert(key_to_insert, hash_function)

    def display_hash_table(self):
        hash_table_display = {}
        for i in range(self.size):
            hash_table_display[i] = self.table[i]
        return hash_table_display
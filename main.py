import json 
import os




class FoobarDB(object):
        def __init__(self, location):
                self.location = os.path.expanduser(location)
                self.load(self.location)

        def load(self, location):
                if os.path.exists(location):
                        self._load()
                else:        
                        self.db = {}
                return True

        def _load(self):
                self.db = json.load(open(self.location, 'r'))
        
        def dumpdb(self):
                try:
                        json.dump(self.db, open(self.location, "w+"))
                        return True
                except:
                        return False

        def set(self, key, value):
                try:
                        self.db[str(key)] = value
                        self.dumpdb()
                        return True
                except Exception as e:
                        print("[X] Erro saveing value to database" + str(e)) 
                        return False
        
        def get(self, key):
                try:
                        return self.db[key]
                except KeyError:
                        print("No value can be found for " + str(key))
                        return False
        
        def delete(self, key):
                if not key in self.db:
                        return False
                del elf.db[key]
                self.dumpdb()
                return True
        
        def resetdb(self):
                self.db = {}
                self.dumpdb()
                return True

def main():
        toy_db = FoobarDB('/root/toy_database/toydb')
        toy_db.set("ddmmyy", "10/03/1997")
        print(toy_db.get("ddmmyy"))

if __name__ == '__main__':
        main()

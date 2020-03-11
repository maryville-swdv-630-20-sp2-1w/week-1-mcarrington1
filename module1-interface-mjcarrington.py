class Teams:
    def __init__(self, members):
        self.__myTeam = members
        self.count = 0

    def __len__(self):
        return len(self.__myTeam)
    
    def __contains__(self, item):
        return item in self.__myTeam
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.__myTeam) > self.count:
            self.count += 1
            return self.__myTeam[self.count - 1]
        else:
            raise StopIteration
        
def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print (len(classmates))
    
    #1
    print('Is Tim a classmate? {}'.format(classmates.__contains__('Tim')))
    print('Is Sam a classmate? {}'.format(classmates.__contains__('Sam')))
    
    #2
    for classmate in classmates:
        print(classmate) 
    
main()

#3 Yes, we're using len in our implementation of __len__
#4 an interface describes how a user interacts with a class, whereas the implementation is the actual inner workings on the class, which is called by the interface.
#5 Refer to separate word file.
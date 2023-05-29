class bio:

    def __init__(self,name):
        self.name = name


    def bio_data(self):
        list1 = []
        list1.append(self.name)
        return list1

b1 = bio("Jai")
result = b1.bio_data()
print(result)

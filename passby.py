class Cat(object):

    @classmethod
    def __filter(cls, data):
        data["price"] = 4



    def call_filter(self, fields):
        Cat.__filter(fields)
        print str(fields)



cat = Cat()
cat.call_filter({"price" : "44"})




class Error(object):
    def __init__(self, key, msg):
        self.key = key
        self.msg = msg
        self.owner = None

    # keep track of the owner class, e.g. APIError.BAD_AUTH
    def __get__(self, instance, owner):
        self.owner = owner
        return self

    def __call__(self, info=None):
        return self.owner(self, info)

    # for easier comparison with API error strings
    def __eq__(self, other):
        if isinstance(other, basestring):
            return self.key == other
        elif isinstance(other, Error):
            return self is other
        elif isinstance(other, TurntableError):
            return self == other.error
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result == NotImplemented:
            return NotImplemented
        return not result

    def __str__(self):
        return '<%s.%s>' % (self.owner, self.key)


class TurntableError(Exception):
    def __init__(self, error, info):
        Exception.__init__(self, error)

        self.error = error
        msg = error.msg
        if info:
            msg += ': ' + str(info)
        self.err = {'error': error.key, 'errmsg': msg}

    INVALID_DOG = Error('INVALID_DOG', "This dog is invalid")
    INVALID_CAT = Error('INVALID_CAT', "This cat is invalid")

class Animal(object):
    @classmethod
    def speak(cls):
        print "Generic sound"

    @classmethod
    def sit_or_raise_error(cls,command):
        if command != "sit":
            raise getattr(TurntableError, "INVALID_%s" % cls.__name__.upper())()


class Dog(Animal):
    @classmethod
    def speak(cls):
        print "woof"

class Cat(Animal):
    @classmethod
    def speak(cls):
        print "miaow"


Dog.speak()
Cat.speak()
Dog.sit_or_raise_error("sit")

try:
    Cat.sit_or_raise_error("scat")
except TurntableError as e:
    if  e.err['error'] == TurntableError.INVALID_CAT:
        print "An invalid cat error was raised!"


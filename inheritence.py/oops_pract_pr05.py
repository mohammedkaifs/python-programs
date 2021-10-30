class vector:
    def __init__(self,vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 + = f"{i}a{index} +"
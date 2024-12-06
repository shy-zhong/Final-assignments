# This Python file uses the following encoding: utf-8

class Check:
    def __init__(self):
        pass
    def checkOption(answer,result):
        if len(answer) == len(result):
            for i in range(len(answer)):
                if answer[i] != result[i]:
                    print("error")
                    return False
            print("right")
            return True
        print("error")
        return False


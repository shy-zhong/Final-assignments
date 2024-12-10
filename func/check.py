# This Python file uses the following encoding: utf-8

class Check:

    @staticmethod
    def checkOption(answer,result):
        print((result))
        if len(answer) == len(result):
            print(1)
            for i in range(len(answer)):
                print(2)
                if answer[i] != result[i]:
                    print("error")
                    return False
            print("right")
            return True
        print("error")
        return False


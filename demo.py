import random as r

def otpgen():
    otp=""
    for i in range(8):
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is ")
    print (otp)
otpgen()

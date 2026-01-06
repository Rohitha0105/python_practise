method="creditcard"
card="hdfc"
options=("upi", "cash", "creditcard")
if method in options:
       print("allowed")
       if method=="creditcard":
            print("discount")
            if card=="hdfc":
                print("5%")
            elif card=="sbi":
                print("10%")
            else:
                print("2%")
else:
     print("not allowed")

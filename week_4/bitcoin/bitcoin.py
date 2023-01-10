# import needed modules
import requests
import sys
import json

# check length if not equal to 2
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
else:
    # get webpage
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        # assign first argument to val
        val = float(sys.argv[1])
    # if catch ValueError
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    # raise an exception
    info = r.json()
    # assign bpi to bpi
    bpi = info["bpi"]
    # assign usd to usdt
    usdt = bpi["USD"]
    # assign rate to amount
    amount = usdt["rate"]
    # repalce comma with none
    amount = amount.replace(",", "")
    # multiply amount to sys.argv[1]
    amount = float(amount) * val
    # print amount with 4 decimal
    print(f"${amount:,.4f}")
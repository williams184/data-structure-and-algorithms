def check_cash_register(price, cash, cid):
    currencies = [
        {"name": "ONE HUNDRED", "amount": 100},
        {"name": "TWENTY", "amount": 20},
        {"name": "TEN", "amount": 10},
        {"name": "FIVE", "amount": 5},
        {"name": "ONE", "amount": 1},
        {"name": "QUARTER", "amount": 0.25},
        {"name": "DIME", "amount": 0.10},
        {"name": "NICKEL", "amount": 0.05},
        {"name": "PENNY", "amount": 0.01},
    ]
    output = {"status": None, "change": []}
    change_needed = cash - price
    change_given = 0
    cid_total = sum(currency[1] for currency in cid)

    if cid_total > change_needed:
        output["status"] = "OPEN"
        cid.reverse()

        for index, currency in enumerate(currencies):
            change_given = 0

            while cid[index][1] > 0 and change_needed >= currency["amount"]:
                change_needed -= currency["amount"]
                cid[index][1] -= currency["amount"]
                change_given += currency["amount"]
                change_needed = round(change_needed * 100) / 100

            if change_given > 0:
                output["change"].append([currency["name"], change_given])

        if change_needed > 0:
            output["status"] = "INSUFFICIENT_FUNDS"
            output["change"] = []
    else:
        if cid_total < change_needed:
            output["status"] = "INSUFFICIENT_FUNDS"
        else:
            output["status"] = "CLOSED"
            output["change"] = cid

    return output

result = check_cash_register(19.5, 20, [
    ["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25],
    ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]
])

print(result)


# Obligasi Patriot

#Given (F = Face Value, C = Coupon yield, r/ y = yield, t = period, n = sum of period)

import pandas as pd


def PatBond(F, coupon_rate, r, t):

    data_tabel = []

    SigmPV = 0
    C = F * coupon_rate

    for i in range(1, t + 1):

        CoumpPV = C / ((1 + r)** i)
        SigmPV += CoumpPV

        data_tabel.append({
            "Year": i,
            "Coupon": C,
            "PV Coupon": CoumpPV
        })

    PV_F = F / ((1 + r) ** t)
    data_tabel.append({
        "Year": "Face Value Repayment",
        "Coupon": F,
        "PV Coupon": PV_F
    })

    df = pd.DataFrame(data_tabel)

    PV = SigmPV + F / ((1 + r)** t)

    return df, PV


F = 100000000000
coupon_rate = 0.02
r = 0.065
t = 5
C = F * coupon_rate

tabel_bond, PV = PatBond(
    100000000000, 
    0.02, 
    0.065, 
    5)


if PV > F:
    status = "Premium Bond"
elif PV < F:
    status = "Discount Bond"
else:
    status = "Par Bond"

#mama i'm a terminal
print("=" * 80)
print("           PATRIOT BOND VALUATION")
print("=" * 80)
print()

print(tabel_bond.to_string(
    index=False,
    formatters={
        "Coupon": "Rp {:,.2f}".format,
        "PV Coupon": "Rp {:,.2f}".format
    }
))

print("-" * 80)

print(f"Face Value (F)           : Rp {F:,.2f}")
print(f"Coupon Rate (c)          : {coupon_rate:.2%}")
print(f"Coupon Payment (C)       : Rp {C:,.2f}")
print(f"Yield to Maturity (y)    : {r:.2%}")
print(f"Maturity (n)             : {t} Years")

print("-" * 80)

print(f"Bond Price (P)           : Rp {PV:,.2f}")
print(f"Bond Classification      : {status}")

print("=" * 80)
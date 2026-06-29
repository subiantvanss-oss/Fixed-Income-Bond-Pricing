# FIxed Income Bond Pricing

A Python implementation of **Time Value of Money (TVM)** and **Coupon Bond Pricing** for fixed-income valuation using the Discounted Cash Flow (DCF) approach.

This project demonstrates how mathematical finance concepts can be translated into Python by calculating the fair value of a coupon bond based on its future cash flows. As an educational case study, the implementation uses publicly available parameters inspired by the Patriot Bond.

---

## Mathematical Background

The price of a coupon bond is calculated as the present value of all future coupon payments and the principal repayment at maturity.

## Mathematical Model

$$
P=\sum_{t=1}^{n}\frac{C}{(1+y)^t}+\frac{F}{(1+y)^n}
$$

Where:

| Symbol | Description             |
| ------ | ----------------------- |
| **P**  | Bond Price              |
| **F**  | Face Value              |
| **C**  | Coupon Payment          |
| **y**  | Yield to Maturity (YTM) |
| **n**  | Number of Periods       |

---

## Features

* Implementation of Time Value of Money (TVM)
* Coupon Bond Pricing
* Present Value calculation for each coupon payment
* Principal repayment valuation
* Bond classification:

  * Premium Bond
  * Par Bond
  * Discount Bond
* Cash flow table using Pandas DataFrame

---

## Technologies

* Python 3
* Pandas

---

## Example Output

The program displays:

* Discounted coupon cash flows
* Present value of the principal repayment
* Bond price
* Bond classification
* Investment parameters

Example:

```text
============================================================
                 PATRIOT BOND PRICING ANALYSIS
============================================================

Year    Coupon Payment        Present Value
1       ...
2       ...
3       ...
...
------------------------------------------------------------

Face Value (F)
Coupon Rate (c)
Coupon Payment (C)
Yield to Maturity (y)
Maturity (n)

Bond Price (P)
Bond Classification
```

---

## Project Structure

```text
bond-pricing-analyzer/
│
├── main.py
├── README.md
├── requirements.txt
└── images/
```

---

## Learning Objectives

This project was developed to strengthen understanding of:

* Time Value of Money (TVM)
* Discounted Cash Flow (DCF)
* Coupon Bond Pricing
* Fixed Income Valuation
* Financial Modeling with Python

---

## Disclaimer

This project is intended for educational purposes only. The implementation demonstrates bond pricing concepts based on standard financial theory and should not be considered financial or investment advice.

# FIxed Income Bond Pricing


![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A quantitative finance project implementing **Time Value of Money (TVM)** and **Coupon Bond Pricing** using Python. This repository demonstrates how mathematical finance concepts are translated into practical code through the valuation of fixed-income securities.

---

# Table of Contents

* Overview
* Time Value of Money
* From Future Value to Present Value
* Continuous Compounding
* Coupon Bond Pricing
* Project Overview
* Features
* Mathematical Model
* Installation
* Usage
* Example Output
* Future Improvements
* Disclaimer

---

# Overview

Fixed-income securities, such as government and corporate bonds, derive their value from future cash flows. Since money has a time value, future payments must be discounted to determine their present value.

This repository implements the mathematical framework behind bond pricing using Python and demonstrates the complete valuation process for a coupon-paying bond.

---

# Time Value of Money (TVM)

The Time Value of Money states that **one unit of currency today is worth more than the same amount received in the future** because today's money can be invested to earn returns.

## Future Value

If an investment grows at an annual interest rate (r),

$
FV = PV(1+r)^n
$

where

* **FV** : Future Value
* **PV** : Present Value
* **r** : Interest Rate
* **n** : Number of Periods

This equation describes how money compounds over discrete time periods.

---

## Present Value

Rearranging the previous equation,

$$ PV=\frac{FV}{(1+r)^n} $$

This equation discounts future cash flows back to today's value.

Every valuation model in fixed income is fundamentally based on this relationship.

---

# Continuous Compounding

In financial markets, especially quantitative finance, interest is often modeled as compounding continuously.

Starting from,

$$ FV = PV\left(1+\frac{r}{m}\right)^{mt} $$

Taking the limit as,

$$ m\rightarrow\infty $$

gives

$$ FV=PVe^{rt} $$

Therefore,

$$ PV=FVe^{-rt} $$

where

* **e** is Euler's Number.

Continuous discounting is widely used in

* Bond mathematics
* Yield curve modelling
* Black-Scholes option pricing
* Interest rate models
* Quantitative finance research

---

# Coupon Bond Pricing

Unlike a zero-coupon bond, a coupon bond pays periodic coupons before returning the principal at maturity.

The price of a coupon bond equals the present value of every coupon payment plus the present value of the principal.

## Mathematical Model

$$
P=\sum_{t=1}^{n}\frac{C}{(1+y)^t}+\frac{F}{(1+y)^n}
$$

where

| Symbol | Description       |
| ------ | ----------------- |
| **P**  | Bond Price        |
| **F**  | Face Value        |
| **C**  | Coupon Payment    |
| **y**  | Yield to Maturity |
| **n**  | Number of Periods |

The implementation in this repository follows this formula directly.

---

# Project Overview

This project develops a Python implementation of coupon bond valuation using publicly available assumptions inspired by the Patriot Bond.

The program

* discounts each coupon payment,
* discounts the principal repayment,
* calculates the fair bond price,
* classifies the bond as Premium, Par, or Discount,
* displays all discounted cash flows in tabular form.

---

# Features

* Time Value of Money implementation
* Present Value calculation
* Coupon Bond Pricing
* Cash Flow Table
* Premium / Par / Discount Classification
* Python implementation using Pandas

---

# Installation

Clone the repository

```bash
git clone https://github.com/subiantvanss-oss/Fixed-Income-Bond-Pricing.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# Example Output

The program displays

* Bond parameters
* Discounted coupon cash flows
* Present value of principal
* Fair bond price
* Bond classification

<img width="1100" height="360" alt="Screenshot 2026-06-30 at 02 06 12" src="https://github.com/user-attachments/assets/4cfff37c-acec-4905-acc1-a3fad3f1fba4" />

---

# Future Improvements

Future versions of this project may include

* Yield to Maturity (YTM) Solver
* Bond Duration
* Modified Duration
* Convexity
* DV01
* Interest Rate Sensitivity Analysis

---

# Disclaimer

This repository is intended solely for educational purposes. It demonstrates the mathematical implementation of fixed-income valuation and should not be interpreted as financial or investment advice.
pts based on standard financial theory and should not be considered financial or investment advice.

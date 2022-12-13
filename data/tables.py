import json
import pandas as pd
import selenium


EBSA_UNDERPAYMENT_URL = "https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/correction-programs/vfcp/table-of-underpayment-rates"


def fetch_underpayment_rates():
    try:
        with open("data/underpayment_rates.json") as f:
            underpayment_rates = json.load(f)
            print("found rates")

    except FileNotFoundError as e:
        print(e)
        print("Rebuilding tables...")
        underpayment_rates = generate_underpayment_rates()
        with open("data/underpayment_rates.json", "w") as f:
            json.dump(underpayment_rates, f)

    return underpayment_rates


def generate_underpayment_rates():
    underpayment_rates = {}
    underpayment_rates[2022] = {}
    underpayment_rates[2022][4] = {"(a)(2)": 6, "(c)(1)": 8}
    return underpayment_rates

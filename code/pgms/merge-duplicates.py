"""Our customer records are sometimes a little messy and contain duplicate entires.
    For instance, we might have two records like "Lumiere Technologies" and "Lumiere Technologies (old DO NOT USE)".
    Please write a small basic function to merge these records together. We've provided a few example inputs below.
    Also please enclose your code sample in three backticks (Markdown-style). If we can't easily read your source code, it will be ignored.
    We are aware this is a very difficult problem: we're looking for what you can do quickly as a basic case, not an ideal solution.
    Please feel free to provide a written explanation for your choices as well.
    """

from typing import List


input = ["Equipment ONLY - Lumiere Technologies",
         "Lumiere Technologies",
         "Lumiere Tech, Inc.",
         "Mendes Metal SA - Central Office",
         " *** DO NOT USE ** * Mendes Metal",
         "Mendes Metal, SA",
         "Ship to Klapisch Aerospace gmbh",
         " Klapisch Aero, gmbh Munich",
         "Klapisch Aerospace tech(use Klapisch Aero, gmbh Munich acct 84719482-A)"]


def remove_duplicate_records(input: List) -> List:
    record_set = set(input)
    marked_seen = {}
    for element in record_set:
        if not marked_seen:
            marked_seen[element] = 1
        
        else:
            for key in marked_seen.keys():
                

    pass
    """You're designing a new system to store players and teams for an online board game. This system will also encode relationships between the users and teams. The company is doing well, so this system needs to support millions of users and teams, and a corresponding number of user-team relationships. One of your colleagues suggests using a document-based system (e.g., MongoDB). Would you support your colleague's idea? Why or why not?
    """
    """
    Our customers often have custom pricing APIs we need to wrap. Their customers often don't all receive the same price. Imagine that we have the code below that wraps custom pricing to make it easier for other parts of our system. Suppose we currently have two customers, Voltaire SA and Leibniz gmbh, and want to add custom pricing code for a new company, Bentham plc. Adapting the code below against the API described, how would you do that? Please enclose your source code in three backticks (Markdown-style). If we cannot easily read your source code, it will not be considered.

Existing code:

def get_price(company, customer_id, product_id):
    if company == 'voltairesa':
        price_group = db.query('voltairesa', customer_id)['price_group']
        raw = requests.get('https://mockend.com/prmsolutions/custom-pricing-challenge/Voltaire',
                           params={'priceGrp_eq': price_group, 'productId_eq': product_id}).json()
        return raw[0]['custPrice']

    elif company == 'leibnizgmbh':
        price_group = 'PRG{}X'.format(db.query('leibnizgmbh', customer_id)['price_group'])
        raw = requests.get('https://mockend.com/prmsolutions/custom-pricing-challenge/Leibniz',
                           params={'pg_eq': price_group, 'pid_eq': product_id}).json()
        return raw[0]['clprx']

    return 0.0
New API: https://mockend.com/prmsolutions/custom-pricing-challenge/Bentham where product_code_eq is the product ID and client_pricing_segment_eq is the price group.
    """[One of your team members is falling behind on their work, which threatens to delay the project. What can you do to bring them back up to speed?]
    """
import os

def get_prime_factor(result):
    ans = os.popen("factor {}".format(result)).read()
    return ans.split(": ")[1].rstrip()
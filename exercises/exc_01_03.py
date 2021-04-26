import json
import os

# This code will run relative to the root of the repo, so we can load files
with open("exercises/bookquotes.json") as f:
    DATA = json.loads(f.read())
    print(f.name)

# Print the first record in the DATA
print(___[____])

# Assign the length of DATA to some_var
some_var = ___

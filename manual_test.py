import pandas as pd
from solution import add_virtual_column

# Test data
fruits_sales = pd.DataFrame({
    "name": ["banana", "apple"],
    "quantity": [10, 3],
    "price": [10, 1]
})

print("INPUT:")
print(fruits_sales)
print()


result = add_virtual_column(fruits_sales, "quantity * price", "total")

print("OUTPUT:")
print(result)

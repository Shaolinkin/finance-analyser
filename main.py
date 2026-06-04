import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/transactions.csv')

df['Date'] = pd.to_datetime(df['Date'])

category_data = {
    "Tesco" : "Shopping",
    "Amazon" : "Shopping",
    "Clothing" : "Shopping",
    "Electricity Bill" : "Bills",
    "Water Bill" : "Bills",
    "Internet Bill" : "Bills",
    "Phone Bill" : "Bills",
    "Car Payment" : "Transport",
    "Netflix" : "Subscription",
    "Groceries" : "Food",
    "Restaurant" : "Food",
    "Salary" : "Income"
}

df['Category'] = df['Description'].map(category_data)

print(df)
print(df.loc[df['Category'].isnull()])

df_pos = df.loc[df.Amount > 0]
df_neg = df.loc[df.Amount < 0]

df_ingoing = df_pos['Amount'].sum()
df_outgoing = df_neg['Amount'].sum()

df_net = df_ingoing + df_outgoing

expenses = df_neg.groupby(['Category'])['Amount'].sum()
print(expenses)

expenses_by_month = df_neg.groupby(df_neg['Date'].dt.to_period('M'))['Amount'].sum()

# Bar chart 
plt.bar(expenses.index, -expenses)
plt.title('Expenses')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.show()

# Pie chart 
plt.figure()
plt.pie(-expenses, labels = expenses.index, autopct='%1.1f%%')
plt.show()

# Bar chart per month
plt.figure()
plt.bar(expenses_by_month.index.astype(str), -expenses_by_month)
plt.title('Expenses per month')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.show()
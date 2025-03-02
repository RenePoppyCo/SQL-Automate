import matplotlib.pyplot as plt
import seaborn as sns
import process as p

sns.barplot(x="product", y="total_revenue", data=p.df)
plt.xticks(rotation=45)
plt.title("Total Revenue by Product")
plt.show()

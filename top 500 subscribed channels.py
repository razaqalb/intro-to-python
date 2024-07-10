import pandas as pd
import matplotlib.pyplot as plt

df_read=pd.read_csv('youtube.csv')


print("\nSummary statistics:")
print(df_read.describe())


top_5_channels = df_read.head(5)

#line graph
plt.figure(figsize=(12,8))
plt.plot(top_5_channels['CHANNEL'], top_5_channels['VIEWS'], marker='o', linestyle='-',color='royalblue')
plt.title('top ranked channels by views')
plt.xlabel('channels')
plt.ylabel('views')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()

# bar graph
# plt.figure(figsize=(8,5))
# plt.bar(top5['CHANNEL'], top5['SUBSCRIBERS'], color='skyblue')
# plt.title('rank by subscribers')
# plt.xlabel('CHANNEL')
# plt.ylabel('SUBSCRIBERS')
# plt.grid(True)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# a. Pobierz dane
#url = "https://huggingface.co/datasets/imodels/credit-card/raw/main/train.csv"
#df = pd.read_csv(url)

# b. Usuń duplikaty
#df_no_duplicates = df.drop_duplicates()
#df_no_duplicates.to_csv("dane_po_usunieciu_duplikatow.csv", index=False)

df = pd.read_csv("dane_po_usunieciu_duplikatow.csv")
df['suma_transakcji'] = df.filter(like='bill_amt').sum(axis=1)
df.to_csv("suma_transakcji.csv", index=False)

correlation_age_limit = df['age'].corr(df['limit_bal'])
# Wyświetl informacje o danych po usunięciu duplikatów
print("Liczba wierszy przed usunięciem duplikatów:", len(df))
#print("Liczba wierszy po usunięciu duplikatów:", len(df_no_duplicates))
print("Korelacja pomiędzy wiekiem a limitem kredytu:", correlation_age_limit)


top_10_oldest = df.sort_values(by='age', ascending=False).head(10)
education_columns = [f"education:{i}" for i in range(0, 6)]
top_10_oldest['education_name'] = top_10_oldest[education_columns].apply(lambda x: x.idxmax(), axis=1)
top_10_oldest.to_csv("education_transakcji.csv", index=False)

# Wybierz określone kolumny
selected_columns = ['limit_bal', 'age', 'education_name', 'suma_transakcji']
top_10_oldest_table = top_10_oldest.loc[:, selected_columns]

# Wyświetl tabelę
print(top_10_oldest_table)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Histogram limitu kredytu
axes[0, 0].hist(df['limit_bal'], bins=30, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Histogram Limitu Kredytu')
axes[0, 0].set_xlabel('Limit Kredytu')
axes[0, 0].set_ylabel('Liczba Klientów')

# Histogram wieku
axes[0, 1].hist(df['age'], bins=30, color='salmon', edgecolor='black')
axes[0, 1].set_title('Histogram Wieku')
axes[0, 1].set_xlabel('Wiek')
axes[0, 1].set_ylabel('Liczba Klientów')

# Zależność limitu kredytu od wieku
axes[1, 0].scatter(df['age'], df['limit_bal'], alpha=0.5, color='green')
axes[1, 0].set_title('Zależność Limitu Kredytu od Wieku')
axes[1, 0].set_xlabel('Wiek')
axes[1, 0].set_ylabel('Limit Kredytu')

# Ukryj pusty subplot
axes[1, 1].axis('off')

# Dostosuj układ
plt.tight_layout()
plt.show()
# Wyświetl tabelę w formie graficznej
"""
plt.table(cellText=top_10_oldest_table.values,
          colLabels=top_10_oldest_table.columns,
          cellLoc='center',
          loc='center')
plt.axis('off')
plt.show()"""
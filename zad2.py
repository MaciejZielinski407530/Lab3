from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt


#url = "https://huggingface.co/datasets/imodels/credit-card/raw/main/train.csv"
#dane = pd.read_csv(url)

dataset = load_dataset("imodels/credit-card")
dane = pd.DataFrame(dataset['train'])


dane = dane.drop_duplicates()  # Usuwanie duplikatów
dane.to_csv("dane_train.csv")

# Korleacja
correlation = dane['age'].corr(dane['limit_bal'])
print("Korelacja pomiędzy wiekiem a limitem kredytu:", correlation)

# Dodaj kolumnę będącą sumą wszystkich transakcji (bill_amt_X)

dane['bill_amt_sum'] = dane.filter(like='bill_amt').sum(axis=1)
dane.to_csv("dane_train.csv")

# Znajdź 10 najstarszych klientów i narysuj tabelkę
oldest_10 = dane.sort_values(by='age', ascending=False).head(10)
education_columns = [f"education:{i}" for i in range(0, 6)]
oldest_10['education_name'] = oldest_10[education_columns].apply(lambda x: x.idxmax(), axis=1)
oldest_10 = oldest_10.loc[:, ['limit_bal', 'age', 'education_name', 'bill_amt_sum']]


plt.table(cellText=oldest_10.values,
          colLabels=oldest_10.columns,
          cellLoc='center',
          loc='center')
plt.axis('off')
plt.show()


# Histogram limitu kredytu, wieku, oraz zależność limitu kredytu od wieku
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 10))
axes[0].hist(dane['limit_bal'], bins=30)
axes[0].set_title('Histogram Limitu Kredytu')
axes[0].set_xlabel('Limit Kredytu')
axes[0].set_ylabel('Liczba Klientów')

axes[1].hist(dane['age'], bins=30)
axes[1].set_title('Histogram Wieku')
axes[1].set_xlabel('Wiek')
axes[1].set_ylabel('Liczba Klientów')

axes[2].scatter(dane['age'], dane['limit_bal'])
axes[2].set_title('Zależność Limitu Kredytu od Wieku')
axes[2].set_xlabel('Wiek')
axes[2].set_ylabel('Limit Kredytu')


plt.tight_layout()
plt.show()


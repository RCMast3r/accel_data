import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shitty_measure.csv')
print(df)

# iterating the columns
# for col in df.
adc1 = df["adc1_val"].tolist()
angle_deg = df["angle_deg"].tolist()
plt.plot(angle_deg, adc1)
plt.show()
# df.plot(x='adc1_p', y='adc1')
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df_wavelength = df.iloc[:, 0]
df = df.loc[:, ~df.columns.str.contains('Wavelength')]

df = pd.concat([df_wavelength, df], axis=1)

df = df.iloc[10:510, :].reset_index(drop=True)

df_standard = df[['Standard Sunset', 'Standard tartarazin']]

df = df.drop(['Standard Sunset', 'Standard tartarazin'], axis=1)
# remove first 210 rows

plt.plot(df.iloc[:, 0], df_standard['Standard Sunset'], label='Sunset Yellow Standard')
plt.plot(df.iloc[:, 0], df_standard['Standard tartarazin'], label='Tartrazine Standard')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.legend()
plt.savefig("Plots (200-700 nm)/standard_sunset_yellow_and_tartarazine.png")
plt.clf()

for i in range(1, len(df.columns)):
    x = df.iloc[:, 0]
    y = df.iloc[:, i]

    plt.plot(x, y, label=df.columns[i])
    plt.plot(x, df_standard["Standard Sunset"].values,  label='Sunset Yellow Standard')
    plt.plot(x, df_standard["Standard tartarazin"].values,  label='Tartrazine Standard')

    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Absorbance")
    plt.title(f'Absorbance vs Wavelength of {df.columns[i]}')
    plt.legend()
    plt.savefig(f'Plots (200-700 nm)/{df.columns[i]}.png')
    plt.clf()


df2 = pd.read_excel('data2.xlsx', sheet_name='Sheet1')
df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]
df2 = df2.loc[:, ~df2.columns.str.contains('Wavelength')]
df2 = df2.iloc[10:510, :].reset_index(drop=True)

for i in range(len(df2.columns)):
    x = df.iloc[:, 0]
    y = df2.iloc[:, i]
    plt.plot(x, y, label=df2.columns[i])


plt.plot(df.iloc[:, 0], df_standard['Standard Sunset'], label='Sunset Yellow Standard')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.title(f'Standard Sunset Yellow calibration curve')
plt.legend()
plt.savefig("Plots (200-700 nm)/standard_sunset_yellow.png")
plt.clf()


df3 = pd.read_excel('data3.xlsx', sheet_name='Sheet1')
df3 = df3[['Wavelength nm.', 'Tartarazine', 'T-2 ppm', 'T-4 ppm', 'T-6 ppm', 'T-8 ppm']]

plot_labels = ['Tartarazine (Stock 10 ppm)', 'Tartarazine (2 ppm)', 'Tartarazine (4 ppm)', 'Tartarazine (6 ppm)', 'Tartarazine (8 ppm)']
df3 = df3.iloc[10:510, :].reset_index(drop=True)

for i in range(1, len(df3.columns)):
    x = df3.iloc[:, 0]
    y = df3.iloc[:, i]

    plt.plot(x, y, label=plot_labels[i-1])

plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.title(f'Standard Tartarazine')
plt.legend()
plt.savefig("Plots (200-700 nm)/standard_tartarazine_at_different_ppm.png")
plt.clf()

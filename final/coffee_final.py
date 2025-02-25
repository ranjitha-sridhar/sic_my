import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

matplotlib.use('TkAgg')
sns.set_palette('pastel')

seed_data = {
    'Supplier': np.random.choice(['Blue Tokai', 'Tata Coffee', 'Nescafe', 'Lavazza'], 100),
    'Year': np.random.choice([2020, 2021, 2022, 2023, 2024], 100),
    'Seeds Bought (kg)': np.random.randint(400, 1000, 100),
    'Sales Generated ($)': np.random.randint(4000, 15000, 100)
}
seeds_df = pd.DataFrame(seed_data)
seeds_df.to_csv('Coffee_Seeds.csv', index=False)

launch_data = {
    'ProductLaunch': np.random.choice(['New Latte', 'Espresso Shot', 'Cold Brew', 'Flat White', 'Macchiato'], 100),
    'Sales': np.random.randint(500, 10000, 100)
}
launch_df = pd.DataFrame(launch_data)
launch_df.to_csv('Product_Launches.csv', index=False)

menu_data = {
    'MenuItem': np.random.choice(['Espresso', 'Latte', 'Cappuccino', 'Mocha', 'Americano', 'Affogato'], 100),
    'Sales': np.random.randint(1000, 10000, 100)
}
menu_df = pd.DataFrame(menu_data)
menu_df.to_csv('Menu_Optimization.csv', index=False)

price_data = {
    'Price': np.random.randint(50, 500, 100),
    'Sales': np.random.randint(1000, 9000, 100)
}
price_df = pd.DataFrame(price_data)
price_df.to_csv('Price_Sensitivity.csv', index=False)

competitor_data = {
    'Competitor': np.random.choice(['Starbucks', 'Costa Coffee', 'Blue Tokai', 'Third Wave Coffee', 'Cafe Coffee Day'], 50),
    'Sales': np.random.randint(1000, 10000, 50),
    'Rating': np.random.uniform(1, 5, 50)
}
competitor_df = pd.DataFrame(competitor_data)
competitor_df.to_csv('Competitor_Analysis.csv', index=False)

def new_product_launches(df):
    launch_data = df.groupby('ProductLaunch')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    launch_data.plot(kind='bar', color=sns.color_palette('pastel'))
    plt.title('New Product Launches')
    plt.xlabel('Product Launch')
    plt.ylabel('Sales')

def menu_optimization(df):
    menu_data = df.groupby('MenuItem')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    menu_data.plot(kind='bar', color=sns.color_palette('pastel'))
    plt.title('Menu Optimization')
    plt.xlabel('Menu Item')
    plt.ylabel('Sales')

def price_sensitivity(df):
    price_effect = df.groupby('Price')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    price_effect.plot(kind='line', marker='o', color=sns.color_palette('pastel')[0])
    plt.title('Price Sensitivity')
    plt.xlabel('Price')
    plt.ylabel('Sales')

def competitor_analysis(df):
    competitor_data = df.groupby('Competitor')[['Sales', 'Rating']].mean()
    competitor_data.plot(kind='bar', color=sns.color_palette('pastel'))
    plt.title('Competitor Sales and Ratings')
    plt.ylabel('Average Value')
    plt.xlabel('Competitor')

new_product_launches(launch_df)
menu_optimization(menu_df)
price_sensitivity(price_df)
competitor_analysis(competitor_df)

plt.show()
competitor_analysis(competitor_df)

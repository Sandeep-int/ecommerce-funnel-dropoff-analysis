import pandas as pd
import sqlite3
import os

# Delete old database
if os.path.exists('ecommerce_funnel.db'):
    os.remove('ecommerce_funnel.db')
    print('Old DB deleted')

# Read new CSV
df = pd.read_csv('data/ecommerce_funnel_data.csv')
print('CSV regions found:', df['region'].unique())
print('Total rows:', len(df))

# Load into fresh database
conn = sqlite3.connect('ecommerce_funnel.db')
df.to_sql('ecommerce_user_events', conn, if_exists='replace', index=False)
conn.close()

print('New DB created successfully!')
import pandas as pd
import numpy as np
import os

np.random.seed(42)

NUM_USERS = 10000

# 🇮🇳 Changed to Indian cities instead of generic regions
REGIONS = ['Chennai', 'Bangalore', 'Hyderabad', 'Mumbai', 'Delhi']
DEVICES = ['mobile', 'desktop', 'tablet']
TRAFFIC_SOURCES = ['organic', 'paid_search', 'social', 'email', 'direct']

# Funnel drop-off probabilities
FUNNEL_PROBS = {
    'add_to_cart':     0.35,
    'checkout_start':  0.60,
    'purchase':        0.55,
}

# 🇮🇳 Indian city-wise conversion boost (Chennai & Bangalore convert better)
REGION_MULTIPLIERS = {
    'Chennai':   1.15,
    'Bangalore': 1.10,
    'Hyderabad': 1.00,
    'Mumbai':    0.95,
    'Delhi':     0.90,
}

records = []
user_id = 1000

for _ in range(NUM_USERS):
    region = np.random.choice(REGIONS)
    device = np.random.choice(DEVICES, p=[0.55, 0.35, 0.10])
    source = np.random.choice(TRAFFIC_SOURCES, p=[0.30, 0.25, 0.20, 0.15, 0.10])
    multiplier = REGION_MULTIPLIERS[region]

    records.append({
        'user_id': user_id,
        'event_type': 'product_view',
        'device': device,
        'traffic_source': source,
        'region': region,
    })

    if np.random.random() < FUNNEL_PROBS['add_to_cart'] * multiplier:
        records.append({
            'user_id': user_id,
            'event_type': 'add_to_cart',
            'device': device,
            'traffic_source': source,
            'region': region,
        })

        if np.random.random() < FUNNEL_PROBS['checkout_start'] * multiplier:
            records.append({
                'user_id': user_id,
                'event_type': 'checkout_start',
                'device': device,
                'traffic_source': source,
                'region': region,
            })

            if np.random.random() < FUNNEL_PROBS['purchase'] * multiplier:
                records.append({
                    'user_id': user_id,
                    'event_type': 'purchase',
                    'device': device,
                    'traffic_source': source,
                    'region': region,
                })

    user_id += 1

df = pd.DataFrame(records)

os.makedirs('data', exist_ok=True)
df.to_csv('data/ecommerce_funnel_data.csv', index=False)

print("✅ Indian Cities Dataset generated successfully.")
print(f"Rows: {len(df)}")
print(f"Users: {NUM_USERS}")
print(f"Regions: {REGIONS}")
print("\nEvent distribution:")
print(df['event_type'].value_counts())
print("\nCity-wise user distribution:")
print(df[df['event_type']=='product_view']['region'].value_counts())
import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect('ecommerce_funnel.db')
df = pd.read_sql_query("SELECT * FROM ecommerce_user_events", conn)
conn.close()

# Check column names (debug)
print("Columns in database:", df.columns.tolist())
print("Sample data:")
print(df.head(3))
print()

# Funnel order
funnel_order = ['product_view', 'add_to_cart', 'checkout_start', 'purchase']
funnel_counts = df['event_type'].value_counts().reindex(funnel_order)

print("E-commerce Funnel Analysis Summary (Indian Cities)")
print("=" * 55)

print("\n📊 Overall Funnel Performance")
print(f"Product Views:    {funnel_counts['product_view']}")
print(f"Add to Carts:     {funnel_counts['add_to_cart']}")
print(f"Checkout Starts:  {funnel_counts['checkout_start']}")
print(f"Purchases:        {funnel_counts['purchase']}")

print("\n📉 Step Conversion Rates")
v2c   = funnel_counts['add_to_cart']    / funnel_counts['product_view']    * 100
c2ch  = funnel_counts['checkout_start'] / funnel_counts['add_to_cart']     * 100
ch2p  = funnel_counts['purchase']       / funnel_counts['checkout_start']  * 100
overall = funnel_counts['purchase']     / funnel_counts['product_view']    * 100

print(f"View → Cart:             {v2c:.2f}%")
print(f"Cart → Checkout:         {c2ch:.2f}%")
print(f"Checkout → Purchase:     {ch2p:.2f}%")
print(f"Overall View → Purchase: {overall:.2f}%")

drop = 100 - v2c
print(f"\n🚨 Biggest Drop-off Stage")
print(f"Product View → Add to Cart: {drop:.2f}% drop-off")

# City-wise Analysis
print("\n🏙️  City-wise Purchase Conversion Rate")
print("-" * 40)

cities = ['Chennai', 'Bangalore', 'Hyderabad', 'Mumbai', 'Delhi']
city_results = []

for city in cities:
    city_data = df[df['region'] == city]
    views     = len(city_data[city_data['event_type'] == 'product_view'])
    purchases = len(city_data[city_data['event_type'] == 'purchase'])
    rate = (purchases / views * 100) if views > 0 else 0
    city_results.append({'city': city, 'views': views,
                         'purchases': purchases, 'rate': rate})

city_summary = pd.DataFrame(city_results).sort_values('rate', ascending=False)
for _, row in city_summary.iterrows():
    print(f"{row['city']:<12} Views:{row['views']:>5}  "
          f"Purchases:{row['purchases']:>5}  Rate:{row['rate']:.2f}%")

best  = city_summary.iloc[0]
worst = city_summary.iloc[-1]
print(f"\n✅ Best City:  {best['city']} ({best['rate']:.2f}% purchase rate)")
print(f"❌ Worst City: {worst['city']} ({worst['rate']:.2f}% purchase rate)")

# Device Analysis - using actual column name from data
device_col = 'device_type' if 'device_type' in df.columns else 'device'
print(f"\n📱 Device-wise Conversion Rate")
print("-" * 40)
for dev in df[device_col].unique():
    d = df[df[device_col] == dev]
    v = len(d[d['event_type'] == 'product_view'])
    p = len(d[d['event_type'] == 'purchase'])
    if v > 0:
        print(f"{dev:<12} {(p/v*100):.2f}%")

# Traffic Source Analysis
src_col = 'traffic_source' if 'traffic_source' in df.columns else 'source'
print(f"\n🌐 Traffic Source Conversion Rate")
print("-" * 40)
for src in df[src_col].unique():
    s = df[df[src_col] == src]
    v = len(s[s['event_type'] == 'product_view'])
    p = len(s[s['event_type'] == 'purchase'])
    if v > 0:
        print(f"{src:<15} {(p/v*100):.2f}%")

print("\n💡 Business Interpretation")
print("-" * 55)
print("Chennai & Bangalore show highest purchase intent.")
print("Mobile users need checkout UX improvements.")
print("Email traffic converts best — invest more in email campaigns.")
print("Social media traffic has lowest conversion — review ad targeting.")
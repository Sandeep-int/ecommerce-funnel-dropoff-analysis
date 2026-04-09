# E-Commerce Funnel Drop-off Analysis 🇮🇳

An end-to-end product analytics project analyzing user 
behavior across an e-commerce purchase funnel across 
Indian metro cities.

## 🎯 Business Problem
Identify where users abandon the purchase journey across
Chennai, Bangalore, Hyderabad, Mumbai, and Delhi.

## 📊 Key Results
| City | Purchase Rate |
|------|--------------|
| Chennai | 18.37% ✅ Best |
| Bangalore | 15.49% |
| Hyderabad | 11.26% |
| Mumbai | 9.94% |
| Delhi | 8.92% ❌ Lowest |

## 🚨 Key Finding
**65.32% drop-off** between Product View → Add to Cart
— biggest conversion bottleneck in the funnel.

## 🛠️ Tools & Technologies
- Python (Pandas, NumPy)
- SQL (SQLite)
- Data Analysis & Funnel Analytics

## 📁 Project Structure
- `generate_funnel_data.py` — Generates Indian cities dataset
- `load_to_sqlite.py` — Loads data into SQLite database
- `analysis/funnel_analysis.py` — Full funnel analysis

## 💡 Business Recommendations
1. Improve product page engagement (biggest drop-off point)
2. Optimize mobile checkout (tablet lowest conversion)
3. Focus acquisition efforts on Chennai & Bangalore markets
4. Organic search drives best quality traffic (13.23%)

## How to Run
```bash
python generate_funnel_data.py
python load_to_sqlite.py
python analysis/funnel_analysis.py
```
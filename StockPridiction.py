# PRODUCT STOCK PREDICTION - ML Micro Project
# Predicts how many units will be sold based on Month and Product Category

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# STEP 1: LOAD DATASET
df = pd.read_csv('stock_data.csv')
print("Dataset:")
print(df)

# STEP 2: CONVERT CATEGORY TEXT TO NUMBERS
le = LabelEncoder()
df['Product_Category'] = le.fit_transform(df['Product_Category'])
print("\nProduct Categories converted to numbers:")
print(dict(zip(le.classes_, le.transform(le.classes_))))

# STEP 3: SPLIT INTO INPUT AND OUTPUT
X = df[['Month', 'Product_Category']]
y = df['Units_Sold']

# STEP 4: SPLIT INTO TRAIN AND TEST DATA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTraining samples : {len(X_train)}")
print(f"Testing  samples : {len(X_test)}")

# STEP 5: TRAIN THE MODEL
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)
print("\nModel Trained Successfully!")

# STEP 6: CHECK ACCURACY
predictions = model.predict(X_test)
accuracy = r2_score(y_test, predictions)
print(f"Model Accuracy : {accuracy * 100:.2f}%")

# STEP 7: PREDICT FOR A NEW INPUT
print("\n--- PREDICT STOCK FOR A PRODUCT ---")
print("Categories available:", list(le.classes_))
month = int(input("Enter Month (1-12): "))
category = input("Enter Product Category (Electronics / Clothing / Food / Furniture): ")

# Fix: auto correct capital letter so "food" and "Food" both work
category = category.strip().title()

if category not in le.classes_:
    print(f"Invalid category! Please choose from: {list(le.classes_)}")
else:
    category_encoded = le.transform([category])[0]
    result = model.predict([[month, category_encoded]])[0]
    print(f"\nPredicted Units to be Sold: {result:.0f} units")

# STEP 8: SHOW GRAPH
plt.figure(figsize=(8, 5))
for cat in le.classes_:
    cat_data = df[df['Product_Category'] == le.transform([cat])[0]]
    plt.plot(cat_data['Month'], cat_data['Units_Sold'], marker='o', label=cat)

plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Product Stock Sold Per Month')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('stock_prediction.png', dpi=150)
plt.show()
print("Graph saved as stock_prediction.png")
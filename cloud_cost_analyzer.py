import pandas as pd
import glob

# Read all CSV files in the folder
csv_files = glob.glob("cloud_billing_*.csv")

# Combine all CSVs into one DataFrame
df_list = []
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

yearly_data = pd.concat(df_list, ignore_index=True)

print("\n--- Combined Yearly Cloud Data ---")
print(yearly_data)
#Analyze Yearly Cloud Cos
# Convert Date column to datetime
yearly_data["Date"] = pd.to_datetime(yearly_data["Date"])

# Total yearly cost
total_yearly_cost = yearly_data["Cost"].sum()
print(f"\n💰 Total Yearly Cloud Cost: ₹{total_yearly_cost}")

# Yearly cost by service
service_yearly_cost = yearly_data.groupby("Service")["Cost"].sum()
print("\n📊 Yearly Cost by Service:")
print(service_yearly_cost)

# Monthly cost breakdown
monthly_cost = yearly_data.groupby(yearly_data["Date"].dt.month)["Cost"].sum()
print("\n📆 Monthly Cost Breakdown:")
print(monthly_cost)
#Finding Unused Resources (Yearly)
unused_resources = yearly_data[yearly_data["UsageHours"] == 0]

print("\n⚠ Unused Resources Across the Year:")
print(unused_resources[["Service", "Resource", "Cost"]])
#Visualizing Yearly Cost
import matplotlib.pyplot as plt

# Plot service-wise yearly cost
plt.figure()
service_yearly_cost.plot(kind="bar")
plt.title("Yearly Cloud Cost by Service")
plt.xlabel("Service")
plt.ylabel("Cost (₹)")
plt.show()

# Plot monthly cost trend
plt.figure()
monthly_cost.plot(marker="o")
plt.title("Monthly Cloud Cost Trend")
plt.xlabel("Month")
plt.ylabel("Cost (₹)")
plt.show()

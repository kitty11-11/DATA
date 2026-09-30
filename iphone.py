#========================================================================================================================================================================================================================================================================================================
#-------------------IPHONE SALES DATASET--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#===================AUTHOR: KIRTI============================================================================================================================================================================================================================
#-------------------TOOLS : Pandas|Matplotlib|NumPy-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#==================================================================================================================================================================================================================================================
#--------------------------IMPORT LIBRARIES------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#----------------------------LOAD DATA-------------------------------------------------------------------------------------------------------------
df=pd.read_csv(r"C:\Users\kriti\Downloads\iphone_sales_dataset.csv")

#============================================================================================================================================================================================================================================
#-----------------------------DATASET EXPLORATION--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#==============================================================================================================================================================================================================================================================
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.columns)
print(df.sample(5))
print(df.shape)
#-----------------------OBSERVATION-------------------------------------------------------------------------------
# It has 100 rows and 10 columns
# It contains columns like Order_Id,Customer_name,country,Iphone_model,Storage,color,Quantitiy,Price,Sale date ,payment method
# It contains details of iphone sales 
#================================================================================================================================================================================================================================================================
#-----------------------------DATA CLEANING----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#==================================================================================================================================================================================================================================================================================
print(df.duplicated().sum())
print(df.isnull().sum())

#---------------------------conversion Sale_date to datetime------------------------------------------------------------------------------------------
df["Sale_Date"]=pd.to_datetime(df["Sale_Date"],errors = "coerce")
df["Sale_Month"]=df["Sale_Date"].dt.month
df["Sale_Year"]=df["Sale_Date"].dt.year
#-----------------------OBSERVATION--------------------------------------------------------------------------------------------------------
# It doesn't have any duplicate row
#it doesn't  have any null value
# converts sales date into date time
#create sales month and year columns
#------------ creation of revenue column----------------------------------
df["Revenue"]=df["Price"]*df["Quantity"]
#==================================================================================================================================================================================================================================================================================
#--------------------------EXPLORATORY DATA ANALYSIS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#==============================================================================================================================================================================================================================================================================================
# Total revenue
total_revenue = df["Revenue"].sum()
print( "Total Revenue :",total_revenue)

# Total Orders
total_orders = df["Order_ID"].nunique()
print("Total Orders : ",total_orders)

#Total Quantity sold
total_quantity_sold = df["Quantity"].sum()
print("Total Quantity sold :",total_quantity_sold)

# Most sold iphone Model
most_sold = df.groupby("iPhone_Model")["Quantity"].sum().sort_values(ascending= False)
print("Most sold iPhone Model :",most_sold.head(1))

# revenue by model
revenue_by_model = df.groupby("iPhone_Model")["Revenue"].sum()
print(revenue_by_model)
revenue_by_model.plot(kind = "bar")
plt.title("Revenue by Model")
plt.xlabel("iPhone Model")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


#Top countries by sales
top_countries = df.groupby ("Country")["Quantity"].sum().sort_values(ascending=False)
print(top_countries.head(5))
top_countries.plot(kind = "bar")
plt.title("Top Countries by Quantity sold")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# most popular storage variant
popular_storage = df["Storage"].str.replace("GB","").astype(int).value_counts().head(1)
print("Most Popular Storage Varianr :",popular_storage)

#most popular color
popular_color = df["Color"].value_counts().head(1)
print("Most Popular Color : ",popular_color)

#most used payment method
most_used_payment_method = df["Payment_Method"].value_counts().head(1)
print("Most Used Payment Method ;",most_used_payment_method)

#monthly sales trend
monthly_sales_trend =df.groupby("Sale_Month")["Quantity"].sum()
print(monthly_sales_trend)
monthly_sales_trend.plot(kind = "line",color= "black",marker = "*")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

#monthly revenue trend
monthly_revenue_trend = df.groupby("Sale_Month")["Revenue"].sum()
print(monthly_revenue_trend)
monthly_revenue_trend.plot(kind ="line",color = "red",marker=".")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
#average selling price
avg_selling_price = df["Revenue"].mean()
print("Average selling price ;",avg_selling_price)

#highest single order
highest_single_order = df.groupby("Order_ID")["Revenue"].sum().sort_values(ascending = False)
print("Highest single order:",highest_single_order.head(1))

#top customers
top_customer = df.groupby("Customer_Name")["Revenue"].sum().sort_values(ascending = False)
print("Top Customers :",top_customer.head(3))


#sales distribution by country
sales_by_country = df.groupby("Country")["Quantity"].sum()
print(sales_by_country)
sales_by_country.plot(kind ="barh",color ="yellow")
plt.title("sales distribution by contries")
plt.xlabel("sales")
plt.ylabel('Country')
plt.tight_layout()
plt.show()

#revenue share 
revenue_share=df.groupby("Country")["Revenue"].sum()
print(revenue_share)
revenue_share.plot(kind="pie",autopct = "%1.1f%%")
plt.title("Revenue Share")
plt.tight_layout()
plt.show()

#quantity sold by Model
quantity_sold_by_model=df.groupby("iPhone_Model")["Quantity"].sum()
print(quantity_sold_by_model)

#top 5 models
top_5_models = df.groupby("iPhone_Model")["Quantity"].sum().sort_values(ascending= False)
print(top_5_models.head(5))

# correlation between Quantity and Price
correlation = df["Quantity"].corr(df["Price"])
print("Correlation:",correlation)

#-----------------EXPORTATION OF CLEANED DATASET------------------------------
df.to_csv("cleaned_iphone_sales.csv",index= False)
#=============================================================================================================================================================================================================================================================
#---------------------------FINAL INSIGHTS---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#===============================================================================================================================================================================================================================================================
# It has generated total revenue of 494453 
# There are 100 total orders
# Total quantity sold is 333
# iPhone 15 pro Max is most sold model
#  UK is the top country in purchasing iPhones
# Most popular storage variant is 256 GB
#  Blue is the most popular color 
#  Most used Payment method is Debit Card
# Customer_17 is top customer
# Average selling price is 1468.75
# Correlation between Quantity and Price is 0.0939...


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("Sales Performance Dashboard")

df = pd.read_csv("cleaned_sales_data.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst = True)
# Sidebar Filters
st.sidebar.header("Filters")
year_list = df['Order Date'].dt.year.unique()
selected_year = st.sidebar.selectbox("Year", sorted(year_list))
region_list = df['Region'].unique()
selected_region = st.sidebar.multiselect("Region", region_list, default=region_list)
segment_list = df['Segment'].unique()
selected_segment = st.sidebar.multiselect("Segment", segment_list, default=segment_list)
# Filter Data
filtered_df = df[(df['Order Date'].dt.year == selected_year) &(df['Region'].isin(selected_region)) &(df['Segment'].isin(selected_segment))]
# Metrics
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df['Order ID'].nunique()
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", f"{total_orders:,}")
st.markdown("---")
# Charts
col1,col2 = st.columns(2)
with col1:
	fig1 = px.bar(filtered_df.groupby("Category")["Sales"].sum().reset_index(),x="Category",y="Sales",title="Sales by Category")
	st.plotly_chart(fig1, use_container_width=True)
with col2:
	monthly_sales = filtered_df.groupby(pd.Grouper(key='Order Date',freq='ME'))['Sales'].sum().reset_index() 
	fig2 = px.line(monthly_sales,x='Order Date',y='Sales',title="Monthly Sales Trend")
	st.plotly_chart(fig2,use_container_width=True)
# Data Table
st.subheader("Data Table")
st.dataframe(filtered_df)
#customer behaviour analysis section
st.markdown('---')
st.header("Customer Behaviour Analysis Dashboard")

col3,col4 = st.columns(2)

with col3:
	st.subheader("Top 10 customers by Sales")
	top_customers = filtered_df.groupby("Customer Name")['Sales'].sum().nlargest(10).reset_index()
	fig3 = px.bar(top_customers,x='Sales',y='Customer Name',orientation='h',
		title="Highest Spending Customers",color = 'Sales')
	fig3.update_layout(yaxis={'categoryorder':'total ascending'})
	st.plotly_chart(fig3)
	
	
with col4:
	st.subheader("Sales By Customer Segment")
	segment_sales = filtered_df.groupby('Segment')['Sales'].sum().reset_index()
	fig4 = px.pie(segment_sales,names="Segment",values='Sales',hole=0.4,
		title = "Which Segment Buys Most?")
	st.plotly_chart(fig4)		
		
st.markdown("---")
st.subheader("Loss Analysis")


col5,col6 = st.columns(2)


with col5:
	st.write("Top 10 Loss Making Products")
	loss_products = filtered_df[filtered_df['Profit']<0.].groupby('Product Name')['Profit'].sum().nsmallest(10).reset_index()
	fig5 = px.bar(loss_products,x='Profit',y='Product Name',orientation = 'h',
			title = "Products Eating Your Money",color = "Profit",
			color_continuous_scale = 'Reds')
	fig5.update_layout(yaxis={'categoryorder':'total ascending'})
	st.plotly_chart(fig5)
	
	
with col6:
	st.write("Top 5 Customers with Negative Profit")
	loss_customers = filtered_df[filtered_df['Profit']<0.].groupby('Customer Name')['Profit'].sum().nsmallest(5).reset_index()
	fig6 = px.bar(loss_customers,x='Profit',y='Customer Name',orientation = 'h',
			title = "Loss Making Customers",color = "Profit",
			color_continuous_scale = 'Reds_r')
	fig5.update_layout(yaxis={'categoryorder':'total ascending'})
	st.plotly_chart(fig6)
		
			


























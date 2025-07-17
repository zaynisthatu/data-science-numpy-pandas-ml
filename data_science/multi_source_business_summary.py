import pandas as pd

# Load datasets
sales = pd.read_csv('sales.csv')
marketing = pd.read_csv('marketing.csv')
support = pd.read_csv('support.csv')

# Combine basic info for a master summary
# Example summaries:

# 1. Total Sales Summary
total_sales = sales['TotalSales'].sum()
total_quantity = sales['Quantity'].sum()
top_category = sales.groupby('Category')['TotalSales'].sum().idxmax()

# 2. Marketing Summary
total_budget = marketing['Budget'].sum()
total_leads = marketing['Leads'].sum()
total_conversions = marketing['Conversions'].sum()
conversion_rate = total_conversions / total_leads if total_leads != 0 else 0

# 3. Support Summary
total_tickets = support.shape[0]
closed_tickets = support[support['Status'] == 'Closed'].shape[0]
avg_resolution_time = support[support['Status'] == 'Closed']['ResolutionTime'].mean()

# Prepare the summary dictionary
summary = {
    'Sales Summary': {
        'Total Sales': total_sales,
        'Total Quantity Sold': total_quantity,
        'Top Category by Sales': top_category
    },
    'Marketing Summary': {
        'Total Budget Spent': total_budget,
        'Total Leads Generated': total_leads,
        'Total Conversions': total_conversions,
        'Conversion Rate': conversion_rate
    },
    'Support Summary': {
        'Total Tickets': total_tickets,
        'Closed Tickets': closed_tickets,
        'Average Resolution Time (hours)': avg_resolution_time
    }
}

# Convert summary to a DataFrame for better presentation
master_report = pd.DataFrame.from_dict({(i, j): summary[i][j] 
                                        for i in summary.keys() 
                                        for j in summary[i].keys()},
                                       orient='index', columns=['Value'])

# Save summary to Excel
master_report.to_excel('master_summary_report.xlsx')

print("Master summary report generated successfully!")
print(master_report)

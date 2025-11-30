"""
Visualize module - Create matplotlib charts

This module creates:
1. Daily revenue line chart for each dataset
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from pathlib import Path
from typing import List, Dict


def plot_daily_revenue(daily_revenue: List[Dict], output_path: str, dataset_name: str) -> str:
    """
    Create a line chart of daily revenue.
    
    Args:
        daily_revenue: List of dicts with 'date' and 'revenue' keys
                       Example: [{'date': '2024-10-15', 'revenue': 325.50}, ...]
        output_path: Directory to save the chart
        dataset_name: Name of the dataset (DATA1, DATA2, DATA3)
    
    Returns:
        Path to the saved chart file
    """
    # convert list of dicts to DataFrame
    df = pd.DataFrame(daily_revenue)
    
    # convert date strings to datetime objects for proper plotting
    df['date'] = pd.to_datetime(df['date'])
    
    # sort by date (should already be sorted, but just to be safe)
    df = df.sort_values('date')
    
    # create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # Plot the line chart
    ax.plot(
        df['date'], 
        df['revenue'], 
        color='#2563eb',       # blue color
        linewidth=1.5,
        marker='o',           # small circles at data points
        markersize=3,
        markerfacecolor='#2563eb',
        markeredgecolor='white',
        markeredgewidth=0.5,
        alpha=0.9
    )
    
    # fill the area under the line
    ax.fill_between(
        df['date'], 
        df['revenue'], 
        alpha=0.15, 
        color='#2563eb'
    )
    
    # set labels and title
    ax.set_xlabel('Date', fontweight='bold', fontsize=10)
    ax.set_ylabel('Revenue (USD)', fontweight='bold', fontsize=10)
    ax.set_title(f'Daily Revenue - {dataset_name}', fontweight='bold', fontsize=14)
    
    # format x-axis to show dates nicely
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # this be -> "Jan 2024"
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # tick every month
    
    # rotate x-axis labels for readability
    plt.xticks(rotation=45, ha='right')
    
    # format y-axis with dollar signs
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # add grid for readability
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.set_axisbelow(True)  # grid behind the data
    
    # set y-axis to start at 0
    ax.set_ylim(bottom=0)
    
    # tight layout to prevent label cutoff
    plt.tight_layout()
    
    # create output directory if it doesn't exist
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # save the chart
    chart_filename = f'{dataset_name.lower()}_daily_revenue.png'
    chart_path = output_dir / chart_filename
    
    plt.savefig(
        chart_path, 
        dpi=150,              # good resolution
        bbox_inches='tight',  # dont cut off labels
        facecolor='white',    # white background
        edgecolor='none'
    )
    
    # close the figure to free memory
    plt.close()
    
    return str(chart_path)

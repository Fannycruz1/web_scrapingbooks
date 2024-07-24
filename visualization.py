# import the required libraries for visualization of data use a bar graph 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def load_data(file_path):
    # Load data from an Excel file into a pandas DataFrame.
    return pd.read_excel(file_path)

def plot_price_distribution(df, save_path):
    #Plot the distribution of book prices and save the plot as an image.
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Price'].astype(float), kde=True, bins=30)
    plt.title('Distribution of Book Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()

def plot_stock_availability(df, save_path):
    #Plot the count of books by stock availability and save the plot as an image.
    
    stock_counts = df['Stock'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=stock_counts.index, y=stock_counts.values)
    plt.title('Count of Books by Stock Availability')
    plt.xlabel('Stock Availability')
    plt.ylabel('Count')
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()

def add_images_to_excel(file_path, image_paths):
    #Add images to an existing Excel file
  
    workbook = load_workbook(file_path)
    sheet = workbook.active
    
    for image_path in image_paths:
        img = Image(image_path)
        # Find a suitable location to place the image
        # Adjust 'A1' for different locations as needed
        sheet.add_image(img, 'A1') 
        
    workbook.save(file_path)

def main():
    """
    Main function to load data, generate visualizations, and update the Excel file.
    """
    # Define file paths
    file_path = 'books.xlsx'
    price_image = 'price_distribution.png'
    stock_image = 'stock_availability.png'
    
    # Load data from the Excel file
    df = load_data(file_path)
    
    # Plot and save images
    plot_price_distribution(df, price_image)
    plot_stock_availability(df, stock_image)
    
    # Add images to the Excel file
    add_images_to_excel(file_path, [price_image, stock_image])

if __name__ == "__main__":
    main()

# 🍄 Mushroom Data Visualization Using Python

## 📌 Project Overview

This project explores and visualizes mushroom characteristics using **Python, Pandas, and Matplotlib**. It analyzes mushroom attributes and presents their distributions through bar charts, horizontal bar charts, and pie charts.

The goal is to understand the dataset through visual analysis of mushroom classes, cap shapes, cap surfaces, colors, bruises, odors, gill attachments, gill spacing, and gill colors.

## 🎯 Project Objectives

- Analyze the distribution of edible and poisonous mushrooms.
- Visualize different mushroom cap shapes, surfaces, and colors.
- Explore mushroom bruises and odor characteristics.
- Analyze gill attachment, spacing, and color distributions.
- Practice data cleaning, data manipulation, and data visualization using Python.

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas** — Data cleaning and data analysis
- **Matplotlib** — Data visualization
- **CSV** — Dataset format

## 📊 Visualizations

The project generates the following charts:

| Visualization | Description |
|---|---|
| Class Distribution | Compares edible and poisonous mushrooms |
| Cap Shape Distribution | Shows the distribution of mushroom cap shapes |
| Cap Surface Varieties | Visualizes different cap surface types |
| Cap Color Varieties | Shows the distribution of cap colors |
| Mushroom Bruises | Compares mushrooms with and without bruises |
| Mushroom Odor | Displays the distribution of different odor categories |
| Gill Attachment | Visualizes different gill attachment types |
| Gill Spacing | Shows the distribution of gill spacing categories |
| Gill Color | Compares different gill colors |

The charts are displayed using Matplotlib and saved as PNG image files for future reference.

## 📁 Project Structure

```text
Mushroom-Data-Visualization/
│
├── mushrooms.csv
├── mushroom_visualization.py
├── Class_Distribution_In_Mushroom.png
├── Cap-shape_In_Mushroom.png
├── Cap_Surface_Varieties_In_Mushroom.png
├── Color_Varieties_In_Mushroom.png
├── Percentage_of_Mushroom_Have_Bruises_or_Not.png
├── Odor_In_Mushroom.png
├── Gill_Attachment_in_Mushroom.png
├── Gill_Spacing_in_Mushroom.png
├── Gill_Color_In_Color.png
└── README.md
```

*Note: The filenames above should match the actual files in your repository.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/VipulDhiman8865/Mushroom-Data-Visualization.git
```

### 2. Navigate to the project directory

```bash
cd Mushroom-Data-Visualization
```

### 3. Install the required libraries

```bash
pip install pandas matplotlib
```

### 4. Add the dataset

Place `mushrooms.csv` in the project directory.

Update the CSV path in the Python script to use a relative path:

```python
df = pd.read_csv('mushrooms.csv')
```

### 5. Run the script

```bash
python mushroom_visualization.py
```

The visualizations will appear on screen and be saved as PNG files in the project directory.

## 🧹 Data Cleaning and Processing

- Removes rows containing missing values in the selected mushroom attributes.
- Converts encoded mushroom categories into readable labels.
- Calculates category frequencies using Pandas.
- Creates charts to represent the distribution of each selected feature.

## 📚 Key Learnings

- Reading CSV files using Pandas.
- Handling missing values with `dropna()`.
- Mapping categorical values to descriptive labels.
- Calculating category frequencies with `value_counts()`.
- Creating bar charts, pie charts, and horizontal bar charts using Matplotlib.
- Saving visualizations as PNG images using `savefig()`.

## 🚀 Future Improvements

- Add more visualizations and feature comparisons.
- Create a correlation or feature relationship analysis where appropriate.
- Build an interactive dashboard.
- Improve chart formatting, legends, and labels.
- Add summary statistics and key findings from the dataset.

## 👨‍💻 Author

**Vipul Dhiman**

- GitHub: [VipulDhiman8865](https://github.com/VipulDhiman8865)

## 📄 License

This project is intended for educational and learning purposes.

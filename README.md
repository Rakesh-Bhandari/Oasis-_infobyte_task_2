
# BMI Calculator

This is a simple, user-friendly BMI (Body Mass Index) Calculator built using Python's CustomTkinter for the GUI and Matplotlib for graph plotting. This application allows users to calculate their BMI based on their weight, height, and age, and provides feedback on their BMI category (Underweight, Normal, Overweight, or Obesity). 

## Features

- **Gender Selection:** Allows users to toggle between male and female, updating the image accordingly.
- **BMI Calculation:** Computes BMI based on the user's weight and height.
- **BMI Classification:** Classifies BMI into categories such as Underweight, Normal, Overweight, and Obesity.
- **Data Storage:** Stores user data (weight, height, and BMI) with the current date in a text file for later analysis.
- **BMI Trend Visualization:** Displays a graph showing the user's BMI trend over time, based on the last five records.
- **Interactive GUI:** Uses CustomTkinter to create a modern, responsive interface with custom colors and styles.
- **Error Handling:** Ensures that only valid inputs for age, weight, and height are accepted.

## How to Use

1. Clone the repository.
2. Ensure you have the required Python packages (`CustomTkinter`, `PIL`, `Matplotlib`).
3. Run the script to launch the BMI Calculator.
4. Enter your age, weight (in kg), and height (in cm).
5. Select your gender.
6. Click the "Calculate" button to get your BMI score and classification.
7. Your BMI history is automatically saved, and you can view your BMI trend on the graph.

## Requirements

- Python 3.x
- CustomTkinter
- Matplotlib
- Pillow (PIL)

## Installation

```bash
pip install customtkinter matplotlib pillow
```

## File Structure

- `BMI/bmi_data.txt` - Stores historical BMI data.
- `BMI/images/` - Contains image assets for the GUI.

## Future Improvements

- Add more detailed analytics based on BMI.
- Integrate database support for better data management.
- Introduce additional features like calorie tracking and exercise suggestions.

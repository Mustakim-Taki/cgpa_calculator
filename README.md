# CGPA Calculator

Library Link: [pip install cgpa-calculator==2.2.0](https://pypi.org/project/cgpa-calculator/)

`pip install cgpa-calculator==2.2.0`

A Python-based CGPA Calculator that helps you manage your courses, calculate your CGPA based on GPAs and credits, and display detailed course-wise results. The tool is simple, efficient, and easy to use.

## Features
- Add multiple courses with GPA and credit values.
- Calculate weighted CGPA based on the entered courses and credits.
- Display detailed results for each course, including course name, GPA, and credit hours.
- Input validation for GPA (0.0–4.0) and credit values (positive numbers).

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository or download the `CGPACalculator.py` file:
   ```bash
   https://github.com/Mustakim-Taki/cgpa_calculator
   cd cgpa_calculator


Ensure Python is installed and properly configured.<br>
### Usage
1. Add Courses
Use the add_course method to add a course with:

Course Name (string)
GPA (float, 0.0–4.0)
Credit Hours (positive integer)<br>
`from cgpa_calculator import CGPACalculator`
`calculator = CGPACalculator()`
##calculator.add_course(course_name, gpa, credit) 
`calculator.add_course("CSE110", 4.0, 3)` <br>
`calculator.add_course("CSE370", 3.7, 3)` <br>
2. Calculate CGPA<br>
Call the calculate_cgpa method to compute your CGPA:<br>
`calculator.calculate_cgpa()`
3. Show Course Results
Display all added courses with their details using the show_results method:
`calculator.show_results()`

### Example Output 
```
Your CGPA is: 3.90
Course Results:
Course: CSE110 || Credit: 3 || GPA: 4.0
Course: CSE370 || Credit: 3 || GPA: 3.7
```

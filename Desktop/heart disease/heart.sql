// Name: BMI Category
IF [BMI] < 18.5 THEN "Underweight"
ELSEIF [BMI] < 25 THEN "Normal"
ELSEIF [BMI] < 30 THEN "Overweight"
ELSE "Obese"
END
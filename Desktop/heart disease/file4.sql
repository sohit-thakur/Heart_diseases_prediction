// Name: Heart Disease Prevalence %
SUM(IF [HeartDisease] = "Yes" THEN 1 ELSE 0 END) / COUNT([HeartDisease])
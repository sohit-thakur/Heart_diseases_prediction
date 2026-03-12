// Name: Personal Risk Factor
(IF [Smoking] = "Yes" THEN 1 ELSE 0 END) +
(IF [AlcoholDrinking] = "Yes" THEN 1 ELSE 0 END) +
(IF [Diabetic] = "Yes" THEN 1 ELSE 0 END) +
(IF [PhysicalActivity] = "No" THEN 1 ELSE 0 END)
# Preicting Rent Petitions in SF

For this project, I predicted the volume of rent petitions in San Francisco using the data freely available through [SF Open Data](https://data.sfgov.org/Housing-and-Buildings/Petitions-to-the-Rent-Board/6swy-cmkq). After a short grid-search, I found that a SARIMA(2, 1, 2)(0, 1, 2)[12] gave me the lowest MAE for a 3-month and 5-year prediction. I also found that using linear regression on the unemployment rate data through [FRED Economic Research](https://fred.stlouisfed.org/series/CASANF0URN) enabled me to get similar results as the SARIMA model.

For more information, please read my [blog post](https://harrisonized.github.io/2019/06/25/sf-rent-petitions.html), which will be updated in a few days.
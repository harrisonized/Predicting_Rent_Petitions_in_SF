# Predicting Rent Petitions in SF

This is the project I presented on [Career Day](https://www.eventbrite.com/e/find-your-next-data-scientist-in-san-francisco-at-metis-career-day-for-employers-tickets-62002954506) at [Metis](https://www.thisismetis.com/), San Francisco.

I predicted the volume of rent petitions in San Francisco using the data freely available through [SF Open Data](https://data.sfgov.org/Housing-and-Buildings/Petitions-to-the-Rent-Board/6swy-cmkq). I used two different SARIMA models, each having their pros and cons. I also found that using linear regression on the San Francisco unemployment rate (available from [FRED Economic Research](https://fred.stlouisfed.org/series/CASANF0URN)) as a predictor enables me to obtain similar results as the SARIMA model.

The order of operations for the notebooks is as follows:

1. zip.ipynb - use to unzip all the data files
2. move-data-to-postgres.ipynb
3. eda-determine-sampling-rate.ipynb - use this to decide on grouping by month
4. eda-group-neighborhoods.ipynb
5. forecast-using-sarima.ipynb
6. forecast-using-linreg.ipynb

For more information, please read my [blog post](https://harrisonized.github.io/2019/06/25/sf-rent-petitions.html) and feel free to [email me](mailto:harrisonized@gmail.com) with any questions.
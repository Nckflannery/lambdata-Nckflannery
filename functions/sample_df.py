import pandas as pd
columns = ['Year', 'Name', 'YearName', 'College', 'POS', 'Height',
       'Weight', 'Hand Size', 'Arm Length', 'Wonderlic',
       '40 Yard', 'Bench Press', 'Vert Leap', 'Broad Jump',
       'Shuttle', '3Cone', '60Yd Shuttle', 'Pick', 'Round']

sample_df = pd.read_csv(r'C:\Users\Nick\Unit2Project\Attempt 2\Data\NFL Combine Data - Combine Results.csv', names=columns).drop(0)
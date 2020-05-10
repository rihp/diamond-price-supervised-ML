import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



def use_my_numeric_scales(df):
    """

                     Diamond G.I.A. Clarity Scale
                   Categories are not equi-distant 

    IF        VVS1   VVS2     VS1   VS2       SI1  SI2        I1
    |----------|-----|---------|-----|---------|----|-------------
    0                                                         10

    more info : https://4cs.gia.edu/en-us/diamond-clarity/
    """

    cleanup_nums = {"clarity":    {'IF':   0,

                                   'VVS1': 2.0, 'VVS2':2.5,

                                   'VS1':  3.1,  'VS2':3.6,

                                   'SI1':  6.0,  'SI2':6.5,

                                   'I1':   10,},

                    "cut": {'Ideal':0, 'Premium':1, 'Very Good':2,  'Good':3, 'Fair':4, },

                    "color": {'D':0, 'E':1, 'F':2, 'G':3,'H':4, 'I':5, 'J':6}
                   }
    df.replace(cleanup_nums, inplace=True)
    return df


def depth_qualifyer(depth):
    """

            Perfect depth (0) refracts more light, a bad depth lets the light escape.
                            Optimal depth is between 59 and 62

        |-------------------------------------------------------------------------|
    good_depth                                                               bad_depth

    """
    d = depth
    good_d = (59, 62)  # Recommended (55, 60) or (59,62)
    reg_d =  (54, 67)  # Arbitrary values  
    bad_d =  (49, 72)  # Arbitrary values  

    if                     (good_d[0] <= d <= good_d[1]):                   return 0.0     # Perfect depth, a lot of light is reflected
    elif   (reg_d[0] <= d < good_d[0])   or  (good_d[1] < d <= reg_d[1]):   return 0.2
    elif   (bad_d[0] <= d <  reg_d[0])   or  ( reg_d[1] < d <= bad_d[1]):   return 0.6        
    else:                                                                   return 2.0     # Bad depth ranges, a lot of light escapes

def to_numeric(df):
    """
    Drop all the non-numeric fields from an input dataframe
    """
    numeric_train_data = data.copy()
    
    for column, dtype in zip(numeric_train_data.columns, numeric_train_data.dtypes):
        if (dtype != 'float64') and (dtype != 'int64'):
            print(f"Dropping the column '{column}', with the dtype {dtype}")   
            numeric_train_data = numeric_train_data.drop(columns=column)
        
    return numeric_train_data

def corr_matrix(df):
    """ 
    Plot the correlation matrix of a pandas dataframe using seaborn
    """
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(8,8))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.8, center=0, annot=True,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})


def visualize_data(X, y):
    f,a = plt.subplots(1, len(X.columns), figsize=(20,4))
    f.tight_layout(pad=5)
    f.suptitle('Features distribution\n', size=16)

    for i, column in enumerate(X.columns):
        sns.scatterplot(X[column], y, ax=a[i])
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


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
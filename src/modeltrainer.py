###### Regression Models 
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVR, NuSVR, SVR
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.gaussian_process import GaussianProcessRegressor


"""
DATA: numfeats_qd
MODEL:  GradientBoostingRegressor(n_estimators=1100, random_state=1)
highest_score = 529.87134
"""
highest_score = 620.9804697290087 

models = {
    'linear_regression':LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None),
    'linearSVR': LinearSVR(),
    #'NuSVR':NuSVR,
    #'SVR':SVR(),
    "DecisionTreeRegressor":DecisionTreeRegressor(),
    "ExtraTreeRegressor":ExtraTreeRegressor(),
    #"GaussianProcessRegressor":GaussianProcessRegressor(),
    "GradientBoostingRegressor":GradientBoostingRegressor(),
    "GradientBoostingRegressorP":GradientBoostingRegressor(n_estimators=1000, random_state=1),
    "HistGradientBoostingRegressor":HistGradientBoostingRegressor(max_bins=255, loss='least_squares',
                                                                  max_iter=88,
                                                                  max_leaf_nodes=25,
                                                                  random_state=1,
                                                                  scoring="neg_root_mean_squared_error"),
    
}







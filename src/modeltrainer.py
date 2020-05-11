###### Regression Models 
from sklearn.linear_model import ElasticNet, LinearRegression, RidgeCV, LassoCV, BayesianRidge, HuberRegressor, TheilSenRegressor, Lars
from sklearn.svm import LinearSVR, NuSVR, SVR
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import GradientBoostingRegressor, HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.ensemble import BaggingRegressor, StackingRegressor, VotingRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor

"""
    ========================================== Tested Models ============================================

    Optimizing: RMSE
    
    =====================================================================================================

    DATA:         'numfeats_qd'
    MODEL:         GradientBoostingRegressor(n_estimators=1100, random_state=1)
        #RMSE    ~    529 ($)
        #RUNTIME ~ UNKOWN (min)

    ESTIMATORS_STACK =  [
        ('RandomForestRegressor', RandomForestRegressor()),
        ('HistGradientBoostingRegressor', HistGradientBoostingRegressor())
    ]

    'VotingRegressor':VotingRegressor(ESTIMATORS_STACK),
        #RMSE    ~ 540 ($)
        #RUNTIME ~  5 (min)

    'HistGradientBoostingRegressor':HistGradientBoostingRegressor(max_bins=255, loss='least_squares',
                                                                max_iter=88,   max_leaf_nodes=25,
                                                                random_state=1,
                                                                scoring="neg_root_mean_squared_error"),
        #RMSE    ~  540 ($)
        #RUNTIME ~    2 (min)
        
    "GradientBoostingRegressorP":GradientBoostingRegressor(n_estimators=1000, random_state=1),
        #RMSE    ~  540 ($)
        #RUNTIME ~   20 (min)

    'RandomForestRegressor':RandomForestRegressor(),
        #RMSE    ~  551 ($)
        #RUNTIME ~   4 (min)

    ======================================== Experimental Models ========================================
"""

highest_score = 530

ESTIMATORS_STACK =  [
    # to be used with StackingRegressor() estimator
    ('RandomForestRegressor', RandomForestRegressor()),
    ('HistGradientBoostingRegressor', HistGradientBoostingRegressor())
]


models = {

    'RandomForestRegressor':RandomForestRegressor(),
        #RMSE    ~  551 ($)
        #RUNTIME ~   4 (min)

    #'StackingRegressor':StackingRegressor(estimators=ESTIMATORS_STACK),
        #COMMENT: Can stack multiple estimators and generate a regression from it.
        #RMSE    ~  528 ($)
        #RUNTIME ~   30 (min)

    #'ARDRegression':ARDRegression(),                     
        #RMSE    ~ UNKOWN needs more RAM
        #RUNTIME ~ UNKOWN (min)

    #'AdaBoostRegressor':AdaBoostRegressor(),             
        #RMSE    ~ 1149 ($)
        #RUNTIME ~ UNKOWN(min)

    #'BayesianRidge':BayesianRidge(),
        #RMSE    ~ 1206 ($)
        #RUNTIME ~    0 (min)

    #"DecisionTreeRegressor":DecisionTreeRegressor(),
        #RMSE    ~   743 ($)
        #RUNTIME ~     0 (min)

    #"ExtraTreeRegressor":ExtraTreeRegressor(),
        #RMSE    ~   772 ($)
        #RUNTIME ~ UNKOWN(min)

    #"GaussianProcessRegressor":GaussianProcessRegressor(),
        #RMSE    ~ UNKOWN needs more RAM($)
        #RUNTIME ~ UNKOWN(min)

    #"GradientBoostingRegressor":GradientBoostingRegressor(),
        #RMSE    ~    623 ($)
        #RUNTIME ~ UNKOWN(min)

    #'HuberRegressor':HuberRegressor(),
        #RMSE    ~ 1289 ($)
        #RUNTIME ~ UNKOWN(min)

    #'IsotonicRegression': IsotonicRegression(),
        #COMMENT: for functions which are always increasing. works only with X as an 1d array
        #RMSE    ~ UNKOWN($)
        #RUNTIME ~ UNKOWN(min)

    #'KNeighborsRegressor':KNeighborsRegressor(),
        #RMSE    ~    748 ($)
        #RUNTIME ~ UNKOWN(min)

    #'LassoCV':LassoCV(),
        #RMSE    ~ 1185 ($)
        #RUNTIME ~    0 (min)

    #'Lars':Lars(),
        #RMSE    ~ 1244 ($)
        #RUNTIME ~ UNKOWN(min)

    #'linear_regression':LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None),
        #RMSE    ~ UNKOWN($)
        #RUNTIME ~ UNKOWN(min)
    
    #'linearSVR': LinearSVR(),                             
        #RMSE    ~ 1600 ($)
        #RUNTIME ~ UNKOWN(min)

    #'LinearSVRP':LinearSVR(random_state=42),
        #RMSE    ~ 1500 ($)
        #RUNTIME ~    1 (min)

    #'ElasticNet':ElasticNet(),
        #RMSE    ~ 1737 ($)
        #RUNTIME ~ UNKOWN(min)


    #'MultiTaskElasticNet':MultiTaskElasticNet(),
        #RMSE    ~ UNKOWN($)
        #RUNTIME ~ UNKOWN(min)

    #'MultiTaskLasso':MultiTaskLasso(),
        #RMSE    ~ UNKOWN($)
        #RUNTIME ~ UNKOWN(min)

    #'MLPRegressor': MLPRegressor(),
        #RMSE    ~ 991 ($)
        #RUNTIME ~ Takes more than 15 (min)

    #'NuSVR':NuSVR(), 
        #RMSE    ~ DOES NOT WORK!
        #RUNTIME ~ TAKES MORE THAN 15 MINUTES(min)
    
    #'RidgeCV':RidgeCV(),
        #RMSE    ~ 1149 ($)
        #RUNTIME ~    1 (min)

    #'SVR':SVR(),
        #RMSE    ~ UNKOWN($)
        #RUNTIME ~ TAKES MORE THAN 5 MINUTES

    #'TheilSenRegressor':TheilSenRegressor(),
        #RMSE    ~ 1540 ($)
        #RUNTIME ~ UNKOWN(min)

    #'VotingRegressor':VotingRegressor(ESTIMATORS_STACK),
        #RMSE    ~ 528 ($)
        #RUNTIME ~  5 (min)

}
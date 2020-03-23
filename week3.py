import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

df = None


def read_data():
    global df
    path = 'automobileEDA.csv'
    df = pd.read_csv(path)


def seaborn_correlation(x=None, y=None):
    global df
    # Engine size as potential predictor variable of price
    # sns.regplot(x="engine-size", y="price", data=df)
    sns.regplot(x=x, y=y, data=df)
    plt.ylim(0,)
    plt.show()


def seaborn_boxplot(x, y):
    sns.boxplot(x=x, y=y, data=df)
    plt.show()


def correlation_values(x=None, y=None):
    result = df[[x, y]].corr()
    # print(result)
    return result


def scipy_pearson_correlation(x, y):
    pearson_coef, p_value = stats.pearsonr(df[x], df[y])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)


def series_to_dataframe(column_name):
    print(df[column_name].value_counts().to_frame())
    drive_wheels_counts = df[column_name].value_counts().to_frame()
    drive_wheels_counts.rename(columns={column_name: 'value_counts'}, inplace=True)
    drive_wheels_counts.index.name = column_name
    print(drive_wheels_counts)


def group():
    df_group_one = df[['drive-wheels', 'body-style', 'price']]
    df_group_one = df_group_one.groupby(['body-style'], as_index=False).mean()

    print(df_group_one)


def group_by_heatmap():
    df_gptest = df[['drive-wheels', 'body-style', 'price']]
    grouped_test1 = df_gptest.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
    print(grouped_test1)
    grouped_pivot = grouped_test1.pivot(index='drive-wheels', columns='body-style')
    print(grouped_pivot)
    grouped_pivot = grouped_pivot.fillna(0)  # fill missing values with 0
    print(grouped_pivot)

    plt.pcolor(grouped_pivot, cmap='RdBu')
    plt.colorbar()
    plt.show()

    fig, ax = plt.subplots()
    im = ax.pcolor(grouped_pivot, cmap='RdBu')
    # label names
    row_labels = grouped_pivot.columns.levels[1]
    col_labels = grouped_pivot.index
    # move ticks and labels to the center
    ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)
    # insert labels
    ax.set_xticklabels(row_labels, minor=False)
    ax.set_yticklabels(col_labels, minor=False)
    # rotate label if too long
    plt.xticks(rotation=90)
    fig.colorbar(im)
    plt.show()


def scipy_anova():
    pass



if __name__ == '__main__':
    read_data()
    # # print(df.head())
    # x_axis = "body-style"
    x_axis = "drive-wheels"
    y_axis = "price"
    # seaborn_correlation(x_axis, y_axis)
    # print(correlation_values(x_axis, y_axis))
    # seaborn_boxplot(x_axis, y_axis)

    # print(df.describe())
    # print(df.describe(include=['object']))

    # scipy_pearson_correlation('horsepower', 'price')
    df_gptest = df[['drive-wheels', 'body-style', 'price']]

    grouped_test2 = df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
    print(grouped_test2.head(2))

    pass

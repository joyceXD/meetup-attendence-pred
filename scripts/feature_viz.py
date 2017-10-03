import matplotlib.pyplot as plt

def generate_plot(df_data, fn, var_names):
    for var_name in var_names:
        x_data = df_data[var_name].values
        y_data = df_data.e_total_attend.values
        plt.scatter(x_data, y_data, alpha=0.3)
        plt.title('Scatter plot {} vs. attendant number'.format(var_name))
        plt.xlabel(var_name)
        plt.ylabel('Total_attend')
        plt.savefig('../plot/plot_{}_{}.png'.format(fn, var_name))
        plt.clf()
        x_data = []
        y_data = []
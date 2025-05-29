def plot_numeric_metric_by_bucket(df, metric, title):
    """
    Plot a given metric across pitch buckets for multiple pitchers.

    Args:
        df (pd.DataFrame): The full raw data OR aggregated DataFrame
        metric (str): The metric column to plot
        title (str): Chart title
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='pitch_bucket', y=metric, hue='pitcher_name', ci=None)
    plt.title(title)
    plt.ylabel(metric.replace("_", " ").title())
    plt.xlabel('Pitch Count Bucket')
    plt.legend(title='Pitcher')
    plt.tight_layout()
    plt.show()

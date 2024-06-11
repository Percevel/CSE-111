import pandas as pd
import matplotlib.pyplot as pyplot

def main():
    df = pd.read_csv("water.csv")
    print(total_increasing_water_rex(df))
    avg_water_per_dwelling(df)

def total_increasing_water_rex(df):
    df['year'] = pd.DatetimeIndex(df['readDate']).year
    group = df.groupby("year")
    sum_df = group.aggregate(sumUsage=("usage","sum"))
    return sum_df

def avg_water_per_dwelling(df):
    filter = (df["accountType"] == "Apartment Complex") | \
            (df["accountType"] == "Residence") | \
            (df["accountType"] == "Trailer Court") | \
            (df["accountType"] == "Town Homes")
    df = df[filter]

    # For each meterNumber, compute the total water
    # usage and the number of dwellings grouped by year.
    group = df.groupby(["meterNumber", "year"])
    interm_df = group.aggregate(usage=("usage", "sum"),
            numberOfDwellings=("numberOfDwellings", "mean"))

    # Discard outliers: rows with numDwellings less than 1.
    filter = (interm_df["numberOfDwellings"] >= 1)
    interm_df = interm_df[filter]

    # For each year, compute the total water
    # usage and the total number of dwellings.
    group = interm_df.groupby("year")
    final_df = group.aggregate(sumUsage=("usage", "sum"),
            sumDwellings=("numberOfDwellings", "sum"))

    # Add a computed column that is sumUsage / numDwellings.
    final_df["usagePerDwelling"] = final_df["sumUsage"] / final_df["sumDwellings"]

    pd.options.display.float_format = "{:.1f}".format
    print()
    print("Average usage per dwelling (in 1000 gallons):")
    print(final_df)

    barplot = final_df.plot(kind="bar", y="usagePerDwelling",
            title="Average Usage per Dwelling", legend=None)
    barplot.set_xlabel("")
    barplot.set_ylabel("x1000 gallons")

    # Call the pyplot.tight_layout function, which will format the
    # previously defined plot so that all of its parts are spaced
    # nicely. Strangely, pyplot.tight_layout must be called multiple
    # times, once for each defined plot, but pyplot.show needs to be
    # called only once.
    pyplot.show()
main()
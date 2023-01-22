import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/data", methods=["POST"])
def data_quality():
    # read in data from request
    data = request.get_json()

    # convert json data to a pandas dataframe
    df = pd.DataFrame(data)
    # check for accuracy by comparing double entries
    df["double_entry"] = df[["field1", "field2"]].apply(
        lambda x: x[0] == x[1], axis=1)

    # check for completeness by checking for missing values
    df["completeness"] = df.isnull().sum()

    # ensure consistency by standardizing data
    df["field1"] = df["field1"].str.upper()
    df["field2"] = df["field2"].round(2)

    # ensure currency by checking the last modified date
    df["currency"] = pd.to_datetime(df["last_modified"], errors='coerce')

    # ensure relevance by filtering data
    df = df[df["field3"] > 0]

    # ensure uniqueness by dropping duplicate records
    df.drop_duplicates(subset=["field1", "field2"], inplace=True)

    # ensure validity by checking for data within a certain range
    df = df[(df["field4"] >= 0) & (df["field4"] <= 100)]

    # return processed data
    return jsonify(df.to_dict())


if __name__ == "__main__":
    app.run(debug=True)

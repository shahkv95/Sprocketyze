{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "KPMG_Virtual_exp_Module2.ipynb",
      "provenance": [],
      "private_outputs": true,
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "zsSAiK7zkKQM"
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "import seaborn as sns\n",
        "import pandas_profiling \n",
        "from pandas_profiling import ProfileReport"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MmRYVei3nc5p"
      },
      "source": [
        "from google.colab import files\n",
        "\n",
        "uploaded = files.upload()\n",
        "\n",
        "for fn in uploaded.keys():\n",
        "  print('User uploaded file \"{name}\" with length {length} bytes'.format(\n",
        "      name=fn, length=len(uploaded[fn])))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2paVntoEkKJd"
      },
      "source": [
        "filename = \"/content/Module_2_file.xlsx\"\n",
        "df = pd.read_excel(filename)\n",
        "df.head()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s2o-4zwckKGV"
      },
      "source": [
        "df.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C2I8-fsjkKDe"
      },
      "source": [
        "df.columns"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "44jy_QZ4kKAc"
      },
      "source": [
        "# Printing the columns with heading Unnamed"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5pBaq9LGkJ9G"
      },
      "source": [
        "df.drop(df.columns[df.shape[1] - 7 : df.shape[1] - 2], axis =1, inplace=True)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XM4hyIJEACuV"
      },
      "source": [
        "df.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bg7HwbMzACq_"
      },
      "source": [
        "df.head()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WwVKp66yANIZ"
      },
      "source": [
        "df.columns"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8_Tvpa99ANFX"
      },
      "source": [
        "df.dtypes"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CnxAc23dANCQ"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "l92jBr94Imtl"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hAHSwEeSImqC"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7J7pNY-4ImnD"
      },
      "source": [
        "df.drop(['first_name', 'last_name'], axis =1, inplace=True)\n",
        "df.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "itWyA3c7Imjk"
      },
      "source": [
        "df.drop(['deceased_indicator'], axis =1, inplace=True)\n",
        "df.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3FVDvLs7MNIb"
      },
      "source": [
        "df.drop(['country'], axis =1, inplace=True)\n",
        "df.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_SPJaFg7MpKV"
      },
      "source": [
        "df.rename(columns={\"past_3_years_bike_related_purchases\": \"purchases\"}, inplace = True)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vO3Vs6iWAM--"
      },
      "source": [
        "df.nunique()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yX5VxiiOqBWb"
      },
      "source": [
        "df.isnull().sum()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OSE4MYlXAXU1"
      },
      "source": [
        "df['gender'].nunique()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lP0ZAsH1AXRo"
      },
      "source": [
        "df['gender'].unique()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EjJpmzoSAXOu"
      },
      "source": [
        "df['gender'].value_counts()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "v2YAZC4eAXLf"
      },
      "source": [
        "# All the 17 records with missing DOBs\n",
        "df[df.DOB.isnull()]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9p-mmf9PAXIs"
      },
      "source": [
        "# Total number of records with gender as U \n",
        "df[df.DOB.isnull()]['gender'].value_counts()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pfo9_ADxKN48"
      },
      "source": [
        "# These means that there are 17 records with gender == U and in which the DOBs are missing"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PlZ6zyhNKN1l"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IZQ2zoeqKNyN"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nIYPFkY3AXF0"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kE8oxHcWAXCX"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BKwG7rPkqBTR"
      },
      "source": [
        "plt.figure(figsize = (10,7))\n",
        "sns.heatmap(df.corr(), annot = True)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wbFD9jcCqBQY"
      },
      "source": [
        "sns.heatmap(df.isnull())"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iQ3LTu92qBNS"
      },
      "source": [
        "sns.factorplot('gender','purchases',data=df)\n",
        "plt.ioff()\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9OAIUMGbqBKM"
      },
      "source": [
        "df.groupby('gender')['purchases'].sum()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ThjpBRfWUeyd"
      },
      "source": [
        "df.groupby('gender')['purchases'].sum().values.sum() # Total 49836 purchases were made in last 3 years"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4_1SSSIzN6q_"
      },
      "source": [
        "df.state.unique()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BxB3rNmQN6nc"
      },
      "source": [
        "df.nunique()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s55ACg92P5_3"
      },
      "source": [
        "df.dtypes"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iCJcAzfJPh-Y"
      },
      "source": [
        "!pip install plotly==4.5.2"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OtvtY4r3N6kt"
      },
      "source": [
        "import plotly.express as px "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SUfJzlq_N6g0"
      },
      "source": [
        "plt.figure(figsize = (15,10))\n",
        "fig = px.sunburst(df, path=['state', 'gender', 'wealth_segment'], values='Age', color='state',\n",
        "                  color_discrete_map={'QLD':'blue', 'NSW':'green', 'VIC':'red' }, title = \"Purchases made in last 3 years\")\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rWZpiKrvN6dd"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BrZCnaNBN6aE"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3Z_uzScxN6Mo"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FObfn4S9qBHJ"
      },
      "source": [
        "summary = pd.concat([pd.crosstab(df[x], df.wealth_segment) for x in df.columns[:-1]], keys=df.columns[:-1])\n",
        "summary"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kbD6-x7uqBD0"
      },
      "source": [
        "# summary['Churn_Percentage'] = summary['Yes'] / (summary['No'] + summary['Yes'])\n",
        "# summary"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7I64ztPVqBAz"
      },
      "source": [
        "plt.figure(figsize = (15,10))\n",
        "fig = px.sunburst(df, path=['gender', 'wealth_segment', 'owns_car'], values='purchases', color='gender',\n",
        "                  color_discrete_map={'Male':'blue', 'Female':'green', 'U':'red' }, title = \"Owns a car or not\")\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MZV4VytyqA9a"
      },
      "source": [
        "df.gender.unique()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JFa2ahRTqA7H"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZwSUjssiqA3z"
      },
      "source": [
        "df_female = df.query(\"gender == 'Female'\")\n",
        "fig = px.bar(df, x='wealth_segment', y='purchases',\n",
        "             hover_data=['job_industry_category', 'owns_car', 'Age', 'state'], color='owns_car',\n",
        "             labels={'purchases':'Purchases_made_within_last_3_years'}, height=500, title = \"Purchases made within last 3 years\")\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "y01te_82qA0o"
      },
      "source": [
        "df.columns"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F1UYuyzmkJ6A"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8WF0_IJ0kJ29"
      },
      "source": [
        "# df.hist(columns = 'Age', bins = 10)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mljuKr2-kJz5"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e9myMz62kJwF"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0DG3Sy-KkJsk"
      },
      "source": [
        "#df_india = gm.query(\"country == 'India'\")\n",
        "fig = px.bar(df, x='Age', y='Value',\n",
        "             hover_data=['Age'], height=450, title = \"Age distribution\", color = 'tenure')\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EZwR5_S7WDhr"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sw00EOA-WDf6"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iwUY_V3WWDbf"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "irge7MPQWDZz"
      },
      "source": [
        "import plotly.graph_objects as go\n",
        "\n",
        "\n",
        "fig1 = go.Figure([go.Bar(x=df.gender.unique(), y=df['gender'].value_counts())])\n",
        "fig1.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VyuL1DxzWDVB"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "txE8t3PlWDSg"
      },
      "source": [
        "fig2 = go.Figure([go.Bar(x=df.job_industry_category.unique(), y=df['job_industry_category'].value_counts())])\n",
        "fig2.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CES6wPWWWDOm"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BthR39APWDMg"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NyCLe4FJWDHj"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Qcrqa5BKWC_h"
      },
      "source": [
        "\n",
        "\n",
        "\n",
        "fig3 = go.Figure(data=[\n",
        "    go.Bar(x=df.job_industry_category.unique(), y=df['job_industry_category'].value_counts()),\n",
        "    go.Bar(x=df.gender.unique(), y=df['gender'].value_counts())\n",
        "])\n",
        "# Change the bar mode\n",
        "fig3.update_layout(barmode='group')\n",
        "fig3.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xJj6DOeXWC7o"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ru63VjjgWC42"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GraJMn5oa7t5"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xOjm7rB9a7p7"
      },
      "source": [
        "fig4 = go.Figure([go.Bar(x=df.groupby('gender').job_industry_category.unique(), y=df.groupby('gender')['job_industry_category'].value_counts())])\n",
        "fig4.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5HUKdV2xa7n_"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vX66rLfya7i1"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Gdk6UvrFa7f1"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hUUjemgha7bN"
      },
      "source": [
        "\n",
        "\n",
        "fig5 = go.Figure()\n",
        "fig5.add_trace(go.Bar(\n",
        "    x=df.job_industry_category.unique(),\n",
        "    y=df['job_industry_category'].value_counts(),\n",
        "  \n",
        "    marker_color='indianred'\n",
        "))\n",
        "fig5.add_trace(go.Bar(\n",
        "    x=df.job_industry_category.unique(),\n",
        "    y=df['gender'].value_counts(),\n",
        "    \n",
        "    marker_color='lightsalmon'\n",
        "))\n",
        "\n",
        "# Here we modify the tickangle of the xaxis, resulting in rotated labels.\n",
        "fig5.update_layout(barmode='group', xaxis_tickangle=-45)\n",
        "fig5.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aCBdbLWNbnQJ"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ByenEBN6bnLs"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "chlbjGqAbnJt"
      },
      "source": [
        "df_female = df.query(\"gender == 'Female'\")\n",
        "df_Male = df.query(\"gender == 'Male'\")\n",
        "df_U = df.query(\"gender == 'U'\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZjfCoprMeO9D"
      },
      "source": [
        "df_female.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i_zGyCS1fFKg"
      },
      "source": [
        "grp_fgender_df = df_female.groupby('job_industry_category')['purchases']\n",
        "grp_mgender_df = df_Male.groupby('job_industry_category')['purchases']\n",
        "grp_ugender_df = df_U.groupby('job_industry_category')['purchases']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "g956Gk3tfakd"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "65quQ5r6faf0"
      },
      "source": [
        "# result_df = pd.concat([grp_fgender_df, grp_mgender_df, grp_ugender_df], axis=1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F5Sb2v6xfad5"
      },
      "source": [
        "############## Task ro join above three series into one dataframe"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0CMQOi2AfacH"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yi_FBUj7faVb"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fHz03wV9faSW"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6hPZyY7nfaOO"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-WdfJIw4bnFL"
      },
      "source": [
        "# years = df.job_industry_category.unique()\n",
        "\n",
        "# fig6 = go.Figure()\n",
        "# fig6.add_trace(go.Bar(x=years,\n",
        "#                 y=df_Male.shape[0],\n",
        "#                 name='Male'\n",
        "                \n",
        "#                 ))\n",
        "# fig6.add_trace(go.Bar(x=years,\n",
        "#                 y=df_female.shape[0],\n",
        "#                 name='Rest of world'\n",
        "                \n",
        "#                 ))\n",
        "# fig6.add_trace(go.Bar(x=years,\n",
        "#                 y=df_U.shape[0],\n",
        "#                 name='China'\n",
        "                \n",
        "#                 ))\n",
        "\n",
        "# fig6.update_layout(\n",
        "#     title='Distribution of Industry sectors with internal dist of gender',\n",
        "#     xaxis_tickfont_size=14,\n",
        "#     yaxis=dict(\n",
        "#         title='USD (millions)',\n",
        "#         titlefont_size=16,\n",
        "#         tickfont_size=14,\n",
        "#     ),\n",
        "#     legend=dict(\n",
        "#         x=0,\n",
        "#         y=1.0,\n",
        "#         bgcolor='rgba(255, 255, 255, 0)',\n",
        "#         bordercolor='rgba(255, 255, 255, 0)'\n",
        "#     ),\n",
        "#     barmode='group',\n",
        "#     bargap=0.15, # gap between bars of adjacent location coordinates.\n",
        "#     bargroupgap=0.1 # gap between bars of the same location coordinate.\n",
        "# )\n",
        "# fig6.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HaNWTUCPbnBq"
      },
      "source": [
        "# https://plotly.com/python/bar-charts/#customizing-individual-bar-widths\n",
        "# For References"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R6htM4mOa7YZ"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9TI5mmOUa7Tm"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GDbCH8WJa7Pg"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pk7fozp-WC0y"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_1tgxLXOWCxN"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cN23F0Lrj6ex"
      },
      "source": [
        "# from datetime import datetime\n",
        "# from datetime import date\n",
        "\n",
        "# def calculate_age(born):\n",
        "#     born = datetime.strptime(born, \"%d.%m.%Y\").date()\n",
        "#     today = date.today()\n",
        "#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))\n",
        "\n",
        "# df['age'] = calculate_age(df['DOB'])\n",
        "# print(df)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qVThoh-vpX-5"
      },
      "source": [
        "# from datetime import datetime\n",
        "# from datetime import date\n",
        "# date.today()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_-9r3WhOBOm8"
      },
      "source": [
        "# for i in range(df.shape[0]):\n",
        "#   df['age'] = df.DOB - date.today()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LEgpNj1EBevX"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2PYa1QB5hPLS"
      },
      "source": [
        "# https://www.kaggle.com/kushshah95/global-gapminder-data-extreme-eda-part-1\n",
        "\n",
        "# https://plotly.com/python/bar-charts/#customizing-individual-bar-widths\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "47OFQQkIhlLJ"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}

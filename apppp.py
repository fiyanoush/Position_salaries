from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # -*- coding: utf-8 -*-
        """Postion_Salaries.xlsx
        Automatically generated by Colaboratory.
        Original file is located at
            https://colab.research.google.com/drive/1gVbxdExLPXNIrJY8kTpzxS6wUjKx9An3
        """

        import os

        import pandas as pd
        import numpy as np
        dataset = pd.read_csv("Student_Marks.csv")

        x = dataset.iloc[:, :-1]

        y = dataset.iloc[:, 2]

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=0)

        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        y_pred = regressor.predict(X_test)

        input1 = request.form.get("subjects")
        input2 = request.form.get("time")

        Xnew = [[input1],[input2]]

        result = regressor.predict(Xnew)

        value = result.tolist()


        # getting input

        final="The Predicted score for the student is" + str(value[0])




        return final

    return render_template("form.html")

if __name__=='__main__':
   app.run()

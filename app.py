{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled22.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM84/MdLzUZtkrufDDJNeIH"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "ONB5YVEv7gio"
      },
      "source": [
        "import numpy as np\n",
        "from flask import Flask, request, jsonify, render_template\n",
        "import pickle"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0zgTvo6V7k_X"
      },
      "source": [
        "app = Flask(__name__)\n",
        "model = pickle.load(open('model.pkl', 'rb'))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YioTi7IT7t49"
      },
      "source": [
        "@app.route('/')\n",
        "def home():\n",
        "    return render_template('sample.html')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jITK0Q3zBmMm"
      },
      "source": [
        "@app.route('/predict',methods=['POST'])\n",
        "def predict():\n",
        "    '''\n",
        "    For rendering results on HTML GUI\n",
        "    '''\n",
        "    if request.method == 'POST':\n",
        "        sqft = int(request.form['sqft'])\n",
        "        bath = int(request.form['bathrooms'])\n",
        "        bhk = int(request.form['bedrooms'])\n",
        "        location = request.form['location']\n",
        "\n",
        "        model_list = [sqft, bath, bhk, location]\n",
        "        x_col = X.columns\n",
        "        model_input = []\n",
        "\n",
        "        model_input.append(model_list[0])\n",
        "        model_input.append(model_list[1])\n",
        "        model_input.append(model_list[2])\n",
        "        for col in X[x_col[3:]]:\n",
        "          if X[[col]].columns == model_list[3]:\n",
        "            model_input.append(1)\n",
        "          else:\n",
        "            model_input.append(0)\n",
        "        data = np.array([model_input])\n",
        "        my_prediction = model.predict(data)\n",
        "        output = round(my_prediction[0], 3)\n",
        "\n",
        "    return render_template('sample.html', prediction_text='Price of the property would be around $ {}'.format(output))\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vSiOqPULBrpb"
      },
      "source": [
        "if __name__ == \"__main__\":\n",
        "    app.run(debug=True)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
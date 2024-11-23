from flask import Flask, request, jsonify
import pandas as pd
import os
from threading import Thread
from tkinter import Tk
from nse_oc_analyser import Nse

app = Flask(__name__)

# Directory where CSV files are stored
DATA_DIR = "bar_data"

# Helper function to get data
def get_bar_data(symbol, timeframe):
    file_path = os.path.join(DATA_DIR, f"{symbol}_{timeframe}.csv")
    if not os.path.exists(file_path):
        return None  # Return None if data doesn't exist
    return pd.read_csv(file_path)

@app.route('/api/get-chart-data', methods=['GET'])
def get_chart_data():
    """
    Endpoint to fetch chart data for a given symbol and timeframe.
    """
    symbol = request.args.get('symbol')
    timeframe = request.args.get('timeframe')

    if not symbol or not timeframe:
        return jsonify({'error': 'Missing symbol or timeframe parameter'}), 400

    data = get_bar_data(symbol, timeframe)
    if data is None:
        return jsonify({'error': f'No data found for {symbol} with {timeframe} timeframe'}), 404

    # Return the data as JSON
    return jsonify(data.to_dict(orient='records'))

def calculate_sma(df, period=50):
    if 'close' not in df.columns:
        return None
    sma = df['close'].rolling(window=period).mean()
    return pd.DataFrame({
        'time': df['date'],
        f'SMA {period}': sma
    }).dropna()

@app.route('/api/get-sma', methods=['GET'])
def get_sma():
    """
    Endpoint to calculate and return the SMA for a given stock symbol, timeframe, and period.
    """
    symbol = request.args.get('symbol')
    timeframe = request.args.get('timeframe')
    period = int(request.args.get('period', 50))  # Default to 50 if period not provided

    if not symbol or not timeframe:
        return jsonify({'error': 'Missing symbol or timeframe parameter'}), 400

    data = get_bar_data(symbol, timeframe)
    if data is None:
        return jsonify({'error': f'No data found for {symbol} with {timeframe} timeframe'}), 404

    sma_data = calculate_sma(data, period)
    if sma_data is None:
        return jsonify({'error': 'Unable to calculate SMA. Ensure the data has a "close" column.'}), 400

    return jsonify(sma_data.to_dict(orient='records'))

@app.route('/launch-tkinter', methods=['GET'])
def launch_tkinter():
    def run_tkinter():
        master_window = Tk()
        Nse(master_window)
        master_window.mainloop()

    # Run Tkinter in a separate thread to avoid blocking Flask
    Thread(target=run_tkinter).start()
    return {"message": "Tkinter application launched successfully"}



if __name__ == '__main__':
    app.run(debug=True)
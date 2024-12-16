from prophet import Prophet
import pandas as pd

dataFrame = pd.read_csv("data_example.csv")
print(dataFrame.head())
# data["ds"] = data["timestamp"]
# data["y"] = data["value"]

model = Prophet()
model.fit(dataFrame)

# Make future predictions
future = model.make_future_dataframe(
    periods=365, include_history=True
)  # Forecasting for 1 year
print(future.tail())
forecast = model.predict(future)
print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())

# Plot the forecast
fig1 = model.plot(forecast)

import plotly.graph_objects as go

# Create a Plotly figure
fig = go.Figure()

# Add actual data
fig.add_trace(
    go.Scatter(x=dataFrame["ds"], y=dataFrame["y"], mode="lines", name="Actual")
)

# Add forecast data
fig.add_trace(
    go.Scatter(x=forecast["ds"], y=forecast["yhat"], mode="lines", name="Forecast")
)

# Add uncertainty interval
fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat_upper"],
        mode="lines",
        line=dict(width=0),
        showlegend=False,
    )
)
fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat_lower"],
        mode="lines",
        fill="tonexty",
        fillcolor="rgba(0,100,80,0.2)",
        line=dict(width=0),
        name="Uncertainty",
    )
)

# Show the figure
fig.show()

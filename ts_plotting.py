"""
Custom time series plotting functions implemented in plotly.
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go

def plot_time_series(
    training_data: pd.DataFrame,
    test_data: pd.DataFrame | None = None,
    forecast: pd.DataFrame | None = None,
    test_data_mode: str = "markers",
    y_axis_label: str = "Value",
    color_dict: dict | None = None,
) -> None:
    """
    Plots univariate time series data using Plotly. Options for displaying
    training, test, and

    Parameters:
    ----------
    training_data: pd.DataFrame
        A pandas DataFrame with a DatetimeIndex containing the training data
        It should have one column representing the time series values.

    test_data: pd.DataFrame, optional (default=None)
        A pandas DataFrame with a DatetimeIndex containing the test data.
        Displayed as black dots or a line based on `test_data_mode`.

    forecast: pd.DataFrame, optional (default=None)
        A pandas DataFrame with a DatetimeIndex containing the forecasted data.

    test_data_mode: str, optional (default='markers')
        Mode for displaying test data.
        Options are 'markers' (dots) or 'lines' (line).

    y_axis_label: str, optional (default='Value')
        The quantity measured by the time series to display on the y-axis

    color_dict: dict, optional (default=None)
        Dictionary with color codes for 'training', 'test', and 'forecast'.

    Returns:
        None: Displays an interactive Plotly figure.
    """
    # Validate test_data_mode input
    if test_data_mode not in ["markers", "lines"]:
        raise ValueError(
            "Invalid value for test_data_mode. Choose 'markers' or 'lines'."
        )

    if color_dict is None:
        color_dict = {
            "training": "#0072B2",  # Default blue color for training data
            "test": "#000000",  # Default black color for test data
            "forecast": "#FF0000",  # Default red color for forecast data
        }

    # Create a Plotly figure
    fig = go.Figure()

    # Add training data as a line plot
    fig.add_trace(
        go.Scatter(
            x=training_data.index,
            y=training_data.iloc[:, 0],
            mode="lines",
            name="Training Data",
            line=dict(color=color_dict["training"]),
        )
    )

    # Add test data based on the selected mode
    if test_data is not None:
        fig.add_trace(
            go.Scatter(
                x=test_data.index,
                y=test_data.iloc[:, 0],
                mode=test_data_mode,
                name="Test Data",
                marker=(
                    dict(color=color_dict["test"], size=6)
                    if test_data_mode == "markers"
                    else None
                ),
                line=(
                    dict(color=color_dict["test"])
                    if test_data_mode == "lines"
                    else None
                ),
            )
        )

    # Add forecast data as a line plot if provided
    if forecast is not None:
        fig.add_trace(
            go.Scatter(
                x=forecast.index,
                y=forecast.iloc[:, 0],
                mode="lines",
                name="Point Forecast",
                line=dict(
                    color=color_dict["forecast"], dash="dash"
                ),  # Dashed red line for forecast
            )
        )

    # Enable vertical spike lines on hover
    fig.update_layout(
        title="Univariate Time Series Visualization",
        xaxis=dict(
            showspikes=True,  # Enable spikes
            spikemode="across",  # Spike spans across all traces
            spikesnap="cursor",  # Spike snaps to cursor position
            spikedash="dot",  # Style of spike line
            spikethickness=1.5,  # Thickness of spike line
            spikecolor="gray",  # Color of spike line
        ),
        yaxis=dict(showspikes=False),  # Disable horizontal spikes
        hovermode="x",  # Hover closest to x-axis value
        template="plotly_white",
        xaxis_title="Date",
        yaxis_title=y_axis_label,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    # Show the figure
    fig.show()




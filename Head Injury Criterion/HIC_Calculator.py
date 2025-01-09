import os
import csv
import math
from typing import Dict, Tuple
from scipy.signal import butter, lfilter
import argparse

class HICCalculator:
    def __init__(self, frequency: float, cutoff: float = 1650.0, order: int = 2):
        self.frequency = frequency
        self.cutoff = cutoff
        self.order = order

    def butter_lowpass(self):
        """
        Creates a Butterworth low-pass filter.

        Returns:
            Tuple: Filter coefficients (b, a).
        """
        nyquist = 0.5 / self.frequency  # Nyquist Frequency
        normal_cutoff = self.cutoff / nyquist  # Normalized cutoff frequency
        b, a = butter(self.order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_lowpass_filter(self, data):
        """
        Applies a Butterworth low-pass filter to the data.

        Args:
            data (list): The data to filter.

        Returns:
            list: Filtered data.
        """
        b, a = self.butter_lowpass()
        return lfilter(b, a, data)

    def get_file(self, file_path: str) -> str:
        """
        Returns the path to the CSV file.
        """
        return file_path.replace(os.sep, os.path.sep)

    def get_data(self, path: str, x_location: int, y_location: int, z_location: int) -> Dict[int, Tuple[float, float]]:
        """
        Reads acceleration data from a CSV file and calculates the magnitude for each time step.

        Args:
            path (str): Path to the input CSV file.
            x_location (int): Column index for X direction data.
            y_location (int): Column index for Y direction data.
            z_location (int): Column index for Z direction data.

        Returns:
            Dict[int, Tuple[float, float]]: A dictionary with time step as the key and a tuple of time and magnitude.
        """
        head_acceleration = {}

        with open(path, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row

            for i, line in enumerate(reader):
                data = list(map(float, line))
                time = round(i * self.frequency, 5)
                magnitude = math.sqrt(data[x_location - 1]**2 + data[y_location - 1]**2 + data[z_location - 1]**2) / 9810
                head_acceleration[i] = (time, magnitude)

        # Filter the magnitude data
        magnitudes = [value[1] for value in head_acceleration.values()]
        filtered_magnitudes = self.butter_lowpass_filter(magnitudes)

        for i, (time, _) in enumerate(head_acceleration.values()):
            head_acceleration[i] = (time, filtered_magnitudes[i])

        return head_acceleration

    def calculate_hic(self, acceleration: Dict[int, Tuple[float, float]], hic_ms: float) -> Tuple[str, float]:
        """
        Calculates the Head Injury Criterion (HIC) over various time windows.

        Args:
            acceleration (Dict[int, Tuple[float, float]]): Acceleration data with time and magnitude.
            hic_ms (float): Time window for HIC calculation in milliseconds.

        Returns:
            Tuple[str, float]: The time window and the maximum HIC value.
        """
        hic_s = hic_ms / 1000
        hic_window = int(hic_ms / (self.frequency * 1000))

        areas = [
            0.5 * self.frequency * (acceleration[i][1] + acceleration[i + 1][1])
            for i in range(len(acceleration) - 1)
        ]

        hic_values = {}
        for i in range(len(areas) - hic_window):
            integral = sum(areas[i:i + hic_window])
            hic_value = (integral / hic_s) ** 2.5 * hic_s
            hic_values[f"{i / 100}:{(i + hic_window) / 100}"] = hic_value

        max_window = max(hic_values, key=hic_values.get)
        return max_window, round(hic_values[max_window])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HIC Calculation Script")
    parser.add_argument("--frequency", type=float, required=True, help="Sampling frequency (e.g., 0.00001)")
    parser.add_argument("--file_path", type=str, required=True, help="Path to the CSV file")
    parser.add_argument("--x_location", type=int, required=True, help="Column index for X direction data")
    parser.add_argument("--y_location", type=int, required=True, help="Column index for Y direction data")
    parser.add_argument("--z_location", type=int, required=True, help="Column index for Z direction data")

    args = parser.parse_args()

    hic_calculator = HICCalculator(args.frequency)
    data_file = hic_calculator.get_file(args.file_path)
    acceleration_data = hic_calculator.get_data(data_file, args.x_location, args.y_location, args.z_location)

    hic_values = {}
    hic_window_limit = args.frequency

    while hic_window_limit < 0.015:
        hic_ms = round(hic_window_limit * 1000, 2)
        time_window, hic_value = hic_calculator.calculate_hic(acceleration_data, hic_ms)
        hic_values[time_window] = hic_value
        hic_window_limit += args.frequency

    max_hic_value = max(hic_values.values())
    max_hic_window = max(hic_values, key=hic_values.get)
    
    #print(max_hic_value)
    print(f'The HIC 15 value is {max_hic_value} and was achieved between the time window of {max_hic_window}')

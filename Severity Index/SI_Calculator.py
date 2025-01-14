import os
import csv
import math
import numpy as np
from scipy.signal import butter, lfilter
import argparse
from typing import Dict, Tuple, List


class SICalculator:
    def __init__(self, frequency: float, cutoff: float = 1650.0, order: int = 2):
        self.frequency = frequency
        self.cutoff = cutoff
        self.order = order

    def butter_lowpass(self):
        """
        Creates Butterworth low-pass filter coefficients.

        Returns:
            Tuple: Filter coefficients (b, a).
        """
        nyquist = 0.5 / self.frequency
        normal_cutoff = self.cutoff / nyquist
        return butter(self.order, normal_cutoff, btype='low', analog=False)

    def butter_lowpass_filter(self, data: List[float]) -> np.ndarray:
        """
        Applies a Butterworth low-pass filter to the data.

        Args:
            data (List[float]): The data to filter.

        Returns:
            np.ndarray: Filtered data.
        """
        b, a = self.butter_lowpass()
        return lfilter(b, a, data)

    @staticmethod
    def read_csv(path: str) -> List[List[float]]:
        """
        Reads a CSV file and returns the content as a list of lists.

        Args:
            path (str): Path to the CSV file.

        Returns:
            List[List[float]]: Parsed CSV data.
        """
        try:
            with open(path, "r") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                return [list(map(float, row)) for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
        except Exception as e:
            raise RuntimeError(f"Error reading file {path}: {e}")

    def calculate_magnitudes(self, data: List[List[float]], x_idx: int, y_idx: int, z_idx: int) -> np.ndarray:
        """
        Calculates the magnitude of acceleration from x, y, and z components.

        Args:
            data (List[List[float]]): Acceleration data.
            x_idx (int): Column index for X data.
            y_idx (int): Column index for Y data.
            z_idx (int): Column index for Z data.

        Returns:
            np.ndarray: Array of magnitudes.
        """

        data_array = np.array(data)
        magnitudes = np.sqrt(data_array[:, x_idx - 1] ** 2 + 
                             data_array[:, y_idx - 1] ** 2 + 
                             data_array[:, z_idx - 1] ** 2 ) / 9810  # Convert to g
        return magnitudes

    def calculate_si(self, time_steps: np.ndarray, magnitudes: np.ndarray) -> float:
        """
        Calculates the Severity Index (SI).

        Args:
            time_steps (np.ndarray): Array of time steps.
            magnitudes (np.ndarray): Array of filtered magnitudes.

        Returns:
            float: SI value.
        """
        magnitudes_power = magnitudes ** 2.5
        si = np.trapezoid(magnitudes_power, dx=time_steps[1] - time_steps[0])
        return si

    def process_file(self, file_path: str, x_idx: int, y_idx: int, z_idx: int) -> float:
        """
        Reads a CSV file, processes the data, and calculates the SI.

        Args:
            file_path (str): Path to the CSV file.
            x_idx (int): X column index.
            y_idx (int): Y column index.
            z_idx (int): Z column index.

        Returns:
            float: SI value.
        """
        # Read and process data
        data = self.read_csv(file_path)
        magnitudes = self.calculate_magnitudes(data, x_idx, y_idx, z_idx)

        # Create time steps
        time_steps = np.arange(0, len(magnitudes) * self.frequency, self.frequency)

        # Filter data
        filtered_magnitudes = self.butter_lowpass_filter(magnitudes)

        # Calculate SI
        return self.calculate_si(time_steps, filtered_magnitudes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Severity Index Calculation Script")
    parser.add_argument("--frequency", type=float, required=True, help="Sampling frequency (e.g., 0.00001)")
    parser.add_argument("--file_path", type=str, required=True, help="Path to the CSV file")
    parser.add_argument("--x_location", type=int, required=True, help="Column index for X direction data")
    parser.add_argument("--y_location", type=int, required=True, help="Column index for Y direction data")
    parser.add_argument("--z_location", type=int, required=True, help="Column index for Z direction data")

    args = parser.parse_args()

    si_calculator = SICalculator(args.frequency)
    si_value = si_calculator.process_file(args.file_path, args.x_location, args.y_location, args.z_location)
    print(f"The SI value is {si_value:.2f}")

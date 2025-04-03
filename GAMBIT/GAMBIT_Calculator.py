import os
import csv
import numpy as np
from scipy.signal import butter, lfilter
import argparse

class GambitCalculator:
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

    def butter_lowpass_filter(self, data: np.ndarray) -> np.ndarray:
        """
        Applies a Butterworth low-pass filter to the data.

        Args:
            data (np.ndarray): The data to filter.

        Returns:
            np.ndarray: Filtered data.
        """
        b, a = self.butter_lowpass()
        return lfilter(b, a, data)

    @staticmethod
    def read_csv(path: str) -> np.ndarray:
        """
        Reads a CSV file and returns the content as a numpy array.

        Args:
            path (str): Path to the CSV file.

        Returns:
            np.ndarray: Parsed CSV data.
        """
        try:
            with open(path, "r") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                return np.array([list(map(float, row)) for row in reader])
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
        except Exception as e:
            raise RuntimeError(f"Error reading file {path}: {e}")

    def calculate_magnitudes(self, data: np.ndarray, x_idx: int, y_idx: int, z_idx: int) -> np.ndarray:
        """
        Calculates the magnitude of acceleration from x, y, and z components.

        Args:
            data (np.ndarray): Acceleration data.
            x_idx (int): Column index for X data.
            y_idx (int): Column index for Y data.
            z_idx (int): Column index for Z data.

        Returns:
            np.ndarray: Array of magnitudes.
        """
        magnitudes = np.sqrt(data[:, x_idx - 1] ** 2 + 
                             data[:, y_idx - 1] ** 2 + 
                             data[:, z_idx - 1] ** 2) / 9810  # Convert to G
        return magnitudes

    def calculate_gambit(self, translational_acc: np.ndarray, rotational_acc: np.ndarray) -> float:
        """
        Calculates the GAMBIT Injury Criterion.

        Args:
            translational_acc (np.ndarray): Array of translational accelerations.
            rotational_acc (np.ndarray): Array of rotational accelerations.

        Returns:
            float: GAMBIT value.
        """
        gambit_value = (translational_acc ** 1 + rotational_acc ** 1) ** (1/1)  # Linear combination
        return np.max(gambit_value)

    def process_file(self, file_path: str, x_idx: int, y_idx: int, z_idx: int) -> float:
        """
        Reads a CSV file, processes the data, and calculates the GAMBIT Injury Criterion.

        Args:
            file_path (str): Path to the CSV file.
            x_idx (int): X column index.
            y_idx (int): Y column index.
            z_idx (int): Z column index.

        Returns:
            float: GAMBIT Injury Criterion value.
        """
        # Read and process data
        data = self.read_csv(file_path)
        translational_acc = self.calculate_magnitudes(data, x_idx, y_idx, z_idx)
        rotational_acc = translational_acc  # In a real case, replace this with rotational data

        # Filter data
        filtered_translational = self.butter_lowpass_filter(translational_acc)
        filtered_rotational = self.butter_lowpass_filter(rotational_acc)

        # Calculate GAMBIT
        return self.calculate_gambit(filtered_translational, filtered_rotational)

if __name__ == "__main__":
    # Define file path and arguments as provided
    args = argparse.Namespace(frequency=0.0001, 
                              file_path='C:\\Users\\ae4514\\OneDrive - Coventry University\\Coventry Work\\SENTINEL\\Code\\SENTINEL-TriageTools-main\\SENTINEL-TriageTools-main\\Severity Index\\EURONCAP_ADULT_VALIDATED_OPENRADIOSS_DoE1T01.csv', 
                              x_location=89, y_location=90, z_location=91)

    gambit_calculator = GambitCalculator(args.frequency)
    gambit_value = gambit_calculator.process_file(args.file_path, args.x_location, args.y_location, args.z_location)
    print(f"The GAMBIT Injury Criterion (G) value is {gambit_value:.2f}")
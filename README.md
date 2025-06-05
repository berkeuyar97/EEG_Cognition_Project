# EEG Cognition Project (Basic EEG Data Analysis and Visualization)

This project aims to load, process, and visualize fundamental EEG (Electroencephalography) data using the MNE-Python library. It serves as an introductory example for those interested in cognitive science and neuroscience, providing a simple case for working with EEG signals.

## Project Objective

* To load a sample EEG dataset using the MNE-Python library.
* To display basic information about the loaded raw EEG data.
* To filter the data by selecting only the EEG channels.
* To visualize the raw EEG signals.

## Technologies Used

* **Python 3.x:** The main programming language for the project.
* **MNE-Python:** A leading open-source Python library for EEG/MEG data analysis.
* **Matplotlib:** A Python library used for data visualization.
* **Git:** Version control system.
* **GitHub:** Platform for hosting the project code.

## Setup and Running the Project

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository

First, clone this repository to your computer:

```bash
git clone [https://github.com/berkeuyar97/EEG_Cognition_Project.git](https://github.com/berkeuyar97/EEG_Cognition_Project.git)
cd EEG_Cognition_Project
### 2. Create and Activate a Virtual Environment

Create a dedicated virtual environment for the project to isolate dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
### 3. Install Required Libraries

With the virtual environment activated, install the MNE-Python and Matplotlib libraries:

```bash
pip install mne matplotlib
### 4. Run the Project

Once all dependencies are installed, you can run the `eeg_analysis.py` script:

```bash
python3 eeg_analysis.py
* **Note:** The first time you run the script, MNE-Python will automatically download the sample EEG dataset. This process might take some time depending on your internet speed (approximately 1-2 GB).
* Upon successful completion of the script, an interactive plot window displaying the EEG signals will open.

## Output Example

![Raw EEG Data Visualization](raw_eeg_data.png)
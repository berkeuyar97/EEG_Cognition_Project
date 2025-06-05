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

  ## ⚙️ Setup and Running the Project

To set up and run this project, please follow these steps:

1.  **Clone the repository:**
    First, clone the project repository to your local machine:
    ```bash
    git clone [https://github.com/berkeuyar97/EEG_Cognition_Project.git](https://github.com/berkeuyar97/EEG_Cognition_Project.git)
    cd EEG_Cognition_Project
    ```

2.  **Create a virtual environment (recommended):**
    It's highly recommended to create a dedicated Python virtual environment for this project to manage dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    3.  **Install the required libraries:**
    Once your virtual environment is active, install all necessary Python libraries using pip:
    ```bash
    pip install numpy pandas matplotlib mne
    ```
    *Note: If you encounter issues, try `pip3` instead of `pip`.*

4.  **Run the EEG analysis script:**
    Execute the main script to perform the EEG data analysis and display visualizations:
    ```bash
    python eeg_analysis.py
    ```
    This script will load a sample EEG dataset, process it, and show the visualizations.

5.  **Deactivate the virtual environment (when done):**
    When you're finished working on the project, you can deactivate your virtual environment:
    ```bash
    deactivate
    ```
    
## Output Example
![Raw EEG Data Visualization](raw_eeg_data.png)

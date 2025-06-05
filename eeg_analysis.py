
import mne
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') 

mne.viz.set_browser_backend('matplotlib') 

print("Script started. Loading sample EEG data...") 

sample_data_folder = mne.datasets.sample.data_path()
print(f"Sample data folder: {sample_data_folder}") 
sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_raw.fif"
)
print(f"Sample data file: {sample_data_raw_file}") 

try: 
    raw = mne.io.read_raw_fif(sample_data_raw_file, preload=True, verbose=False)
    print("Sample EEG data loaded successfully.")
except Exception as e:
    print(f"Error loading sample data: {e}")
    print("Please ensure the sample data is downloaded and accessible.")
    exit() 

print("\nData information:")
print(raw.info) # Prints general information about the recording
print(f"Number of channels: {len(raw.ch_names)}")
print(f"Sampling frequency: {raw.info['sfreq']} Hz")
print(f"Duration: {raw.times[-1]:.2f} seconds")

raw.pick_types(eeg=True, meg=False, eog=False, stim=False, exclude='bads')
print(f"\nNumber of EEG channels selected: {len(raw.ch_names)}")

print("\nPlotting raw EEG data...") 
fig = raw.plot(
    n_channels=20, # Display first 20 EEG channels
    scalings='auto', # Automatically adjust amplitude scaling
    title='Raw EEG Data (First 20 Channels)',
    show=True, # Display the plot
    duration=10 # Show 10 seconds of data at a time
)
<<<<<<< HEAD
#fig.savefig('raw_eeg_data.png') 
# --- Optional: Keep the plot open until closed manually ---
# If you're running this from an IDE or script, the plot might close quickly.
# This line ensures the plot stays open until you close it.
=======

>>>>>>> 0c58e68b53405cde1dd94eda723247a13818ee7c
plt.show() # This line is often implicitly called by raw.plot(show=True) but can be explicit for other plots.

print("Script finished. Close the plot window to exit.")

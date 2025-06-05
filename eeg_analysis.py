
import mne
import os
import matplotlib.pyplot as plt # Matplotlib genellikle görselleştirme için gereklidir
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

# Plotting raw EEG data (this part should be visible and not commented out)
fig = raw.plot(
    n_channels=20, # Display first 20 EEG channels
    scalings='auto', # Automatically adjust amplitude scaling
    title='Raw EEG Data (First 20 Channels)',
    show=True, # Display the plot
    duration=10 # Show 10 seconds of data at a time
)
print("\nPlotting Power Spectral Density (PSD)...")
# Plotting the power spectral density of EEG channels
fig_psd = raw.plot_psd(fmin=1, fmax=40, average=True, spatial_colors=False, exclude='bads', verbose=False)
fig_psd.suptitle('EEG Power Spectral Density (1-40 Hz)', y=1.05) # Add a title

# Optional: Adjust PSD plot settings
# fig_psd.tight_layout() # Uncomment if plots overlap

# raw.plot() için plt.show() var, fig_psd için de gerekebilir
# plt.show() # Eğer raw.plot() ile tek plt.show() yetmiyorsa, buraya da ekleyebilirsiniz.

plt.show() # This line is often implicitly called by raw.plot(show=True) but can be explicit for other plots.

print("Script finished. Close the plot window to exit.")
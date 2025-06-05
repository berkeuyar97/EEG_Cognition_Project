# Import necessary libraries
import mne
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') # Bu satırı ekleyin
# EKLE: Matplotlib'in arkaplanını (backend) belirgin şekilde ayarla
# Bu, grafik penceresinin açılmasını sağlamaya yardımcı olabilir.
mne.viz.set_browser_backend('matplotlib') # Bu satırı ekleyin

print("Script started. Loading sample EEG data...") # Güncelleme: Başlangıç mesajı

# --- Step 1: Load a sample EEG dataset ---
# MNE-Python comes with some small sample datasets.
# We'll use a very basic one to get started.
# This function will download the data if it's not already on your computer.
sample_data_folder = mne.datasets.sample.data_path()
print(f"Sample data folder: {sample_data_folder}") # EKLE: Veri klasörü yolu
sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_raw.fif"
)
print(f"Sample data file: {sample_data_raw_file}") # EKLE: Veri dosyası yolu

# Read the raw EEG/MEG data from the file
# 'preload=True' loads the data into memory, allowing us to manipulate it.
try: # EKLE: Hata yakalama
    raw = mne.io.read_raw_fif(sample_data_raw_file, preload=True, verbose=False)
    print("Sample EEG data loaded successfully.")
except Exception as e: # EKLE: Hata durumunda mesaj yazdır
    print(f"Error loading sample data: {e}")
    print("Please ensure the sample data is downloaded and accessible.")
    exit() # Hata durumunda betiği sonlandır

# --- Step 2: Basic Data Information and Selection ---
# Good practice to quickly see what's in the data
print("\nData information:")
print(raw.info) # Prints general information about the recording
print(f"Number of channels: {len(raw.ch_names)}")
print(f"Sampling frequency: {raw.info['sfreq']} Hz")
print(f"Duration: {raw.times[-1]:.2f} seconds")

# Let's select only the EEG channels for our analysis
# This dataset also contains MEG, EOG, etc.
# We are interested in 'eeg' channel type for our project.
raw.pick_types(eeg=True, meg=False, eog=False, stim=False, exclude='bads')
print(f"\nNumber of EEG channels selected: {len(raw.ch_names)}")


# --- Step 3: Visualize Raw EEG Data ---
# Plotting the raw data to see the brain signals
# 'n_channels' specifies how many channels to display
# 'scalings' adjusts the amplitude for better visibility
# 'title' sets the plot title
print("\nPlotting raw EEG data...") # Güncelleme: Plotting mesajı
fig = raw.plot(
    n_channels=20, # Display first 20 EEG channels
    scalings='auto', # Automatically adjust amplitude scaling
    title='Raw EEG Data (First 20 Channels)',
    show=True, # Display the plot
    duration=10 # Show 10 seconds of data at a time
)

# --- Optional: Keep the plot open until closed manually ---
# If you're running this from an IDE or script, the plot might close quickly.
# This line ensures the plot stays open until you close it.
plt.show() # This line is often implicitly called by raw.plot(show=True) but can be explicit for other plots.

print("Script finished. Close the plot window to exit.") # Güncelleme: Bitiş mesajı
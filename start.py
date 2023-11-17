import os
import webbrowser
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def create_file(file_path, file_content):
    with open(file_path, 'w') as file:
        file.write(file_content)

def browse_directory():
    folder_path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, folder_path)

def create_script():
    folder_path = directory_entry.get()
    file_name = filename_entry.get()
    coin = coin_entry.get()
    mining_address = mining_address_entry.get()
    machine_name = machine_name_entry.get()
    referral_code = referral_code_entry.get() if referral_code_var.get() else "#wvev-7038"

    # Get the selected CPU/GPU option
    cpu_gpu_option = cpu_gpu_combobox.get()

    # Prepare the script content with the selected CPU/GPU option, coin, mining address, machine name, and referral code
    if cpu_gpu_option == "CPU":
        script_content = f'xmrig.exe -o stratum+ssl://rx.unmineable.com:443 -a rx -k -u {coin}:{mining_address}.{machine_name}{referral_code} -p x\npause'
    else:
        algorithm = algorithm_combobox.get()
        if algorithm == "ETCHASH":
            pool_address = "etchash.unmineable.com:3333"
        elif algorithm == "ETHASH":
            pool_address = "ethash.unmineable.com:3333"
        elif algorithm == "AUTOLYKOS2":
            pool_address = "stratum+ssl://autolykos.unmineable.com:4444"
        elif algorithm == "BEAM-III":
            pool_address = "stratum+ssl://beamhash.unmineable.com:4444"
        elif algorithm == "ZEL":
            pool_address = "stratum+ssl://zelhash.unmineable.com:4444"
        elif algorithm == "EQUI144_5":
            pool_address = "stratum+ssl://zhash.unmineable.com:4444"
        elif algorithm == "KASPA":
            pool_address = "stratum+ssl://kheavyhash.unmineable.com:4444"
        elif algorithm == "ALEPH":
            pool_address = "stratum+ssl://blake3.unmineable.com:4444"
        elif algorithm == "IRONFISH":
            pool_address = "stratum+ssl://ironfish.unmineable.com:4444"
        elif algorithm == "NEXA":
            pool_address = "stratum+ssl://nexapow.unmineable.com:4444"
        else:
            pool_address = "rx.unmineable.com:443"  # Default pool address for other algorithms
        script_content = f'lolminer --algo {algorithm} --pool {pool_address} --user {coin}:{mining_address}.{machine_name}{referral_code} --pause-on-battery\npause'

    file_path = os.path.join(folder_path, file_name + get_file_extension())
    create_file(file_path, script_content)

    result_label.config(text=f"{file_path} has been created successfully!")
    os.startfile(file_path)  # Open the script file with the default program

def get_file_extension():
    if script_type_combobox.get() == "Linux/Mac (.sh)":
        return ".sh"
    else:
        return ".bat"

# Create the main window
window = tk.Tk()
window.title("Create Script File")
window.geometry("400x600")

# Directory selection
directory_label = tk.Label(window, text="Select Directory:")
directory_label.pack()

directory_entry = tk.Entry(window, width=40)
directory_entry.pack()

browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.pack()

# File name entry
filename_label = tk.Label(window, text="File Name:")
filename_label.pack()

filename_entry = tk.Entry(window, width=40)
filename_entry.pack()

# Script type selection
script_type_label = tk.Label(window, text="Select Script Type:")
script_type_label.pack()

script_type_combobox = ttk.Combobox(window, values=["Linux/Mac (.sh)", "Batch Script (.bat)"])
script_type_combobox.pack()

# CPU/GPU selection
cpu_gpu_label = tk.Label(window, text="Select CPU/GPU:")
cpu_gpu_label.pack()

cpu_gpu_combobox = ttk.Combobox(window, values=["CPU", "GPU"])
cpu_gpu_combobox.pack()

# Algorithm selection (GPU)
algorithm_label = tk.Label(window, text="Select Algorithm:")
algorithm_label.pack()

algorithm_combobox = ttk.Combobox(window, values=["ETCHASH", "ETHASH", "AUTOLYKOS2", "BEAM-III", "EQUI144_5", "KASPA", "ALEPH", "IRONFISH", "NEXA"])
algorithm_combobox.pack()

# Coin to mine entry
coin_label = tk.Label(window, text="Coin to Mine:")
coin_label.pack()

coin_entry = tk.Entry(window, width=40)
coin_entry.pack()

# Mining address entry
mining_address_label = tk.Label(window, text="Mining Address:")
mining_address_label.pack()

mining_address_entry = tk.Entry(window, width=40)
mining_address_entry.pack()

# Machine name entry
machine_name_label = tk.Label(window, text="Machine Name:")
machine_name_label.pack()

machine_name_entry = tk.Entry(window, width=40)
machine_name_entry.pack()

# Referral code entry
referral_code_var = tk.BooleanVar()
referral_code_checkbox = tk.Checkbutton(window, text="Include Referral Code", variable=referral_code_var)
referral_code_checkbox.pack()

referral_code_label = tk.Label(window, text="Referral Code:")
referral_code_label.pack()

referral_code_entry = tk.Entry(window, width=40)
referral_code_entry.pack()

# Create button
create_button = tk.Button(window, text="Create Script", command=create_script)
create_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Function to handle CPU/GPU selection change
def handle_cpu_gpu_selection(event):
    selection = cpu_gpu_combobox.get()
    if selection == "CPU":
        algorithm_label.pack_forget()
        algorithm_combobox.pack_forget()
    else:
        algorithm_label.pack()
        algorithm_combobox.pack()

# Function to handle algorithm selection change
def handle_algorithm_selection(event):
    selection = algorithm_combobox.get()
    if selection == "ETCHASH":
        mining_address_label.config(text="Mining Address (ETCHASH):")
    elif selection == "ETHASH":
        mining_address_label.config(text="Mining Address (ETHASH):")
    else:
        mining_address_label.config(text="Mining Address:")

# Bind the handle_cpu_gpu_selection function to the CPU/GPU combobox
cpu_gpu_combobox.bind("<<ComboboxSelected>>", handle_cpu_gpu_selection)

# Bind the handle_algorithm_selection function to the algorithm combobox
algorithm_combobox.bind("<<ComboboxSelected>>", handle_algorithm_selection)


donate_label = tk.Label(window, text="Donate Bitcoin:bc1qnk0ftxa4ep296phhnxl5lv9c2s5f8xakpcxmth")
def open_donation_link():
    import webbrowser
    webbrowser.open("bitcoin:bc1qnk0ftxa4ep296phhnxl5lv9c2s5f8xakpcxmth?message=Donate")

donate_label = tk.Label(window, text="Donate Bitcoin", cursor="hand2", fg="blue")
donate_label.pack()
donate_label.bind("<Button-1>", lambda event: open_donation_link())

donate_label = tk.Label(window, text="Download Xmrig")
def open_donation_link():
    import webbrowser
    webbrowser.open("https://xmrig.com/download")

donate_label = tk.Label(window, text="Download Xmrig", cursor="hand2", fg="blue")
donate_label.pack()
donate_label.bind("<Button-2>", lambda event: open_donation_link())

donate_label = tk.Label(window, text="Download lolminer")
def open_donation_link():
    import webbrowser
    webbrowser.open("https://github.com/Lolliedieb/lolMiner-releases/releases")

donate_label = tk.Label(window, text="Download lolminer", cursor="hand2", fg="blue")
donate_label.pack()
donate_label.bind("<Button-3>", lambda event: open_donation_link())

# Start the GUI event loop
window.mainloop()
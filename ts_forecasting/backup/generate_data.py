import pandas as pd
import numpy as np
import argparse
from data.columns import Columns

# Parametri di default
default_start_date = "2023-01-01"
default_end_date = "2025-08-18"
default_output_name = f"serie_storica_{default_end_date}.csv"
default_output_folder = "/Volumes/ts_catalog/ts_data/ts_input/"
default_seed = 100

# Funzione per generare la serie dataframe
def generate_series(name, dates, amp_28=10, amp_7=5, noise_scale=0.1):
    days = np.arange(len(dates))
    sin_28 = amp_28 * np.sin(2 * np.pi * days / 28)
    sin_7 = amp_7 * np.sin(2 * np.pi * days / 7)
    noise_amp = (amp_28 + amp_7) * noise_scale
    noise = noise_amp * np.random.randn(len(dates))
    amount = sin_28 + sin_7 + noise
    
    df = pd.DataFrame({
        Columns.DATE.value: dates,
        Columns.AMOUNT.value: amount,
        Columns.NAME.value: name
    })
    return df

# Funzione principale
def main(start_date, end_date, output_name, output_folder, seed):
    np.random.seed(seed)
    output_file = f"{output_folder}{output_name}"
    
    # Genera le date lavorative
    dates = pd.bdate_range(start=start_date, end=end_date)
    
    # Genera serie 1
    df1 = generate_series("series_1", dates)
    
    # Genera serie 2 (qui puoi variare ad es. ampiezze o rumore se vuoi)
    df2 = generate_series("series_2", dates)
    
    # Unisci i due DataFrame
    df = pd.concat([df1, df2], ignore_index=True)
    
    # Formatta la data nel modo richiesto
    df[Columns.DATE.value] = df[Columns.DATE.value].dt.strftime("%d-%b-%y")
    
    # Salva in CSV
    df.to_csv(output_file, index=False)
    
    print(f"File '{output_file}' creato con successo con due serie distinte.")
    print(df.head(10))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera una serie storica e salva in un file CSV.")
    parser.add_argument("--start_date", type=str, default=default_start_date, help="Data di inizio (formato YYYY-MM-DD)")
    parser.add_argument("--end_date", type=str, default=default_end_date, help="Data di fine (formato YYYY-MM-DD)")
    parser.add_argument("--output_name", type=str, default=default_output_name, help="Nome del file di output")
    parser.add_argument("--output_folder", type=str, default=default_output_folder, help="Cartella di output")
    parser.add_argument("--seed", type=int, default=default_seed, help="Seed per il generatore di numeri casuali")
    
    args = parser.parse_args()
    main(args.start_date, args.end_date, args.output_name, args.output_folder, args.seed)
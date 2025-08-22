# Progetto `ts_forecasting`


---

## File e cartelle:

- **/setup/**  
  Notebook di setup:
  - `catalog_prepare`: per creare l'alberatura di catalogo/schema/volumi
  - `generate_data`: per creare dati di input. Crea dati storici daily, tra una `start_date` e una `end_date`. Tipicamente, lo lanci almeno due volte con stessa `start_date` ma diversa `end_date`: una prima volta per creare un file su cui si farà training (es. `dato_input_2025-07-25.csv`), e una seconda volta per creare un file con dati più aggiornati (es. `dato_input_2025-08-18.csv`) per fare forecast.
  
    **NB**: assicurati che il nome del file di output contenga nel nome la `end_date`: infatti i task di preparazione del dato, train e forecast riconoscono il file da lavorare attraverso il nome del file (quella che viene chiamata `file_date`). 
    
    Verranno in seguito  aggiunti controlli sul fatto che la data nel nome corrisponda a quella massima della serie, perciò il nome del file di output è stato lasciato editabile in questo notebook.


- **/src/**  
  Moduli Python richiamati nei notebook. 

- **/**

  I seguenti **notebook** sono richiamati dai job:
  - `data_extraction`: partendo da un file di input, fa filtri e operazioni per generare una serie più pulita e salvarla.
  - `train`: procede al training e al logging del modello.
  - `forecast`: procede al download dell'ultimo modello e al forecasting
  
  NB: Per questi notebook, il parametro principale è la `file_date`, che corrisponde alla massima data contenuta nel file da lavorare.

- **/jobs/**

  contiene il .yml di due job:
  -  **forecasting_job**: per il forecasting (tipicamente giornaliero).
  -  **training_job**: per il training (tipicamente periodico).


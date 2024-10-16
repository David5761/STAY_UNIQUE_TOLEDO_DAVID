import pandas as pd
import matplotlib.pyplot as plt


def clean_and_transform_data_scraping():
    df = pd.read_csv('data/hotels_list.csv')

    df['availability'] = df['availability'].astype(str).fillna('')

    # Se usa 'split' correctamente para dividir en 'availability' y 'price_detail'
    df[['availability', 'price_detail']] = df['availability'].str.split('Precio', n=1, expand=True)
    df['price_detail'] = df['price_detail'].fillna('N/A').apply(lambda x: x.split('Ver')[0].strip())
    df['availability'] = df['availability'].apply(lambda x: x.split('US$')[0].strip())

    df.to_csv('data/hotels_list_cleaned.csv', index=False)


def clean_and_transform_data_stay_unique():
    properties_df = pd.read_csv('info_properties.csv')
    bookings_df = pd.read_csv('reservas_info.csv')

    #Convertir a datetime
    properties_df['ReadyDate'] = pd.to_datetime(properties_df['ReadyDate'], errors='coerce')
    bookings_df['BookingCreatedDate'] = pd.to_datetime(bookings_df['BookingCreatedDate'], errors='coerce')
    bookings_df['ArrivalDate'] = pd.to_datetime(bookings_df['ArrivalDate'], errors='coerce')
    bookings_df['DepartureDate'] = pd.to_datetime(bookings_df['DepartureDate'], errors='coerce')


    #union de archivos
    merged_df = pd.merge(bookings_df, properties_df, on='PropertyId', how='inner')

    #creacion de nuevos campos
    merged_df['OccupancyRate'] = merged_df['Persons'] / merged_df['Capacity']
    merged_df['RevenuePerNight'] = merged_df['TotalPaid'] / merged_df['NumNights']

    merged_df.to_csv('data/stay_unique_merged.csv', index=False)

    return merged_df

def eda_process(merged_df: pd.DataFrame):
    numeric_df = merged_df.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numeric_df.corr()

    #Descripcion general de los datos
    print(merged_df.describe())

    plt.figure(figsize=(10, 8))
    plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)
    plt.xticks(range(correlation_matrix.shape[1]), correlation_matrix.columns, rotation=90)
    plt.yticks(range(correlation_matrix.shape[1]), correlation_matrix.columns)
    plt.colorbar()
    plt.title('Matriz de Correlación de Variables Numéricas', pad=20)
    plt.show()

    channel_revenue = merged_df.groupby('Channel')['Revenue'].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 6))
    channel_revenue.plot(kind='bar', color='purple', edgecolor='black')
    plt.title('Ingresos Totales por Canal de Reserva')
    plt.xlabel('Canal de Reserva')
    plt.ylabel('Ingresos Totales')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    clean_and_transform_data_scraping()
    merged_df = clean_and_transform_data_stay_unique()
    eda_process(merged_df)
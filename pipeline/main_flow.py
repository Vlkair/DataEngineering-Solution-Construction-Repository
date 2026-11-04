import os
import requests
import psycopg2
from prefect import task, flow

@task(retries=3, retry_delay_seconds=5)
def extract_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

@task
def transform_data(raw_data):
    transformed = []
    for coin, data in raw_data.items():
        transformed.append({
            "symbol": coin.upper(),
            "price_usd": float(data["usd"])
        })
    return transformed

@task
def load_to_supabase(data):
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL no está configurada.")

    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO crypto_rates (symbol, price_usd)
    VALUES (%s, %s);
    """
    
    for row in data:
        cursor.execute(insert_query, (row["symbol"], row["price_usd"]))

    conn.commit()
    cursor.close()
    conn.close()

@flow(name="ETL_Crypto_Pipeline")
def run_pipeline():
    raw_data = extract_crypto_prices()
    clean_data = transform_data(raw_data)
    load_to_supabase(clean_data)

if __name__ == "__main__":
    run_pipeline()
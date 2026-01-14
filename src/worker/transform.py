from worker.connect import get_connection

def query_form(data_dict:dict):
    """
    Формирование запроса.
    """

    if not data_dict:
        raise ValueError("Пустой словарь данных")

    columns = list(data_dict.keys())
    columns_str = ', '.join(columns)

    placeholders = ', '.join(['%s'] * len(columns))

    values = tuple(data_dict.values())

    sql_query = f"""
        INSERT INTO fraud({columns_str})
        VALUES ({placeholders})
        RETURNING id;
    """

    return sql_query, values

def insert_transaction(data_dict: dict):
    """
    Dynamic insertion of a transaction.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            query, values = query_form(data_dict)
            cur.execute(query, values)
            transaction_id = cur.fetchone()[0]
        conn.commit()

    return transaction_id


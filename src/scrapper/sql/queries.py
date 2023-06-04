query = """
    UPDATE prices
    SET prices = %s, updated_at = CURRENT_TIMESTAMP
    WHERE label = %s
"""
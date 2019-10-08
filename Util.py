import uuid


def generate_unique_uuid_retry(table):
    """Generate a unique UUID that's not found in the table. Will retry indefinitely if it already exists.

    Arguments:
        table (Dictionary)

    Returns:
        uuid (UUID): The guarenteed unique UUID
    """
    generatedUuid = uuid.uuid4()

    while generatedUuid.hex in table:
        generatedUuid = uuid.uuid4()
        break

    return generatedUuid

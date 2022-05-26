from typing import List

refer_sample = """
You can refer to the cURL request samples for examples on how to consume this
endpoint.
"""


def fields_to_md(field_names: List[str]) -> str:
    """
    Create a Markdown representation of the given list of names to use in
    Swagger documentation.
    :param field_names: the list of field names to convert to Markdown
    :return: the names as a Markdown string
    """

    *all_but_last, last = field_names
    all_but_last = ", ".join([f"`{name}`" for name in all_but_last])
    return f"{all_but_last} and `{last}`"

def detect_if_double_quote_exists_at_end_of_string(strings_to_check):
    """
    The extracted data in the file looks like:
        " Plummer
        Plummers R' Us
        new
        Houston, Tx 75043
        just posted"

    This function checks each line to determine if it ends with a double quote.
    Finding the double quotes at the end of a string will determine if the line is the
    end of the data for a specific job.
    :param string_to_check:
    :return: True
    """
    strings_ending_in_double_quotes = []

    for i, string_to_check in enumerate(strings_to_check):
        if string_to_check.endswith('"'):
            strings_ending_in_double_quotes.append(i)
    return strings_ending_in_double_quotes


def detect_if_double_quote_exists_at_beggining_of_string(strings_to_check):
    """
    The extracted data in the file looks like:
        " Plummer
        Plummers R' Us
        new
        Houston, Tx 75043
        just posted"

    This function checks each line to determine if it begins with a double quote.
    Finding the double quotes at the beggining of a string will determine if the line is the
    beginning of the data for a specific job.
    :param string_to_check:
    :return: True
    """
    strings_ending_in_double_quotes = []

    for i, string_to_check in enumerate(strings_to_check):
        if string_to_check.startswith('"'):
            strings_ending_in_double_quotes.append(i)
    return strings_ending_in_double_quotes

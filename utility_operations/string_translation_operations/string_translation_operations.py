def perform_string_translation(string_to_translate):
    """

    :param string_to_translate:
    :return: translated string
    """

    translation_dict = {'(': ' ', ')': ' ', '/': ' ', '\\': ' ', '$': ' ', '-': ' ', '.': ' ',
                        '&': ' ', '!': ' ', '0': ' ', '1': ' ', '2': ' ', '3': ' ', '4': ' ',
                        '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': '', '_': ' ', '+': ' ',
                        '*': ' ', '^': ' ', '%': ' ', '#': ' ', '#': ' ', '@': ' ', ';': ' ',
                        ':': ' ', '"': ' ', '\'': ' ', '|': ' ', '[': ' ', ']': ' ', '{': ' ',
                        '}': ' '}

    translation_table = string_to_translate.maketrans(translation_dict)
    translated_string = string_to_translate.translate(translation_table).strip()

    return translated_string


def perform_string_translation_on_job_title(list_of_strings):
    """

    :param list_of_strings:
    :return:
    """

    jobs_with_translated_job_title = []

    for job in list_of_strings:
        job[0] = ' '.join(perform_string_translation(job[0]).split())

        jobs_with_translated_job_title.append(job)

    return jobs_with_translated_job_title
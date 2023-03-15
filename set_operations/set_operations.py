def create_a_set_of_uique_strings_from_job_titles(list_of_strings):
    """
    :param list_of_strings:
    :return:
    """

    all_jobs_titles = []
    unique_job_titles = set()
    translation_dict = {'(': ' ', ')': ' ', '/': ' ', '\\': ' ', '$': ' ', '-': ' ', '.': ' ',
                        '&': ' ', '!': ' ', '0': ' ', '1': ' ', '2': ' ', '3': ' ', '4': ' ',
                        '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': '', '_': ' ', '+': ' ',
                        '*': ' ', '^': ' ', '%': ' ', '#': ' ', '#': ' ', '@': ' ', ';': ' ',
                        ':': ' ', '"': ' ', '\'': ' ', '|': ' ', '[': ' ', ']': ' ', '{': ' ',
                        '}': ' '}

    for job in list_of_strings:
        translation_table = job[0].maketrans(translation_dict)
        translated_string = job[0].translate(translation_table)

        split_job_title = translated_string.split(' ')
        all_jobs_titles.extend(split_job_title)

    for word in all_jobs_titles:
        if len(word) > 1:
            unique_job_titles.add(word)

    return unique_job_titles, all_jobs_titles


def create_set_of_unique_companies(list_of_strings):
    """

    :param list_of_strings:
    :return:
    """

    pass
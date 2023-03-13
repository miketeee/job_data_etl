import datetime as dt


def get_todays_date_and_format_it_as_m_d_y():

    todays_date = dt.datetime.today().strftime('%m-%d-%y')

    return todays_date

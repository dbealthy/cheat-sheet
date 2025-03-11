Source: http://russianpenguin.ru/2019/09/11/python-%D1%87%D0%B5%D0%BC-%D0%BF%D0%BB%D0%BE%D1%85-datetime-replace/

# Correctly set set timezones for datetime.

Never use `.replace(tzinfo=...)`, use `.localize()` instead




Reason why start_date is convert from str to date:
- the while loop needs to subtract day
- first loop could in theory deal with str but it would have covert to date then back to str
- there will be many combinations of how to deal with str-date conversion, I've just picked one of them

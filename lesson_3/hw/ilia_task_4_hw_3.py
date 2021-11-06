earth_days_quantity, hours_quantity = map(int, input('количество_земных_дней, количество_часов :').split(','))
martian_solos = 1.02595675
martian_solos_quantity = round(((earth_days_quantity + (hours_quantity / 24)) * martian_solos), 2)

print('{} земных дней и {} часов, составляют {} марсианских солов'.format(earth_days_quantity, hours_quantity,
                                                                          martian_solos_quantity))

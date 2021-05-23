def unit (name, surname, year_born, live_city, email, num_phone):
    print(f"Name - {name}; Surname - {surname}; Year - {year_born}; City - {live_city}; Email - {email}; "
          f"Phone - {num_phone}")
unit (name = input('Введи имя'),
      surname = input('Введи фамилию'),
      year_born = input('Введи год рождения'),
      live_city = input('Введи город проживания'),
      email = input('Введи email'),
      num_phone = input('Введи номер телефона'))
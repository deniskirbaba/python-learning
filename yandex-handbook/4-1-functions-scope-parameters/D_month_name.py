def month(n, lang):
    months = {'ru': ['Январь', 
                     'Февраль', 
                     'Март', 
                     'Апрель', 
                     'Май', 
                     'Июнь', 
                     'Июль', 
                     'Август', 
                     'Сентябрь', 
                     'Октябрь', 
                     'Ноябрь', 
                     'Декабрь'],
              'en': ['January', 
                     'February', 
                     'March', 
                     'April', 
                     'May', 
                     'June', 
                     'July', 
                     'August', 
                     'September', 
                     'October', 
                     'Novebmer', 
                     'December']}
    return months[lang][n - 1]
    
from datetime import datetime
def main():
    horadesalida=19
    date = datetime.now()
    print(date)
    print("Date:", date.date())
    print("Time:", date.time())
    timeFormatter = "%H:%M:%S"
    hora=(date.now().strftime(timeFormatter))
    print((int(hora[0])*10)+int(hora[1]))
    if ((int(hora[0])*10)+int(hora[1])) >= horadesalida:
        print('Ha terminado su jornada laboral')
    else:
        faltanh=horadesalida-(int(hora[0])*10+int(hora[1]))
        faltanm=60-(int(hora[3])*10+int(hora[4]))
        faltans=60-(int(hora[6])*10+int(hora[7]))
        print('Faltan:',faltanh,':',faltanm,':',faltans,'para terminar su jornada laboral')



if __name__ == '__main__':
    main()
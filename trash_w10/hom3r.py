import os,time,keyboard
from colorama import Fore, Back, Style

os.system('cls')
r=Fore.RED
b=Fore.BLUE
g=Fore.GREEN
y=Fore.YELLOW
r2=Back.RED
b2=Back.BLUE
g2=Back.GREEN
y2=Back.YELLOW
bl=Back.BLACK
res=Style.RESET_ALL

def bucle():
    try:
        q3 = input(f'\n{b2}Quieres continuar?{res} S/N ')
        if q3.lower() == 's':
            main()
        elif q3.lower() == 'n':
            raise SystemExit
        else:
            os.system('cls')
            bucle()
    except KeyboardInterrupt:
        raise SystemExit
    except ValueError:
        bucle()

def main():
    os.system('cls')
    #os.system('mode 80,18')
    #os.system('title Hom3r0!')
    #print(f'\t{y}\thi! {os.getenv("username")}{res}')
    homero=r'''
         &
      .-"`"-.       
     /       \
     |   __  _|
     |  /  \/ \
    WW  \_o/_o/
    (        _)
     |   .----\
     ;  | '----'
      \__'--;`
      |___/\|
'''
    print(f'{y}{homero}{res}')
    print(f'\t{bl}[{res}{y} 1 {res}] Programado de apagado en {r}HORAS{res}')
    print(f'\t[{y} 2 {res}] Programado de apagado en {r}MINUTOS{res}')
    print(f'\t[{y} 3 {res}] Anular apagado ')
    print(f'\t[{y} 4 {res}] Salir del programa ')
    
    question=input(f'\n{b2}Ingresa la opcion {res}~{y}>{res}')
    if question == '1':
        question2=int(input(f'{b2}Ingresa la cantidad de horas activo{res}~{y}>{res} '))
        horas = question2*3600
        os.system(f'shutdown /t {horas} /s')
        time.sleep(question2*3550)
        keyboard.write('stop')
        time.sleep(0.3)
        keyboard.press('enter')
        time.sleep(0.3)
        keyboard.press('enter')
        bucle()

    elif question == '2':
        question3=int(input(f'{b2}Ingresa la cantidad de minutos activo{res}~{y}>{res} '))
        horas = question3*60
        os.system(f'shutdown /t {horas} /s')
        time.sleep(question3*50)
        keyboard.write('stop')
        time.sleep(0.3)
        keyboard.press('enter')
        time.sleep(0.3)
        keyboard.press('enter')        
        bucle()
        
        
    elif question == '3':
        os.system('shutdown /a')
        bucle()

    elif question == '4':
        print('\nSaliendo...')
        raise SystemExit
        
        
    else:
        print('No existe la opcion ingresada!')
        bucle()
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit
    except ValueError:
        main()
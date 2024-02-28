'''

     Part of case-study #2: Task elasticity


    Многие жители Камеруна до сих пор используют крышечки, чтобы приобрести товар или расплатиться за услуги.
    Здесь их приравнивают к мелочи. Ценность крышечкам придают постоянные акции производителей пива.
    Цена на папайю выросла с 95 до 148 крышечек. Доходы деревенских жителей снизились на 17%.
    В результате величина спроса на фрукт снизилась,и если раньше потребители были готовы покупать 500 кг папайи,
     то теперь покупают 380 кг. В то же время величина предложения на папайю увеличилась на 7%.
    Эластичными или неэластичными оказались спрос по цене, спрос по доходу, предложение по цене?


     Developers: Denisova D., Batrakova K., Simonov A., Shatilov A.

'''
import art_local as art

def main():

 
    '''
    Main function.
    :return: None
    '''
    


    P1 = int(input(art.count_price_1))
    P2 = int(input(art.count_price_1))
    Q1 = int(input(art.count_demand_1))
    Q2 = int(input(art.count_demand_2))
    I = int(input(art.count_income))
    S= int(input(art.count_demand))


    if P1/P2 < 1:
        price = int((1-(P1/P2))*100)
        print(f'Цена выросла на: {price} %')
    elif P2/P1<1:
        price = int(((P2/P1) - 1)*100)
        print(f'Цена снизилась на: {price} %')



    if Q1/Q2 < 1:
        quantity = int((1 - (Q1 / Q2)) * 100)
        print(f'Количество выросло на: {quantity} %')
    elif Q2/Q1 < 1:
        quantity = int(((Q2 / Q1) - 1) * 100)
        print(f'Количество снизилось на: {quantity} %')



    elasticitydP = abs(quantity / price)


    elastisitydI = abs(quantity / I)


    elastisityP = (S) / (P1 - P2) * (P1 / S)



    if elasticitydP > 1:
        print(f'{elasticitydP}, спрос эластичен.')
    elif 0 < elasticitydP < 1:
        print(f'{elasticitydP}, спрос неэластичен.')


    if elastisitydI > 1:
        print(f'{elastisitydI}, спрос эластичный,товар роскоши.')
    if 0 < elastisitydI < 1:
        print(f'{elastisitydI}, спрос неэластичный,нормальный товар.')
    if elastisitydI == 0:
        print(f'{elastisitydI}, спрос неэластичный,товар первой необходимости.')

    if (elastisityP > 1):
        print(f'{elastisityP}, предложение по цене эластично.')
    else:
        print(f'{elastisityP}, предложение по цене неэластично.')
 


if __name__ == "__main__":
    main()

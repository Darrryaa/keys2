'''

     Part of case-study #2: Task elasticity


     Developers: Denisova D., Batrakova K., Simonov A., Shatilov A.

'''
import art_local as art

def main():

 
    '''
    Main function.
    :return: None
    '''
    


    starting_price = int(input(art.count_price_1))
    final_price = int(input(art.count_price_1))
    initial_quantity = int(input(art.count_demand_1))
    final_quantity = int(input(art.count_demand_2))
    income = int(input(art.count_income))
    supply = int(input(art.count_demand))


    if starting_price/final_price < 1:
        price = int((1-(starting_price/final_price))*100)
        print(f'Цена выросла на: {price} %')
    elif final_price/starting_price<1:
        price = int(((final_price/starting_price) - 1)*100)
        print(f'Цена снизилась на: {price} %')



    if initial_quantity/final_quantity < 1:
        quantity = int((1 - (initial_quantity / final quantity)) * 100)
        print(f'Количество выросло на: {quantity} %')
    elif final quantity/initial_quantity < 1:
        quantity = int(((final quantity / initial_quantity) - 1) * 100)
        print(f'Количество снизилось на: {quantity} %')



    elasticitydP = abs(quantity / price)


    elastisitydI = abs(quantity / income)


    elastisityP = (supply) / (starting_price - final_price) * (starting_price / supply)



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

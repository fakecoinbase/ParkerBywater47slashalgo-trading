import sys 
import time
import sma 


def optimize(price_data, fee_rate, verbose_output, silent): 
    """
    Algorithm to find optimal parameters for ema with price movement threshold
    """
    best_performers = []
    for sma_length in range(1, 50):
        for price_movement_threshold in range(5, 100):
            update_best(best_performers, \
                (sma_length, price_movement_threshold / 1000, sma.simulate(price_data, sma_length, price_movement_threshold / 1000, fee_rate=fee_rate, verbose_output=verbose_output, silent=True)))
    if not silent:
        print(best_performers)


def update_best(a_list, current): 
    if len(a_list) < 6:
        a_list.append(current)
    else:
        mindx = 0 
        minimum = a_list[0][2]
        for i in range(1, len(a_list)):
            if a_list[i][2] < minimum: 
                mindx = i
                minimum = a_list[i][2]
            
        if current[2] > minimum: 
            a_list[mindx] = current


if __name__ == "__main__": 
    main()



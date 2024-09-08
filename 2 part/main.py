import concurrent.futures
import multiprocessing as mp
import time
import logging

logging.basicConfig(level=logging.INFO)

def factorize(*numbers):
    factors = []
    for number in numbers:
        number_factors = []
        for num in range(1, number + 1):
            if number % num == 0:
                number_factors.append(num)
        factors.append(number_factors)
    return factors


if __name__ == '__main__':
    numbers_list = (128, 255, 99999, 10651060)
    start_sync = time.time()
    for result in factorize(*numbers_list):
        logging.info(result)
    end_sync = time.time()
    logging.info(f'Function done with synchronization done by: {end_sync - start_sync}')

    logging.info('--------------------------------------------------------------------')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        start = time.time()
        for result in executor.map(factorize, numbers_list):
            logging.info(result)
        end = time.time()
        logging.info(f'Function done with multiprocessing done by {end - start}')
        logging.info(f'Used processors - {mp.cpu_count()}')

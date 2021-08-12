from memory_profiler import memory_usage
from timeit import default_timer


def profile_code(num=1000000):
    def profile_dec(func):
        def wrapper(*args, **kwargs):
            result_time = 0
            result_mem = 0
            result = None
            for _ in range(num):
                start_time = default_timer()
                start_mem = memory_usage()[0]
                result = func(*args, **kwargs)
                delta_mem = memory_usage()[0] - start_mem
                delta_time = default_timer() - start_time
                result_mem += delta_mem
                result_time += delta_time
            print(f'Время: {result_time}, Память: {result_mem}')
            return result
        return wrapper
    return profile_dec


if __name__ == '__main__':

    @profile_code(1)
    def test_func(num):
        lst = [elem for elem in range(num)]
        return lst

    # если запускать каждый вариант отдельно, остальные закомментировав:
    test_func(10)
    # Время: 0.2125299, Память: 0.0078125
    test_func(100)
    # Время: 0.2181048, Память: 0.0078125
    test_func(1000)
    # Время: 0.21715430000000002, Память: 0.0078125
    test_func(10000)
    # Время: 0.2152829, Память: 0.41015625

    # если всё разом запустить:
    # Время: 0.2091853, Память: 0.0078125
    # Время: 0.21498479999999998, Память: 0.0
    # Время: 0.21604259999999997, Память: 0.18359375
    # Время: 0.21756200000000003, Память: 0.38671875

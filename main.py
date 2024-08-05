import timeit

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    # Ініціалізація результату у вигляді словника
    result = {}

    # Проходимо по кожному номіналу монет (починаючи з найбільшого)
    for coin in coins:
        # Перевірка, чи потрібно ще видавати решту
        if amount == 0:
            break
        
        # Визначаємо максимальну кількість монет поточного номіналу
        count = amount // coin
        
        # Якщо ми можемо використати монети цього номіналу
        if count > 0:
            result[coin] = count  # Додаємо у словник кількість монет
            amount -= coin * count  # Зменшуємо суму на вартість використаних монет

    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    # Ініціалізація масиву для мінімальної кількості монет
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для суми 0 потрібно 0 монет

    # Масив для зберігання останньої монети, використаної для кожної суми
    coin_used = [0] * (amount + 1)

    # Проходимо по кожній монеті
    for coin in coins:
        # Проходимо по кожній сумі від вартості монети до цільової суми
        for x in range(coin, amount + 1):
            # Якщо додавання цієї монети зменшує кількість монет для досягнення суми x
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1  # Оновлюємо кількість монет
                coin_used[x] = coin  # Записуємо, що ця монета була використана

    # Відновлюємо набір монет, які склали цільову суму
    result = {}
    x = amount
    while x > 0:
        this_coin = coin_used[x]
        if this_coin in result:
            result[this_coin] += 1
        else:
            result[this_coin] = 1
        x -= this_coin

    return result

def main():
    amount = 1243  # Виберіть велику суму для тестування
    coins = [50, 25, 10, 5, 2, 1]
    
    # Вимірювання часу виконання жадібного алгоритму
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount, coins), number=1000)
    
    # Вимірювання часу виконання алгоритму динамічного програмування
    dp_time = timeit.timeit(lambda: find_min_coins(amount, coins), number=1000)
    
    # Виведення результатів
    print(f"Жадібний алгоритм: {find_coins_greedy(amount, coins)}")
    print(f"Динамічне програмування: {find_min_coins(amount, coins)}")
    print(f"Час виконання жадібного алгоритму: {greedy_time:.5f} секунд")
    print(f"Час виконання динамічного програмування: {dp_time:.5f} секунд")

if __name__ == "__main__":
    main()

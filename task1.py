def find_coins_greedy(amount):
    coin_values = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coin_values:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount -= num_coins * coin

    return result

def find_min_coins(amount):
    coin_values = [50, 25, 10, 5, 2, 1]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    last_coin_used = [0] * (amount + 1)

    for coin in coin_values:
        for value in range(coin, amount + 1):
            if min_coins[value - coin] + 1 < min_coins[value]:
                min_coins[value] = min_coins[value - coin] + 1
                last_coin_used[value] = coin

    result = {}
    remaining_amount = amount

    while remaining_amount > 0:
        coin = last_coin_used[remaining_amount]
        result[coin] = result.get(coin, 0) + 1
        remaining_amount -= coin

    return result


def main():
    
    amount = 118

    greedy_result = find_coins_greedy(amount)
    print("Greedy Algorithm Result:", greedy_result)

    min_coins_result = find_min_coins(amount)
    print("Dynamic Programming Result:", min_coins_result)


if __name__ == "__main__":
    main()
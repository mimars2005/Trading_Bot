from strategy.strategy import Strategy,BBRS,MovingAverage

strategy=BBRS()
strategy2=MovingAverage()

def print_type(strategy:Strategy):
    print(type(strategy))


print_type(strategy=strategy)
print_type(strategy=strategy2)



import berserk
import matplotlib.pyplot as plt


def test():
    with open('./lichess.token') as f:
        token = f.read().strip()

    session = berserk.TokenSession(token)
    client = berserk.Client(session)

    ratings = [
        (p['date'], p['rating'])
        for p in client.users.get_puzzle_activity()]
    plt.plot(list(range(len(ratings))), [x[1] for x in ratings])
    plt.show()


if __name__ == '__main__':
    test()

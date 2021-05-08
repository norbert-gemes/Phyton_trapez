def tt(a: int, b: int, c: int, d: int, m: int) -> float:
    TT: float = ((a + c) / 2) * m
    return TT


def tk(a: int, b: int, c: int, d: int) -> int:
    TK: int = a + b + c + d
    return TK


def main() -> None:
    print('Trapéz területe, kerülete!')

    a: int = int(input('Adja meg a trapéz első oldalát:'))
    b: int = int(input('Adja meg a trapéz második oldalát:'))
    c: int = int(input('Adja meg a trapéz harmadik oldalát:'))
    d: int = int(input('Adja meg a trapéz negyedik oldalát:'))
    m: int = int(input('Adja meg a trapéz magasságát:'))

    terület: float = tt(a, b, c, d, m)
    kerület: int = tk(a, b, c, d)
    print(f'A trapéz területe: {terület} cm^2')
    print(f'A trapéz kerülete: {kerület} cm')


if __name__ == '__main__':
    main()

#reversebypass

import time as t
import webbrowser as wb

def _clr_scr():
    """Clear terminal screen."""
    print("\033[H\033[J", end="")

def __banner__():
    """Hidden banner display."""
    print("=" * 50)
    print("\033[34mPrediction Tool - Access Portal\033[0m")
    print("=" * 50)

def __calculate(_pd_):
    """Complex calculation."""
    __res__ = ((_pd_ ** 2) + (_pd_ * 3)) % 10
    return "BIG" if __res__ > 7 or __res__ < 3 else "SMALL"

def __result_view(_p_, _r_):
    """Show result with obfuscation."""
    t.sleep(2)  # Delay for result
    print("\n" + "-" * 50)
    print(f"Period Number: {_p_}")
    print(f"\033[32mResult: {_r_.upper()}\033[0m")  # Green
    print("-" * 50)

def __options__(_tg_, _pwd_):
    """Entry point for options."""
    while True:
        _clr_scr()
        __banner__()
        print("1. Join Telegram")
        print("2. Start Prediction")
        __ch__ = input("Enter your choice (1/2): ").strip()

        if __ch__ == "1":
            print("\033[34mRedirecting to Telegram...\033[0m")
            wb.open(_tg_)
            continue
        elif __ch__ == "2":
            while True:
                _usr_inp = input("Enter your password: ").strip()
                if _usr_inp == _pwd_:
                    print("\033[32mAccess Granted!\033[0m")
                    return True
                else:
                    print("\033[31mInvalid Password. Retry.\033[0m")
        else:
            print("\033[31mInvalid Choice. Retry.\033[0m")
            t.sleep(2)

def __predict__(_tg_):
    """Prediction logic."""
    while True:
        try:
            _pn = int(input("\nEnter a 3-digit period number: "))
            if _pn < 100 or _pn > 999:
                raise ValueError("Period must be 3 digits.")
        except ValueError as e:
            print(f"\033[31mError: {e}\033[0m")
            continue

        _res = __calculate(_pn)
        __result_view(_pn, _res)

        _inp = input("Predict again? (yes/no): ").strip().lower()
        if _inp != "yes":
            print("\033[34mExiting and redirecting to Telegram...\033[0m")
            t.sleep(2)
            wb.open(_tg_)
            break

if __name__ == "__main__":
    _tg_link = "https://t.me/ReverseCracking"
    _pswd = "reverse"

    if __options__(_tg_link, _pswd):
        __predict__(_tg_link)
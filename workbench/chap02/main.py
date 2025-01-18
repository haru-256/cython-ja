from fib.fib import fib
from libs.profile import timefn
from loguru import logger


@timefn
def main() -> None:
    logger.info(fib(100000))


if __name__ == "__main__":
    main()

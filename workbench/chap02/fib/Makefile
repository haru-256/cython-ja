.PHONY: build
build:
	CC=gcc CXX=g++ uv run setup.py build_ext --inplace

.PHONY: clean
clean:
	-rm -r build fib*.{c,so}

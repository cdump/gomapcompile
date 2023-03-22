N=50000

array slice:
	python3 a.py $(N) $@ > src/slow.go
	/usr/bin/time -v go build -o /dev/null ./src |& grep -E 'wall clock|Maximum resident set'

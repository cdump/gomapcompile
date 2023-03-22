# go map with slice/array compile time/memory

## Numbers
Compilation time & memory usage:

`go version go1.20.2 linux/amd64`

- 22.49s vs 2.16s
- 2260Mb vs 234Mb

## Code
```go
type MyStruct struct {
    a string
    b [32]int
    c []int
}
```

Slow slice:
```go
var b2c = map[uint32]MyStruct{
    0: MyStruct{
        a: " 0 ",
        c: []int{ 0 },
    },
    7: MyStruct{
        a: " 1 ",
        c: []int{ 1 },
    },
    ...
}
```

Fast array:
```go
var b2c = map[uint32]MyStruct{
    0: MyStruct{
        a: " 0 ",
        b: [32]int{ 0 },
    },
    7: MyStruct{
        a: " 1 ",
        b: [32]int{ 1 },
    },
    ...
}
```

## Reproducer
```sh
$ make array
python3 a.py 50000 array > src/slow.go
/usr/bin/time -v go build -o slow ./src |& grep -E 'wall clock|Maximum resident set'
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:02.16
        Maximum resident set size (kbytes): 234332

$ make slice
python3 a.py 50000 slice > src/slow.go
/usr/bin/time -v go build -o /dev/null ./src |& grep -E 'wall clock|Maximum resident set'
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:22.49
        Maximum resident set size (kbytes): 2260508
```

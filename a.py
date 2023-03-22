import sys
import time

N = int(sys.argv[1])
V = sys.argv[2]

print("""
package main
import (
    "fmt"
    "os"
)

type MyStruct struct {
    a string
    b [32]int
    c []int
}

var b2c = map[uint32]MyStruct{
""")


for i in range(N):
    print(i*7, ': MyStruct{')
    print('a: "', i, '",')
    if V == 'array':
        print('b: [32]int{', i, '},')
    else:
        print('c: []int{', i, '},')
    print('},')

print('} // no cache ', time.time())
print('''
func main() {
    fmt.Println(b2c[uint32(len(os.Args))])
}
''')

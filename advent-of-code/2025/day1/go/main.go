package main

import (
	"fmt"
	"os"
)

func main() {
	path := "input.txt"
	f, err := os.Open(path)

	if err != nil {
		_ = fmt.Errorf("File opening error")
	}
	b1 := make([]byte, 3)
	n1, err := f.Read(b1)

	fmt.Println(b1[:n1])
}

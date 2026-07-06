package main

import "fmt"

func BasicPrint() {
	name := "Fred"
	age := 42
	fmt.Printf("%v is %v years old.\n", name, age)
}

func ForloopBits(n int) []string {
	if n < 0 {
		return []string{}
	} else if n == 1 {
		return []string{"0", "1"}
	} else {
		n1bits := ForloopBits(n - 1)
		zero := append([]string{}, n1bits...)
		one := append([]string{}, n1bits...)
		for i := range n1bits {
			zero[i] = "0" + zero[i]
			one[i] = "1" + one[i]
		}
		return append(zero, one...)
	}
}

func FibGoChan() {
	fibgen := func() chan int {
		ch := make(chan int)
		go func() {
			a, b := 1, 1
			for {
				ch <- a
				a, b = b, a+b
			}
		}()
		return ch
	}

	nextFib := fibgen()
	for i := 0; i < 5; i++ {
		fmt.Print(<-nextFib)
	}
}

// anonymous function doesn't support generic
func Index[T comparable](s []T, x T) int {
	for i, v := range s {
		if v == x {
			return i
		}
	}
	return -1
}
func GenericTest() {
	si := []int{10, 20, 15, -10}
	fmt.Println("int slice Index: ", Index(si, 15))
}

func MakeSlice() {
	s := make([]int, 5, 10)
	fmt.Println(s)

	s = append(s, []int{1, 2, 3, 4, 5, 6}...)
	fmt.Println(s)
	fmt.Println(len(s)) // 11
	fmt.Println(cap(s)) // 10*2 = 20

	// copy
	dst := make([]int, len(s))
	fmt.Println("copy()", dst)
	copy(dst, s)
	fmt.Println(dst)

	//clear
	clear(s)
	fmt.Println("clear()",s)
	fmt.Println("Length:", len(s))
	fmt.Println("Capacity:", cap(s))

}

func main() {
	// BasicPrint()
	// ForloopBits(10)
	// FibGoChan()
	// GenericTest()
	MakeSlice()
}

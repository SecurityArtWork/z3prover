package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter key: ")
	key, _ := reader.ReadString('\n')

	if validateKey(strings.Trim(key, "\n \r")) {
		fmt.Println("Access granted!")
	} else {
		fmt.Println("Try again, ∞ attemps remaining...")
	}
}

func validateKey(key string) bool {

	intKey := []byte(key)

	if len(intKey) != 15 {
		return false
	}

	if int(intKey[0])*int(intKey[7]) != 8784 {
		return false
	}

	if int(intKey[1])*int(intKey[8]) != 2601 {
		return false
	}

	if int(intKey[2])*int(intKey[9]) != 9025 {
		return false
	}

	if int(intKey[3])*int(intKey[10]) != 10290 {
		return false
	}

	if int(intKey[4])*int(intKey[11]) != 4233 {
		return false
	}

	if int(intKey[5])*int(intKey[12]) != 11590 {
		return false
	}

	if int(intKey[6])*int(intKey[13]) != 9744 {
		return false
	}

	if int(intKey[7])*int(intKey[14]) != 2376 {
		return false
	}

	if int(intKey[0])+int(intKey[14]) != 155 {
		return false
	}

	if int(intKey[1])+int(intKey[13]) != 135 {
		return false
	}

	if int(intKey[2])+int(intKey[12]) != 217 {
		return false
	}

	if int(intKey[3])+int(intKey[11]) != 156 {
		return false
	}

	return true
}

// [122, 51, 95, 105, 83, 95, 116, 72, 51, 95, 98, 51, 122, 84, 33]

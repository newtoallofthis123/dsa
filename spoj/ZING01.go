package main

import (
	"fmt"
	"strconv"
	"strings"
)

func findChars(char rune, str string) []int {
	var indices []int
	for i, c := range str {
		if c == char {
			indices = append(indices, i)
		}
	}
	return indices
}

func kthInstance(k int, char rune, str string) string {
	indices := findChars(char, str)
	if len(indices) < k {
		return "-1"
	}
	return fmt.Sprintf("%d", indices[k-1])
}

func main() {
	str := ""
	fmt.Scan(&str)
	n := 0
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		query := ""
		fmt.Scan(&query)

		queries := strings.Split(query, " ")
		fmt.Println(queries)

		queryType := queries[0]
		if queryType == "1" {
			char := rune(queries[2][0])
			k, _ := strconv.Atoi(queries[1])
			fmt.Println(kthInstance(k, char, str))
		}
	}
}

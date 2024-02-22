package main

import "fmt"

func INTARR01() {
	testcases := 0
	fmt.Scanf("%d", &testcases)

	for i := 0; i < testcases; i++ {
		nums := []int{}
		n := 0
		fmt.Scanf("%d", &n)

		i := 0
		for i < n {
			num := 0
			fmt.Scanf("%d", &num)
			nums = append(nums, num)
			i++
		}

		occurrences := make(map[int]int)
		for _, num := range nums {
			occurrences[num]++
		}

		for k, v := range occurrences {
			if v != 2 {
				fmt.Println(k)
				break
			}
		}
	}
}

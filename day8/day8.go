package main

import s "strings"
import (
	"bufio"
    "fmt"
    "log"
    "os"
	"strconv"
)

var println = fmt.Println
var print = fmt.Print

//// Test size
//const COL int = 7
//const LIG int = 3

// Real size
const COL int = 50
const LIG int = 6

const ON string = "#"
const OFF string = "."

func printScreen(screen [][]string) {
	println("=====================")
	for i := 0; i < LIG; i++ {
		for j := 0; j < COL; j++ {
			print(screen[i][j]);
		}
		println()
	}
	println("=====================")
}

func extractRotateParameters(instruction string) (int, int) {
	splitResult := s.Split(instruction, " by ")
	by, _ := strconv.Atoi(splitResult[1])
	first, _ := strconv.Atoi(s.Split(splitResult[0], "=")[1])
	return first, by
}

func executeRectCommand(instruction string, screen [][]string) {		
	splitResult := s.Split(instruction, "x")
	col, _ := strconv.Atoi(splitResult[0])
	lig, _ := strconv.Atoi(splitResult[1])
		
	for i := 0; i < lig; i++ {
		for j := 0; j < col; j++ {
			screen[i][j] = ON
		}
	}
}

func executeRotateColumnCommand(instruction string, screen [][]string) {
	col, by := extractRotateParameters(instruction)	
	ligs := make([]int, 0)
	
	for i := 0; i < LIG; i++ {
		if screen[i][col] == ON {
			ligs = append(ligs, i)
			screen[i][col] = OFF
		}
	}
	
	for _, lig := range ligs {
		lig = (lig + by) % LIG
		screen[lig][col] = ON
	}
}

func executeRotateRowCommand(instruction string, screen [][]string) {
	lig, by := extractRotateParameters(instruction)	
	cols := make([]int, 0)
	
	for j := 0; j < COL; j++ {
		if screen[lig][j] == ON {
			cols = append(cols, j)
			screen[lig][j] = OFF
		}
	}
	
	for _, col := range cols {
		col = (col + by) % COL
		screen[lig][col] = ON
	}
}

func applyInstruction(instruction string, screen [][]string) {
	println(instruction)

	if s.HasPrefix(instruction, "rect") {
		executeRectCommand(s.Replace(instruction, "rect ", "", -1), screen)
	} else if s.HasPrefix(instruction, "rotate row") {
		executeRotateRowCommand(s.Replace(instruction, "rotate row ", "", -1), screen)
	} else if s.HasPrefix(instruction, "rotate column") {
		executeRotateColumnCommand(s.Replace(instruction, "rotate column ", "", -1), screen)
	}	
}

func countPixelsOn(screen [][]string) (int) {
	count := 0
	for i := 0; i < LIG; i++ {
		for j := 0; j < COL; j++ {
			if screen[i][j] == ON {
				count += 1
			}
		}
	}
	return count
}

func main() {
	screen := make([][]string, LIG)	

	for i := 0; i < LIG; i++ {
		screen[i] = make([]string, COL)
		for j := 0; j < COL; j++ {
			screen[i][j] = OFF
		}
	}
	
	file, err := os.Open("data.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        applyInstruction(scanner.Text(), screen)
		printScreen(screen)
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
	
	println("Number of pixels on: ", countPixelsOn(screen))
}
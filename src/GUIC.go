package main

import (
	"bufio"
	"fmt"
	"os"
)

//TODO make commands

func main() {
	args := os.Args

	if args[1] == "build" {
		fmt.Println("Function does not done yet")
	} else {
		//NOTE if it' s need you can do the same do with errors to other type of problems like warnings or informative

		var errors []error
		var lines []string

		// read file
		file, err := os.Open(args[1])
		if err != nil {
			errors = append(errors, err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)

		for scanner.Scan() {
			line := scanner.Text()
			lines = append(lines, line)
		}

		if err := scanner.Err(); err != nil {
			errors = append(errors, err)
		}

		//TODO know what command is and the arguments give

		// Empty errors.log
		errorsFile, err := os.OpenFile("errors.log", os.O_WRONLY|os.O_TRUNC, 0644)

		if err != nil {
			panic(err)
		}

		// save errors in errors.log
		if len(errors) > 0 {
			for _, actualError := range errors {
				if actualError != nil {
					_, writeErr := errorsFile.WriteString(fmt.Sprintf("Error: %v\n", actualError))
					if writeErr != nil {
						fmt.Printf("Unexpected error writing to errors.log: %v\n", writeErr)
					}
				}
			}
		}

		defer errorsFile.Close()
	}
}

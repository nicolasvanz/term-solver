package main

import (
	"fmt"
	"strings"
)

func main() {
	c := 0
	instructions()
	var wordSlice []string = words
	for c < 5 {
		output := inputWord()
		split := strings.Split(output, "#")
		if len(split) != 2 {
			if output == "stop" {
				break
			} else {
				fmt.Println("Entrada invalida.")
			}
		} else {
			var wordBase = wordSlice
			wordSlice = make([]string, 0)
			if len(split[0]) == len(split[1]) && len(split[1]) == 5 {
				rightPosition := [5]string{"#", "#", "#", "#", "#"}
				haveWrongPosition := [5]string{"#", "#", "#", "#", "#"}
				dontHaveat := [5]string{"#", "#", "#", "#", "#"}
				for j, _ := range split[1] {
					param := string(split[0][j])
					paramReffer := string(split[1][j])
					if paramReffer == "r" {
						dontHaveat[j] = string(param)
					} else if paramReffer == "y" {
						haveWrongPosition[j] = string(param)
					} else if paramReffer == "g" {
						rightPosition[j] = string(param)
					} else {
						fmt.Println(">> Entrada invalida")
					}
				}
				for _, word := range wordBase {
					naoAdiciona := false
					for _, l := range haveWrongPosition {
						if !strings.Contains(word, l) && l != "#" {
							naoAdiciona = true
							break
						}
					}
					// nao possui
					if !naoAdiciona {
						for i, j := range dontHaveat {
							if j == string(word[i]) {
								naoAdiciona = true
								break
							}
						}
					}
					if !naoAdiciona {
						for i, l := range rightPosition {
							// verificando palavra posicao correta
							if l != "#" {
								if string(word[i]) != l {
									naoAdiciona = true
									break
								}
								// verificando posicao incorreta
								if string(word[i]) == string(haveWrongPosition[i]) && string(haveWrongPosition[i]) != "#" {
									naoAdiciona = true
									break
								}
							}
						}
					}

					if !naoAdiciona {
						wordSlice = append(wordSlice, word)
					}
				}
			} else {
				fmt.Println("Entrada invalida.")
			}
			if len(wordSlice) > 0 {
				fmt.Printf("Dica : %s \n", wordSlice[0])
			} else {
				fmt.Println("Erro ?")
			}
		}
		c++
	}
}

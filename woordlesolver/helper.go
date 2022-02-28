package main

import "fmt"

func instructions() {
	fmt.Println(">> Você recebera provaveis respostas e com elas ir adicionando novas dicas ao programa")
	fmt.Println(">> Insira sua palavra#resultados")
	fmt.Println(">> Para sessão de resultado temos as seguintes resposta: ")
	fmt.Println(">> y letra pertence a palavra mas esta em posição incorreta. ")
	fmt.Println(">> r letra não pertence a palavra.")
	fmt.Println(">> g letra pertence a palavra e esta na posição correta.")
	fmt.Println(">> Exemplo de entrada: termo#rrgyy")
}

func inputWord() (output string) {
	var input string
	fmt.Println(">> Insira a palavra e o resultado obtido. ")
	fmt.Scanf("%s", &input)
	return input
}

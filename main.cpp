#include <iostream>
#include <string>


int main(){
    std::string nome;
    int idade;

    std::cout << "Digite seu nome" << std::endl;
    std::cin >> nome;
    std::cout << "Digite sua idade" << std::endl;
    std::cin >> idade;

    if (idade >= 18){
        std::cout << "Bem vindo ao sistema" << nome << "sua idade é de " << idade << std::endl;
    } else if (idade < 18){
        std::cout << "Sistema bloqueado, idade não ideal para logar" << std::endl;
    } else if (idade <= 0){
        std::cout << "Idade precisa ser maior que 0" << std::endl;
    }
    
    return 0;

}
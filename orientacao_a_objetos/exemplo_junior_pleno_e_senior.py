from orientacao_a_objetos.alura import Alura
from orientacao_a_objetos.caelum import Caelum


def verificar_cada_nivel():
    """
    exemplo de herança, pois dessa forma quando a classe Junior for instanciada, poderá usar todos os métodos
    da classe alura
    """
    class Junior(Alura):
        pass

    """"
    exemplo de herança múltipla, pois desse forma quando a classe Pleno for instanciada, poderá usar todos os métodos
    das classes Alura e Caelum. Considerando que nesse caso a busca pelos métodos a serem executados respeitará
    basicamente a seguinte ordem:
    1. Métodos da própria classe, no caso Pleno;
    2. Métodos da primeira classe herdada, no caso Alura;
    3. Métodos da classes mães dessa primeira classe herdada, ou seja Funcionário. Porém cabe ressaltar que se essa
    classe mãe se repetir para as demais classes herdadas por pleno, ela é desconsiderada. Sendo assim, nesse caso
    em específico, em vez de olhar para a classe Funcionário, iria para a classe Caelum.
    É possível verificar isso comentando qualquer método que se repita entre essas classes e executar esse arquivo, 
    para verificar o que é impresso no console.
    """
    class Pleno(Alura, Caelum):
        pass

    jose = Junior('José')
    jose.busca_perguntas_sem_resposta()

    luan = Pleno('Luan')
    luan.busca_perguntas_sem_resposta()
    luan.busca_cursos_do_mes()
    luan.mostrar_tarefas()

    """
    Aqui temos o exemplo de como criar um mixin, que nada mais é do que uma classe que não será instanciada, mas terá
    seu código reutilizado por outras classes, através de herança múltipla, como é o caso de uso na classe Senior, mais
    abaixo.
    """
    class Hipster:
        def __str__(self):
            return f"Hipster, {self.nome}"

    class Senior(Alura, Caelum, Hipster):
        pass

    paulo = Senior('Paulo')

    """
    No caso o print abaixo irá exibir o nome 'Paulo' onde em Hipster está a variável de instância 'nome'. 
    """
    print(paulo)


if __name__ == '__main__':
    verificar_cada_nivel()

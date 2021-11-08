de  Sem  importação  Não

classe  ListaDuplaEncadeada :

    def  __init__ ( self ):
        eu . inicio  =  Nenhum
        eu . fim  =  Nenhum
        eu . tamanho  =  0

    
    def  adicionar ( próprio , dado ):

        # Cria um novo no local para Nenhum (anterior e proximo)
        não  =  Não ( dado , nenhum , nenhum )

        # Se o inicio para None a lista esta vazia
        # O inicio e o fim obtem o novo não
        se  eu . inicio  é  nenhum :
            eu . inicio  =  não
            eu . fim  =  não

        # Caso ja exista algum valor na lista
        mais :
            # O anterior aponta para o fim
            não . anterior  =  self . fim
            # O proximo aponta para Nenhum
            não . proximo  =  Nenhum
            # O proximo do fim sempre aponta para o novo no
            eu . fim . proximo  =  não
            # O fim passa a ser o novo não
            eu . fim  =  não


    def  imprimir ( próprio ):
        
        print ( "Lista duplamente encadeada na ordem dos elementos adequados:" )

        # O não atual e o primeiro no lista
        no_atual  =  self . inicio

        não  =  ""
        # Para cada no valido da lista
        enquanto  no_atual  não é  nenhum : 
            se  não_atual . anterior  é  nenhum :
                não  + =  "Nenhum"
            não  + =  "<---> |"  +  str ( no_atual . dado ) +  "|"
            se  não_atual . proximo  é  nenhum :
                não  + =  "<---> Nenhum"

            no_atual  =  no_atual . proximo
        imprimir ( não )
        imprimir ( "="  *  110 )



    def  imprimir_invertido ( self ):

        
        print ( "Lista duplamente encadeada em ordem invertida:" )

        # O no atual e o ultimo no da lista
        no_atual  =  self . fim

        não  =  ""
        # Para cada no valido da lista
        enquanto  no_atual  não é  nenhum : 
            se  não_atual . proximo  é  nenhum :
                não  + =  "Nenhum"
            não  + =  "<---> |"  +  str ( no_atual . dado ) +  "|"
            se  não_atual . anterior  é  nenhum :
                não  + =  "<---> Nenhum"

            no_atual  =  no_atual . anterior
        imprimir ( não )
        imprimir ( "="  *  110 )
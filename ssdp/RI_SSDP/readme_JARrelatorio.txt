//Passar: o nome do arquivo, valor de k e o valor de atributo que quero desprezar        
        //args[0]: caminho da base 
        //args[1]: nome da base 
        //args[2]: k
        //args[3]: tipo de avaliação (ex. "Qg", "WRAcc", "WRAccN", "WRAccOverSize", "Sub", "DiffSup")		
        //args[4]: valor a filtrar (ex. "zero")
        //args[5]: rótulos (ex. "6","80","104","116","134","145","151","153","156","256")
        //args[6]: AND (1) ou OR (0)

java -jar DP4.jar "pasta" "arquivo.csv" "k" "metrica" "valorDesconsiderar" "<rolulo1>,<rotulo2>,..." "ANDouOR"

Exemplo:
java -jar DP4.jar "C:/Users/Tarcisio  Lucas/Documents/NetBeansProjects/DP4/pastas/bases/" "doc_term_matrix_discrete.csv" "10" "Qg" "zero" "6,80,104,116,134,145,151,153,156,256" "1"

java -jar DP4.jar "C:/Users/Tarcisio  Lucas/Documents/NetBeansProjects/DP4/pastas/bases/" "doc_term_matrix_discrete.csv" "20" "WRAccN" "zero" "6,80,104,116,134,145,151,153,156,256" "1"


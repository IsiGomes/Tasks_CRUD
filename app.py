from flask import Flask

#Dentro da variavel "(__main__)" que geralmente a gente passa como name, que é aqui justamente o nome do nosso arquivo. 
# E esse geralmente, utilizamos quando estamos executando isso de forma manual, esse __name__ ele vai ter aqui o valor __main__. 
# Então sempre quando a gente executar aqui de forma manual, executar esse arquivo diretamente, essa variável name vai ter essa estrutura aqui __name__ = "__main__". 
# Então vai ser uma string com o main. E aí a gente sabe que isso aqui está sendo executado de forma manual e não está sendo implantado ou importado por outro arquivo.

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello world!"
    
@app.route("/about")
def about():
    return "Página Sobre"

if __name__=="__main__":
    app.run(debug=True)
    
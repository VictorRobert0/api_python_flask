from flask import Flask,jsonify,request

app = Flask(__name__)


livros = [
    {
     'id': 1,
     'titulo': 'Criando APIS solidas',
     'autor': 'Victor Robierto'
    },
    {
        'id': 2,
        'titulo': 'Será que criei a API?',
        'autor': 'Desespero para aprender'
        
    }
]
#--------------------------------------------------------------------
#--------------------------------------------------------------------

#Consultar (todos)

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
#--------------------------------------------------------------------
#--------------------------------------------------------------------

#-----------------------Consultar por ID-----------------------------

@app.route('/livros/<int:id>', methods=['GET'])
def obter_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#--------------------------------------------------------------------    
#--------------------------------------------------------------------


#------------------------ATUALIZAR DADOS DA API----------------------
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#--------------------------------------------------------------------    
#-------------------------------------------------------------------- 

#---------------------CRIAR NOVO RECURSO NA API, METHOD POST------------------------

@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)

#--------------------------------------------------------------------    
#-------------------------------------------------------------------- 


#------------------------DELETAR DADOS DA API----------------------

@app.route ('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            
            return jsonify(livros)
#--------------------------------------------------------------------    
#-------------------------------------------------------------------- 





app.run(port=5000,host='localhost', debug=True)


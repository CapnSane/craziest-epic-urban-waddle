import sqlite3


try:
  
  banco = sqlite3.connect('primeiro_banco.db')

  cursor = banco.cursor()

  cursor.execute("DELETE FROM pessoas WHERE idade = 42")

  banco.commit()
  banco.close()
  print("os dados foram removidos com sucesso!!")
  
except sqlite3.Error as erro:
  print("Erro ao excluir : ", erro)


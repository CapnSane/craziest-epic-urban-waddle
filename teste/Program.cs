// Quantos Múltiplos de 2, Múltiplos de 49 e  Múltiplos de 37 existem no intervalo de 1 a 5.000.000?
int i = 1;
int count = 0 ;
while (i < 5000001)
{
  if (i % 49 == 0 & i % 37 == 0 & i % 2 == 0)
  {
    count += 1;
  }
  i += 1;
}
// while (i < 5000001)
//     if (i % 49 == 0 | i % 37 == 0 | i % 2 == 0)
//         count += 1;
//     i += 1;
int outra_resposta = 5_000_000 / (2 * 49 * 37);
Console.WriteLine("-----Questão 1------------------------------------------------------------------------------------");
Console.WriteLine("Existem " + count + " números pares que são múltiplos de 49 e de 37 simultaneamente entre 1 e 5.000.000");
Console.WriteLine("Outra solução, a mesma resposta: " + outra_resposta);
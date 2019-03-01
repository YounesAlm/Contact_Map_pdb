setwd('~/Documents/Perso/Code/Contact_Map_pdb')

mat = read.csv('contact_matrix_Mt.csv',header=T,row.names = 1,blank.lines.skip=T)
head(mat)
colnames(mat)=rownames(mat)
dim(mat)
head(mat) 

add_loops = function(M){
  for (i in 1:length(M[1,])){ 
    M[i,i]=1
  } 
  M
}

make_stochastic = function(M)
{
  M=apply(M,1,function(X) if (sum(X)>0){X/sum(X)} else{Y=1; X/Y} )
  M=t(M)
}

expanse = function(M){
  M<-M %*% M
  M
}

inflate <- function(M, inflate=2) {
  
  return (make_stochastic(M^inflate))
}
max_row = function(M){
  apply(M,1, max)
}

sum_sq = function(M){
  apply(M,1, function(X) sum(X**2))
}

row_chaos = function(M){ 
  max_row(M)-sum_sq(M)
}

chaos = function(M){
  max(row_chaos(M))
}
MCL = function(M, inflate=2){
  M2 = add_loops(M) #Permet à tout les sommets de boucler sur eux même.
  M2 = make_stochastic(M2) #Permet à la matrice d'être une matrice d'émission (modèle de markov).
  change = 1 #Initialisation à 1. Nous permettra plus tard, en lui attribuant la valeur du chaos, à savoir quand la matrice converge vers un état stable. 
  while (change > 0.001){ #Le 'tant que' nous permet de simuler la marche aléatoire tant que la matrice ne converge pas. 
    M2 = expanse(M2) #Permet de simuler la marche aléatoire. 
    M2 = inflate(M2, inflate) #Permet d'accentuer la marche aléatoire. 
    change = chaos(M2) 
  }
  round(M2,3) #Permet d'arrondir les valeurs de la Matrice M2 à trois chiffres après la virgule, obtenue après traitemement des données de la matrice M.
}

m=MCL(mat, inflate=2)
head(m)
for (i in 1:length(mat[1,])){
  for (j in 1:length(mat[,1])){
    if (mat[i,j]==700 && i!=j){
      print('couple')
      print(i)
      print(j)
    }
  }
}
library(igraph)
g=graph.adjacency(mat, mode='undirected', weighted=TRUE)
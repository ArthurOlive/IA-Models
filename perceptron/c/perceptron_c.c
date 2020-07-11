#include <stdlib.h>
#include <stdio.h>
#include <math.h>

typedef struct {
    float ** x;
    float * y;
    float * w;
    float n;
    int epoc;
    int size, dim;
} perceptron;

perceptron * Perceptron();
void fit(perceptron * p, float ** x, float * y, int dim, int size);
void predict(perceptron * p, float ** x, int size);
void score(perceptron * p, float ** x, float * y, int size);
void printPerceptron(perceptron * p);
void destroy(perceptron * p);
float g(float u);
void printw(perceptron * p);
void printx(perceptron * p);
void printy(perceptron * p);

int main(){
    perceptron * rna = Perceptron();
    
	float x1 [] = {0.75, 0.75};
	float x2 [] = {0.75, 0.25};
	float x3 [] = {0.25, 0.75};
	float x4 [] = {0.25, 0.25};
	float y [] = {1, -1, -1, 1};
	
	float ** x = (float ** ) calloc (4, sizeof(float *));
	
	x[0] = x1;
	x[1] = x2;
	x[2] = x3;
	x[3] = x4;
	
    int dim = 2;
    int size = 4;

	//treinamento
    fit(rna, x, y, dim, size);
    
    //teste
	predict(rna, x, size);
	score(rna, x, y, size);
	
	free(x);
	destroy(rna);
    return 0;
}

perceptron * Perceptron(){
    //alocação dinamica
    perceptron * p = ( perceptron *) calloc(1, sizeof (perceptron ));

    return p;
}
void destroy(perceptron * p){
	int j;
	for (j = 0; j <= p->dim; j ++){
    	free(p->x[j]);
    }
    free(p->x);
    free(p->y);
	free(p->w);;
	free(p);
}
    
void fit(perceptron * p, float ** x, float * y, int dim, int size){
	//Variaveis auxiliares.
    int j, i;
    float * x_temp;
    int err;
    float u, yi;
    
    p->dim = dim;
    p->size = size;
    
    //Armazena o valor passado mais 1 espaço para o limiar
    p->x = (float **) calloc(p->size + 1, sizeof(float));
    p->y = (float *) calloc(p->dim + 1, sizeof(float));

    //Copia so valores mais o limiar para formar os dados
    for (j = 0; j < p->size; j ++){
    	x_temp = (float * ) calloc(p->dim + 1, sizeof(float)); 
        for ( i = 0; i <= p->dim; i ++ ){
            if(i == 0){
                x_temp[i] = -1;
            } else {
                x_temp[i] = x[j][i-1];
            }
        }
        p->y[j] = y[j];
        p->x[j] = x_temp;
    }


    //Dimensão recebe dim + 1 por conta do valor do limiar
    p->w = (float *) calloc(p->dim + 1, sizeof(float));

    //inicializa o vetor de pesos sinaticos com valores pequenos e vazios
    for ( i = 0; i <= p->size; i ++){
        //gera numeros entre 0 e 1
        p->w[i] = ((float)rand()/(float)(RAND_MAX)) * 1;
    }

    //taxa de aprendizado 
    p->n = (p->size * p->dim) + (p->size * p->dim);
    p->n = 1/p->n;

    //inicializa a epoca da rede com o valor nulo
    p->epoc = 0;

    //repita até que err seja inexistente
    for ( j = 0; j < p->size; j ++){
		do {
	        err = 0; //erro começa com o valor nulo
	        u = 0;
	        
            for ( i = 0; i <= p->dim; i ++ ){
                u += p->w[i] * p->x[j][i];
            }
            
			//Aplica a fun��o de limiar de ativa��o
            yi = g(u);
			
            if (yi != p->y[j]){
                for ( i = 0; i <= p->dim; i ++ ){
                    p->w[i] = p->w[i] + p->n * ( p->y[i] - yi ) * p->x[j][i];
                }
                err = 1;
            }
            
			p->epoc ++;
    	}while(err);
	}
	printPerceptron(p);
	system("pause");
}

void predict(perceptron * p, float ** x, int size){
	float u, yi;
	int i, j;
	
	printf("Saida: ");
	for (j = 0; j < size; j++){
		for ( i = 0; i <= p->dim; i ++ ){
        	u += p->w[i] * p->x[j][i];
    	}
    
    	printf("%0.f ", g(u));
	}
	printf("\n");

}

void score(perceptron * p, float ** x, float * y, int size){
	float u, yi;
	int i, j;
	int hit = 0;
	int miss = 0;
	
	for (j = 0; j < size; j++){
		for ( i = 0; i <= p->dim; i ++ ){
        	u += p->w[i] * p->x[j][i];
    	}
    
    	if( g(u) == y[j]){
    		hit ++;
		} else {
			miss ++;
		}
	}
	printf("O perceptron acertou %d e errou %d casos.\nEle acertou %f porcento dos dados.\n", hit, miss, (float)hit/size );

}

void printPerceptron(perceptron * p){
	printf("Rede RNA Perceptron feedforward de camada unica:\n");
	printf("===================================================\n");
	printf("Quantidade de Epocas do treinamento: %d\n", p->epoc);
	printf("Dimensao dos dados: %d\n", p->dim);
	printf("Quantidade de dados do treinamento: %d\n", p->size);
	printw(p);	
	printf("===================================================\n");
	printf("\n");
}

float g(float u ){
    //Funcao inicial
    //u >= 0 entao 1 
    //u < 0 entao -1

    
    if (u >= 0){
        return 1;
    } else {
        return -1;
    } 
}

void printw(perceptron * p){
    printf("Pesos sinapticos (w): \n");
    int i;
    for ( i = 0; i <= p->dim; i++){
        printf("w%d : '%.4f' ", i, p->w[i]);
    }
    printf("\n");
}


void printx(perceptron * p){
    printf("Exibindo valores de X do perceptron: \n");
    int j, i;
    for (j = 0; j < p->size; j ++){
        for ( i = 0; i <= p->dim; i++){
            printf("%f ", p->x[j][i]);
        }
        printf("\n");
    }
    printf("\n");
}

void printy(perceptron * p){
    printf("Exibindo valores de Y do perceptron: \n");
    int i;
    for ( i = 0; i < p->size; i++){
        printf("%f ", p->y[i]);
    }

    printf("\n");
}

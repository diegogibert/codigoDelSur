/* programa que cuenta palabras y sus repeticiones en un texto
manera de correrlo: compilar con gcc archivo.c -o archivo y luego ./archivo < texto.txt
o solo ./archivo, escribir algo y luego presionar ctrl + D (valido en linux)*/

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#define MAXWORD 100


struct tnode {

    char *word;
    int count;
    struct tnode *left;
    struct tnode *right;

};


struct tnode *addtree(struct tnode *, char *);
void treeprint(struct tnode *);
int getword(char *, int);

main()
{

    struct tnode *root;
    char word[MAXWORD];

    root = NULL;

    while (getword(word, MAXWORD) != EOF)
        if (isalpha(word[0])) {
            root = addtree(root, word);
        }
    treeprint(root);
    return 0;
}

struct tnode *talloc(void);
char *mystrdup(char *);

struct tnode *addtree(struct tnode *p, char *w)
{

    int cond;
    if (p == NULL) {     //llego nueva palabra
        p = talloc();    //creo nuevo nodo
        p->word = mystrdup(w);
        p->count = 1;
        p->left = p->right = NULL;
    } else if ((cond = strcmp(w, p->word)) == 0) {
        p->count++;     // palabra repetida
    } else if (cond < 0) {
        p->left = addtree(p->left, w);
    } else {
        p->right = addtree(p->right, w);
    }
    return p;
}
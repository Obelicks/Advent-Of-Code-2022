#ifndef VECTOR__C
#define VECTOR__C

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "vector.h"

//-----------------------------------------------------------------------------
// Vector, a dynamic array using size doubling to achieve amortized constant time insertion
// There are prerequisites mentions in each function description. The user has to make sure
// that these conditions are fulfilled before the function call. Nevertheless, the function
// should check these conditions as well and react accordingly (e.g., exit the program)
//-----------------------------------------------------------------------------

// forward declare structs and bring them from the tag namespace to the ordinary namespace
//typedef struct Vector Vector;

// actually define the structs
// Initialize a vector to be empty
// Pre: 'vector' != NULL
void expand_vector_array(Vector *vector){
    if(vector->size == vector->max_size){
        vector->max_size=vector->max_size*2;
        vector->array=realloc(&vector, vector->max_size);
    }
}
void vector_init(Vector *vector){
    vector->array = malloc(8);
    vector->max_size = 8;
    vector->size=0;
}

// Deallocate internal structures of the vector
// Note: the user is responsible for deleting all values
// Note: the user is responsible for deleting the actual vector if it was dynamically allocated
void vector_delete(Vector *vector){
    free(vector);
}

// Insert a new element at the end of the vector
// Pre: 'vector' != NULL
void vector_push(Vector *vector, void *value){
    vector->array[vector->size]= value;
    vector->size++;
}

// Remove the last element in the vector and return the value
// Pre: the vector is non-empty, 'vector' != NULL
void *vector_pop(Vector *vector){
    void *temp = vector->array[vector->size];
    free(vector->array[vector->size]);
    return temp;
}

// Return the number of elements in the vector
// Pre: 'vector' != NULL
size_t vector_size(const Vector *vector){
    return (size_t) vector->size;
}

// Return the current capacity of the vector
// Pre: 'vector' != NULL
size_t vector_capacity(const Vector *vector){
    return (size_t) vector->max_size;
}

// Return the value at the given index
// Pre: index < vector_size(vector)
void *vector_get_element(const Vector *vector, size_t index){
    return vector->array[index];
}

// Return a pointer to the underlying array
void **vector_get_array(const Vector *vector){
    return (void **) &vector->array;
}

void print_array(Vector vector){
    int i;
    for (i=0;i<vector.size;i++){
        int *temp = (int *)vector.array[i];
        printf("%i\n", *temp);
    }
}

int main( int argc, const char* argv[] ) {
    /*lets do some testing*/
    Vector s;
    vector_init(&s);
    int temp = 10;
    void *val = temp;
    s.array[0] = &val;
    s.size++;
    int hej = 20;
    void *phej = hej;
    s.array[1] = &phej;
    s.size++;
    vector_push(&s, &phej);
    print_array(s);
}
#endif

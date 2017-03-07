#include <stdlib.h>
#include <math.h>
#include <Python.h>

#define CHUNK_SIZE 16

int compare_int(const void * a, const void * b) {
    if( *(int*)a == *(int*)b ) return 0;
    return *(int*)a < *(int*)b ? -1 : 1;
}

int * factor(int n) {
	if (n == 0)
		return 0;
	else if (n < 0)
		n *= -1;
	
	int * factors = malloc(CHUNK_SIZE * sizeof(int));
	unsigned int count = 0;
	int increases = 0;
	
	size_t size;
	for (int i = 1; i < ((int) sqrt(n)) + 1; i++) {
		/* increase size of factors array if needed */
		size = CHUNK_SIZE * sizeof(int) * (increases + 1);
		if (count >= (size / sizeof(int)) - 2) {
			factors = realloc(factors, size + (CHUNK_SIZE * sizeof(int)));
			increases++;
		}
		
		/* check if i is a factor */
		if (n % i == 0) {
			if (i == n / i) {
				*(factors + count + 1) = i;
				count++;
			}
			else {
				*(factors + count + 1) = i;
				*(factors + count + 2) = n / i;
				count += 2;
			}
		}
	}
	/* assign the first value to be the number of factors */
	*factors = count;
	
	/* sort the factors */
	qsort(factors + 1, count, sizeof(int), compare_int);
	
	return factors;
}

static PyObject * factor_wrapper(PyObject * self, PyObject * args) {
	int n;
	if (!PyArg_ParseTuple(args, "i", &n))
		return NULL;

	int * factors = factor(n);
	PyObject * retfactors = PyList_New(*factors);

	for (int i = 1; i <= *factors; i++)
		PyList_SetItem(retfactors, i -1, Py_BuildValue("i", *(factors + i)));

	return retfactors;
}

static PyMethodDef functions[] = {
	{"factor_c", factor_wrapper, METH_VARARGS, "Finds the factors of a number"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef factoring_c = {
	PyModuleDef_HEAD_INIT,
	"factoring_c",
	"Faster factoring.",
	-1,
	functions
};

PyMODINIT_FUNC PyInit_factoring_c(void) {
	return PyModule_Create(&factoring_c);
}

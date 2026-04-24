#include <Python.h>
#include <dirent.h>

// This is the C function behind os.listdir()
static PyObject* posix_listdir(PyObject *self, PyObject *args) {
    const char *path = ".";
    DIR *dir;
    struct dirent *entry;
    PyObject *list;

    // Get argument from Python
    if (!PyArg_ParseTuple(args, "|s", &path)) {
        return NULL;
    }

    // Open directory
    dir = opendir(path);
    if (dir == NULL) {
        return PyErr_SetFromErrno(PyExc_OSError);
    }

    // Create Python list
    list = PyList_New(0);

    // Read entries
    while ((entry = readdir(dir)) != NULL) {
        PyObject *name = PyUnicode_FromString(entry->d_name);
        PyList_Append(list, name);
        Py_DECREF(name);
    }

    // Close directory
    closedir(dir);

    return list;
}
"""
Module to handle a binary search tree (bst) data structure.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

from typing import Any, Callable

from DataStructures.List import single_linked_list as sllt
from DataStructures.Utils import error as err

# Importar la definición de nodo desde bst_node.py para evitar duplicación.
from .bst_node import new_node, get_key, get_value



def dflt_tree_node_cmp(key1: Any, key2: Any) -> int:
    """Función de comparación por defecto para los nodos del BST.
    
    Returns:
        int: -1 si key1 < key2, 0 si key1 == key2, 1 si key1 > key2
    """
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


def new_map(cmp_func=dflt_tree_node_cmp) -> dict:
    """Crea un nuevo árbol binario de búsqueda (BST).
    
    Returns:
        dict: Diccionario que representa el BST.
    """
    try:
        _new_bst = dict(
            root=None,
            size=0,
            cmp_func=cmp_func,
            _type="BST"
        )
        if _new_bst["cmp_func"] is None:
            _new_bst["cmp_func"] = dflt_tree_node_cmp
        return _new_bst
    except Exception as exp:
        err("bst", "new_tree()", exp)


def insert(tree: dict, k: Any, v: Any) -> dict:
    """Agrega un nuevo nodo al BST.
    
    Args:
        tree (dict): Árbol en el que se inserta.
        k (Any): Llave del nodo.
        v (Any): Valor del nodo.
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        _root = _insert(_root, k, v, _cmp)
        tree["root"] = _root
    except Exception as exp:
        err("bst", "insert()", exp)


def _insert(node: dict, k: Any, v: Any, cmp_func: Callable) -> dict:
    """Función recursiva para insertar un nodo en el BST."""
    try:
        if node is None:
            node = new_node(k, v)
        else:
            _cmp = cmp_func(k, node["key"])
            if _cmp < 0:
                node["left"] = _insert(node["left"], k, v, cmp_func)
            elif _cmp > 0:
                node["right"] = _insert(node["right"], k, v, cmp_func)
            else:
                node["value"] = v
        _left_n = _size(node["left"])
        _right_n = _size(node["right"])
        node["size"] = _left_n + _right_n + 1
        return node
    except Exception as exp:
        err("bst", "_insert()", exp)


def get(tree: dict, k: Any) -> dict:
    """Recupera un nodo del BST."""
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _get(_root, k, _cmp)
    except Exception as exp:
        err("bst", "get()", exp)


def _get(node: dict, k: Any, cmp_func: Callable) -> dict:
    """Función recursiva para buscar un nodo en el BST."""
    try:
        _node = None
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            if _cmp == 0:
                _node = node
            elif _cmp < 0:
                _node = _get(node["left"], k, cmp_func)
            elif _cmp > 0:
                _node = _get(node["right"], k, cmp_func)
        return _node
    except Exception as exp:
        err("bst", "_get()", exp)


def remove(tree: dict, k: Any) -> dict:
    """Elimina un nodo del BST."""
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _remove(_root, k, _cmp)
    except Exception as exp:
        err("bst", "remove()", exp)


def _remove(node: dict, k: Any, cmp_func: Callable) -> dict:
    """Función recursiva para eliminar un nodo del BST."""
    try:
        if node is None:
            return None
        elif node is not None:
            _cmp = cmp_func(k, node["key"])
            if _cmp == 0:
                if node["right"] is None:
                    return node["left"]
                elif node["left"] is None:
                    return node["right"]
                else:
                    _node = node
                    node = _min(node["right"])
                    node["right"] = _delete_min(_node["right"])
                    node["left"] = _node["left"]
            elif _cmp < 0:
                node["left"] = _remove(node["left"], k, cmp_func)
            elif _cmp > 0:
                node["right"] = _remove(node["right"], k, cmp_func)
        _left_n = _size(node["left"])
        _right_n = _size(node["right"])
        node["size"] = _left_n + _right_n + 1
        return node
    except Exception as exp:
        err("bst", "_remove()", exp)


def contains(tree: dict, k: Any) -> bool:
    """Verifica si existe un nodo con la llave dada en el BST."""
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        _found = False
        return _contains(_root, k, _cmp, _found)
    except Exception as exp:
        err("bst", "contains()", exp)


def _contains(node: dict, k: Any, cmp_func: Callable, found: bool) -> bool:
    """Función recursiva para verificar la existencia de un nodo en el BST."""
    try:
        if node is None:
            return found
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            if _cmp == 0:
                found = True
            elif _cmp < 0:
                found = _contains(node["left"], k, cmp_func, found)
            elif _cmp > 0:
                found = _contains(node["right"], k, cmp_func, found)
        return found
    except Exception as exp:
        err("bst", "_contains()", exp)


def size(tree: dict) -> int:
    """Retorna el número de nodos del BST."""
    try:
        return _size(tree["root"])
    except Exception as exp:
        err("bst", "size()", exp)


def _size(node: dict) -> int:
    """Función recursiva para contar el tamaño del BST."""
    if node is None:
        return 0
    return node["size"]


def is_empty(tree: dict) -> bool:
    """Verifica si el BST está vacío."""
    try:
        return tree["root"] is None
    except Exception as exp:
        err("bst", "is_empty()", exp)


def min(tree: dict) -> dict:
    """Recupera la llave mínima del BST."""
    try:
        _min_node = _min(tree["root"])
        if _min_node is not None:
            return _min_node["key"]
        return None
    except Exception as exp:
        err("bst", "min()", exp)


def _min(node: dict) -> dict:
    """Función recursiva para obtener el nodo con la llave mínima."""
    try:
        __min__ = node
        if node is not None:
            if node["left"] is not None:
                __min__ = node
            else:
                __min__ = _min(node["left"])
        return __min__
    except Exception as exp:
        err("bst", "_min()", exp)


def delete_min(tree: dict) -> dict:
    """Elimina el nodo con la llave mínima del BST."""
    try:
        return _delete_min(tree["root"])
    except Exception as exp:
        err("bst", "delete_min()", exp)


def _delete_min(node: dict) -> dict:
    """Función recursiva para eliminar el nodo con la llave mínima."""
    try:
        if node is not None:
            if node["left"] is None:
                return node["right"]
            else:
                node["left"] = _delete_min(node["left"])
            node["size"] = _size(node["left"]) + _size(node["right"]) + 1
        return node
    except Exception as exp:
        err("bst", "_delete_min()", exp)


def max(tree: dict) -> dict:
    """Recupera la llave máxima del BST."""
    try:
        _max_node = _max(tree["root"])
        if _max_node is not None:
            return _max_node["key"]
        return None
    except Exception as exp:
        err("bst", "max()", exp)


def _max(node: dict) -> dict:
    """Función recursiva para obtener el nodo con la llave máxima."""
    try:
        __max__ = None
        if node is not None:
            if node["right"] is not None:
                __max__ = node
            else:
                __max__ = _max(node["right"])
        return __max__
    except Exception as exp:
        err("bst", "_max()", exp)


def delete_max(tree: dict) -> dict:
    """Elimina el nodo con la llave máxima del BST."""
    try:
        return _delete_max(tree["root"])
    except Exception as exp:
        err("bst", "delete_max()", exp)


def _delete_max(node: dict) -> dict:
    """Función recursiva para eliminar el nodo con la llave máxima."""
    try:
        # Implementación pendiente
        pass
    except Exception as exp:
        err("bst", "_delete_max()", exp)


def height(tree: dict) -> int:
    """Retorna la altura del BST."""
    try:
        return _height(tree["root"])
    except Exception as exp:
        err("bst", "height()", exp)


def _height(node: dict) -> int:
    try:
        if node is None:
            return -1
        else:
            left_h = _height(node["left"])
            right_h = _height(node["right"])
            return max(left_h, right_h) + 1
    except Exception as exp:
        err("bst", "_height()", exp)


def keys(tree: dict) -> dict:
    """Retorna una lista de llaves del BST."""
    try:
        keys_lt = sllt.new_list(cmp_function=tree["cmp_func"])
        return keys_lt
    except Exception as exp:
        err("bst", "keys()", exp)


def _keys(node: dict, keys_lt: dict) -> None:
    # Implementación pendiente
    pass


def values(tree: dict) -> dict:
    """Retorna una lista de valores del BST."""
    try:
        values_lt = sllt.new_list(cmp_function=tree["cmp_func"])
        return values_lt
    except Exception as exp:
        err("bst", "values()", exp)


def _values(node: dict, values_lt: dict) -> None:
    # Implementación pendiente
    pass

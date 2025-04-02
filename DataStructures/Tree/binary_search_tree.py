"""
Module to handle a binary search tree (bst) data structure.

This code is based on the implementation proposed by the following authors/books:
    #. Algorithms, 4th Edition, Robert Sedgewick and Kevin Wayne.
    #. Data Structure and Algorithms in Python, M.T. Goodrich, R. Tamassia, M.H. Goldwasser.
"""

# import python modules
from typing import Any, Callable

# import modules for data structures ranges in tree
from DataStructures.List import single_linked_list as sllt

# import error handler
from DataStructures.Utils import error as err

# import map entry
from DataStructures.Tree import bst_node as trn


def dflt_tree_node_cmp(key1: Any, key2: Any) -> int:
    """dflt_tree_node_cmp funcion de comparacion por defecto para los nodos de un árbol binario de búsqueda (BST).

    Args:
        key1 (Any): primera llave a comparar
        key2 (Any): segunda llave a comparar

    Returns:
        int: -1 si key1 < key2, 0 si key1 == key2, 1 si key1 > key2
    """
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


def new_tree(cmp_func=dflt_tree_node_cmp) -> dict:
    """new_tree _crea un nuevo árbol binario de búsqueda (BST) y lo retorna.

    Args:
        cmp_func (function, optional): funcion de comparacion para los elementos del árbol. Por defecto es dflt_tree_node_cmp

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST)
    """
    try:
        # definir el árbol binario de búsqueda (BST)
        # y sus propiedades
        # root: nodo raiz del árbol
        # size: tamaño del árbol
        # cmp_func: funcion de comparacion para los elementos del árbol
        # _type: tipo de árbol (BST o RBT)
        _new_bst = dict(
            root=None,
            size=0,
            cmp_func=cmp_func,
            _type="BST"
        )
        if _new_bst["cmp_func"] is None:
            _new_bst["cmp_func"] = dflt_tree_node_cmp
        # retorna el árbol binario de búsqueda (BST)
        return _new_bst
    except Exception as exp:
        err("bst", "new_tree()", exp)


def insert(tree: dict, k: Any, v: Any) -> dict:
    """insert aggrega un nuevo nodo al árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)
        k (Any): llave del nodo a agregar
        v (Any): valor del nodo a agregar

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST) actualizado
    """
    try:
        # configurando los parametros para la funcion recursiva
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        # invocando la funcion recursiva para agregar el nodo al árbol
        _root = _insert(_root, k, v, _cmp)
        # actualizando la raiz del árbol
        tree["root"] = _root
    except Exception as exp:
        err("bst", "insert()", exp)


def _insert(node: dict, k: Any, v: Any, cmp_func: Callable) -> dict:
    """_insert funcion recursiva que agrega un nuevo nodo al árbol binario de búsqueda (BST) y lo retorna.

    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a agregar
        v (Any): valor del nodo a agregar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST) actualizado
    """
    try:
        # caso base, el arbol esta vacio
        if node is None:
            node = trn.new_bst_node(k, v, 1)
        # caso base, el arbol no esta vacio
        else:
            _cmp = cmp_func(k, node["key"])
            # si la llave es menor, insertar en el subarbol izquierdo
            if _cmp < 0:
                node["left"] = _insert(node["left"],
                                       k,
                                       v,
                                       cmp_func)
            # si la llave es mayor, insertar en el subarbol derecho
            elif _cmp > 0:
                node["right"] = _insert(node["right"],
                                        k,
                                        v,
                                        cmp_func)
            # si la llave es igual, actualizar el valor
            else:
                node["value"] = v
        _left_n = _size(node["left"])
        _right_n = _size(node["right"])
        # actualizar el tamaño del nodo
        node["size"] = _left_n + _right_n + 1
        return node
    except Exception as exp:
        err("bst", "_insert()", exp)


def get(tree: dict, k: Any) -> dict:
    """get recupera un nodo del árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)
        k (Any): llave del nodo a recuperar

    Returns:
        dict: diccionario con el nodo recuperado
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _get(_root, k, _cmp)
    except Exception as exp:
        err("bst", "get()", exp)


def _get(node: dict, k: Any, cmp_func: Callable) -> dict:
    """_get funcion recursiva que recupera un nodo del árbol binario de búsqueda (BST) y lo retorna.

    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a recuperar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario con el nodo recuperado
    """
    try:
        # caso base, el arbol esta vacio
        _node = None
        # caso base, el arbol no esta vacio
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            # si el nodo es igual a la llave, retornar el nodo
            if _cmp == 0:
                _node = node
            # si el nodo es menor que la llave, buscar en el subarbol izquierdo
            elif _cmp < 0:
                _node = _get(node["left"], k, cmp_func)
            # si el nodo es mayor que la llave, buscar en el subarbol derecho
            elif _cmp > 0:
                _node = _get(node["right"], k, cmp_func)
        return _node
    except Exception as exp:
        err("bst", "_get()", exp)


def remove(tree: dict, k: Any) -> dict:
    """remove elimina un nodo del árbol binario de búsqueda (BST) y retorna el nodo a eliminar.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)
        k (Any): llave del nodo a eliminar

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST) actualizado
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        return _remove(_root, k, _cmp)
    except Exception as exp:
        err("bst", "remove()", exp)


def _remove(node: dict, k: Any, cmp_func: Callable) -> dict:
    """_remove funcion recursiva que elimina un nodo del árbol binario de búsqueda (BST) y retorna el nodo a eliminar.

    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a eliminar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST) actualizado
    """
    try:
        # caso base, el arbol esta vacio\
        if node is None:
            return None
        # caso base, el arbol no esta vacio
        elif node is not None:
            _cmp = cmp_func(k, node["key"])
            # si la llave es igual
            if _cmp == 0:
                # caso 1, el nodo no tiene hijo derecho
                if node["right"] is None:
                    return node["left"]
                # caso 2, el nodo no tiene hijo izquierdo
                elif node["left"] is None:
                    return node["right"]
                # caso 3, el nodo tiene ambos hijos
                else:
                    _node = node
                    # encontrar el nodo minimo del subarbol derecho
                    node = _min(node["right"])
                    # reemplazar el nodo por el nodo minimo
                    node["right"] = _delete_min(_node["right"])
                    node["left"] = _node["left"]
            # si la llave es menor, buscar en el subarbol izquierdo
            elif _cmp < 0:
                node["left"] = _remove(node["left"], k, cmp_func)
            # si la llave es mayor, buscar en el subarbol derecho
            elif _cmp > 0:
                node["right"] = _remove(node["right"], k, cmp_func)
        # actualizar el tamaño del nodo
        _left_n = _size(node["left"])
        _right_n = _size(node["right"])
        node["size"] = _left_n + _right_n + 1
        return node
    except Exception as exp:
        err("bst", "_remove()", exp)


def contains(tree: dict, k: Any) -> bool:
    """contains revisa si un nodo existe en el árbol binario de búsqueda (BST) y retorna True o False.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)
        k (Any): llave del nodo a buscar

    Returns:
        bool: True si el nodo existe, False si no existe
    """
    try:
        _root = tree["root"]
        _cmp = tree["cmp_func"]
        _found = False
        return _contains(_root, k, _cmp, _found)
    except Exception as exp:
        err("bst", "contains()", exp)


def _contains(node: dict, k: Any, cmp_func: Callable, found: bool) -> bool:
    """_contains funcion recursiva que revisa si un nodo existe en el árbol binario de búsqueda (BST) y retorna True o False.

    Args:
        node (dict): nodo actual del árbol
        k (Any): llave del nodo a buscar
        cmp_func (Callable): funcion de comparacion para los elementos del árbol
        found (bool): bandera que indica si el nodo fue encontrado. False por defecto

    Returns:
        bool: True si el nodo existe, False si no existe
    """
    try:
        # caso base, el arbol esta vacio
        if node is None:
            return found
        # caso base, el arbol no esta vacio
        if node is not None:
            _cmp = cmp_func(k, node["key"])
            # si la llave es igual, retornar True
            if _cmp == 0:
                found = True
            # si la llave es menor, buscar en el subarbol izquierdo
            elif _cmp < 0:
                found = _contains(node["left"], k, cmp_func, found)
            # si la llave es mayor, buscar en el subarbol derecho
            elif _cmp > 0:
                found = _contains(node["right"], k, cmp_func, found)
        return found
    except Exception as exp:
        err("bst", "_contains()", exp)


def size(tree: dict) -> int:
    """size contador de nodos del árbol binario de búsqueda (BST) y retorna el tamaño del árbol.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)

    Returns:
        int: tamaño del árbol binario de búsqueda (BST)
    """
    try:
        return _size(tree["root"])
    except Exception as exp:
        err("bst", "size()", exp)


def _size(node: dict) -> int:
    """_size funcion recursiva que cuenta los nodos del árbol binario de búsqueda (BST) y retorna el tamaño del árbol.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        int: tamaño del árbol binario de búsqueda (BST), por defecto 0. Ademas, recordar que el nodo BST por defecto es de tamaño 1
    """
    if node is None:
        return 0
    return node["size"]


def is_empty(tree: dict) -> bool:
    """is_empty revisa si el árbol binario de búsqueda (BST) está vacío y retorna True o False.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)

    Returns:
        bool: True si el árbol está vacío, False si no está vacío
    """
    try:
        return tree["root"] is None
    except Exception as exp:
        err("bst", "is_empty()", exp)


def min(tree: dict) -> dict:
    """min recupera el nodo con la llave mínima del árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)

    Returns:
        dict: diccionario con el nodo minimo
    """
    try:
        _min_node = _min(tree["root"])
        if _min_node is not None:
            return _min_node["key"]
        return None
    except Exception as exp:
        err("bst", "min()", exp)


def _min(node: dict) -> dict:
    """_min funcion recursiva que recupera el nodo con la llave mínima del árbol binario de búsqueda (BST) y lo retorna.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        dict: diccionario con el nodo minimo
    """
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
    """delete_min elimina el nodo con la llave mínima del árbol binario de búsqueda (BST) y retorna el nodo a eliminar.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST) actualizado
    """
    try:
        return _delete_min(tree["root"])
    except Exception as exp:
        err("bst", "delete_min()", exp)


def _delete_min(node: dict) -> dict:
    """_delete_min funcion recursiva que elimina el nodo con la llave mínima del árbol binario de búsqueda (BST) y retorna el nodo a eliminar.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST) actualizado
    """
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
    """max recupera el nodo con la llave máxima del árbol binario de búsqueda (BST) y lo retorna.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)

    Returns:
        dict: diccionario con el nodo maximo
    """
    try:
        _max_node = _max(tree["root"])
        if _max_node is not None:
            return _max_node["key"]
        return None
    except Exception as exp:
        err("bst", "max()", exp)


def _max(node: dict) -> dict:
    """_max funcion recursiva que recupera el nodo con la llave máxima del árbol binario de búsqueda (BST) y lo retorna.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        dict: diccionario con el nodo maximo
    """
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
    """delete_max elimina el nodo con la llave máxima del árbol binario de búsqueda (BST) y retorna el nodo a eliminar.

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST) actualizado
    """
    try:
        return _delete_max(tree["root"])
    except Exception as exp:
        err("bst", "delete_max()", exp)


def _delete_max(node: dict) -> dict:
    """_delete_max funcion recursiva que elimina el nodo con la llave máxima del árbol binario de búsqueda (BST) y retorna el nodo a eliminar.

    Args:
        node (dict): diccionario que representa el nodo actual del árbol

    Returns:
        dict: diccionario que representa el árbol binario de búsqueda (BST) actualizado
    """
    try:
        pass
    except Exception as exp:
        err("bst", "_delete_max()", exp)


def height(tree: dict) -> int:
    """height retorna la altura del árbol binario de búsqueda (BST).

    Args:
        tree (dict): diccionario que representa el árbol binario de búsqueda (BST)

    Returns:
        int: altura del árbol binario de búsqueda (BST)
    """
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
    """keys _summary_

    Args:
        tree (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        keys_lt = sllt.new_list(cmp_function=tree["cmp_func"])
        return keys_lt
    except Exception as exp:
        err("bst", "keys()", exp)


def _keys(node: dict, keys_lt: dict) -> None:
    pass


def values(tree: dict) -> dict:
    """values _summary_

    Args:
        tree (dict): _description_

    Returns:
        dict: _description_
    """
    try:
        values_lt = sllt.new_list(cmp_function=tree["cmp_func"])
        return values_lt
    except Exception as exp:
        err("bst", "values()", exp)


def _values(node: dict, values_lt: dict) -> None:
    pass
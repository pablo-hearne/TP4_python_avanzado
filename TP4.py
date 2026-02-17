"""Ejercicio 1: "Fuerza de Manos"

Descripción:
Se modelará un sistema en el que una persona tiene dos manos, cada una con una capacidad de carga máxima. 
Además, la persona posee una fuerza total, que representa el peso máximo que puede levantar combinando ambas manos.

El objetivo es determinar si una persona puede levantar un objeto de determinado peso usando una o ambas manos.

Requisitos del programa:

Crear una clase Mano

Debe tener un atributo para almacenar el peso máximo que puede sostener.
Debe contener un método para verificar si una mano puede sostener un objeto por sí sola.
Crear una clase Persona

Debe tener dos manos.
Debe tener un atributo que represente su fuerza total (peso máximo que puede levantar sumando ambas manos).
Debe incluir un método que reciba un peso y determine si la persona puede levantarlo con una sola mano o con ambas.
Casos de prueba esperados:

Una persona con suficiente fuerza total y con manos capaces de sostener el objeto, debe poder levantarlo.
Si el objeto es demasiado pesado para una sola mano pero no para ambas juntas, debe levantarlo con ambas manos.
Si el objeto excede la fuerza total de la persona, no podrá levantarlo.
Pista:
Usar POO para estructurar bien las clases y sus relaciones. 

Definir métodos que permitan tomar decisiones sobre si el objeto puede levantarse o no.


------------------------------------------------------
Ejercicio 2: "Sistema de Compra y Envío de Productos"
------------------------------------------------------

Descripción:
Se requiere un sistema de compra y venta de productos,
donde los usuarios puedan elegir entre diferentes métodos de entrega.

Cada tipo de servicio de entrega tiene sus propias características, 
como el costo del envío y el tiempo estimado de entrega.

Objetivo:
Diseñar un sistema flexible donde, si en el futuro se agregan nuevos métodos de entrega, 
no sea necesario modificar el código existente.

Requisitos del programa:

Crear una clase Producto

Debe contener atributos como nombre y precio.
Crear una clase Pedido

Debe permitir asociar un producto con un método de envío.
Debe poder calcular el costo total sumando el precio del producto y el costo del envío.
Debe poder mostrar el tiempo estimado de entrega según el tipo de envío seleccionado.
Debe implementar un método especial (__str__) que dé formato legible al pedido para su almacenamiento.
Persistencia de datos:

Se debe usar un método estático para registrar los pedidos en un archivo externo.

Puede ser un archivo .txt o .json (a elección del programador).

El método debe recibir un pedido y guardar sus datos utilizando el __str__ o convertirlos a formato adecuado para JSON.


Diferentes tipos de envío

Crear al menos tres métodos de entrega distintos, por ejemplo:
Envío estándar: Económico, pero demora más.
Envío express: Más caro, pero entrega rápida.
Envío personalizado: Puede tener un costo variable dependiendo de la distancia.
Casos de prueba esperados:

Un usuario debe poder elegir el tipo de envío.
El sistema debe calcular el costo total correctamente.
Si en el futuro se agregan nuevos métodos de envío, el código debe seguir funcionando sin cambios.
Pista:
Organizar el código usando clases y herencia para estructurar los distintos tipos de envío.
Asegurar que el sistema sea escalable, permitiendo agregar más opciones sin alterar las clases existentes.
"""



"""
                    Ejercicio 1
"""


class Mano():
    def __init__(self,strength):
        self.strength = strength
        pass
    def movable(self,weight):
        return self.strength >= weight
    pass

class Persona():
    def __init__(self,hand1:Mano,hand2:Mano) -> None:
        self.right_hand = hand1
        self.left_hand = hand2
        self.total_strength = hand1.strength + hand2.strength
        pass
    def movable(self,weight):
        if weight < self.total_strength:
            if self.right_hand.movable(weight):
                print ("Se puede levantar con la mano derecha!!")
                return
            elif self.left_hand.movable(weight):
                print("Se puede levantar con la mano izquierda!!")
                return
            print("Se debe levantar con las dos manos")
            return
        else:
            print("No se puede levantar el objeto")
            return
    pass


"""
                    Ejercicio 2 


            ------------------------------------------------------------------------------
            Quiero pedir disculpas de manera pública porque entre que me ayudé con IA y quise usar
            las consignas en español todo éste ejercicio está en spanglish
            ------------------------------------------------------------------------------
"""


class Producto():
    def __init__(self,product_name,price) -> None:
        self.product_name = product_name
        self.price = price
        pass

class Metodo_de_envio():
    def __init__(self,cost,time):
        self.cost = cost
        self.time = time
        pass
    def envio(self) -> str:
        return ""

class Envio_express(Metodo_de_envio):
    """
    Clase de Envío Exprés
    """
    def __init__(self, cost, time):
        super().__init__(cost, time)
        self.cost = 10000
        self.time = 24
        pass

    def envio(self):
        return "Envío expres"
    pass

class Envio_estandar(Metodo_de_envio):
    """
    Clase de un Envío Estándar
    """
    def __init__(self, cost, time):
        super().__init__(cost, time)
        self.cost = 5000
        self.time = 72
        pass
    def envio(self):
        return "Envío estándar"
    
class Envio_personalizado(Metodo_de_envio):
    """
    Clase de Envío Personalizada
    """
    def __init__(self, cost, time):
        super().__init__(cost, time)
        self.cost = cost
        self.time = time
        pass

    def envio(self):
        return "Envío Personalizado"


class Pedido:
    """Clase que representa un pedido individual."""
    def __init__(self, id_pedido,Producto : Producto, metodo_envio : Metodo_de_envio):
        self.id_pedido = id_pedido
        self.Producto = Producto
        self.metodo_envio = metodo_envio
        pass


    def __str__(self):
        # Esta función define cómo se imprime el pedido en pantalla
        return f"Pedido #{self.id_pedido} | Artículo: {self.Producto.product_name} | Envío: {self.metodo_envio.envio()} | Precio final: {self.Producto.price + self.metodo_envio.cost}"
    pass

import os
import json

class Gestor_pedidos():
    data_base = "pedidos.json"
    
    @staticmethod
    def pedidos_reading() -> list:
        if os.path.exists(Gestor_pedidos.data_base):
            try:
                with open(Gestor_pedidos.data_base, "r") as f:
                    lista_pedidos = json.load(f)
                    return lista_pedidos
            except (ValueError, json.JSONDecodeError) as e:
                return [e]


    @staticmethod
    def pedidos_storage(Pedido:Pedido):
            try:
                lista_pedidos = Gestor_pedidos.pedidos_reading()
                
            except (ValueError, json.JSONDecodeError):
                lista_pedidos = []
            
            lista_pedidos.append(Pedido)
            try:
                with open(Gestor_pedidos.data_base, "w") as f:
                    json.dump(lista_pedidos, f, indent=4, ensure_ascii=False)
                    print("✓ Pedido registrado")
            except IOError as e:
                print(f"Error al escribir en el archivo: {e}")
        pass

    
        


class SistemaPedidos:
    """Clase para gestionar la lista de pedidos."""
    def __init__(self):
        self.lista_pedidos = []

    def agregar_pedido(self, id_pedido, cliente, articulo, metodo_envio):
        nuevo_pedido = Pedido(id_pedido, cliente, articulo, metodo_envio)
        self.lista_pedidos.append(nuevo_pedido)
        print(f"✅ Pedido #{id_pedido} registrado con éxito.")

    def mostrar_pedidos(self):
        print("\n--- Registro Actual de Pedidos ---")
        if not self.lista_pedidos:
            print("No hay pedidos almacenados en este momento.")
        else:
            for pedido in self.lista_pedidos:
                print(pedido)
        print("----------------------------------\n")
    pass



# ==========================================
# Ejemplo de uso del programa
# ==========================================

# 1. Iniciamos el sistema
mi_sistema = SistemaPedidos()

# 2. Agregamos algunos pedidos de prueba
mi_sistema.agregar_pedido(101, "Ana García", "Laptop", "Envío Express")
mi_sistema.agregar_pedido(102, "Juan Pérez", "Teclado Mecánico", "Retiro en Tienda")
mi_sistema.agregar_pedido(103, "Carlos López", "Monitor 24 pulgadas", "Correo Estándar")

# 3. Mostramos todos los pedidos almacenados
mi_sistema.mostrar_pedidos()














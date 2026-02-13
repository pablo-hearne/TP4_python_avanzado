"""Ejercicio 1: "Fuerza de Manos"

Descripción:
Se modelará un sistema en el que una persona tiene dos manos, cada una con una capacidad de carga máxima. Además, la persona posee una fuerza total, que representa el peso máximo que puede levantar combinando ambas manos.

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
Usar POO para estructurar bien las clases y sus relaciones. Definir métodos que permitan tomar decisiones sobre si el objeto puede levantarse o no.

Ejercicio 2: "Sistema de Compra y Envío de Productos"

Descripción:
Se requiere un sistema de compra y venta de productos, donde los usuarios puedan elegir entre diferentes métodos de entrega.

Cada tipo de servicio de entrega tiene sus propias características, como el costo del envío y el tiempo estimado de entrega.

Objetivo:
Diseñar un sistema flexible donde, si en el futuro se agregan nuevos métodos de entrega, no sea necesario modificar el código existente.

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
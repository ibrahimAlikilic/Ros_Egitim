#!/usr/bin/env python3

###################################################################

# Düğüm oluşturma adımları :
# 1) Kütüphaneleri ekle
# 2) class yaz
# 3) Metot yaz
# 4) if __name__ cloğunu yaz

###################################################################

# 1)
import rclpy
from rclpy.node import Node

###################################################################

# 2)
class CustomNodeName(Node):
    def __init__(self): # Bu, sınıfın kurucu fonksiyonudur ve nesne oluşturulduğunda çalışır.
        super().__init__("custom_node_name")
        '''
        super(), üst sınıf olan Node'un kurucu metodunu çağırır.
        Node sınıfı, ROS 2'nin temel düğüm sınıfıdır ve düğüm oluşturabilmek için bu sınıfın kurucu fonksiyonunu çağırmamız gerekir.
        "custom_node_name" bu düğümün adıdır. ROS 2'de her düğümün bir adı olması gerekir.
        '''
'''
Bu Kodun Yaptığı İşler Özetle:
Bir ROS 2 düğümü oluşturan CustomNodeName adlı bir sınıf tanımlar.
Bu sınıf, Node sınıfından miras alarak bir ROS düğümü haline gelir.
Sınıfın kurucu fonksiyonunda super().__init__() çağrılarak düğüm adı "custom_node_name" olarak belirlenir.

'''

###################################################################
# 3)
def main(args=None):
    rclpy.init(args=args)
    node=CustomNodeName() # Node oluşturmak için class'ımı kullanmış oluyorum ve nesneye yönelik hale getirmiş oluoyurm.
    rclpy.spin(node)
    rclpy.shutdown()
        

###################################################################

# 4)
if __name__=="__main__":
    main()

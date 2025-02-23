#!/usr/bin/env python3

###################################################################

# 1)
import rclpy
from rclpy.node import Node

###################################################################

# 2)
class CunterNode(Node):
    def __init__(self): # Bu, sınıfın kurucu fonksiyonudur ve nesne oluşturulduğunda çalışır.
        super().__init__("counter_node")

        self.counter_=0
        self.create_timer(1,self.timer_collback) # periyodumuzu tanımladık = 1sn.
    
    def timer_collback(self):
        self.counter_+=1
        self.get_logger().info("Hello World "+str(self.counter_)) # "info" sadece "string" alır.
    

###################################################################
# 3)
def main(args=None):
    rclpy.init(args=args)
    node=CunterNode() # Node oluşturmak için class'ımı kullanmış oluyorum ve nesneye yönelik hale getirmiş oluoyurm.
    rclpy.spin(node)
    rclpy.shutdown()

###################################################################

# 4)
if __name__=="__main__":
    main()
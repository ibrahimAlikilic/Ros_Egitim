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
from example_interfaces.msg import String

###################################################################

# 2)
class RemoteComtrollerNode(Node):
    def __init__(self): # Bu, sınıfın kurucu fonksiyonudur ve nesne oluşturulduğunda çalışır.
        super().__init__("remote_controller_node")
        self.subscriber_ = self.create_subscription(String , "channel_something", self.callback_television , 10) 
                                # Mesaj tipi 'String' olan yayına abone oluyorum , topic => yayıncı , call_back methodu , kuyruk sayım 

        self.get_logger().info("Remote Controller has been subscribed !")

    def callback_television(self,msg):
        self.get_logger().info(msg.data)

###################################################################

# 3)
def main(args=None):
    rclpy.init(args=args)
    node=RemoteComtrollerNode() # Node oluşturmak için class'ımı kullanmış oluyorum ve nesneye yönelik hale getirmiş oluoyurm.
    rclpy.spin(node)
    rclpy.shutdown()
        

###################################################################

# 4)
if __name__=="__main__":
    main()
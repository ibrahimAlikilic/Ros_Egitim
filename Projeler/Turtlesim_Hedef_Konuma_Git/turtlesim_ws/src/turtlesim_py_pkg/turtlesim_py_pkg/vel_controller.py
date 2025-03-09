#!/usr/bin/env python3

###################################################################

# Düğüm oluşturma adımları :
# 1) Kütüphaneleri ekle
# 2) class yaz
# 3) Metot yaz
# 4) if __name__ cloğunu yaz

###################################################################

# 1)
import sys # kullanıcıdan değer almak için kullandığımız kütüphane
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # publisher mesaj tipi

###################################################################

# 2)
class VelControllerNode(Node):
    def __init__(self): # Bu, sınıfın kurucu fonksiyonudur ve nesne oluşturulduğunda çalışır.
        super().__init__("vel_controller_node")
        
        # Publisher yazıyoruz:
        self.publisher_=self.create_publisher(Twist , "/turtle1/cmd_vel",10) # /turtle1/cmd_vel nereden geldiğini hatırlamak için ss aldım.
        self.timer=self.create_timer(1,self.publish_vel)

    # Yayın işlemimizi gerçekleştirecek temel methodumuz
    def publish_vel(self): # Açısal velinner hız değerlerimizi buradan yayınlayacağız.
        msg=Twist()
        
        '''
        msg.linear.x = 1.0 # hatırla float olması lazım
        msg.linear.y = 0.0
        # 2 boyutta çalıştığım için z değerine gerek yok

        msg.angular.z = 0.5 # (-3.14) - 3.14 aralığında değerler alır çünkü bu değerler radyan cinsindendir.
        # aynı şekilde 2 boyutta çalıştığımız için açısal olarak sadece z var.
        
        '''
        
        # Açısal hız = doğrusal hız / radius ( yarı çap ) değeri.
        # Diyelim ki yukarıdaki değerleri drek vermeyeceim de bu değerleri ben göndereceğim.
        linear_x = float(sys.argv[1]) # bu script'im çalışırken benim gönderecek olduğum ilk değer linner x değerimi ifade edecek.
        msg.linear.x = linear_x
        radius = float(sys.argv[2])
        msg.linear.y = 0.0
        msg.angular.z = float(linear_x / radius)
        self.publisher_.publish(msg)

###################################################################

# 3)
def main(args=None):
    rclpy.init(args=args)
    node=VelControllerNode() # Node oluşturmak için class'ımı kullanmış oluyorum ve nesneye yönelik hale getirmiş oluoyurm.
    rclpy.spin(node)
    rclpy.shutdown()
        

###################################################################

# 4)
if __name__=="__main__":
    main()
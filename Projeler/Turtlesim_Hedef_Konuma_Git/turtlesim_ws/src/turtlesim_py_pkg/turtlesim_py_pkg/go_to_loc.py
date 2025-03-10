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
import math # matematiksel hesaplamalar için lazım.
from rclpy.node import Node
from geometry_msgs.msg import Twist # publisher mesaj tipi
from turtlesim.msg import Pose # Pose işlemleri için
###################################################################

# 2)
class GoToLocationNode(Node):
    def __init__(self): # Bu, sınıfın kurucu fonksiyonudur ve nesne oluşturulduğunda çalışır.
        super().__init__("go_to_loc_node")

        # "turtle_controller" içerisinde gerçekleştirmiş olduğumuz karşılaştırma değerlerini ( threshold değeri olarak da adlandırılıyor ) tanımlayalım.
        self.pose_threshold = 0.3 # şimdilik ikisine de aynı değeri verdim ama ileride daha optimum varışlar için linear ve angular için farklı değerler tanımlamak gerekebilir.

        '''
        ihtiyaçlarımız :
        1) Hedef nokta
        2) Hedef noktaya gitmek için hız değerleri
        '''

        # Hedef nokta belirleyelim
        self.target_x = float(sys.argv[1]) # Çıktıda gördük ki sınırlarımız 0.0 - 11.0 [Info : default loc_x =~ 5.5] (ros2 topic echo /turtle1/pose)
        self.target_y = float(sys.argv[2]) # Çıktıda gördük ki sınırlarımız 0.0 - 11.0 [Info : default loc_y =~ 5.5] (ros2 topic echo /turtle1/pose)

        
        # Publisher yazıyoruz:
        self.publisher_=self.create_publisher(Twist , "/turtle1/cmd_vel",10) # /turtle1/cmd_vel nereden geldiğini hatırlamak için ss aldım.
        # Subscriber yazıyoruz :
        self.subscriber = self.create_subscription(Pose,"/turtle1/pose",self.callback_turtle_pose,10)
        self.timer=self.create_timer(1,self.turtle_controller)


        self.get_logger().info("Go To Location Node has been started .")

    def callback_turtle_pose(self,msg): # Değerleri yayınlamak için call back methodu.
        self.pose_=msg

    def turtle_controller(self):
        msg = Twist()
        # Hedefime yönelmek için tanjant kadar dönmem lazım ( basit geometri).
        # Devamlı olarak pose alarak yönelimi ve hedefe varmayı sağlayacağım.
        '''
        ros2 topic info /turtle1/pose 
        Type: turtlesim/msg/Pose
        Publisher count: 1
        Subscription count: 0
        '''
        # İle pose hakkında bilgileri aldım ve pose bilgilerimin "turtlesim/msg/Pose" içerisinde olduğunu öğrendim. Ve bunu 1. aşamada import ettim 

        # 1) hipotenüsten hedefo olan uzaklığımı tespit etmeliyim.
        dist_x = self.target_x - self.pose_.x
        dist_y = self.target_y - self.pose_.y
        # Hedef koordinatları - bulunduğum konumun koordinatları hesabıyla x ve y eksenindeki mesafelerimi hesaplamış oldum artık hipotenüsü hesaplayabilirim.
        distance = math.sqrt(dist_x**2 + dist_y**2)
        # Gerekli uzunlukları öğrentim artık hedefe olan açımı ayarlayabilirim.
        target_theta = math.atan2(dist_y,dist_x) # Hatırlatma : Tanjant değerini hesaplattık.

        # 2) şimdi msg ile göndermem gereken değerleri göndereceğim.
        # Bunlar : 
        '''
        linear → Doğrusal hız (ileri-geri, sağ-sol hareket)
        angular → Açısal hız (dönme hareketi)
        '''
        if abs(target_theta - self.pose_.theta) >self.pose_threshold : # Yani demiş oluyoruz ki benim şu anki z eksenindeki açım ile olmam gereken konumun z ekseni arasındaki fark > 0.1 ise 
                                                                       # Yani dönmeye devam etmem gerekiyorsa 
            # Bu fark açı yönünden kaynaklı negatif de olabilir bu yüzden kontrolümüzü mutlak değer (abs) olarak yaptık.
            msg.angular.z = target_theta - self.pose_.theta # Yapmam gereken açısal hareket
        
        else: # açımızı ayarladık yani artık hedefe döndük şimdi ilerleme vakti
            if distance >= self.pose_threshold : # vardım mı kontrolü için
                msg.linear.x = distance # Artık hipotenüs doğrultusunda olduğumdan direk o çizgi kadar gideceğim.
            else:
                msg.linear.x = 0.0
                self.get_logger().info("Success :)")
        
        # 3) Artık bu yapmış olduğumuz hesaplamaları yayınlayabiliriz.
        self.publisher_.publish(msg)
        

###################################################################

# 3)
def main(args=None):
    rclpy.init(args=args)
    node=GoToLocationNode() # Node oluşturmak için class'ımı kullanmış oluyorum ve nesneye yönelik hale getirmiş oluoyurm.
    rclpy.spin(node)
    rclpy.shutdown()
        

###################################################################

# 4)
if __name__=="__main__":
    main()
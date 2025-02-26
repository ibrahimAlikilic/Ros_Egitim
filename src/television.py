#!/usr/bin/env python3

###################################################################

# 1)
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String # Veri tipini çekeceğimiz kütüphane

###################################################################

# 2)
class ChannelNode(Node):
    def __init__(self): # Bu, sınıfın kurucu fonksiyonudur ve nesne oluşturulduğunda çalışır.
        super().__init__("channel_node")

        self.greeting_ = "Hi awesome people :)"
        self.publisher_=self.create_publisher(String,"channel_something",10)
        # Parametreler :
            # 1 : Düğümümün yayınlayacağı mesajın veri tipi
            # 2 : Topic, yani hangi konu üzerinden mesajımızı yayınlayacağımızı belirtiyoruz
            # 3 : q size , varsayılanı 10dur ve bunun anlamı yayıncının yayınladığı mesajın kuyrukta birikebilme mesaj sayısıdır
        
        # Timer oluşturup "publish_channel" methodumu callback yapmam lazım
        self.timer_ = self.create_timer(0.5,self.publish_channel)

        # Benim düğümüm çalıştığında beni bilgilendirmek amacıyal Log versin
        # Log, bir programın çalışması sırasında hata ayıklama, durum takibi ve performans analizi gibi amaçlarla oluşturulan kayıt mesajlarıdır. Log'lar genellikle bir dosyaya veya terminale yazdırılır ve sistemin nasıl çalıştığını anlamak için kullanılır.
        self.get_logger().info("Channel Something has been published !")

    # veriyi publis etmek için method tanımlayalım.
    def publish_channel(self):
        msg = String() # Local değişkenlerin sonuna "_" konulmazmış.
        msg.data = str(self.greeting_) +"\nWelcome to the Channel Something"
        self.publisher_.publish(msg) # mesajımı yayınla dedim.

###################################################################

# 3)
def main(args=None):
    rclpy.init(args=args)
    node=ChannelNode() # Node oluşturmak için class'ımı kullanmış oluyorum ve nesneye yönelik hale getirmiş oluoyurm.
    rclpy.spin(node)
    rclpy.shutdown()

###################################################################

# 4)
if __name__=="__main__":
    main()
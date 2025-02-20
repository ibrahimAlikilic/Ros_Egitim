#!/usr/bin/env python3
# ilk önce python3'ün path'ini vermem lazım ve bunu her python script'imin başına eklemem lazım.
# ilk başta neden python3 adresini yazdığımızı sorgulamıştım lakin terminator'de çağırırken "python3" şeklinde değil de "./" ile çağırıldığını öğrendim ve bu durumda yazan kod için python adresini belirtmemiz gerektiğini anladım

###################################################################



###################################################################
# Düğüm oluşturma adımları :
# 1) Kütüphaneleri ekle
# 2) Metot yaz
# 3) if __name__ cloğunu yaz

###################################################################

# 1)
import rclpy
from rclpy.node import Node

###################################################################

# 2)
def main(args=None):
    rclpy.init(args=args)
    '''
    1. rclpy.init(args=args) Ne Yapıyor?
        Bu fonksiyon, ROS 2 altyapısını başlatır ve rclpy kütüphanesinin kullanılabilmesi için gerekli ortamı hazırlar.

        * ROS 2'de her bir program (node) rclpy üzerinden ROS sistemine bağlanır.
        * rclpy.init() çağrılmadan önce hiçbir ROS işlemi yapılamaz (mesaj gönderme, dinleme, düğüm oluşturma vb.).
        * Tek seferlik bir işlemdir, bir Python programında sadece bir kez çağrılması gerekir.
   
    2. args=args Parametresi Ne İşe Yarar?
        * Bu parametre, komut satırından gelen argümanları ROS 2'ye iletmeye yarar.
        * Örneğin, terminalden bir ROS 2 düğümünü şu şekilde çalıştırdığını düşünelim:
            python3 simple_py_node.py --ros-args --log-level info
        Bu komutun içindeki --ros-args --log-level info gibi ek argümanlar ROS 2’ye özel komutlar olabilir.
        * Eğer rclpy.init(args=args) fonksiyonuna bu argümanları iletmezsen, ROS 2 bunları anlayamaz ve hata verebilir.
    
    3. Ne Zaman Kullanılır?
        * ROS 2 düğümleri çalıştırmadan önce (Node nesnesi oluşturmadan önce) kullanılır.
        * Komut satırından alınan argümanları ROS 2'ye iletmek için gereklidir.
        * Birden fazla düğüm başlatan bir programda sadece 1 kez çağrılır.
    '''
    node=Node("py_node") # py_node adında bir düğüm oluşturdum
    # çıktı : [INFO] [1740076711.239908791] [py_node]: py_node oluşturuldu.
    # [INFO] : bunu nbir log ,info olfuğunu belirtir.(Log, bir programın veya sistemin çalışması sırasında oluşturduğu kayıtlardır. Programın ne yaptığını, hangi hatalarla karşılaştığını ve nasıl çalıştığını anlamak için loglar kullanılır.)
    # [py_node] : Log'un gönderildiği düğüm 
    node.get_logger().info("py_node oluşturuldu.") # ros'da print yerine bu kullanılır.

    rclpy.spin(node) # py_node düğümümün yaşam döngüsünü başlatyorum
    node.get_logger().info("py_node yaşam döngüsü başladı.")
    rclpy.shutdown() # Ben düğümümü kapattığımda ya da yok ettiğimde düğümümün kapanmasını sağlar.
    node.get_logger().info("py_node kapandı.")


###################################################################

# 3)
if __name__=="__main__":
    main() # Mein methodunu ben "__main__" string'ini çağırdığımda çağır demek.
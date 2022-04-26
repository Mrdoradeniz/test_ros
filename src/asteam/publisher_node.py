
import queue
import roslib; roslib.load_manifest('asteam')
import rospy 
from std_msgs.msg import String



def send_data():

    publisher_node=rospy.publisher("my_topic",String,queue_size=10)
    rospy.init_node("publisher1",anonymous=True)


    while not rospy.is_shutdown():

        msg="Hellow world {}".format(rospy.get_time())

        publisher_node.publish(msg)






if __name__=="__main__":

    try: 
        send_data()


    except rospy.ROSInterruptException:
        pass





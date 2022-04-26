import queue
import roslib;
import rospy 
from std_msgs.msg import String


def callback(data):

    rospy.loginfo("Message has recived : {}".format(data.data))


def listener():

    rospy.init_node("Listener1",anonymous=True)
    
    rospy.Subscriber("my_topic",String,callback)
    
    rospy.spin()



if __name__=="__main__":


    try: 
        listener()

    except rospy.ROSInterruptException:

        pass



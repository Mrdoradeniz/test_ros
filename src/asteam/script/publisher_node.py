
import queue
import roslib;
import rospy 
from std_msgs.msg import String



def send_data():

    publisher_node=rospy.Publisher("my_topic",String,queue_size=10)
    rospy.init_node("publisher1",anonymous=True)
    rate=rospy.Rate(1)
    rospy.loginfo("Loggedn in")

    while not rospy.is_shutdown():

        msg="Hellow world {}".format(rospy.get_time())

        publisher_node.publish(msg)

        rate.sleep()




if __name__=="__main__":

    try: 
        send_data()


    except rospy.ROSInterruptException:
        pass





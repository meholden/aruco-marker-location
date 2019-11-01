import multiprocessing
import time


def withdraw(bal,lock):
    for ii in range(10):
        lock.acquire()
        for i in range(5):
            bal[i]=ii+10*i
        #bal= [6,7,8,9,10]
        #bal.extend([ii+5,ii+6,ii+7,ii+8,ii+9])
        lock.release()
        #print("read {}".format(bal[1:-1]))
        time.sleep(2)
        
    
    
if __name__ == "__main__":
    corners = multiprocessing.Array('i',5)
    
    lock = multiprocessing.Lock()
    
    p1 = multiprocessing.Process(target=withdraw, args=(corners,lock))
    
    p1.start()
    for jj in range(10):
        lock.acquire()
        print("go {} at {}".format(jj,corners[1:-1]))
        lock.release()
        time.sleep(1)
    
    p1.join()
    #p2.join()
        
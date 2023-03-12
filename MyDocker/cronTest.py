import redis
from rq import Queue


COUNT = 0

if __name__ == '__main__':
    COUNT = COUNT + 1
    print(f"Hello Srikanth {COUNT}")
    r = redis.Redis(host='192.168.142.128', port=6379, password='d9f9ef5f2fef8da852b43c58c7f1c6c1')
    print(r.get("Total_Memory"))
    q = Queue(connection=r)
    print("JOBS IN THE QUEUE CURRENLTY : ", q.job_ids)
    r.close()

import redis
from rq import Queue
import pickle
import json

if __name__ == '__main__':
    print("Hello Srikanth")
    r = redis.Redis(host='192.168.142.128', port=6379, password='d9f9ef5f2fef8da852b43c58c7f1c6c1')
    
    
    server_contents = r.lrange('server_resource', 0, -1)
    server_dict = [json.loads(json_dict) for json_dict in server_contents]
    
    Tds = server_dict[0]["Total_Disk_Space"]
    Tm = server_dict[0]["Total_Memory"]/1024
 
    #Tds = int(r.get("Total_Disk_Space"))
    #Tm = int(r.get("Total_Memory"))/1024 
    #print(Tds)
    #print(r.get("Disk_Used"))
    #print(Tm)
    #print(r.get("Used_Memory"))
    
    queue_contents = r.lrange('preds_queue', 0, -1)
    queue_dict = [json.loads(json_dict) for json_dict in queue_contents]
    
    q = Queue(connection=r)
    jobs_ids = q.job_ids
    print("JOBS IN THE QUEUE CURRENLTY : ", jobs_ids)
    
    Disk_InUse = 0
    RAM_InUse = 0
    
    running_jobs = q.jobs
    running_jobs = [job for job in running_jobs if job.get_status()=='started']
    
    for job in running_jobs:
        for dic in queue_dict:
            if dic['simulation_id'] == job.id:
                du = dic['pred_peak_disk_usage']
                ru = max(dic['pred_peak_RAM_simulation'],dic['pred_peak_RAM_results'])
                Disk_InUse = Disk_InUse + du
                RAM_InUse = RAM_InUse + ru
                
    Disk_Avail = max(0,Tds-Disk_InUse)
    RAM_Avail = max(0,Tm-RAM_InUse)
    
    print("Availabile Resources : ",Disk_Avail,RAM_Avail)
    
    queued_jobs = q.jobs
    queued_jobs = [job for job in queued_jobs if job.get_status()=='queued']
    
    for job in queued_jobs:
        for dic in queue_dict:
            if dic['simulation_id'] == job.id:
                q_du = dic['pred_peak_disk_usage']
                q_ru = max(dic['pred_peak_RAM_simulation'],dic['pred_peak_RAM_results'])
                print("Queued Prediction Resources : ",q_du,q_ru)
                if q_du<=Disk_Avail and q_ru<=RAM_Avail:
                    if len(queued_jobs)>1:
                        if q.get_job_position(job)!=0 and queued_jobs[0]!=job:
                            #job.requeue(at_front=True)
                            #nob = q.fetch_job(job.id)
                            job.cancel()
                            print("CANCELLED")
                            q.enqueue_job(job,at_front=True)
                            print("Q's order Changed")
                #elif q_du<=Disk_Avail or q_ru<=RAM_Avail:
                #    if len(queued_jobs)>1:
                #        if q.get_job_position(job)!=0 and queued_jobs[0]!=job:
                #            #job.requeue(at_front=True)
                #            nob = q.fetch_job(job.id)
                #            q.enqueue_job(job,at_front=True)
                #            print("Q's order Changed")
                else:
                    print("Q's order Unchanged")
    r.close()

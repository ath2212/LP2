print("Hello World")


class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


class JobScheduling:
    def __init__(self, jobs):
        self.job_list = jobs
        self.scheduling(self.job_list)

    def scheduling(self, job_list):
        job_list = sorted(job_list, key=self.profit_sort, reverse=True)
        res = []
        curr = 1
        total_profit = 0
        for i in range(len(job_list)):
            if curr <= job_list[i].deadline:
                total_profit += job_list[i].profit
                res.append(job_list[i].id)
                curr += 1
        print("Total profit is {}".format(total_profit))
        print("Job Seq is {}".format(res))

    def profit_sort(self, job):
        return job.profit


def main():
    jobs = [Job('a', 2, 100), Job('b', 1, 19),
            Job('c', 2, 27), Job('d', 1, 25),
            Job('e', 3, 15)]
    # for i in range(int(input("No of jobs"))):
    #     id = input('Enter job id ')
    #     deadline = int(input("enter job deadline"))
    #     profit = int(input("Enter job profit; "))
    #     jobs.append(Job(id, deadline, profit))
    sch = JobScheduling(jobs)

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)


# main()
selectionSort([4, 3, 1, 2])
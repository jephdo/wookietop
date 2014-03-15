import psutil

def poll_processes():
    procs = []
    procs_status = {}
    for p in psutil.process_iter():
        try:
            p.dict = p.as_dict(['username', 'nice', 'memory_info',
                                'memory_percent', 'cpu_percent',
                                'cpu_times', 'name', 'status'])
            try:
                procs_status[p.dict['status']] += 1
            except KeyError:
                procs_status[p.dict['status']] = 1
        except psutil.NoSuchProcess:
            pass
        else:
            procs.append(p)

    # return processes sorted by CPU percent usage
    processes = sorted(procs, key=lambda p: p.dict['cpu_percent'],
                       reverse=True)
    return (processes, procs_status)

def processes_to_dict(processes):
    procs = []

    for p in processes:
        process = {}
        process['pid'] = p.pid
        process['username'] = p.dict.get('username', "")
        process['nice'] = p.dict['nice']
        process['virt'] = getattr(p.dict['memory_info'], 'vms', 0)
        process['res'] = getattr(p.dict['memory_info'], 'rss', 0)
        process['cpu_percent'] = p.dict['cpu_percent']
        process['memory_percent'] = p.dict['memory_percent']
        process['cpu_times'] = 1#p.dict['cpu_times']
        process['name'] = p.dict.get('name', "")

        procs.append(process)

    return procs

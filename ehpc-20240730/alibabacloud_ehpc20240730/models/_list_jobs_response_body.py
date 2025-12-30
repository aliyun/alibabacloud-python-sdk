# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListJobsResponseBody(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ListJobsResponseBodyJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The jobs.
        self.jobs = jobs
        # The page number. Default value: 1
        self.page_number = page_number
        # The number of entries per page. Default value: 10
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListJobsResponseBodyJobs(DaraModel):
    def __init__(
        self,
        job_name: str = None,
        job_spec: main_models.ListJobsResponseBodyJobsJobSpec = None,
    ):
        # The job name.
        self.job_name = job_name
        # The job configurations.
        self.job_spec = job_spec

    def validate(self):
        if self.job_spec:
            self.job_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_spec is not None:
            result['JobSpec'] = self.job_spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobSpec') is not None:
            temp_model = main_models.ListJobsResponseBodyJobsJobSpec()
            self.job_spec = temp_model.from_map(m.get('JobSpec'))

        return self

class ListJobsResponseBodyJobsJobSpec(DaraModel):
    def __init__(
        self,
        array_job_id: str = None,
        array_job_sub_id: str = None,
        array_request: str = None,
        comment: str = None,
        id: str = None,
        job_queue: str = None,
        last_modify_time: str = None,
        node_list: str = None,
        priority: str = None,
        resources: main_models.ListJobsResponseBodyJobsJobSpecResources = None,
        resources_actual_occupied: main_models.ListJobsResponseBodyJobsJobSpecResourcesActualOccupied = None,
        runas_user: str = None,
        start_time: str = None,
        state: str = None,
        stderr_path: str = None,
        stdout_path: str = None,
        submit_time: str = None,
        variables: str = None,
    ):
        # The array job ID.
        self.array_job_id = array_job_id
        # The ID of the job in the array.
        self.array_job_sub_id = array_job_sub_id
        # The queue format of the job.
        # 
        # *   If the job is not in a queue, the output is empty.
        # *   The format is X-Y:Z. X indicates the first index, Y indicates the final index, and Z indicates the step size. For example, 2-7:2 indicates three sub-jobs numbered 2, 4, and 6.
        self.array_request = array_request
        # The job description.
        self.comment = comment
        # The job ID.
        self.id = id
        # The queue name.
        self.job_queue = job_queue
        # The time when the job was last updated.
        self.last_modify_time = last_modify_time
        # The compute nodes that were used to run the job.
        self.node_list = node_list
        # The job priority. Valid values: 0 to 9. A larger value indicates a higher priority.
        self.priority = priority
        # The information about the resources required to run the job.
        self.resources = resources
        # Actual resource usage of the job program
        self.resources_actual_occupied = resources_actual_occupied
        # The user that ran the job.
        self.runas_user = runas_user
        # Job start time.
        self.start_time = start_time
        # The job state. Valid values: (PBS cluster and Slurm cluster)
        # 
        # *   FINISHED/Completed
        # *   RUNNING/Running
        # *   QUEUED/Pending
        # *   FAILED/Failed
        self.state = state
        # The error output path.
        self.stderr_path = stderr_path
        # The standard output path.
        self.stdout_path = stdout_path
        # The time when the job was submitted.
        self.submit_time = submit_time
        # The variables of the job.
        self.variables = variables

    def validate(self):
        if self.resources:
            self.resources.validate()
        if self.resources_actual_occupied:
            self.resources_actual_occupied.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_job_id is not None:
            result['ArrayJobId'] = self.array_job_id

        if self.array_job_sub_id is not None:
            result['ArrayJobSubId'] = self.array_job_sub_id

        if self.array_request is not None:
            result['ArrayRequest'] = self.array_request

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.id is not None:
            result['Id'] = self.id

        if self.job_queue is not None:
            result['JobQueue'] = self.job_queue

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.node_list is not None:
            result['NodeList'] = self.node_list

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.resources_actual_occupied is not None:
            result['ResourcesActualOccupied'] = self.resources_actual_occupied.to_map()

        if self.runas_user is not None:
            result['RunasUser'] = self.runas_user

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.stderr_path is not None:
            result['StderrPath'] = self.stderr_path

        if self.stdout_path is not None:
            result['StdoutPath'] = self.stdout_path

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.variables is not None:
            result['Variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayJobId') is not None:
            self.array_job_id = m.get('ArrayJobId')

        if m.get('ArrayJobSubId') is not None:
            self.array_job_sub_id = m.get('ArrayJobSubId')

        if m.get('ArrayRequest') is not None:
            self.array_request = m.get('ArrayRequest')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobQueue') is not None:
            self.job_queue = m.get('JobQueue')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('NodeList') is not None:
            self.node_list = m.get('NodeList')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Resources') is not None:
            temp_model = main_models.ListJobsResponseBodyJobsJobSpecResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('ResourcesActualOccupied') is not None:
            temp_model = main_models.ListJobsResponseBodyJobsJobSpecResourcesActualOccupied()
            self.resources_actual_occupied = temp_model.from_map(m.get('ResourcesActualOccupied'))

        if m.get('RunasUser') is not None:
            self.runas_user = m.get('RunasUser')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StderrPath') is not None:
            self.stderr_path = m.get('StderrPath')

        if m.get('StdoutPath') is not None:
            self.stdout_path = m.get('StdoutPath')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        return self

class ListJobsResponseBodyJobsJobSpecResourcesActualOccupied(DaraModel):
    def __init__(
        self,
        cores: str = None,
        gpus: str = None,
        memory: str = None,
        nodes: str = None,
    ):
        # Number of CPU cores.
        self.cores = cores
        # Number of CPUs
        self.gpus = gpus
        # Number of memory.
        self.memory = memory
        # Number of compute nodes.
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.gpus is not None:
            result['Gpus'] = self.gpus

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('Gpus') is not None:
            self.gpus = m.get('Gpus')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        return self

class ListJobsResponseBodyJobsJobSpecResources(DaraModel):
    def __init__(
        self,
        cores: str = None,
        gpus: str = None,
        memory: str = None,
        nodes: str = None,
    ):
        # The number of vCPUs that were used to run the job.
        self.cores = cores
        # The number of GPUs that were used to run the job.
        self.gpus = gpus
        # The size of memory that was used to run the job.
        self.memory = memory
        # The number of compute nodes that were used to run the job.
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.gpus is not None:
            result['Gpus'] = self.gpus

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('Gpus') is not None:
            self.gpus = m.get('Gpus')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        return self


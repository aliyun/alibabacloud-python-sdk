# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListQueueTopJobsResponseBody(DaraModel):
    def __init__(
        self,
        queue_top_jobs: main_models.ListQueueTopJobsResponseBodyQueueTopJobs = None,
        request_id: str = None,
    ):
        # The job details.
        self.queue_top_jobs = queue_top_jobs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.queue_top_jobs:
            self.queue_top_jobs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.queue_top_jobs is not None:
            result['queueTopJobs'] = self.queue_top_jobs.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queueTopJobs') is not None:
            temp_model = main_models.ListQueueTopJobsResponseBodyQueueTopJobs()
            self.queue_top_jobs = temp_model.from_map(m.get('queueTopJobs'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListQueueTopJobsResponseBodyQueueTopJobs(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ListQueueTopJobsResponseBodyQueueTopJobsJobs] = None,
        max_results: str = None,
        queue_name: str = None,
        total_cu: str = None,
        total_job_count: int = None,
    ):
        # The list of jobs.
        self.jobs = jobs
        # The maximum number of records returned in a single request.
        self.max_results = max_results
        # The name of the queue.
        self.queue_name = queue_name
        # The total number of CUs consumed by the queue.
        self.total_cu = total_cu
        # The total number of jobs in the queue.
        self.total_job_count = total_job_count

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
        result['jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['jobs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.total_cu is not None:
            result['totalCu'] = self.total_cu

        if self.total_job_count is not None:
            result['totalJobCount'] = self.total_job_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k1 in m.get('jobs'):
                temp_model = main_models.ListQueueTopJobsResponseBodyQueueTopJobsJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('totalCu') is not None:
            self.total_cu = m.get('totalCu')

        if m.get('totalJobCount') is not None:
            self.total_job_count = m.get('totalJobCount')

        return self

class ListQueueTopJobsResponseBodyQueueTopJobsJobs(DaraModel):
    def __init__(
        self,
        cpu_cores: str = None,
        cu: str = None,
        job_id: str = None,
        job_type: str = None,
        memory_gi_b: str = None,
    ):
        # The number of CPU cores requested by the job.
        self.cpu_cores = cpu_cores
        # The number of CUs consumed by the job.
        self.cu = cu
        # The job ID.
        self.job_id = job_id
        # The job type.
        self.job_type = job_type
        # The amount of memory requested by the job.
        self.memory_gi_b = memory_gi_b

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_cores is not None:
            result['cpuCores'] = self.cpu_cores

        if self.cu is not None:
            result['cu'] = self.cu

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_type is not None:
            result['jobType'] = self.job_type

        if self.memory_gi_b is not None:
            result['memoryGiB'] = self.memory_gi_b

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCores') is not None:
            self.cpu_cores = m.get('cpuCores')

        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')

        if m.get('memoryGiB') is not None:
            self.memory_gi_b = m.get('memoryGiB')

        return self


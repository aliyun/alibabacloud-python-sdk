# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListJobExecutorsResponseBody(DaraModel):
    def __init__(
        self,
        exexutors: List[main_models.ListJobExecutorsResponseBodyExexutors] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of executors.
        self.exexutors = exexutors
        # The maximum number of records returned.
        self.max_results = max_results
        # The token for the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.exexutors:
            for v1 in self.exexutors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['exexutors'] = []
        if self.exexutors is not None:
            for k1 in self.exexutors:
                result['exexutors'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exexutors = []
        if m.get('exexutors') is not None:
            for k1 in m.get('exexutors'):
                temp_model = main_models.ListJobExecutorsResponseBodyExexutors()
                self.exexutors.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListJobExecutorsResponseBodyExexutors(DaraModel):
    def __init__(
        self,
        active_tasks: int = None,
        add_time: int = None,
        completed_tasks: int = None,
        disk_used: int = None,
        executor_id: str = None,
        executor_type: str = None,
        failed_tasks: int = None,
        host_port: str = None,
        job_run_id: str = None,
        max_memory: int = None,
        memory_used: int = None,
        rdd_blocks: int = None,
        status: str = None,
        total_cores: int = None,
        total_duration: int = None,
        total_gctime: int = None,
        total_input_bytes: int = None,
        total_shuffle_read: int = None,
        total_shuffle_write: int = None,
        total_tasks: int = None,
        workspace_id: str = None,
    ):
        # The total number of active tasks that the executor is running.
        self.active_tasks = active_tasks
        # The time when the executor was created.
        self.add_time = add_time
        # The total number of completed tasks that the executor has run.
        self.completed_tasks = completed_tasks
        # The disk usage of the executor.
        self.disk_used = disk_used
        # The job executor ID.
        self.executor_id = executor_id
        # The executor type.
        self.executor_type = executor_type
        # The total number of failed tasks that the executor has run.
        self.failed_tasks = failed_tasks
        # The address of the executor.
        self.host_port = host_port
        # The job run ID.
        self.job_run_id = job_run_id
        # The maximum memory of the executor.
        self.max_memory = max_memory
        # The memory usage of the executor.
        self.memory_used = memory_used
        # The number of Resilient Distributed Dataset (RDD) blocks managed by the executor.
        self.rdd_blocks = rdd_blocks
        # The running status of the executor.
        self.status = status
        # The total number of cores for the executor.
        self.total_cores = total_cores
        # The total runtime of the executor.
        self.total_duration = total_duration
        # The total garbage collection (GC) time of the executor.
        self.total_gctime = total_gctime
        # The number of bytes of input data for the executor.
        self.total_input_bytes = total_input_bytes
        # The number of bytes read during the shuffle phase by the executor.
        self.total_shuffle_read = total_shuffle_read
        # The number of bytes written during the shuffle phase by the executor.
        self.total_shuffle_write = total_shuffle_write
        # The total number of tasks that the executor has run.
        self.total_tasks = total_tasks
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_tasks is not None:
            result['activeTasks'] = self.active_tasks

        if self.add_time is not None:
            result['addTime'] = self.add_time

        if self.completed_tasks is not None:
            result['completedTasks'] = self.completed_tasks

        if self.disk_used is not None:
            result['diskUsed'] = self.disk_used

        if self.executor_id is not None:
            result['executorId'] = self.executor_id

        if self.executor_type is not None:
            result['executorType'] = self.executor_type

        if self.failed_tasks is not None:
            result['failedTasks'] = self.failed_tasks

        if self.host_port is not None:
            result['hostPort'] = self.host_port

        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id

        if self.max_memory is not None:
            result['maxMemory'] = self.max_memory

        if self.memory_used is not None:
            result['memoryUsed'] = self.memory_used

        if self.rdd_blocks is not None:
            result['rddBlocks'] = self.rdd_blocks

        if self.status is not None:
            result['status'] = self.status

        if self.total_cores is not None:
            result['totalCores'] = self.total_cores

        if self.total_duration is not None:
            result['totalDuration'] = self.total_duration

        if self.total_gctime is not None:
            result['totalGCTime'] = self.total_gctime

        if self.total_input_bytes is not None:
            result['totalInputBytes'] = self.total_input_bytes

        if self.total_shuffle_read is not None:
            result['totalShuffleRead'] = self.total_shuffle_read

        if self.total_shuffle_write is not None:
            result['totalShuffleWrite'] = self.total_shuffle_write

        if self.total_tasks is not None:
            result['totalTasks'] = self.total_tasks

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeTasks') is not None:
            self.active_tasks = m.get('activeTasks')

        if m.get('addTime') is not None:
            self.add_time = m.get('addTime')

        if m.get('completedTasks') is not None:
            self.completed_tasks = m.get('completedTasks')

        if m.get('diskUsed') is not None:
            self.disk_used = m.get('diskUsed')

        if m.get('executorId') is not None:
            self.executor_id = m.get('executorId')

        if m.get('executorType') is not None:
            self.executor_type = m.get('executorType')

        if m.get('failedTasks') is not None:
            self.failed_tasks = m.get('failedTasks')

        if m.get('hostPort') is not None:
            self.host_port = m.get('hostPort')

        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')

        if m.get('maxMemory') is not None:
            self.max_memory = m.get('maxMemory')

        if m.get('memoryUsed') is not None:
            self.memory_used = m.get('memoryUsed')

        if m.get('rddBlocks') is not None:
            self.rdd_blocks = m.get('rddBlocks')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalCores') is not None:
            self.total_cores = m.get('totalCores')

        if m.get('totalDuration') is not None:
            self.total_duration = m.get('totalDuration')

        if m.get('totalGCTime') is not None:
            self.total_gctime = m.get('totalGCTime')

        if m.get('totalInputBytes') is not None:
            self.total_input_bytes = m.get('totalInputBytes')

        if m.get('totalShuffleRead') is not None:
            self.total_shuffle_read = m.get('totalShuffleRead')

        if m.get('totalShuffleWrite') is not None:
            self.total_shuffle_write = m.get('totalShuffleWrite')

        if m.get('totalTasks') is not None:
            self.total_tasks = m.get('totalTasks')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self


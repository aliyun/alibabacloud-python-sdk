# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class DeleteJobsRequest(DaraModel):
    def __init__(
        self,
        executor_ids: List[str] = None,
        job_scheduler: str = None,
        job_spec: List[main_models.DeleteJobsRequestJobSpec] = None,
    ):
        # The list of executor IDs. A maximum of 100 IDs are supported.
        self.executor_ids = executor_ids
        # The type of the job scheduler.
        # 
        # *   HPC
        # *   K8S
        # 
        # Default value: HPC
        self.job_scheduler = job_scheduler
        # The information about the job to be deleted.
        self.job_spec = job_spec

    def validate(self):
        if self.job_spec:
            for v1 in self.job_spec:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids

        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler

        result['JobSpec'] = []
        if self.job_spec is not None:
            for k1 in self.job_spec:
                result['JobSpec'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids = m.get('ExecutorIds')

        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')

        self.job_spec = []
        if m.get('JobSpec') is not None:
            for k1 in m.get('JobSpec'):
                temp_model = main_models.DeleteJobsRequestJobSpec()
                self.job_spec.append(temp_model.from_map(k1))

        return self

class DeleteJobsRequestJobSpec(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        task_spec: List[main_models.DeleteJobsRequestJobSpecTaskSpec] = None,
    ):
        # The ID of the job to be deleted.\\
        # You can call the ListJobs operation to query job IDs.
        self.job_id = job_id
        # The task details of the job to be deleted.
        self.task_spec = task_spec

    def validate(self):
        if self.task_spec:
            for v1 in self.task_spec:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['TaskSpec'] = []
        if self.task_spec is not None:
            for k1 in self.task_spec:
                result['TaskSpec'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.task_spec = []
        if m.get('TaskSpec') is not None:
            for k1 in m.get('TaskSpec'):
                temp_model = main_models.DeleteJobsRequestJobSpecTaskSpec()
                self.task_spec.append(temp_model.from_map(k1))

        return self

class DeleteJobsRequestJobSpecTaskSpec(DaraModel):
    def __init__(
        self,
        array_index: List[int] = None,
        task_name: str = None,
    ):
        # The list of array job indexes to be deleted.
        self.array_index = array_index
        # The name of the task to be deleted.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self


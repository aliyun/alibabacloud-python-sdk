# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ListLifecycleRetrieveJobsResponseBody(DaraModel):
    def __init__(
        self,
        lifecycle_retrieve_jobs: List[main_models.ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The collection of data retrieval task information.
        self.lifecycle_retrieve_jobs = lifecycle_retrieve_jobs
        # The page number of the list.
        self.page_number = page_number
        # The number of data retrieval tasks on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of data retrieval tasks.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_retrieve_jobs:
            for v1 in self.lifecycle_retrieve_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LifecycleRetrieveJobs'] = []
        if self.lifecycle_retrieve_jobs is not None:
            for k1 in self.lifecycle_retrieve_jobs:
                result['LifecycleRetrieveJobs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lifecycle_retrieve_jobs = []
        if m.get('LifecycleRetrieveJobs') is not None:
            for k1 in m.get('LifecycleRetrieveJobs'):
                temp_model = main_models.ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs()
                self.lifecycle_retrieve_jobs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLifecycleRetrieveJobsResponseBodyLifecycleRetrieveJobs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        discovered_file_count: int = None,
        file_system_id: str = None,
        job_id: str = None,
        paths: List[str] = None,
        retrieved_file_count: int = None,
        status: str = None,
        storage_type: str = None,
        update_time: str = None,
    ):
        # The time when the task was created.
        # 
        # The time follows the ISO 8601 standard in the format of `yyyy-MM-ddTHH:mm:ssZ`.
        self.create_time = create_time
        # The total number of files read by the data retrieval task.
        self.discovered_file_count = discovered_file_count
        # The file system ID.
        self.file_system_id = file_system_id
        # The data retrieval task ID.
        self.job_id = job_id
        # The execution paths of the data retrieval task.
        self.paths = paths
        # The number of files successfully retrieved by the data retrieval task.
        self.retrieved_file_count = retrieved_file_count
        # The status of the data retrieval task. Valid values:
        # - active: running.
        # - canceled: canceled.
        # - completed: completed.
        # - failed: failed.
        self.status = status
        # The storage class. Valid values:
        # - InfrequentAccess: IA storage class.
        # - Archive: Archive storage class.
        self.storage_type = storage_type
        # The time when the task was last updated.
        # 
        # The time follows the ISO 8601 standard in the format of `yyyy-MM-ddTHH:mm:ssZ`.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.discovered_file_count is not None:
            result['DiscoveredFileCount'] = self.discovered_file_count

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.retrieved_file_count is not None:
            result['RetrievedFileCount'] = self.retrieved_file_count

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DiscoveredFileCount') is not None:
            self.discovered_file_count = m.get('DiscoveredFileCount')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('RetrievedFileCount') is not None:
            self.retrieved_file_count = m.get('RetrievedFileCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self


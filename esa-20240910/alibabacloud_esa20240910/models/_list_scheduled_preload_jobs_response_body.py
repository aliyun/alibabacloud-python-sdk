# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListScheduledPreloadJobsResponseBody(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ListScheduledPreloadJobsResponseBodyJobs] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # List of prefetch job details.
        self.jobs = jobs
        # Request ID.
        self.request_id = request_id
        # Total number of records after filtering.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.ListScheduledPreloadJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScheduledPreloadJobsResponseBodyJobs(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        created_at: str = None,
        domains: str = None,
        error_info: str = None,
        execution_count: int = None,
        failed_file_oss: str = None,
        file_id: str = None,
        id: str = None,
        insert_way: str = None,
        name: str = None,
        site_id: int = None,
        task_submitted: int = None,
        task_type: str = None,
        url_count: int = None,
        url_submitted: int = None,
    ):
        # Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # Job creation time.
        self.created_at = created_at
        # List of domains to prefetch.
        self.domains = domains
        # Error message.
        self.error_info = error_info
        # Number of prefetch schedules.
        self.execution_count = execution_count
        # The OSS address of the failed file.
        self.failed_file_oss = failed_file_oss
        # URL list file ID (used for downloading).
        self.file_id = file_id
        # Job ID.
        self.id = id
        # URL insertion method.
        self.insert_way = insert_way
        # Job name.
        self.name = name
        # Site ID
        self.site_id = site_id
        # Number of URLs submitted to the system for prefetching.
        self.task_submitted = task_submitted
        # Task type (refresh or prefetch).
        self.task_type = task_type
        # Total number of URLs.
        self.url_count = url_count
        # Number of URLs submitted.
        self.url_submitted = url_submitted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.domains is not None:
            result['Domains'] = self.domains

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.execution_count is not None:
            result['ExecutionCount'] = self.execution_count

        if self.failed_file_oss is not None:
            result['FailedFileOss'] = self.failed_file_oss

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.id is not None:
            result['Id'] = self.id

        if self.insert_way is not None:
            result['InsertWay'] = self.insert_way

        if self.name is not None:
            result['Name'] = self.name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.task_submitted is not None:
            result['TaskSubmitted'] = self.task_submitted

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.url_count is not None:
            result['UrlCount'] = self.url_count

        if self.url_submitted is not None:
            result['UrlSubmitted'] = self.url_submitted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('ExecutionCount') is not None:
            self.execution_count = m.get('ExecutionCount')

        if m.get('FailedFileOss') is not None:
            self.failed_file_oss = m.get('FailedFileOss')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InsertWay') is not None:
            self.insert_way = m.get('InsertWay')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('TaskSubmitted') is not None:
            self.task_submitted = m.get('TaskSubmitted')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UrlCount') is not None:
            self.url_count = m.get('UrlCount')

        if m.get('UrlSubmitted') is not None:
            self.url_submitted = m.get('UrlSubmitted')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListLiveSnapshotJobsResponseBody(DaraModel):
    def __init__(
        self,
        job_list: List[main_models.ListLiveSnapshotJobsResponseBodyJobList] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sort_by: str = None,
        total_count: int = None,
    ):
        # The list of jobs.
        self.job_list = job_list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The sorting order of the jobs by creation time.
        self.sort_by = sort_by
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.job_list:
            for v1 in self.job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobList'] = []
        if self.job_list is not None:
            for k1 in self.job_list:
                result['JobList'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k1 in m.get('JobList'):
                temp_model = main_models.ListLiveSnapshotJobsResponseBodyJobList()
                self.job_list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLiveSnapshotJobsResponseBodyJobList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        job_id: str = None,
        job_name: str = None,
        snapshot_output: main_models.ListLiveSnapshotJobsResponseBodyJobListSnapshotOutput = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
        time_interval: int = None,
    ):
        # The time when the template was created.
        self.create_time = create_time
        # The job ID.
        self.job_id = job_id
        # The name of the job.
        self.job_name = job_name
        # The output information.
        self.snapshot_output = snapshot_output
        # The state of the job.
        # 
        # Valid values:
        # 
        # *   init: The job is not started.
        # *   paused: The job is paused.
        # *   started: The job is in progress.
        self.status = status
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The interval between two adjacent snapshots. Unit: seconds.
        self.time_interval = time_interval

    def validate(self):
        if self.snapshot_output:
            self.snapshot_output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.snapshot_output is not None:
            result['SnapshotOutput'] = self.snapshot_output.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('SnapshotOutput') is not None:
            temp_model = main_models.ListLiveSnapshotJobsResponseBodyJobListSnapshotOutput()
            self.snapshot_output = temp_model.from_map(m.get('SnapshotOutput'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        return self

class ListLiveSnapshotJobsResponseBodyJobListSnapshotOutput(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        endpoint: str = None,
        storage_type: str = None,
    ):
        # The bucket of the output endpoint. If the storage type is set to oss, the OSS bucket is returned.
        self.bucket = bucket
        # The output endpoint. If the storage type is set to oss, the Object Storage Service (OSS) domain name is returned.
        self.endpoint = endpoint
        # The storage type. The value can only be oss.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListLiveRecordJobsResponseBody(DaraModel):
    def __init__(
        self,
        live_record_jobs: List[main_models.ListLiveRecordJobsResponseBodyLiveRecordJobs] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sort_by: str = None,
        total_count: int = None,
    ):
        # The list of live stream recording jobs.
        self.live_record_jobs = live_record_jobs
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The sorting order. By default, the query results are sorted by creation time in descending order.
        self.sort_by = sort_by
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.live_record_jobs:
            for v1 in self.live_record_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveRecordJobs'] = []
        if self.live_record_jobs is not None:
            for k1 in self.live_record_jobs:
                result['LiveRecordJobs'].append(k1.to_map() if k1 else None)

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
        self.live_record_jobs = []
        if m.get('LiveRecordJobs') is not None:
            for k1 in m.get('LiveRecordJobs'):
                temp_model = main_models.ListLiveRecordJobsResponseBodyLiveRecordJobs()
                self.live_record_jobs.append(temp_model.from_map(k1))

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

class ListLiveRecordJobsResponseBodyLiveRecordJobs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        job_id: str = None,
        name: str = None,
        notify_url: str = None,
        record_output: main_models.ListLiveRecordJobsResponseBodyLiveRecordJobsRecordOutput = None,
        status: str = None,
        stream_input: main_models.ListLiveRecordJobsResponseBodyLiveRecordJobsStreamInput = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # The time when the job was created.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        # The ID of the recording job.
        self.job_id = job_id
        # The name of the recording job.
        self.name = name
        # The callback URL.
        self.notify_url = notify_url
        # The storage address of the recording.
        self.record_output = record_output
        # The state of the recording job.
        self.status = status
        # The URL of the live stream.
        self.stream_input = stream_input
        # The ID of the recording template.
        self.template_id = template_id
        # The name of the recording template.
        self.template_name = template_name

    def validate(self):
        if self.record_output:
            self.record_output.validate()
        if self.stream_input:
            self.stream_input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.record_output is not None:
            result['RecordOutput'] = self.record_output.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_input is not None:
            result['StreamInput'] = self.stream_input.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('RecordOutput') is not None:
            temp_model = main_models.ListLiveRecordJobsResponseBodyLiveRecordJobsRecordOutput()
            self.record_output = temp_model.from_map(m.get('RecordOutput'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamInput') is not None:
            temp_model = main_models.ListLiveRecordJobsResponseBodyLiveRecordJobsStreamInput()
            self.stream_input = temp_model.from_map(m.get('StreamInput'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class ListLiveRecordJobsResponseBodyLiveRecordJobsStreamInput(DaraModel):
    def __init__(
        self,
        type: str = None,
        url: str = None,
    ):
        # The type of the live stream URL.
        self.type = type
        # The URL of the live stream.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ListLiveRecordJobsResponseBodyLiveRecordJobsRecordOutput(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        endpoint: str = None,
        type: str = None,
    ):
        # The bucket name.
        self.bucket = bucket
        # The endpoint of the storage service.
        self.endpoint = endpoint
        # The type of the storage address.
        # 
        # Valid values:
        # 
        # *   vod
        # *   oss
        self.type = type

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


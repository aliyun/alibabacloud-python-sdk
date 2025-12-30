# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetLiveRecordJobResponseBody(DaraModel):
    def __init__(
        self,
        record_job: main_models.GetLiveRecordJobResponseBodyRecordJob = None,
        request_id: str = None,
    ):
        # The details of the recording job.
        self.record_job = record_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.record_job:
            self.record_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_job is not None:
            result['RecordJob'] = self.record_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordJob') is not None:
            temp_model = main_models.GetLiveRecordJobResponseBodyRecordJob()
            self.record_job = temp_model.from_map(m.get('RecordJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLiveRecordJobResponseBodyRecordJob(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        job_id: str = None,
        name: str = None,
        notify_url: str = None,
        record_output: main_models.GetLiveRecordJobResponseBodyRecordJobRecordOutput = None,
        status: str = None,
        stream_input: main_models.GetLiveRecordJobResponseBodyRecordJobStreamInput = None,
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
        # 
        # Valid values:
        # 
        # *   paused: The job is paused.
        # *   initial: The job is not started.
        # *   started: The job is in progress.
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
            temp_model = main_models.GetLiveRecordJobResponseBodyRecordJobRecordOutput()
            self.record_output = temp_model.from_map(m.get('RecordOutput'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamInput') is not None:
            temp_model = main_models.GetLiveRecordJobResponseBodyRecordJobStreamInput()
            self.stream_input = temp_model.from_map(m.get('StreamInput'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class GetLiveRecordJobResponseBodyRecordJobStreamInput(DaraModel):
    def __init__(
        self,
        type: str = None,
        url: str = None,
    ):
        # The type of the live stream. The value can only be rtmp.
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

class GetLiveRecordJobResponseBodyRecordJobRecordOutput(DaraModel):
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetLiveSnapshotJobResponseBody(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        create_time: str = None,
        job_id: str = None,
        job_name: str = None,
        last_modified: str = None,
        overwrite_format: str = None,
        request_id: str = None,
        sequence_format: str = None,
        snapshot_output: main_models.GetLiveSnapshotJobResponseBodySnapshotOutput = None,
        status: str = None,
        stream_input: main_models.GetLiveSnapshotJobResponseBodyStreamInput = None,
        template_id: str = None,
        template_name: str = None,
        time_interval: int = None,
    ):
        # The snapshot callback URL.
        self.callback_url = callback_url
        # The time when the file was created.
        self.create_time = create_time
        # The job ID.
        self.job_id = job_id
        # The name of the job.
        self.job_name = job_name
        # The time when the file was last modified.
        self.last_modified = last_modified
        # The naming format of the snapshot captured in overwrite mode.
        self.overwrite_format = overwrite_format
        # The request ID.
        self.request_id = request_id
        # The naming format of the snapshot captured in time series mode.
        self.sequence_format = sequence_format
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
        # The input information.
        self.stream_input = stream_input
        # The template ID.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The interval between two adjacent snapshots.
        self.time_interval = time_interval

    def validate(self):
        if self.snapshot_output:
            self.snapshot_output.validate()
        if self.stream_input:
            self.stream_input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.overwrite_format is not None:
            result['OverwriteFormat'] = self.overwrite_format

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sequence_format is not None:
            result['SequenceFormat'] = self.sequence_format

        if self.snapshot_output is not None:
            result['SnapshotOutput'] = self.snapshot_output.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_input is not None:
            result['StreamInput'] = self.stream_input.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('OverwriteFormat') is not None:
            self.overwrite_format = m.get('OverwriteFormat')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SequenceFormat') is not None:
            self.sequence_format = m.get('SequenceFormat')

        if m.get('SnapshotOutput') is not None:
            temp_model = main_models.GetLiveSnapshotJobResponseBodySnapshotOutput()
            self.snapshot_output = temp_model.from_map(m.get('SnapshotOutput'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamInput') is not None:
            temp_model = main_models.GetLiveSnapshotJobResponseBodyStreamInput()
            self.stream_input = temp_model.from_map(m.get('StreamInput'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        return self

class GetLiveSnapshotJobResponseBodyStreamInput(DaraModel):
    def __init__(
        self,
        type: str = None,
        url: str = None,
    ):
        # The type of the input stream. The value can only be rtmp.
        self.type = type
        # The URL of the input stream.
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

class GetLiveSnapshotJobResponseBodySnapshotOutput(DaraModel):
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


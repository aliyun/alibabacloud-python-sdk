# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitLiveSnapshotJobRequest(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        job_name: str = None,
        snapshot_output: main_models.SubmitLiveSnapshotJobRequestSnapshotOutput = None,
        stream_input: main_models.SubmitLiveSnapshotJobRequestStreamInput = None,
        template_id: str = None,
    ):
        # The snapshot callback URL.
        # 
        # *   It cannot exceed 255 characters in length.
        # *   Both HTTP and HTTPS URLs are supported.
        self.callback_url = callback_url
        # The name of the job.
        # 
        # *   It cannot exceed 128 characters in length.
        # 
        # This parameter is required.
        self.job_name = job_name
        # The information about the output snapshot.
        # 
        # This parameter is required.
        self.snapshot_output = snapshot_output
        # The information about the input stream.
        # 
        # This parameter is required.
        self.stream_input = stream_input
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

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

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.snapshot_output is not None:
            result['SnapshotOutput'] = self.snapshot_output.to_map()

        if self.stream_input is not None:
            result['StreamInput'] = self.stream_input.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('SnapshotOutput') is not None:
            temp_model = main_models.SubmitLiveSnapshotJobRequestSnapshotOutput()
            self.snapshot_output = temp_model.from_map(m.get('SnapshotOutput'))

        if m.get('StreamInput') is not None:
            temp_model = main_models.SubmitLiveSnapshotJobRequestStreamInput()
            self.stream_input = temp_model.from_map(m.get('StreamInput'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitLiveSnapshotJobRequestStreamInput(DaraModel):
    def __init__(
        self,
        type: str = None,
        url: str = None,
    ):
        # The type of the input stream. The value can only be rtmp.
        # 
        # This parameter is required.
        self.type = type
        # The URL of the input stream.
        # 
        # *   It cannot exceed 255 characters in length.
        # 
        # This parameter is required.
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

class SubmitLiveSnapshotJobRequestSnapshotOutput(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        endpoint: str = None,
        storage_type: str = None,
    ):
        # The bucket of the snapshot output endpoint.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The output endpoint of the snapshot.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The storage type of the snapshot. The value can only be oss.
        # 
        # This parameter is required.
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


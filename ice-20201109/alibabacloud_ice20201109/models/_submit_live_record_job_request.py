# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitLiveRecordJobRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        notify_url: str = None,
        record_output: main_models.SubmitLiveRecordJobRequestRecordOutput = None,
        stream_input: main_models.SubmitLiveRecordJobRequestStreamInput = None,
        template_id: str = None,
    ):
        # The name of the recording job.
        # 
        # This parameter is required.
        self.name = name
        # The callback URL.
        self.notify_url = notify_url
        # The storage address of the recording.
        # 
        # This parameter is required.
        self.record_output = record_output
        # The URL of the live stream.
        # 
        # This parameter is required.
        self.stream_input = stream_input
        # The ID of the recording template.
        # 
        # This parameter is required.
        self.template_id = template_id

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
        if self.name is not None:
            result['Name'] = self.name

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.record_output is not None:
            result['RecordOutput'] = self.record_output.to_map()

        if self.stream_input is not None:
            result['StreamInput'] = self.stream_input.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('RecordOutput') is not None:
            temp_model = main_models.SubmitLiveRecordJobRequestRecordOutput()
            self.record_output = temp_model.from_map(m.get('RecordOutput'))

        if m.get('StreamInput') is not None:
            temp_model = main_models.SubmitLiveRecordJobRequestStreamInput()
            self.stream_input = temp_model.from_map(m.get('StreamInput'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitLiveRecordJobRequestStreamInput(DaraModel):
    def __init__(
        self,
        type: str = None,
        url: str = None,
    ):
        # The type of the live stream URL. The value can only be rtmp.
        # 
        # This parameter is required.
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

class SubmitLiveRecordJobRequestRecordOutput(DaraModel):
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
        # This parameter is required.
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


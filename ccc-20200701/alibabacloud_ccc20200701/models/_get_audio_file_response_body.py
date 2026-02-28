# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetAudioFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAudioFileResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAudioFileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAudioFileResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_file_name: str = None,
        audio_resource_id: str = None,
        created_time: str = None,
        instance_id: str = None,
        name: str = None,
        oss_file_key: str = None,
        updated_time: str = None,
    ):
        self.audio_file_name = audio_file_name
        self.audio_resource_id = audio_resource_id
        self.created_time = created_time
        self.instance_id = instance_id
        self.name = name
        self.oss_file_key = oss_file_key
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_file_name is not None:
            result['AudioFileName'] = self.audio_file_name

        if self.audio_resource_id is not None:
            result['AudioResourceId'] = self.audio_resource_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_file_key is not None:
            result['OssFileKey'] = self.oss_file_key

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioFileName') is not None:
            self.audio_file_name = m.get('AudioFileName')

        if m.get('AudioResourceId') is not None:
            self.audio_resource_id = m.get('AudioResourceId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssFileKey') is not None:
            self.oss_file_key = m.get('OssFileKey')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self


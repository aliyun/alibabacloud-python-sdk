# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailianvoicebot20250101 import models as main_models
from darabonba.model import DaraModel

class ListCloneVoiceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCloneVoiceResponseBodyData = None,
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
            temp_model = main_models.ListCloneVoiceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCloneVoiceResponseBodyData(DaraModel):
    def __init__(
        self,
        clone_voices: List[main_models.ListCloneVoiceResponseBodyDataCloneVoices] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.clone_voices = clone_voices
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.clone_voices:
            for v1 in self.clone_voices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloneVoices'] = []
        if self.clone_voices is not None:
            for k1 in self.clone_voices:
                result['CloneVoices'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clone_voices = []
        if m.get('CloneVoices') is not None:
            for k1 in m.get('CloneVoices'):
                temp_model = main_models.ListCloneVoiceResponseBodyDataCloneVoices()
                self.clone_voices.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloneVoiceResponseBodyDataCloneVoices(DaraModel):
    def __init__(
        self,
        clone_voice_id: str = None,
        created_time: int = None,
        instance_id: str = None,
        model: str = None,
        name: str = None,
        nls_engine: str = None,
        status: str = None,
        tenant_id: str = None,
        updated_time: int = None,
        voice: str = None,
    ):
        self.clone_voice_id = clone_voice_id
        self.created_time = created_time
        self.instance_id = instance_id
        self.model = model
        self.name = name
        self.nls_engine = nls_engine
        self.status = status
        self.tenant_id = tenant_id
        self.updated_time = updated_time
        self.voice = voice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clone_voice_id is not None:
            result['CloneVoiceId'] = self.clone_voice_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.voice is not None:
            result['Voice'] = self.voice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloneVoiceId') is not None:
            self.clone_voice_id = m.get('CloneVoiceId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        return self


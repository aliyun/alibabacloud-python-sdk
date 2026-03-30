# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class GetVocabularyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetVocabularyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
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

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetVocabularyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVocabularyResponseBodyData(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        tenant_id: str = None,
        updated_time: int = None,
        vocabulary_id: str = None,
        word_count: str = None,
        words: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.instance_id = instance_id
        self.name = name
        self.tenant_id = tenant_id
        self.updated_time = updated_time
        self.vocabulary_id = vocabulary_id
        self.word_count = word_count
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        if self.word_count is not None:
            result['WordCount'] = self.word_count

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self


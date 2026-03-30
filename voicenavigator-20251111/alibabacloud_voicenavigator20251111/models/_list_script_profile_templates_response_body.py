# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class ListScriptProfileTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListScriptProfileTemplatesResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListScriptProfileTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListScriptProfileTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        description: str = None,
        name: str = None,
        schema: str = None,
        template_id: str = None,
        updated_time: int = None,
    ):
        self.created_time = created_time
        self.description = description
        self.name = name
        self.schema = schema
        self.template_id = template_id
        self.updated_time = updated_time

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

        if self.name is not None:
            result['Name'] = self.name

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self


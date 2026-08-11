# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class GetScriptProfileTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetScriptProfileTemplateResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The list of variable values in the error message.
        self.params = params
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetScriptProfileTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetScriptProfileTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        description: str = None,
        labels: str = None,
        name: str = None,
        schema: str = None,
        template_id: str = None,
        updated_time: int = None,
        variables: str = None,
    ):
        # The creation time, in millisecond-level timestamp.
        self.created_time = created_time
        # The description.
        self.description = description
        # The label definition.
        self.labels = labels
        # The name.
        self.name = name
        # The template details.
        self.schema = schema
        # The template ID.
        self.template_id = template_id
        # The update time, in millisecond-level timestamp.
        self.updated_time = updated_time
        # The variable definition.
        self.variables = variables

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

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.name is not None:
            result['Name'] = self.name

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.variables is not None:
            result['Variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        return self


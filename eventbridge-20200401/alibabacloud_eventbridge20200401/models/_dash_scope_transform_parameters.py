# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class DashScopeTransformParameters(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        messages: List[main_models.DashScopeTransformParametersMessages] = None,
        model: str = None,
        request_per_minute: int = None,
        structured_output_json_schema: str = None,
        token_per_minute: int = None,
    ):
        self.api_key = api_key
        self.messages = messages
        self.model = model
        self.request_per_minute = request_per_minute
        self.structured_output_json_schema = structured_output_json_schema
        self.token_per_minute = token_per_minute

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.model is not None:
            result['Model'] = self.model

        if self.request_per_minute is not None:
            result['RequestPerMinute'] = self.request_per_minute

        if self.structured_output_json_schema is not None:
            result['StructuredOutputJsonSchema'] = self.structured_output_json_schema

        if self.token_per_minute is not None:
            result['TokenPerMinute'] = self.token_per_minute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.DashScopeTransformParametersMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('RequestPerMinute') is not None:
            self.request_per_minute = m.get('RequestPerMinute')

        if m.get('StructuredOutputJsonSchema') is not None:
            self.structured_output_json_schema = m.get('StructuredOutputJsonSchema')

        if m.get('TokenPerMinute') is not None:
            self.token_per_minute = m.get('TokenPerMinute')

        return self

class DashScopeTransformParametersMessages(DaraModel):
    def __init__(
        self,
        form: str = None,
        role: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.role = role
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.role is not None:
            result['Role'] = self.role

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


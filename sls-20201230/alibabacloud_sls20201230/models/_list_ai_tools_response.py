# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListAiToolsResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.ListAiToolsResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.ListAiToolsResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class ListAiToolsResponseBody(DaraModel):
    def __init__(
        self,
        fields: List[main_models.ListAiToolsResponseBodyFields] = None,
        name: str = None,
        description: str = None,
    ):
        self.fields = fields
        self.name = name
        self.description = description

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.ListAiToolsResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('description') is not None:
            self.description = m.get('description')

        return self

class ListAiToolsResponseBodyFields(DaraModel):
    def __init__(
        self,
        name: str = None,
        option: List[str] = None,
        required: bool = None,
        type: str = None,
        example: str = None,
        description: str = None,
    ):
        self.name = name
        self.option = option
        self.required = required
        self.type = type
        self.example = example
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.option is not None:
            result['option'] = self.option

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        if self.example is not None:
            result['example'] = self.example

        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('option') is not None:
            self.option = m.get('option')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('example') is not None:
            self.example = m.get('example')

        if m.get('description') is not None:
            self.description = m.get('description')

        return self


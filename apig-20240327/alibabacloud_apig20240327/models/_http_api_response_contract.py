# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiResponseContract(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        items: List[main_models.HttpApiResponseContractItems] = None,
    ):
        # This parameter is required.
        self.content_type = content_type
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.HttpApiResponseContractItems()
                self.items.append(temp_model.from_map(k1))

        return self

class HttpApiResponseContractItems(DaraModel):
    def __init__(
        self,
        code: int = None,
        description: str = None,
        example: str = None,
        json_schema: str = None,
    ):
        self.code = code
        self.description = description
        self.example = example
        self.json_schema = json_schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.example is not None:
            result['example'] = self.example

        if self.json_schema is not None:
            result['jsonSchema'] = self.json_schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('example') is not None:
            self.example = m.get('example')

        if m.get('jsonSchema') is not None:
            self.json_schema = m.get('jsonSchema')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetAllSheetsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        value: List[main_models.GetAllSheetsResponseBodyValue] = None,
    ):
        # requestId
        self.request_id = request_id
        self.value = value

    def validate(self):
        if self.value:
            for v1 in self.value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['value'] = []
        if self.value is not None:
            for k1 in self.value:
                result['value'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.value = []
        if m.get('value') is not None:
            for k1 in m.get('value'):
                temp_model = main_models.GetAllSheetsResponseBodyValue()
                self.value.append(temp_model.from_map(k1))

        return self

class GetAllSheetsResponseBodyValue(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


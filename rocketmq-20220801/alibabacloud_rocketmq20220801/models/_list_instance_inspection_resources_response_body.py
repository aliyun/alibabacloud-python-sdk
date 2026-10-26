# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListInstanceInspectionResourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListInstanceInspectionResourcesResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        total: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.total = total

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListInstanceInspectionResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListInstanceInspectionResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        result: str = None,
        summary: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
        self.result = result
        self.summary = summary
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.result is not None:
            result['result'] = self.result

        if self.summary is not None:
            result['summary'] = self.summary

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


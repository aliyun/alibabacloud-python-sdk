# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetConversationsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetConversationsResponseBodyData] = None,
        has_more: str = None,
        limit: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.has_more = has_more
        self.limit = limit
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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetConversationsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetConversationsResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        introduction: str = None,
        name: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.introduction = introduction
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.id is not None:
            result['Id'] = self.id

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


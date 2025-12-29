# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListSecondRanksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListSecondRanksResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the fine sort expression.
        # 
        # For more information, see [SecondRank](https://help.aliyun.com/document_detail/170008.html).
        self.result = result
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListSecondRanksResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListSecondRanksResponseBodyResult(DaraModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        description: str = None,
        id: str = None,
        is_default: str = None,
        is_sys: str = None,
        meta: str = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The time when the expression was created.
        self.created = created
        # Description
        self.description = description
        # The expression ID. This parameter is displayed only in the response.
        self.id = id
        # Indicates whether the expression is the default one. This parameter is displayed only in the response. Valid values:
        # 
        # *   true: the expression is the default one.
        # *   false: the expression is not the default one.
        self.is_default = is_default
        # Indicates whether the expression is a system expression. This parameter is displayed only in the response. Valid values:
        # 
        # *   true: The expression is a system expression.
        # *   false:The expression is not a system expression
        self.is_sys = is_sys
        # The content of the fine sort expression. You can define an expression that consists of fields, feature functions, and mathematical functions to implement complex sort logic.
        self.meta = meta
        # Parameter
        self.name = name
        # The time when the expression was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.created is not None:
            result['created'] = self.created

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.is_sys is not None:
            result['isSys'] = self.is_sys

        if self.meta is not None:
            result['meta'] = self.meta

        if self.name is not None:
            result['name'] = self.name

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('isSys') is not None:
            self.is_sys = m.get('isSys')

        if m.get('meta') is not None:
            self.meta = m.get('meta')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self


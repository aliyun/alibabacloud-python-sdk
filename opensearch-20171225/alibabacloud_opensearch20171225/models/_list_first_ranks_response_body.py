# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListFirstRanksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListFirstRanksResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the rough sort expression.
        # 
        # For more information, see [FirstRank](https://help.aliyun.com/document_detail/170007.html).
        self.result = result

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListFirstRanksResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListFirstRanksResponseBodyResult(DaraModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        description: str = None,
        meta: List[main_models.ListFirstRanksResponseBodyResultMeta] = None,
        name: str = None,
        updated: int = None,
    ):
        # Specifies whether to set the fine sort expression as the default sort expression.
        self.active = active
        # The time when the expression was created.
        self.created = created
        # Description
        self.description = description
        # The information about the expression.
        self.meta = meta
        # The name.
        self.name = name
        # The time when the expression was updated.
        self.updated = updated

    def validate(self):
        if self.meta:
            for v1 in self.meta:
                 if v1:
                    v1.validate()

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

        result['meta'] = []
        if self.meta is not None:
            for k1 in self.meta:
                result['meta'].append(k1.to_map() if k1 else None)

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

        self.meta = []
        if m.get('meta') is not None:
            for k1 in m.get('meta'):
                temp_model = main_models.ListFirstRanksResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class ListFirstRanksResponseBodyResultMeta(DaraModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: int = None,
    ):
        # The parameters that are used by a function in the expression.
        # 
        # For more information, see [Rough sort functions](https://help.aliyun.com/document_detail/180765.html).
        self.arg = arg
        # The attribute, feature function, or field to be searched for.
        # 
        # For more information about supported feature functions, see [Rough sort functions](https://help.aliyun.com/document_detail/180765.html).
        self.attribute = attribute
        # The weight. Valid values: -100000 to 100000. The value cannot be 0.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arg is not None:
            result['arg'] = self.arg

        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arg') is not None:
            self.arg = m.get('arg')

        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self


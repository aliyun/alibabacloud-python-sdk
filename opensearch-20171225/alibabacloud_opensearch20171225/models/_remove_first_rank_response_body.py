# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class RemoveFirstRankResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.RemoveFirstRankResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the rough sort expression.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.RemoveFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class RemoveFirstRankResponseBodyResult(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        meta: List[main_models.RemoveFirstRankResponseBodyResultMeta] = None,
        name: str = None,
    ):
        # Specifies whether to set the fine sort expression as the default sort expression.
        self.active = active
        # Description
        self.description = description
        # The information about the expression.
        self.meta = meta
        # Parameter
        self.name = name

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

        if self.description is not None:
            result['description'] = self.description

        result['meta'] = []
        if self.meta is not None:
            for k1 in self.meta:
                result['meta'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.meta = []
        if m.get('meta') is not None:
            for k1 in m.get('meta'):
                temp_model = main_models.RemoveFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class RemoveFirstRankResponseBodyResultMeta(DaraModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        # The parameters that are used by a function in the expression. For more information, see Rough sort functions.[](~~170007~~)
        self.arg = arg
        # The attribute, which refers to the scoring feature or search field, For more information about supported feature functions, see Rough sort functions.[](~~170007~~)
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class CreateFirstRankResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateFirstRankResponseBodyResult = None,
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
            temp_model = main_models.CreateFirstRankResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class CreateFirstRankResponseBodyResult(DaraModel):
    def __init__(
        self,
        active: bool = None,
        meta: List[main_models.CreateFirstRankResponseBodyResultMeta] = None,
        name: str = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The content of the expression.
        self.meta = meta
        # The name of the expression.
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

        self.meta = []
        if m.get('meta') is not None:
            for k1 in m.get('meta'):
                temp_model = main_models.CreateFirstRankResponseBodyResultMeta()
                self.meta.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class CreateFirstRankResponseBodyResultMeta(DaraModel):
    def __init__(
        self,
        arg: str = None,
        attribute: str = None,
        weight: float = None,
    ):
        # The parameters that are used by a function in the expression.
        self.arg = arg
        # The attribute, feature functions, or field to be searched for.
        self.attribute = attribute
        # The weight. Valid values: [-100000,100000]. The value cannot be 0.
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribePocFunctionsResponseBody(DaraModel):
    def __init__(
        self,
        functions: List[main_models.DescribePocFunctionsResponseBodyFunctions] = None,
        request_id: str = None,
    ):
        self.functions = functions
        self.request_id = request_id

    def validate(self):
        if self.functions:
            for v1 in self.functions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Functions'] = []
        if self.functions is not None:
            for k1 in self.functions:
                result['Functions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('Functions') is not None:
            for k1 in m.get('Functions'):
                temp_model = main_models.DescribePocFunctionsResponseBodyFunctions()
                self.functions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePocFunctionsResponseBodyFunctions(DaraModel):
    def __init__(
        self,
        expire_time: int = None,
        type: str = None,
    ):
        self.expire_time = expire_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


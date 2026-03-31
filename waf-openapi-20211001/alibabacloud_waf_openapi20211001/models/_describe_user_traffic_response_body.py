# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeUserTrafficResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_traffic: List[main_models.DescribeUserTrafficResponseBodyUserTraffic] = None,
    ):
        self.request_id = request_id
        self.user_traffic = user_traffic

    def validate(self):
        if self.user_traffic:
            for v1 in self.user_traffic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserTraffic'] = []
        if self.user_traffic is not None:
            for k1 in self.user_traffic:
                result['UserTraffic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.user_traffic = []
        if m.get('UserTraffic') is not None:
            for k1 in m.get('UserTraffic'):
                temp_model = main_models.DescribeUserTrafficResponseBodyUserTraffic()
                self.user_traffic.append(temp_model.from_map(k1))

        return self

class DescribeUserTrafficResponseBodyUserTraffic(DaraModel):
    def __init__(
        self,
        index: int = None,
        pv: int = None,
    ):
        self.index = index
        self.pv = pv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.pv is not None:
            result['Pv'] = self.pv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Pv') is not None:
            self.pv = m.get('Pv')

        return self


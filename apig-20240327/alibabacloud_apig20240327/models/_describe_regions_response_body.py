# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeRegionsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class DescribeRegionsResponseBodyData(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['localName'] = self.local_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('localName') is not None:
            self.local_name = m.get('localName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self


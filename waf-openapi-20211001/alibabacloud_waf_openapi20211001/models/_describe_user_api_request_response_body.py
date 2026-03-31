# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeUserApiRequestResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        requests: List[main_models.DescribeUserApiRequestResponseBodyRequests] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics.
        self.requests = requests

    def validate(self):
        if self.requests:
            for v1 in self.requests:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Requests'] = []
        if self.requests is not None:
            for k1 in self.requests:
                result['Requests'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.requests = []
        if m.get('Requests') is not None:
            for k1 in m.get('Requests'):
                temp_model = main_models.DescribeUserApiRequestResponseBodyRequests()
                self.requests.append(temp_model.from_map(k1))

        return self

class DescribeUserApiRequestResponseBodyRequests(DaraModel):
    def __init__(
        self,
        count: int = None,
        value: str = None,
    ):
        # The number of entries returned.
        self.count = count
        # The type of the statistics. Valid values:
        # 
        # *   **client_list**: client
        # *   **ip**: IP address
        # *   **region_id** region
        # *   **country_id**: country
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


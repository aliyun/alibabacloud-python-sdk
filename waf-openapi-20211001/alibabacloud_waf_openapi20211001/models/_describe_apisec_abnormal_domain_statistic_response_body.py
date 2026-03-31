# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecAbnormalDomainStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecAbnormalDomainStatisticResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The response parameters.
        self.data = data
        # Id of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApisecAbnormalDomainStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisecAbnormalDomainStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        api_count: int = None,
        domain: str = None,
        high: int = None,
        low: int = None,
        medium: int = None,
    ):
        # The number of APIs.
        self.api_count = api_count
        # The domain name.
        self.domain = domain
        # The number of high-level risks.
        self.high = high
        # The number of low-level risks.
        self.low = low
        # The number of medium-level risks.
        self.medium = medium

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_count is not None:
            result['ApiCount'] = self.api_count

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.high is not None:
            result['High'] = self.high

        if self.low is not None:
            result['Low'] = self.low

        if self.medium is not None:
            result['Medium'] = self.medium

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiCount') is not None:
            self.api_count = m.get('ApiCount')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('High') is not None:
            self.high = m.get('High')

        if m.get('Low') is not None:
            self.low = m.get('Low')

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        return self


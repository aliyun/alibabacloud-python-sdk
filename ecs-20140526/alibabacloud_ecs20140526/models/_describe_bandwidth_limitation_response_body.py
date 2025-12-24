# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeBandwidthLimitationResponseBody(DaraModel):
    def __init__(
        self,
        bandwidths: main_models.DescribeBandwidthLimitationResponseBodyBandwidths = None,
        request_id: str = None,
    ):
        # Details about the maximum public bandwidth.
        self.bandwidths = bandwidths
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.bandwidths:
            self.bandwidths.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidths is not None:
            result['Bandwidths'] = self.bandwidths.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidths') is not None:
            temp_model = main_models.DescribeBandwidthLimitationResponseBodyBandwidths()
            self.bandwidths = temp_model.from_map(m.get('Bandwidths'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBandwidthLimitationResponseBodyBandwidths(DaraModel):
    def __init__(
        self,
        bandwidth: List[main_models.DescribeBandwidthLimitationResponseBodyBandwidthsBandwidth] = None,
    ):
        self.bandwidth = bandwidth

    def validate(self):
        if self.bandwidth:
            for v1 in self.bandwidth:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bandwidth'] = []
        if self.bandwidth is not None:
            for k1 in self.bandwidth:
                result['Bandwidth'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bandwidth = []
        if m.get('Bandwidth') is not None:
            for k1 in m.get('Bandwidth'):
                temp_model = main_models.DescribeBandwidthLimitationResponseBodyBandwidthsBandwidth()
                self.bandwidth.append(temp_model.from_map(k1))

        return self

class DescribeBandwidthLimitationResponseBodyBandwidthsBandwidth(DaraModel):
    def __init__(
        self,
        internet_charge_type: str = None,
        max: int = None,
        min: int = None,
        unit: str = None,
    ):
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth
        # *   PayByTraffic
        self.internet_charge_type = internet_charge_type
        # The maximum public bandwidth.
        self.max = max
        # The minimum public bandwidth.
        self.min = min
        # The unit of the public bandwidth.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self


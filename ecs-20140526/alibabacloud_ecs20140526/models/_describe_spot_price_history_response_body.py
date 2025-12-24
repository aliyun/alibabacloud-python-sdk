# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSpotPriceHistoryResponseBody(DaraModel):
    def __init__(
        self,
        currency: str = None,
        next_offset: int = None,
        request_id: str = None,
        spot_prices: main_models.DescribeSpotPriceHistoryResponseBodySpotPrices = None,
    ):
        # The instance type of the spot instance.
        self.currency = currency
        # The network type of the spot instance.
        self.next_offset = next_offset
        # The instance type of the spot instance.
        self.request_id = request_id
        # The zone ID of the spot instance.
        self.spot_prices = spot_prices

    def validate(self):
        if self.spot_prices:
            self.spot_prices.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.next_offset is not None:
            result['NextOffset'] = self.next_offset

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.spot_prices is not None:
            result['SpotPrices'] = self.spot_prices.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('NextOffset') is not None:
            self.next_offset = m.get('NextOffset')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SpotPrices') is not None:
            temp_model = main_models.DescribeSpotPriceHistoryResponseBodySpotPrices()
            self.spot_prices = temp_model.from_map(m.get('SpotPrices'))

        return self

class DescribeSpotPriceHistoryResponseBodySpotPrices(DaraModel):
    def __init__(
        self,
        spot_price_type: List[main_models.DescribeSpotPriceHistoryResponseBodySpotPricesSpotPriceType] = None,
    ):
        self.spot_price_type = spot_price_type

    def validate(self):
        if self.spot_price_type:
            for v1 in self.spot_price_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SpotPriceType'] = []
        if self.spot_price_type is not None:
            for k1 in self.spot_price_type:
                result['SpotPriceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spot_price_type = []
        if m.get('SpotPriceType') is not None:
            for k1 in m.get('SpotPriceType'):
                temp_model = main_models.DescribeSpotPriceHistoryResponseBodySpotPricesSpotPriceType()
                self.spot_price_type.append(temp_model.from_map(k1))

        return self

class DescribeSpotPriceHistoryResponseBodySpotPricesSpotPriceType(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        io_optimized: str = None,
        network_type: str = None,
        origin_price: float = None,
        spot_price: float = None,
        timestamp: str = None,
        zone_id: str = None,
    ):
        # The instance type of the spot instance.
        self.instance_type = instance_type
        # Details about the price history of the spot instance.
        self.io_optimized = io_optimized
        # Queries the price history of a spot instance within the last 30 days.
        self.network_type = network_type
        # The price for a pay-as-you-go instance that has the same configuration as the specified spot instance.
        self.origin_price = origin_price
        # The price for a pay-as-you-go instance that has the same configurations as the spot instance.
        self.spot_price = spot_price
        # The currency unit of the price.
        # 
        # Alibaba Cloud China site (aliyun.com): CNY.
        # 
        # Alibaba Cloud International site (alibabacloud.com): USD.
        self.timestamp = timestamp
        # The ID of the request.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price

        if self.spot_price is not None:
            result['SpotPrice'] = self.spot_price

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')

        if m.get('SpotPrice') is not None:
            self.spot_price = m.get('SpotPrice')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


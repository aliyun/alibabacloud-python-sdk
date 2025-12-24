# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeSpotDiscountHistoryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        spot_discounts: List[main_models.DescribeSpotDiscountHistoryResponseBodySpotDiscounts] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The discount for the preemptible instance.
        self.spot_discounts = spot_discounts

    def validate(self):
        if self.spot_discounts:
            for v1 in self.spot_discounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SpotDiscounts'] = []
        if self.spot_discounts is not None:
            for k1 in self.spot_discounts:
                result['SpotDiscounts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spot_discounts = []
        if m.get('SpotDiscounts') is not None:
            for k1 in m.get('SpotDiscounts'):
                temp_model = main_models.DescribeSpotDiscountHistoryResponseBodySpotDiscounts()
                self.spot_discounts.append(temp_model.from_map(k1))

        return self

class DescribeSpotDiscountHistoryResponseBodySpotDiscounts(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_discount: str = None,
        timestamp: str = None,
        zone_id: str = None,
    ):
        # The type of the ECS instance.
        self.instance_type = instance_type
        # The discount for the preemptible instance. For example, 0.1 represents a 90% discount.
        self.spot_discount = spot_discount
        # The time when the discount is available. The time must be in UTC.
        self.timestamp = timestamp
        # The zone ID.
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

        if self.spot_discount is not None:
            result['SpotDiscount'] = self.spot_discount

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SpotDiscount') is not None:
            self.spot_discount = m.get('SpotDiscount')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


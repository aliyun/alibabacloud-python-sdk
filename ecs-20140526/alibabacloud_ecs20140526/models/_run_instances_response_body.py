# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class RunInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_id_sets: main_models.RunInstancesResponseBodyInstanceIdSets = None,
        order_id: str = None,
        request_id: str = None,
        trade_price: float = None,
    ):
        # The instance IDs.
        self.instance_id_sets = instance_id_sets
        # The ID of the order. This parameter is returned only when `InstanceChargeType` is set to PrePaid.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # The transaction price.
        self.trade_price = trade_price

    def validate(self):
        if self.instance_id_sets:
            self.instance_id_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id_sets is not None:
            result['InstanceIdSets'] = self.instance_id_sets.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdSets') is not None:
            temp_model = main_models.RunInstancesResponseBodyInstanceIdSets()
            self.instance_id_sets = temp_model.from_map(m.get('InstanceIdSets'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')

        return self

class RunInstancesResponseBodyInstanceIdSets(DaraModel):
    def __init__(
        self,
        instance_id_set: List[str] = None,
    ):
        self.instance_id_set = instance_id_set

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id_set is not None:
            result['InstanceIdSet'] = self.instance_id_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdSet') is not None:
            self.instance_id_set = m.get('InstanceIdSet')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class PurchaseReservedInstancesOfferingResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
        reserved_instance_id_sets: main_models.PurchaseReservedInstancesOfferingResponseBodyReservedInstanceIdSets = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id
        # The IDs of the reserved instances.
        self.reserved_instance_id_sets = reserved_instance_id_sets

    def validate(self):
        if self.reserved_instance_id_sets:
            self.reserved_instance_id_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reserved_instance_id_sets is not None:
            result['ReservedInstanceIdSets'] = self.reserved_instance_id_sets.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReservedInstanceIdSets') is not None:
            temp_model = main_models.PurchaseReservedInstancesOfferingResponseBodyReservedInstanceIdSets()
            self.reserved_instance_id_sets = temp_model.from_map(m.get('ReservedInstanceIdSets'))

        return self

class PurchaseReservedInstancesOfferingResponseBodyReservedInstanceIdSets(DaraModel):
    def __init__(
        self,
        reserved_instance_id: List[str] = None,
    ):
        self.reserved_instance_id = reserved_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')

        return self


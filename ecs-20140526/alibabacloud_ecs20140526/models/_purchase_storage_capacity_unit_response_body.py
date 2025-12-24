# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class PurchaseStorageCapacityUnitResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
        storage_capacity_unit_ids: main_models.PurchaseStorageCapacityUnitResponseBodyStorageCapacityUnitIds = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id
        # The IDs of the SCUs.
        self.storage_capacity_unit_ids = storage_capacity_unit_ids

    def validate(self):
        if self.storage_capacity_unit_ids:
            self.storage_capacity_unit_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage_capacity_unit_ids is not None:
            result['StorageCapacityUnitIds'] = self.storage_capacity_unit_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StorageCapacityUnitIds') is not None:
            temp_model = main_models.PurchaseStorageCapacityUnitResponseBodyStorageCapacityUnitIds()
            self.storage_capacity_unit_ids = temp_model.from_map(m.get('StorageCapacityUnitIds'))

        return self

class PurchaseStorageCapacityUnitResponseBodyStorageCapacityUnitIds(DaraModel):
    def __init__(
        self,
        storage_capacity_unit_id: List[str] = None,
    ):
        self.storage_capacity_unit_id = storage_capacity_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_capacity_unit_id is not None:
            result['StorageCapacityUnitId'] = self.storage_capacity_unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageCapacityUnitId') is not None:
            self.storage_capacity_unit_id = m.get('StorageCapacityUnitId')

        return self


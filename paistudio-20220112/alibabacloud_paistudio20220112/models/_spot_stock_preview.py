# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SpotStockPreview(DaraModel):
    def __init__(
        self,
        available_quantity: int = None,
        cluster_id: str = None,
        instance_type: str = None,
        spot_discount: float = None,
        stock_status: str = None,
    ):
        self.available_quantity = available_quantity
        self.cluster_id = cluster_id
        self.instance_type = instance_type
        self.spot_discount = spot_discount
        self.stock_status = stock_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_quantity is not None:
            result['AvailableQuantity'] = self.available_quantity

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.spot_discount is not None:
            result['SpotDiscount'] = self.spot_discount

        if self.stock_status is not None:
            result['StockStatus'] = self.stock_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableQuantity') is not None:
            self.available_quantity = m.get('AvailableQuantity')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SpotDiscount') is not None:
            self.spot_discount = m.get('SpotDiscount')

        if m.get('StockStatus') is not None:
            self.stock_status = m.get('StockStatus')

        return self


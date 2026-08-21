# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketCreateOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        contact_shrink: str = None,
        distributor_order_id: str = None,
        order_product_shrink: str = None,
        quantity: int = None,
        total_distribution_price_shrink: str = None,
        travelers_shrink: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.contact_shrink = contact_shrink
        # This parameter is required.
        self.distributor_order_id = distributor_order_id
        # This parameter is required.
        self.order_product_shrink = order_product_shrink
        # This parameter is required.
        self.quantity = quantity
        # This parameter is required.
        self.total_distribution_price_shrink = total_distribution_price_shrink
        self.travelers_shrink = travelers_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.contact_shrink is not None:
            result['Contact'] = self.contact_shrink

        if self.distributor_order_id is not None:
            result['DistributorOrderId'] = self.distributor_order_id

        if self.order_product_shrink is not None:
            result['OrderProduct'] = self.order_product_shrink

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.total_distribution_price_shrink is not None:
            result['TotalDistributionPrice'] = self.total_distribution_price_shrink

        if self.travelers_shrink is not None:
            result['Travelers'] = self.travelers_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('Contact') is not None:
            self.contact_shrink = m.get('Contact')

        if m.get('DistributorOrderId') is not None:
            self.distributor_order_id = m.get('DistributorOrderId')

        if m.get('OrderProduct') is not None:
            self.order_product_shrink = m.get('OrderProduct')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('TotalDistributionPrice') is not None:
            self.total_distribution_price_shrink = m.get('TotalDistributionPrice')

        if m.get('Travelers') is not None:
            self.travelers_shrink = m.get('Travelers')

        return self


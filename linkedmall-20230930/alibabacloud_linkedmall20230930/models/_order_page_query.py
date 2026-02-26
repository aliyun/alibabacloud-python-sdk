# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OrderPageQuery(DaraModel):
    def __init__(
        self,
        order_id_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        purchase_order_id: str = None,
    ):
        self.order_id_list = order_id_list
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.purchase_order_id = purchase_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id_list is not None:
            result['orderIdList'] = self.order_id_list

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.purchase_order_id is not None:
            result['purchaseOrderId'] = self.purchase_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderIdList') is not None:
            self.order_id_list = m.get('orderIdList')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('purchaseOrderId') is not None:
            self.purchase_order_id = m.get('purchaseOrderId')

        return self


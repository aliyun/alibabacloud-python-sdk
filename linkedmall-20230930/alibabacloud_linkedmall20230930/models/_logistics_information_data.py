# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LogisticsInformationData(DaraModel):
    def __init__(
        self,
        logistics_status: str = None,
        modified_time: str = None,
        order_id: str = None,
        order_line_id: str = None,
        outer_purchase_order_id: str = None,
        purchaser_id: str = None,
        tracking_company_code: str = None,
        tracking_company_name: str = None,
        tracking_number: str = None,
    ):
        self.logistics_status = logistics_status
        self.modified_time = modified_time
        self.order_id = order_id
        self.order_line_id = order_line_id
        self.outer_purchase_order_id = outer_purchase_order_id
        self.purchaser_id = purchaser_id
        self.tracking_company_code = tracking_company_code
        self.tracking_company_name = tracking_company_name
        self.tracking_number = tracking_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logistics_status is not None:
            result['logisticsStatus'] = self.logistics_status

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id

        if self.outer_purchase_order_id is not None:
            result['outerPurchaseOrderId'] = self.outer_purchase_order_id

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        if self.tracking_company_code is not None:
            result['trackingCompanyCode'] = self.tracking_company_code

        if self.tracking_company_name is not None:
            result['trackingCompanyName'] = self.tracking_company_name

        if self.tracking_number is not None:
            result['trackingNumber'] = self.tracking_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logisticsStatus') is not None:
            self.logistics_status = m.get('logisticsStatus')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')

        if m.get('outerPurchaseOrderId') is not None:
            self.outer_purchase_order_id = m.get('outerPurchaseOrderId')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        if m.get('trackingCompanyCode') is not None:
            self.tracking_company_code = m.get('trackingCompanyCode')

        if m.get('trackingCompanyName') is not None:
            self.tracking_company_name = m.get('trackingCompanyName')

        if m.get('trackingNumber') is not None:
            self.tracking_number = m.get('trackingNumber')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBasicAcceleratorResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the basic GA instance.
        self.accelerator_id = accelerator_id
        # The order ID.
        # 
        # This parameter is returned only if ChargeType is set to PREPAY.
        # 
        # If **AutoPay** is set to **false**, go to [Order Center](https://usercenter2-intl.aliyun.com/order/list) to complete the payment after an order is generated.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


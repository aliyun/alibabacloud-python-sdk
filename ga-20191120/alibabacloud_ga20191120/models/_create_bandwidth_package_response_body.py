# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBandwidthPackageResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id
        # The order ID.
        # 
        # If bills are not automatically paid, you must go to the Order Center to complete the payments.
        # 
        # This parameter is returned only if ChargeType is set to PREPAY. If AutoPay is set to false, you must go to the [Order Center](https://usercenter2-intl.aliyun.com/order/list) to complete the payment.
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
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


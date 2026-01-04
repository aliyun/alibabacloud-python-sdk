# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateEipAddressProResponseBody(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        eip_address: str = None,
        order_id: int = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The EIP ID.
        self.allocation_id = allocation_id
        # The IP address that is allocated to the EIP. This parameter is returned only when **InstanceChargeType** is set to **PostPaid**.
        self.eip_address = eip_address
        # The order ID.
        # 
        # This parameter is returned when InstanceChargeType is set to PrePaid. If AutoPay is set to false, you must manually complete the payment in the [Order Center](https://usercenter2-intl.aliyun.com/order/list).
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group. This parameter is returned only when **InstanceChargeType** is set to **PostPaid**.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self


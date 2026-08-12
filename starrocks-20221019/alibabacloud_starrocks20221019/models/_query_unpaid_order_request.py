# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUnpaidOrderRequest(DaraModel):
    def __init__(
        self,
        billing_instance_id: str = None,
        instance_id: str = None,
        order_type: str = None,
    ):
        # The ID of the instance that is associated with the bill. For the default compute group, which includes the FE compute group and the default BE compute group, this parameter is the instance ID. For other compute groups, this parameter is the compute group ID.
        # 
        # This parameter is required.
        self.billing_instance_id = billing_instance_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Order type
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_instance_id is not None:
            result['BillingInstanceId'] = self.billing_instance_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingInstanceId') is not None:
            self.billing_instance_id = m.get('BillingInstanceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self


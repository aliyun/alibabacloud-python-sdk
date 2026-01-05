# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransformDBClusterPayTypeResponseBody(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        dbcluster_id: str = None,
        expired_time: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.charge_type = charge_type
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The time when the cluster expires.
        # 
        # >  This parameter is returned if you set the **PayType** parameter to **Prepaid**.
        self.expired_time = expired_time
        # The ID of the order.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


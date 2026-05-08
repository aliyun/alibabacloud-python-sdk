# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterPayTypeResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order_id: str = None,
        pay_type: str = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The order ID.
        self.order_id = order_id
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransformDBInstancePayTypeResponseBody(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        dbinstance_id: str = None,
        expired_time: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        # The payment type.
        # 
        # *   Valid value if the new billing method is pay-as-you-go: POSTPAY
        # *   Valid value if the new billing method is subscription: PREPAY
        self.charge_type = charge_type
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The expiration time.
        # 
        # > If you call this operation to change the billing method of an instance from subscription to pay-as-you-go, this parameter is not returned.
        self.expired_time = expired_time
        # The order ID.
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
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

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

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


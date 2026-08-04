# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGwConsumerOrderResponseBody(DaraModel):
    def __init__(
        self,
        credit_token: str = None,
        expire_time: str = None,
        gateway_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The redemption code used for subsequent activation.
        self.credit_token = credit_token
        # The expiration time.
        self.expire_time = expire_time
        # The ID of the AI gateway instance.
        self.gateway_id = gateway_id
        # The order ID returned after the order is placed.
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
        if self.credit_token is not None:
            result['CreditToken'] = self.credit_token

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditToken') is not None:
            self.credit_token = m.get('CreditToken')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


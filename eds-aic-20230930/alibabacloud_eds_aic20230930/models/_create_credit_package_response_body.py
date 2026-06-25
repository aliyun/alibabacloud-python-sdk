# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCreditPackageResponseBody(DaraModel):
    def __init__(
        self,
        credit_package_id: str = None,
        effective_time: str = None,
        expired_time: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The credit package ID.
        self.credit_package_id = credit_package_id
        # The time when the credit package takes effect.
        self.effective_time = effective_time
        # The time when the credit package expires.
        self.expired_time = expired_time
        # The order ID.
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
        if self.credit_package_id is not None:
            result['CreditPackageId'] = self.credit_package_id

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditPackageId') is not None:
            self.credit_package_id = m.get('CreditPackageId')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


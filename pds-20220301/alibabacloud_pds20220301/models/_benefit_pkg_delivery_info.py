# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BenefitPkgDeliveryInfo(DaraModel):
    def __init__(
        self,
        amount: int = None,
        created_at: str = None,
        expire_time: str = None,
        is_permanent: bool = None,
    ):
        # Number of benefit packages delivered.
        self.amount = amount
        # The creation time of the benefit package delivery.
        self.created_at = created_at
        # The expiration time of the benefit package delivery.
        # 
        # If is_permit is set to false, a valid value is returned.
        self.expire_time = expire_time
        # Whether it is permanently valid.
        self.is_permanent = is_permanent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.expire_time is not None:
            result['expire_time'] = self.expire_time

        if self.is_permanent is not None:
            result['is_permanent'] = self.is_permanent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')

        if m.get('is_permanent') is not None:
            self.is_permanent = m.get('is_permanent')

        return self


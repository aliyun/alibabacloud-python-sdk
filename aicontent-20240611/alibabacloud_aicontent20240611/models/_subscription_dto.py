# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubscriptionDTO(DaraModel):
    def __init__(
        self,
        balance_type: str = None,
        client_id: int = None,
        create_time: str = None,
        id: int = None,
        status: str = None,
        stop_time: str = None,
        subscription_amount: float = None,
        update_time: str = None,
        valid_from: str = None,
    ):
        # The balance type (permanent/monthly).
        self.balance_type = balance_type
        # The department ID.
        self.client_id = client_id
        # The creation time.
        self.create_time = create_time
        # The subscription ID.
        self.id = id
        # The subscription status. Valid values:
        # - active: The subscription is active.
        # - stopped: The subscription is stopped.
        self.status = status
        # The stop time. This value is empty if the subscription has not been stopped.
        self.stop_time = stop_time
        # The subscription recharge amount.
        self.subscription_amount = subscription_amount
        # The update time.
        self.update_time = update_time
        # The effective period.
        self.valid_from = valid_from

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balance_type is not None:
            result['balanceType'] = self.balance_type

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.status is not None:
            result['status'] = self.status

        if self.stop_time is not None:
            result['stopTime'] = self.stop_time

        if self.subscription_amount is not None:
            result['subscriptionAmount'] = self.subscription_amount

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.valid_from is not None:
            result['validFrom'] = self.valid_from

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('balanceType') is not None:
            self.balance_type = m.get('balanceType')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('stopTime') is not None:
            self.stop_time = m.get('stopTime')

        if m.get('subscriptionAmount') is not None:
            self.subscription_amount = m.get('subscriptionAmount')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('validFrom') is not None:
            self.valid_from = m.get('validFrom')

        return self


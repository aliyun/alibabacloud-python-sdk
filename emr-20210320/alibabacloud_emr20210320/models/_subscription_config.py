# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubscriptionConfig(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
    ):
        # Specifies whether auto-renewal is enabled. Valid values:
        # 
        # - true: Auto-renewal is enabled.
        # 
        # - false: Auto-renewal is disabled (default).
        self.auto_renew = auto_renew
        # The auto-renewal duration. This parameter takes effect only when AutoRenew is set to true. When AutoRenewDurationUnit is Month, valid values are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.auto_renew_duration = auto_renew_duration
        # The auto-renewal duration unit. Valid value:
        # 
        # - Month
        self.auto_renew_duration_unit = auto_renew_duration_unit
        # The payment duration. When PaymentDurationUnit is Month, valid values are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        # 
        # This parameter is required.
        self.payment_duration = payment_duration
        # The payment duration unit. Valid value:
        # 
        # - Month
        # 
        # This parameter is required.
        self.payment_duration_unit = payment_duration_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        return self


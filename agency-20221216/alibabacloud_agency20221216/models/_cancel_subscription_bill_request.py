# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelSubscriptionBillRequest(DaraModel):
    def __init__(
        self,
        subscribe_type: str = None,
    ):
        # The type of the bill to which you want to cancel the subscription. Valid values: PartnerBillingItemDetailForBillingPeriod, PartnerBillingItemDetailMonthly, PartnerInstanceDetailForBillingPeriod, and PartnerInstanceDetailMonthly.
        # 
        # This parameter is required.
        self.subscribe_type = subscribe_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')

        return self


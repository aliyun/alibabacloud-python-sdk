# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnsubscribeBillToOSSRequest(DaraModel):
    def __init__(
        self,
        mult_account_rel_subscribe: str = None,
        subscribe_type: str = None,
    ):
        # For multi-level accounts, specifies the type of bill to push. Valid values:
        # 
        # - MA: Pushes the bill of the main account.
        # - ACP1: Pushes the bill of the Partner Platform V2.0 sub-account.
        # 
        # Default value: MA.
        self.mult_account_rel_subscribe = mult_account_rel_subscribe
        # The subscription type. Valid values:
        # - BillingItemDetailForBillingPeriod: billable item-level consumption details.
        # - InstanceDetailForBillingPeriod: instance-level consumption details.
        # - BillingItemDetailMonthly: billable item-level consumption summary by billing cycle.
        # - InstanceDetailMonthly: instance-level consumption summary by billing cycle.
        # - SplitItemDetailDaily: split bill summarized by day.
        # - MonthBill: monthly bill in PDF format. Only MA subscriptions are supported.
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
        if self.mult_account_rel_subscribe is not None:
            result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe

        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MultAccountRelSubscribe') is not None:
            self.mult_account_rel_subscribe = m.get('MultAccountRelSubscribe')

        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')

        return self


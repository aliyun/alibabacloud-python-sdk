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
        # The type of accounts whose bills are to be pushed if multi-tier accounts are involved. Valid values:
        # 
        # *   MA: management account.
        # *   ACP1: member account of a virtual network operator (VNO).
        # 
        # Default value: MA.
        self.mult_account_rel_subscribe = mult_account_rel_subscribe
        # The type of the bill to which you want to subscribe. Valid values:
        # 
        # *   BillingItemDetailForBillingPeriod: bills of billable items
        # *   InstanceDetailForBillingPeriod: bills of instances
        # *   BillingItemDetailMonthly: billable item-based bills summarized by billing cycle
        # *   InstanceDetailMonthly: instance-based bills summarized by billing cycle
        # *   SplitItemDetailDaily: split bills summarized by day
        # *   MonthBill: monthly bills in the PDF format You can subscribe to the monthly PDF bills only of the master account.
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


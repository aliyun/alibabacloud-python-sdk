# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadMeteringDailyDetailCmd(DaraModel):
    def __init__(
        self,
        bill_period: str = None,
        billing_item: str = None,
        end_time: str = None,
        start_time: str = None,
        sub_account_id: str = None,
    ):
        self.bill_period = bill_period
        self.billing_item = billing_item
        self.end_time = end_time
        self.start_time = start_time
        self.sub_account_id = sub_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_period is not None:
            result['billPeriod'] = self.bill_period

        if self.billing_item is not None:
            result['billingItem'] = self.billing_item

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billPeriod') is not None:
            self.bill_period = m.get('billPeriod')

        if m.get('billingItem') is not None:
            self.billing_item = m.get('billingItem')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')

        return self


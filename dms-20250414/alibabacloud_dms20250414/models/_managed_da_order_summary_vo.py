# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManagedDaOrderSummaryVO(DaraModel):
    def __init__(
        self,
        available_quota: int = None,
        total_quota: int = None,
        trial_expire_time: str = None,
        trial_used: bool = None,
        used_quota: int = None,
        valid_order_count: int = None,
    ):
        self.available_quota = available_quota
        self.total_quota = total_quota
        self.trial_expire_time = trial_expire_time
        self.trial_used = trial_used
        self.used_quota = used_quota
        self.valid_order_count = valid_order_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_quota is not None:
            result['availableQuota'] = self.available_quota

        if self.total_quota is not None:
            result['totalQuota'] = self.total_quota

        if self.trial_expire_time is not None:
            result['trialExpireTime'] = self.trial_expire_time

        if self.trial_used is not None:
            result['trialUsed'] = self.trial_used

        if self.used_quota is not None:
            result['usedQuota'] = self.used_quota

        if self.valid_order_count is not None:
            result['validOrderCount'] = self.valid_order_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableQuota') is not None:
            self.available_quota = m.get('availableQuota')

        if m.get('totalQuota') is not None:
            self.total_quota = m.get('totalQuota')

        if m.get('trialExpireTime') is not None:
            self.trial_expire_time = m.get('trialExpireTime')

        if m.get('trialUsed') is not None:
            self.trial_used = m.get('trialUsed')

        if m.get('usedQuota') is not None:
            self.used_quota = m.get('usedQuota')

        if m.get('validOrderCount') is not None:
            self.valid_order_count = m.get('validOrderCount')

        return self


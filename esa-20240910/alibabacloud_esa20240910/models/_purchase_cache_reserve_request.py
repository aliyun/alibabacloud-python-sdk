# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurchaseCacheReserveRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        charge_type: str = None,
        cr_region: str = None,
        period: int = None,
        quota_gb: int = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.charge_type = charge_type
        self.cr_region = cr_region
        self.period = period
        self.quota_gb = quota_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cr_region is not None:
            result['CrRegion'] = self.cr_region

        if self.period is not None:
            result['Period'] = self.period

        if self.quota_gb is not None:
            result['QuotaGb'] = self.quota_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CrRegion') is not None:
            self.cr_region = m.get('CrRegion')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('QuotaGb') is not None:
            self.quota_gb = m.get('QuotaGb')

        return self


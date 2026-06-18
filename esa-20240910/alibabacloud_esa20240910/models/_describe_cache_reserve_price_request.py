# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCacheReservePriceRequest(DaraModel):
    def __init__(
        self,
        cr_region: str = None,
        period: int = None,
        quota_gb: int = None,
    ):
        # The cache reserve region.
        # 
        # - HK: Hong Kong (China)
        # 
        # - CN: the Chinese mainland.
        self.cr_region = cr_region
        # The purchase period. Unit: months.
        self.period = period
        # The cache reserve specification. Unit: GB.
        self.quota_gb = quota_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cr_region is not None:
            result['CrRegion'] = self.cr_region

        if self.period is not None:
            result['Period'] = self.period

        if self.quota_gb is not None:
            result['QuotaGb'] = self.quota_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrRegion') is not None:
            self.cr_region = m.get('CrRegion')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('QuotaGb') is not None:
            self.quota_gb = m.get('QuotaGb')

        return self


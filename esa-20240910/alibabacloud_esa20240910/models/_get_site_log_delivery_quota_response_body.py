# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSiteLogDeliveryQuotaResponseBody(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        free_quota: int = None,
        request_id: str = None,
        site_id: int = None,
    ):
        # The log category. Valid values:
        # 
        # 1.  dcdn_log_access_l1 (default): access logs.
        # 2.  dcdn_log_er: Edge Routine logs.
        # 3.  dcdn_log_waf: firewall logs.
        # 4.  dcdn_log_ipa: TCP/UDP proxy logs.
        self.business_type = business_type
        # The remaining quota.
        self.free_quota = free_quota
        # The request ID.
        self.request_id = request_id
        # The website ID.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.free_quota is not None:
            result['FreeQuota'] = self.free_quota

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('FreeQuota') is not None:
            self.free_quota = m.get('FreeQuota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self


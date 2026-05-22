# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserLogDeliveryQuotaResponseBody(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        free_quota: int = None,
        request_id: str = None,
    ):
        # The log category. Valid values:
        # 
        # *   dcdn_log_access_l1 (default): access logs.
        # *   dcdn_log_er: Edge Routine logs.
        # *   dcdn_log_waf: firewall logs.
        # *   dcdn_log_ipa: TCP/UDP proxy logs.
        self.business_type = business_type
        # The remaining quota.
        self.free_quota = free_quota
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('FreeQuota') is not None:
            self.free_quota = m.get('FreeQuota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


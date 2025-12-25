# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserLogDeliveryQuotaRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
    ):
        # The log category. Valid values:
        # 
        # *   dcdn_log_access_l1 (default): access logs.
        # *   dcdn_log_er: Edge Routine logs.
        # *   dcdn_log_waf: firewall logs.
        # *   dcdn_log_ipa: TCP/UDP proxy logs.
        # 
        # This parameter is required.
        self.business_type = business_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        return self


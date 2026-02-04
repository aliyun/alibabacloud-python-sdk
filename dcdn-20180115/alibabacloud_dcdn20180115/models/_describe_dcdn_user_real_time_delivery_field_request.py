# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnUserRealTimeDeliveryFieldRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
    ):
        # The type of the collected logs. Default value: cdn_log_access_l1. Valid values:
        # 
        # *   **cdn_log_access_l1**: access logs of L1 Dynamic Content Delivery Network (DCDN) points of presence (POPs)
        # *   **cdn_log_origin**: back-to-origin logs
        # *   **cdn_log_er**: EdgeRoutine logs
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


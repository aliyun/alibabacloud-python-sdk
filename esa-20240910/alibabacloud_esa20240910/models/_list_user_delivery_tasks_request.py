# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserDeliveryTasksRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The log category. Valid values:
        # 
        # 1.  dcdn_log_access_l1 (default): access logs.
        # 2.  dcdn_log_er: Edge Routine logs.
        # 3.  dcdn_log_waf: firewall logs.
        # 4.  dcdn_log_ipa: TCP/UDP proxy logs.
        self.business_type = business_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


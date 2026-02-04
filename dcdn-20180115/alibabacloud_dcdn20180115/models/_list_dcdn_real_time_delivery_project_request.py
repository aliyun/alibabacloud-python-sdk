# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDcdnRealTimeDeliveryProjectRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        domain_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The type of the collected logs. Default value: cdn_log_access_l1. Valid values:
        # 
        # *   **cdn_log_access_l1**: access logs of Dynamic Content Delivery Network (DCDN) points of presence (POPs)
        # *   **cdn_log_origin**: back-to-origin logs
        # *   **cdn_log_er**: EdgeRoutine logs
        # *   By default, this parameter is left empty, and all logs are returned.
        self.business_type = business_type
        # The domain name. You can specify only one domain name in each request. If this parameter is not specified, all domain names are queried.
        self.domain_name = domain_name
        # The number of the page to return. Valid values: **1** to **100000**. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. The default value is 20.
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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


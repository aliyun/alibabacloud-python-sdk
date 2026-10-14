# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnLinkageRulesRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The domain name of your website.
        # 
        # > The domain name must be added to your Anti-DDoS instance. Call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        self.domain = domain
        # The number of the page to return for a paged query.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the resource group to which the Anti-DDoS instance belongs in Resource Management. If you leave this parameter empty, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self


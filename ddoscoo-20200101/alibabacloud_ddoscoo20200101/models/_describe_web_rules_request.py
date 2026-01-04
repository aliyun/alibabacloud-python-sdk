# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeWebRulesRequest(DaraModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        instance_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        query_domain_pattern: str = None,
        resource_group_id: str = None,
    ):
        # The CNAME address to query.
        self.cname = cname
        # The domain name of the website to query.
        # 
        # > The domain must have been configured with website business forwarding rules. You can call [DescribeDomains](~~DescribeDomains~~) to query all domains that have been configured with website business forwarding rules.
        self.domain = domain
        # The list of DDoS protection instance IDs to query.
        self.instance_ids = instance_ids
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1** to **10**.
        self.page_size = page_size
        # The query matching pattern. Values:
        # - **fuzzy** (default): Indicates fuzzy query.
        # - **exact**: Indicates exact query.
        self.query_domain_pattern = query_domain_pattern
        # The resource group ID of the DDoS protection instance in the resource management service.
        # 
        # Not setting this parameter indicates the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self


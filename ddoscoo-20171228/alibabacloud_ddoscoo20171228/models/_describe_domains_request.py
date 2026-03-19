# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDomainsRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_ids: List[str] = None,
        offset: int = None,
        page_size: str = None,
        query_domain_pattern: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.domain = domain
        self.instance_ids = instance_ids
        # This parameter is required.
        self.offset = offset
        # This parameter is required.
        self.page_size = page_size
        self.query_domain_pattern = query_domain_pattern
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


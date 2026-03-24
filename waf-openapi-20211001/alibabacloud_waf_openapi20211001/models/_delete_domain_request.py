# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDomainRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        domain: str = None,
        domain_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The access type of the WAF instance. Valid values:
        # 
        # - **share** (default): CNAME access.
        # 
        # - **hybrid_cloud_cname**: Hybrid cloud reverse proxy access.
        self.access_type = access_type
        # The domain name that is added to WAF.
        self.domain = domain
        # The domain ID.
        self.domain_id = domain_id
        # The ID of the WAF instance.
        # 
        # > Call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to view the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region of the WAF instance. Valid values:
        # 
        # - **cn-hangzhou**: The Chinese mainland.
        # 
        # - **ap-southeast-1**: Outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


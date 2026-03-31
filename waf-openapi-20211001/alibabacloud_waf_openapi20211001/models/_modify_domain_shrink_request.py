# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDomainShrinkRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        domain: str = None,
        domain_id: str = None,
        instance_id: str = None,
        listen_shrink: str = None,
        redirect_shrink: str = None,
        region_id: str = None,
    ):
        # The mode in which you want to add the domain name to WAF. Set the value to share.
        # 
        # *   **share:** adds the domain name to WAF in CNAME record mode. This is the default value.
        self.access_type = access_type
        # The domain name whose access configurations you want to modify.
        self.domain = domain
        self.domain_id = domain_id
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to obtain the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The listener configurations.
        # 
        # This parameter is required.
        self.listen_shrink = listen_shrink
        # The forwarding configurations.
        # 
        # This parameter is required.
        self.redirect_shrink = redirect_shrink
        # The region where the WAF instance resides. Valid values:
        # 
        # *   **cn-hangzhou:** the Chinese mainland.
        # *   **ap-southeast-1:** outside the Chinese mainland.
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

        if self.listen_shrink is not None:
            result['Listen'] = self.listen_shrink

        if self.redirect_shrink is not None:
            result['Redirect'] = self.redirect_shrink

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

        if m.get('Listen') is not None:
            self.listen_shrink = m.get('Listen')

        if m.get('Redirect') is not None:
            self.redirect_shrink = m.get('Redirect')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebCacheModeRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        mode: str = None,
        resource_group_id: str = None,
    ):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name, and the domain name must be associated with an instance that uses the Enhanced function plan. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The cache mode of the Static Page Caching policy. Valid values:
        # 
        # *   **standard**: uses the standard cache mode.
        # *   **aggressive**: uses the enhanced cache mode.
        # *   **bypass**: caches no data.
        # 
        # This parameter is required.
        self.mode = mode
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
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

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self


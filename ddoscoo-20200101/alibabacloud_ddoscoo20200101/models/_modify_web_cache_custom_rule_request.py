# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebCacheCustomRuleRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
        rules: str = None,
    ):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name, and the domain name must be associated with an instance that uses the Enhanced function plan. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The details of the custom rule. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **Name**: the name of the rule. This field is required and must be of the string type.
        # 
        # *   **Uri**: the path to the cached page. This field is required and must be of the STRING type.
        # 
        # *   **Mode**: the cache mode. This field is required and must be of the STRING type. Valid values:
        # 
        #     *   **standard**: uses the standard mode.
        #     *   **aggressive**: uses the enhanced mode.
        #     *   **bypass**: No data is cached.
        # 
        # *   **CacheTtl**: the expiration time of the page cache. This field is required and must be of the INTEGER type. Unit: seconds.
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rules is not None:
            result['Rules'] = self.rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        return self


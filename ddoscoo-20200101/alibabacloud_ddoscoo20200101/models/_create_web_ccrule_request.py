# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWebCCRuleRequest(DaraModel):
    def __init__(
        self,
        act: str = None,
        count: int = None,
        domain: str = None,
        interval: int = None,
        mode: str = None,
        name: str = None,
        resource_group_id: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        # The action on the requests that trigger the custom frequency control rule. Valid values:
        # 
        # *   **close**: blocks the requests.
        # *   **captcha**: triggers Completely Automated Public Turing test to tell Computers and Humans Apart (CAPTCHA) verification for the requests.
        # 
        # This parameter is required.
        self.act = act
        # This parameter is required.
        self.count = count
        # The domain name of the website.
        # 
        # >  A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.interval = interval
        # The matching mode. Valid values:
        # 
        # *   **prefix**: prefix match.
        # *   **match**: exact match.
        # 
        # >  If the **URI** of the check path contains parameters, you must set this parameter to **prefix**.
        # 
        # This parameter is required.
        self.mode = mode
        # The name of the rule. The name can be up to 128 characters in length and contain letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group to which the Anti-DDoS Proxy instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id
        # The blocking duration. Valid values: **60** to **86400**. Unit: seconds.
        # 
        # This parameter is required.
        self.ttl = ttl
        # The check path.
        # 
        # >  The URI cannot be modified. The domain name of the website, the check path, and the rule name uniquely identify a rule.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.act is not None:
            result['Act'] = self.act

        if self.count is not None:
            result['Count'] = self.count

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self


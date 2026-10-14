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
        # The action to be performed on requests that match the rule. Valid values:
        # 
        # - **close**: blocks the request.
        # - **captcha**: initiates bot detection.
        # 
        # This parameter is required.
        self.act = act
        # The number of access requests from a single IP address. Valid values: **2** to **2000**.
        # 
        # This parameter is required.
        self.count = count
        # The domain name of the website.
        # 
        # > The domain name must have a website forwarding rule configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The detection duration. Valid values: **5** to **10800**. Unit: seconds.
        # 
        # This parameter is required.
        self.interval = interval
        # The matching mode. Valid values:
        # 
        # - **prefix**: prefix match.
        # - **match**: exact match.
        # 
        # > If the detection path **URI** contains parameters, select prefix match (**prefix**).
        # 
        # This parameter is required.
        self.mode = mode
        # The rule name. The name can contain letters, digits, and underscores (_) and cannot exceed 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The resource group ID of the Anti-DDoS instance in Resource Management. Default value: empty, which indicates that the instance belongs to the default resource group.
        # 
        # For more information, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id
        # The blocking duration. Valid values: **60** to **86400**. Unit: seconds.
        # 
        # This parameter is required.
        self.ttl = ttl
        # The detection path.
        # 
        # > The URI cannot be modified. A rule is uniquely identified by the domain name of the website, the detection path, and the rule name.
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


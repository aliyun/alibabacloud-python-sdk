# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class CreateFirewallRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        firewall_rules_shrink: str = None,
        instance_id: str = None,
        region_id: str = None,
        tag: List[main_models.CreateFirewallRulesShrinkRequestTag] = None,
    ):
        # The client token.
        self.client_token = client_token
        # The array of firewall rules.
        self.firewall_rules_shrink = firewall_rules_shrink
        # The instance ID of the specified simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the regions where simple application servers are available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of tags. The list can contain up to 20 tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.firewall_rules_shrink is not None:
            result['FirewallRules'] = self.firewall_rules_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FirewallRules') is not None:
            self.firewall_rules_shrink = m.get('FirewallRules')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateFirewallRulesShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateFirewallRulesShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key that is specified for the firewall rule. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. It can be up to 64 characters in length, cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The tag value that is specified for the firewall rule. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


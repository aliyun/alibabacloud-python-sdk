# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableFirewallRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        rule_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. A client-generated parameter value that is unique among different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The instance ID of the specified simple application server.
        self.instance_id = instance_id
        # The region ID of the specified simple application server. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query the list of supported Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The remarks of the firewall rule.
        self.remark = remark
        # The firewall rule ID. You can call the ListFirewallRules operation to obtain the firewall rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self


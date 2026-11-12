# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFirewallTemplateRulesApplyResultRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        firewall_template_id: str = None,
        instance_id: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the firewall template.
        # 
        # This parameter is required.
        self.firewall_template_id = firewall_template_id
        # The ID of the simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the execution to apply the template rule.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.firewall_template_id is not None:
            result['FirewallTemplateId'] = self.firewall_template_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FirewallTemplateId') is not None:
            self.firewall_template_id = m.get('FirewallTemplateId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self


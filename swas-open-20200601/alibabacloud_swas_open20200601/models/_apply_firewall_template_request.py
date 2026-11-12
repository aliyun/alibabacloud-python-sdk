# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ApplyFirewallTemplateRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        firewall_template_id: str = None,
        instance_ids: List[str] = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can generate the value on your client and must ensure that the value is unique among different requests. The **ClientToken** parameter supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the firewall template.
        # 
        # This parameter is required.
        self.firewall_template_id = firewall_template_id
        # The instance IDs of the Simple Application Server instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query available regions.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.firewall_template_id is not None:
            result['FirewallTemplateId'] = self.firewall_template_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FirewallTemplateId') is not None:
            self.firewall_template_id = m.get('FirewallTemplateId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebAreaBlockSwitchRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        domain: str = None,
        resource_group_id: str = None,
    ):
        # Specifies whether to enable or disable the Location Blacklist (Domain Names) policy for a domain name. The value is a string that consists of a JSON struct. The JSON struct contains the following parameters:
        # 
        # *   **RegionblockEnable**: the status of the Location Blacklist (Domain Names) policy. This parameter is required and must be of the INTEGER type. Valid values:
        # 
        #     *   **1**: enables the policy.
        #     *   **0**: disables the policy.
        # 
        # This parameter is required.
        self.config = config
        # The domain name for which you want to enable or disable the Location Blacklist policy.
        # 
        # > You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all the domain names that are added to Anti-DDoS Pro or Anti-DDoS Premium.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self


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
        # The status of the Location Blacklist feature (for domain names). This parameter is a string that is converted from a JSON struct. The JSON struct contains the following parameter:
        # 
        # - **RegionblockEnable**: An Integer value that is required. The status of the Location Blacklist feature (for domain names). Valid values:
        # 
        #   - **1**: enables the feature.
        # 
        #   - **0**: disables the feature.
        # 
        # This parameter is required.
        self.config = config
        # The domain name for which you want to set the Location Blacklist feature.
        # 
        # > You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names that are protected by Anti-DDoS Proxy.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the resource group to which the Anti-DDoS Proxy instance belongs in Resource Management.
        # 
        # If you do not set this parameter, the default resource group is used.
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebAIProtectSwitchRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        domain: str = None,
        resource_group_id: str = None,
    ):
        # The details of the Intelligent Protection policy. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **AiRuleEnable**: the status of the Intelligent Protection policy. This field is required and must be of the integer type. Valid values:
        # 
        #     *   **0**: disabled
        #     *   **1**: enabled
        # 
        # This parameter is required.
        self.config = config
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for a domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
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


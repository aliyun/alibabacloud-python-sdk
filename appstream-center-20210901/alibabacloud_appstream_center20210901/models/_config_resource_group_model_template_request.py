# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigResourceGroupModelTemplateRequest(DaraModel):
    def __init__(
        self,
        model_template_id: str = None,
        resource_group_id: str = None,
    ):
        # The model group ID.
        # 
        # This parameter is required.
        self.model_template_id = model_template_id
        # The WUYING resource group ID, which starts with rg-. This resource group is managed by the WUYING Enterprise Edition management and control service, and its automatic creation is performed by the system after the deployment of agent runtimes such as JVS Computer, OpenClaw, and Hermes Agent. You can obtain it from the ResourceGroup[].ResourceGroupId field in the response of the DescribeResourceGroups operation of WUYING Workspace eds-user (API version 2021-03-08), or from the Data.ResourceGroupId field in the response of the GetRuntimeModelConfig operation of this service.
        # 
        # > Other IDs such as the account-level resource group ID and node pool ID in Alibaba Cloud Resource Manager cannot be passed as this parameter. Only WUYING resource group IDs are valid.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self


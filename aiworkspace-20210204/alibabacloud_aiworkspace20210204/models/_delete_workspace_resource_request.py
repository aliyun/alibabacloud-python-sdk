# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWorkspaceResourceRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        labels: str = None,
        option: str = None,
        product_type: str = None,
        resource_ids: str = None,
        resource_type: str = None,
    ):
        # The resource group name. To get the resource group name, see [ListResources](https://help.aliyun.com/document_detail/449143.html).
        self.group_name = group_name
        # A comma-separated list of labels.
        self.labels = labels
        # The deletion behavior. Valid values:
        # 
        # - `DetachAndDelete` (default): Detaches the resource from the workspace and deletes the resource.
        # 
        # - `Detach`: Detaches the resource from the workspace.
        self.option = option
        # **This parameter is deprecated and will be removed. Use the `ResourceType` parameter instead.**
        self.product_type = product_type
        # A comma-separated list of resource IDs. All specified resources must belong to the same `GroupName`. You must specify a value for at least one of the `GroupName` or `ResourceIds` parameters.
        self.resource_ids = resource_ids
        # The resource type. Valid values:
        # 
        # - `ECS`: general-purpose computing resources
        # 
        # - `Lingjun`: Lingjun intelligent computing resources
        # 
        # - `ACS`: ACS computing resources
        # 
        # - `Flink`: Flink resources.
        # 
        # - `MaxCompute`: MaxCompute resources. For this resource type, the `Option` parameter can only be set to `Detach`.
        # 
        # - `SelfManagedAckPro`: AckPro unified management cluster resources
        # 
        # - `SelfManagedAckLingjun`: AckLinjun unified management cluster resources
        # 
        # - `SelfManagedASI`: ASI unified management cluster resources (third-party cloud)
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.option is not None:
            result['Option'] = self.option

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self


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
        # The name of the resource group. You can call [ListResources](https://help.aliyun.com/document_detail/449143.html) to obtain the name of the resource group.
        self.group_name = group_name
        # The tags. Multiple tags are separated by commas (,).
        self.labels = labels
        # The operation to perform. Valid values:
        # 
        # *   DetachAndDelete: disassociates a resource from a workspace and deletes the resource in the workspace. This is the default value.
        # *   Detach: disassociates a resource group from a workspace.
        self.option = option
        # **This field is no longer used and will be removed. Use the ResourceType field instead.
        self.product_type = product_type
        # The resource IDs. Multiple resource IDs are separated by commas (,). The GroupName values for the specified resources must be the same. You cannot leave both GroupName and ResourceIds empty. You can specify both parameters.
        self.resource_ids = resource_ids
        # The resource type. Valid values:
        # 
        # *   ECS
        # *   Lingjun
        # *   ACS
        # *   FLINK
        # *   MaxCompute (This resource type is valid only if Option is set to Detach.)
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


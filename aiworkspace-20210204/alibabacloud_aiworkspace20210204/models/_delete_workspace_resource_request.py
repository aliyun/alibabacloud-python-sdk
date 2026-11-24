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
        # The name of the resource group. To obtain the name of the resource group, see [ListResources](https://help.aliyun.com/document_detail/449143.html).
        self.group_name = group_name
        # The list of tags, separated by commas.
        self.labels = labels
        # The deletion behavior. Valid values:
        # - DetachAndDelete: Unbinds the resources from the workspace and deletes the resources. This is the default value.
        # - Detach: Unbinds the resources from the workspace.
        self.option = option
        # **[Deprecated]** This field is deprecated and will be retired. Use the ResourceType field.
        self.product_type = product_type
        # The IDs of the resources, separated by commas. The GroupName of these resource IDs must be the same. GroupName and ResourceIds cannot be empty at the same time, but both can be specified.
        self.resource_ids = resource_ids
        # The list of resource types. Valid values:
        # - ECS: general computing resources
        # - Lingjun: Lingjun AI computing resources
        # - ACS: ACS computing resources
        # - FLINK: Flink resources
        # - MaxCompute: MaxCompute resources. Only the Detach option is supported. The DetachAndDelete option is not supported.
        # - SelfManagedAckPro: ACK Pro unified management cluster resources
        # - SelfManagedAckLingjun: ACK Lingjun unified management cluster resources
        # - SelfManagedASI: ASI unified management cluster resources (third-party cloud)
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


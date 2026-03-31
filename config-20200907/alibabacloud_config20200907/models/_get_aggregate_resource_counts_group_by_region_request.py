# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAggregateResourceCountsGroupByRegionRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        folder_id: str = None,
        resource_account_id: int = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The ID of the folder in the resource directory. For more information about how to obtain the ID of a folder, see [View the basic information of a folder](https://help.aliyun.com/document_detail/111223.html).
        self.folder_id = folder_id
        # The ID of the Alibaba Cloud account to which the resources in the account group belong.
        # 
        # > You can use either the ResourceAccountId or ResourceOwnerId parameter. We recommend that you use the ResourceAccountId parameter.
        self.resource_account_id = resource_account_id
        self.resource_owner_id = resource_owner_id
        # The resource type.
        # 
        # For more information about how to obtain the type of a resource, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/265983.html).
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self


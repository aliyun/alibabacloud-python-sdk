# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClustersRequest(DaraModel):
    def __init__(
        self,
        ai_node_type: str = None,
        dbcluster_description: str = None,
        dbcluster_ids: str = None,
        dbcluster_status: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeAIDBClustersRequestTag] = None,
    ):
        # The node type. To specify multiple types, separate them with a comma. Valid values:
        # 
        # - **vnode**: a node managed by Kubernetes
        # 
        # - **container**: a container that you can log on to
        # 
        # - **maas**: model service
        self.ai_node_type = ai_node_type
        # The cluster description. Fuzzy search is supported.
        self.dbcluster_description = dbcluster_description
        # The cluster ID. To specify multiple clusters, separate their IDs with a comma.
        self.dbcluster_ids = dbcluster_ids
        # The cluster status. Valid values:
        # 
        # - **Creating**: The cluster is being created.
        # 
        # - **Running**: The cluster is running.
        # 
        # - **Deleting**: The cluster is being released.
        # 
        # - **Rebooting**: The cluster is restarting.
        # 
        # - **DBNodeCreating**: A node is being added.
        # 
        # - **DBNodeDeleting**: A node is being deleted.
        # 
        # - **ClassChanging**: The node specifications are being changed.
        # 
        # - **NetAddressCreating**: A network connection is being created.
        # 
        # - **NetAddressDeleting**: A network connection is being deleted.
        # 
        # - **NetAddressModifying**: A network connection is being modified.
        # 
        # - **Deleted**: The cluster is released.
        # 
        # * **ClassChanged**: Resources are being reclaimed after the upgrade or downgrade.
        self.dbcluster_status = dbcluster_status
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30**, **50**, and **100**.
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go
        # 
        # - **Prepaid**: subscription
        self.pay_type = pay_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A list of tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_node_type is not None:
            result['AiNodeType'] = self.ai_node_type

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids

        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiNodeType') is not None:
            self.ai_node_type = m.get('AiNodeType')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')

        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAIDBClustersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAIDBClustersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Use this parameter with `Tag.n.Value` to filter clusters by tag. You can specify up to 20 tag pairs. The index n must be a unique, consecutive integer starting from 1.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


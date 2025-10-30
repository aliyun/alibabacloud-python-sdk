# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesRequest(DaraModel):
    def __init__(
        self,
        dbinstance_categories: List[str] = None,
        dbinstance_description: str = None,
        dbinstance_ids: str = None,
        dbinstance_modes: List[str] = None,
        dbinstance_statuses: List[str] = None,
        instance_deploy_types: List[str] = None,
        instance_network_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.DescribeDBInstancesRequestTag] = None,
        vpc_id: str = None,
    ):
        # The edition of the instance. Separate multiple values with commas (,).
        self.dbinstance_categories = dbinstance_categories
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID. Separate multiple values with commas (,).
        self.dbinstance_ids = dbinstance_ids
        # The resource type of the instance. Separate multiple values with commas (,).
        self.dbinstance_modes = dbinstance_modes
        # The state of the instance.
        self.dbinstance_statuses = dbinstance_statuses
        # This parameter is no longer used.
        self.instance_deploy_types = instance_deploy_types
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**: virtual private cloud (VPC).
        # *   **Classic**: classic network.
        # 
        # > If you do not specify this parameter, instances of all network types are returned.
        self.instance_network_type = instance_network_type
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30**
        # *   **50**
        # *   **100**
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag = tag
        # The VPC ID. You can use this parameter to filter instances that reside in the specified VPC.
        self.vpc_id = vpc_id

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
        if self.dbinstance_categories is not None:
            result['DBInstanceCategories'] = self.dbinstance_categories

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids

        if self.dbinstance_modes is not None:
            result['DBInstanceModes'] = self.dbinstance_modes

        if self.dbinstance_statuses is not None:
            result['DBInstanceStatuses'] = self.dbinstance_statuses

        if self.instance_deploy_types is not None:
            result['InstanceDeployTypes'] = self.instance_deploy_types

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceCategories') is not None:
            self.dbinstance_categories = m.get('DBInstanceCategories')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')

        if m.get('DBInstanceModes') is not None:
            self.dbinstance_modes = m.get('DBInstanceModes')

        if m.get('DBInstanceStatuses') is not None:
            self.dbinstance_statuses = m.get('DBInstanceStatuses')

        if m.get('InstanceDeployTypes') is not None:
            self.instance_deploy_types = m.get('InstanceDeployTypes')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeDBInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
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


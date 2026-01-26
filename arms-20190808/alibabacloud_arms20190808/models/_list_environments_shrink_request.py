# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnvironmentsShrinkRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        bind_resource_id: str = None,
        environment_type: str = None,
        fee_package: str = None,
        filter_region_ids: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag_shrink: str = None,
    ):
        # The add-on name. You must specify at least one of the AddonName and EnvironmentType parameters.
        self.addon_name = addon_name
        # The ID of the resource.
        self.bind_resource_id = bind_resource_id
        # The environment type. You must specify at least one of the AddonName and EnvironmentType parameters.
        # 
        # Valid values:
        # 
        # *   CS
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Container Service for Kubernetes (ACK)
        # 
        #     <!-- -->
        # 
        # *   ECS
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Elastic Compute Service (ECS)
        # 
        #     <!-- -->
        # 
        # *   Cloud
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     cloud service
        # 
        #     <!-- -->
        self.environment_type = environment_type
        # The payable resource plan.
        # 
        # *   If the EnvironmentType parameter is set to CS, set the value to CS_Basic or CS_Pro. Default value: CS_Basic.
        # *   Otherwise, leave the parameter empty.
        # 
        # Valid values:
        # 
        # *   CS_Pro: Container Monitoring Pro
        # *   CS_Basic: Container Monitoring Basic
        self.fee_package = fee_package
        # The region IDs to be queried.
        self.filter_region_ids = filter_region_ids
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name

        if self.bind_resource_id is not None:
            result['BindResourceId'] = self.bind_resource_id

        if self.environment_type is not None:
            result['EnvironmentType'] = self.environment_type

        if self.fee_package is not None:
            result['FeePackage'] = self.fee_package

        if self.filter_region_ids is not None:
            result['FilterRegionIds'] = self.filter_region_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('BindResourceId') is not None:
            self.bind_resource_id = m.get('BindResourceId')

        if m.get('EnvironmentType') is not None:
            self.environment_type = m.get('EnvironmentType')

        if m.get('FeePackage') is not None:
            self.fee_package = m.get('FeePackage')

        if m.get('FilterRegionIds') is not None:
            self.filter_region_ids = m.get('FilterRegionIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self


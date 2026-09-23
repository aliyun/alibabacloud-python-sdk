# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyTemplateResourcesRequest(DaraModel):
    def __init__(
        self,
        bind_assets: List[str] = None,
        bind_resource_groups: List[str] = None,
        bind_resources: List[str] = None,
        dry_run: bool = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        template_id: int = None,
        unbind_assets: List[str] = None,
        unbind_resource_groups: List[str] = None,
        unbind_resources: List[str] = None,
    ):
        # The IDs of the protected assets to associate, in the format of ["XX1","XX2",...].
        self.bind_assets = bind_assets
        # The protected object groups to associate, in the format of [**"group1","group2",...**].
        self.bind_resource_groups = bind_resource_groups
        # The protected objects to associate, in the format of [**"XX1","XX2",...**].
        self.bind_resources = bind_resources
        # Specifies whether to enable the dry run mode. If you do not specify this parameter, a normal request is sent. Valid values:
        # - **true**: A dry run request is sent. The system checks whether the request meets the execution conditions without performing the specified operation. If the dry run fails, the corresponding error code is returned. If the dry run succeeds, the error code Defense.Control.DryRunOperation is returned.
        # - **false**: A normal request is sent. The specified operation is performed after the request passes the check.
        self.dry_run = dry_run
        # Instance ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query instance ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The ID of the protection template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The IDs of the protected assets to disassociate, in the format of ["XX1","XX2",...].
        self.unbind_assets = unbind_assets
        # The protected object groups to disassociate, in the format of [**"group1","group2",...**].
        self.unbind_resource_groups = unbind_resource_groups
        # The protected objects to disassociate, in the format of [**"XX1","XX2",...**].
        self.unbind_resources = unbind_resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_assets is not None:
            result['BindAssets'] = self.bind_assets

        if self.bind_resource_groups is not None:
            result['BindResourceGroups'] = self.bind_resource_groups

        if self.bind_resources is not None:
            result['BindResources'] = self.bind_resources

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.unbind_assets is not None:
            result['UnbindAssets'] = self.unbind_assets

        if self.unbind_resource_groups is not None:
            result['UnbindResourceGroups'] = self.unbind_resource_groups

        if self.unbind_resources is not None:
            result['UnbindResources'] = self.unbind_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindAssets') is not None:
            self.bind_assets = m.get('BindAssets')

        if m.get('BindResourceGroups') is not None:
            self.bind_resource_groups = m.get('BindResourceGroups')

        if m.get('BindResources') is not None:
            self.bind_resources = m.get('BindResources')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UnbindAssets') is not None:
            self.unbind_assets = m.get('UnbindAssets')

        if m.get('UnbindResourceGroups') is not None:
            self.unbind_resource_groups = m.get('UnbindResourceGroups')

        if m.get('UnbindResources') is not None:
            self.unbind_resources = m.get('UnbindResources')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceTypesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        deploy_mode: str = None,
        instance_type: str = None,
        is_modification: bool = None,
        node_group_id: str = None,
        node_group_type: str = None,
        payment_type: str = None,
        region_id: str = None,
        release_version: str = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster type.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # Specifies the deployment mode.
        self.deploy_mode = deploy_mode
        # The instance type.
        self.instance_type = instance_type
        # Specifies whether the instance type is for an instance type change. A value of true indicates an instance type change.
        self.is_modification = is_modification
        # The node group ID.
        self.node_group_id = node_group_id
        # The node group type.
        # 
        # This parameter is required.
        self.node_group_type = node_group_type
        # The billing method.
        # 
        # This parameter is required.
        self.payment_type = payment_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The EMR release version.
        self.release_version = release_version
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_modification is not None:
            result['IsModification'] = self.is_modification

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsModification') is not None:
            self.is_modification = m.get('IsModification')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


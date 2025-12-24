# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyDedicatedHostAttributeRequest(DaraModel):
    def __init__(
        self,
        network_attributes: main_models.ModifyDedicatedHostAttributeRequestNetworkAttributes = None,
        action_on_maintenance: str = None,
        auto_placement: str = None,
        cpu_over_commit_ratio: float = None,
        dedicated_host_cluster_id: str = None,
        dedicated_host_id: str = None,
        dedicated_host_name: str = None,
        description: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.network_attributes = network_attributes
        # The policy for migrating the instances deployed on the dedicated host when the dedicated host fails or needs to be repaired online. Valid values:
        # 
        # *   Migrate: The instances are migrated to another physical machine and then restarted.
        # *   Stop: The instances are stopped. If the dedicated host cannot be repaired, the instances are migrated to another physical machine and then restarted.
        # 
        # If the dedicated host has cloud disks attached, the default value is Migrate.
        # 
        # If the dedicated host has local disks attached, the default value is Stop.
        self.action_on_maintenance = action_on_maintenance
        # Specifies whether to add the dedicated host to the resource pool for automatic deployment. If you do not specify **DedicatedHostId** when you create an instance on a dedicated host, Alibaba Cloud automatically selects a dedicated host from the resource pool to host the instance. Valid values:
        # 
        # *   on: adds the dedicated host to the resource pool for automatic deployment.
        # *   off: does not add the dedicated host to the resource pool for automatic deployment.
        # 
        # For information about automatic deployment, see [Functions and features](https://help.aliyun.com/document_detail/118938.html).
        self.auto_placement = auto_placement
        # The CPU overcommit ratio. You can configure CPU overcommit ratios only for the following dedicated host types: g6s, c6s, and r6s. Valid values: 1 to 5.
        # 
        # The CPU overcommit ratio affects the number of available vCPUs on a dedicated host. You can use the following formula to calculate the number of available vCPUs on a dedicated host: Number of available vCPUs = Number of physical CPU cores × 2 × CPU overcommit ratio. For example, the number of physical CPU cores on each g6s dedicated host is 52. If you change the CPU overcommit ratio of a g6s dedicated host to 4, the number of available vCPUs on the dedicated host is 416. For scenarios that have minimal requirements for CPU stability or where CPU load is not heavy, such as development and test environments, you can increase the number of available vCPUs on a dedicated host by increasing the CPU overcommit ratio. This allows you to deploy more ECS instances of the same specifications on the dedicated host and reduce the unit deployment cost.
        self.cpu_over_commit_ratio = cpu_over_commit_ratio
        # The ID of the dedicated host cluster to which to assign the dedicated host.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The ID of the dedicated host.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # The name of the dedicated host. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with http:// or https://. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.dedicated_host_name = dedicated_host_name
        # The description of the dedicated host. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the dedicated host resides. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.network_attributes:
            self.network_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_attributes is not None:
            result['NetworkAttributes'] = self.network_attributes.to_map()

        if self.action_on_maintenance is not None:
            result['ActionOnMaintenance'] = self.action_on_maintenance

        if self.auto_placement is not None:
            result['AutoPlacement'] = self.auto_placement

        if self.cpu_over_commit_ratio is not None:
            result['CpuOverCommitRatio'] = self.cpu_over_commit_ratio

        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name

        if self.description is not None:
            result['Description'] = self.description

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAttributes') is not None:
            temp_model = main_models.ModifyDedicatedHostAttributeRequestNetworkAttributes()
            self.network_attributes = temp_model.from_map(m.get('NetworkAttributes'))

        if m.get('ActionOnMaintenance') is not None:
            self.action_on_maintenance = m.get('ActionOnMaintenance')

        if m.get('AutoPlacement') is not None:
            self.auto_placement = m.get('AutoPlacement')

        if m.get('CpuOverCommitRatio') is not None:
            self.cpu_over_commit_ratio = m.get('CpuOverCommitRatio')

        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyDedicatedHostAttributeRequestNetworkAttributes(DaraModel):
    def __init__(
        self,
        slb_udp_timeout: int = None,
        udp_timeout: int = None,
    ):
        # The timeout period for a UDP session between a Server Load Balancer (SLB) instance and the dedicated host. Unit: seconds. Valid values: 15 to 310.
        self.slb_udp_timeout = slb_udp_timeout
        # The timeout period for a UDP session between a user and an Alibaba Cloud service on the dedicated host. Unit: seconds. Valid values: 15 to 310.
        self.udp_timeout = udp_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slb_udp_timeout is not None:
            result['SlbUdpTimeout'] = self.slb_udp_timeout

        if self.udp_timeout is not None:
            result['UdpTimeout'] = self.udp_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlbUdpTimeout') is not None:
            self.slb_udp_timeout = m.get('SlbUdpTimeout')

        if m.get('UdpTimeout') is not None:
            self.udp_timeout = m.get('UdpTimeout')

        return self


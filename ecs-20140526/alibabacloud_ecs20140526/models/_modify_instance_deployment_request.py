# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceDeploymentRequest(DaraModel):
    def __init__(
        self,
        affinity: str = None,
        dedicated_host_cluster_id: str = None,
        dedicated_host_id: str = None,
        deployment_set_group_no: int = None,
        deployment_set_id: str = None,
        force: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        migration_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_from_deployment_set: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tenancy: str = None,
    ):
        # Specifies whether to associate the instance with a dedicated host. Valid values:
        # 
        # *   host: associates the instance with a dedicated host. When you start a stopped instance in economical mode, the instance remains on its original dedicated host.
        # *   default: does not associate the instance with a dedicated host. When you start a stopped instance in economical mode, the instance can be automatically deployed to another dedicated host in the automatic deployment resource pool if the resources of the original dedicated host are insufficient.
        # 
        # If you want to migrate the instance from a shared host to a dedicated host, use the default value. Default value: default.
        self.affinity = affinity
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The ID of the destination dedicated host. You can call the [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) operation to query the most recent list of dedicated hosts.
        # 
        # When you migrate an instance from a shared host to a dedicated host or between dedicated hosts, take note of the following items:
        # 
        # *   To migrate the instance to a specific dedicated host, specify this parameter.
        # *   To migrate the instance to a system-selected dedicated host, leave this parameter empty and set `Tenancy` to host.
        # 
        # For information about the automatic deployment feature, see [Functions and features](https://help.aliyun.com/document_detail/118938.html).
        self.dedicated_host_id = dedicated_host_id
        # The number of the deployment set group in which to deploy the instance in the destination deployment set. This parameter is valid only when the destination deployment set uses the high availability group strategy (AvailabilityGroup). Valid values: 1 to 7.
        # 
        # > If you call this operation to deploy an instance to a deployment set that uses the high availability group strategy (`AvailablilityGroup`) and leave this parameter empty, the system evenly distributes instances among the deployment set groups in the deployment set. If you call this operation to change the deployment set of an instance and specify the current deployment set of the instance as the destination deployment set, the system evenly distributes instances again among the deployment set groups in the deployment set.
        self.deployment_set_group_no = deployment_set_group_no
        # The ID of the destination deployment set.
        # 
        # This parameter is required when you add an instance to a deployment set or change the deployment set of an instance.
        # 
        # > You cannot change the deployment set when you modify dedicated host configurations, including the `Tenancy`, `Affinity`, and `DedicatedHostId` parameters.
        self.deployment_set_id = deployment_set_id
        # Specifies whether to forcefully change the host of the instance when the deployment set of the instance is changed. Valid values:
        # 
        # *   true: forcefully changes the host of the instance when the deployment set of the instance is changed. Hosts can be forcefully changed only for instances in the Running (Running) or Stopped (Stopped) state. The instances that are in the Stopped (Stopped) state do not include pay-as-you-go instances that are stopped in economical mode.
        # 
        #     **
        # 
        #     **Note** If the specified instance has local disks attached, the local disks are forcefully changed when the host of the instance is forcefully changed. This may cause data loss in the local disks. Proceed with caution.
        # 
        # *   false: does not forcefully change the host of the instance when the deployment set of the instance is changed. You can add the instance to a deployment set only when the instance remains on the current host. When the Force parameter is set to false, the deployment set may fail to be changed.
        # 
        # Default value: false.
        self.force = force
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance type to which the instance is changed. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the most recent list of instance types.
        # 
        # You can change the instance type of an instance when you migrate the instance to a dedicated host. The new instance type must match the type of the specified dedicated host. For more information, see [Dedicated host types](https://help.aliyun.com/document_detail/68564.html).
        # 
        # *   If you specify this parameter, you must also specify `DedicatedHostId`.
        # *   You cannot change the instance type of an instance if you use the automatic deployment feature to migrate the instance.
        self.instance_type = instance_type
        # Specifies whether to stop the instance before it is migrated to the destination dedicated host. Valid values:
        # 
        # *   reboot: stops the instance before it is migrated.
        # *   live: migrates the instance without stopping it. If you set MigrationType to live, you must specify DedicatedHostId. In this case, you cannot change the instance type of the instance when the instance is migrated.
        # 
        # Default value: reboot.
        self.migration_type = migration_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to remove the specified instance from the specified deployment set. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        # 
        # > If you set this parameter to true, you must specify InstanceId and DeploymentSetId and make sure that the specified instance belongs to the specified deployment set.
        self.remove_from_deployment_set = remove_from_deployment_set
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to deploy the instance on a dedicated host. Set the value to host, which indicates that the instance is deployed on a dedicated host.
        self.tenancy = tenancy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affinity is not None:
            result['Affinity'] = self.affinity

        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.deployment_set_group_no is not None:
            result['DeploymentSetGroupNo'] = self.deployment_set_group_no

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.force is not None:
            result['Force'] = self.force

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remove_from_deployment_set is not None:
            result['RemoveFromDeploymentSet'] = self.remove_from_deployment_set

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DeploymentSetGroupNo') is not None:
            self.deployment_set_group_no = m.get('DeploymentSetGroupNo')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoveFromDeploymentSet') is not None:
            self.remove_from_deployment_set = m.get('RemoveFromDeploymentSet')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')

        return self


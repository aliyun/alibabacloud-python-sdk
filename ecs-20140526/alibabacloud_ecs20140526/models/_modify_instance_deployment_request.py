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
        # Specifies whether the instance is associated with the dedicated host. Valid values:
        # 
        # - host: The instance is associated with the dedicated host. When an instance that has economical mode enabled is restarted after being stopped, the instance is still deployed on the original dedicated host.
        # 
        # - default: The instance is not associated with the dedicated host. When an instance that has economical mode enabled is restarted after being stopped, if the resources of the original dedicated host are insufficient, the instance can be migrated to another dedicated host in the automatic deployment resource pool.
        # 
        # Default value when migrating an instance from a shared host to a dedicated host: default.
        self.affinity = affinity
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The ID of the dedicated host. You can call [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) to query available dedicated hosts.
        # 
        # When you modify the host of an ECS instance (migrate the instance from a shared host to a dedicated host or between dedicated hosts):
        # - To migrate the instance to a specified dedicated host, you must specify this parameter.
        # - To migrate the instance to a dedicated host that is automatically selected by the system, you must set this parameter to empty and set the `Tenancy` parameter to host.
        # 
        # For more information about the automatic deployment feature, see [Features of dedicated hosts](https://help.aliyun.com/document_detail/118938.html).
        self.dedicated_host_id = dedicated_host_id
        # The group number of the instance in the deployment set when the deployment set uses the availability group strategy (AvailabilityGroup). Valid values: 1 to 7.
        # 
        # > If you change the deployment set of an ECS instance and the deployment set uses the availability group strategy (`AvailablilityGroup`), the system automatically distributes ECS instances evenly across groups when this parameter is not specified. If you specify the same deployment set that the instance currently belongs to, the system also redistributes ECS instances evenly across groups.
        self.deployment_set_group_no = deployment_set_group_no
        # The ID of the deployment set.
        # 
        # This parameter is required when you add an ECS instance to a deployment set or change the deployment set of an ECS instance.
        # 
        # > When you modify dedicated host-related parameters (`Tenancy`, `Affinity`, and `DedicatedHostId`), you cannot modify the deployment set at the same time.
        self.deployment_set_id = deployment_set_id
        # Specifies whether to forcefully change the host when the instance is added to a deployment set. Valid values:
        #          
        # - true: Allows the operation. Allows restarting ECS instances in the Running or Stopped state. Stopped instances do not include pay-as-you-go ECS instances that have economical mode enabled.
        #     > If the specified ECS instance has local disks attached, the local disks are also forcefully replaced. This may cause data loss on the local disks during host replacement. Proceed with caution.
        # 
        # - false: Does not allow the operation. The instance is added to the deployment set only on the current host. This may cause the deployment set change to fail.
        # 
        # Default value: false.
        self.force = force
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The target instance type of the ECS instance. You can call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the most recent instance type list.
        # 
        # When you modify the host of an ECS instance, you can also change ECS instance type. The target instance type must match the specifications of the specified dedicated host. For more information, see [Dedicated host types](https://help.aliyun.com/document_detail/68564.html).
        # - To change ECS instance type, you must specify the dedicated host ID by setting the `DedicatedHostId` parameter.
        # - You cannot change ECS instance type when using the automatic deployment feature to migrate an ECS instance.
        self.instance_type = instance_type
        # Specifies whether to stop ECS instance before migrating it to the destination dedicated host. Valid values:
        # 
        # - reboot: Stops ECS instance before migration.
        # 
        # - live: Migrates ECS instance without stopping it. In this case, you must specify the DedicatedHostId parameter. This value does not support changing ECS instance type while migrating ECS instance.
        # 
        # Default value: reboot.
        self.migration_type = migration_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to remove the selected instance from the selected deployment set. Valid values:
        # 
        # - true: Yes.
        # 
        # - false: No.
        # 
        # Default value: false.
        # 
        # > When this parameter is set to true, you must specify the InstanceId and DeploymentSetId that have an ownership relationship.
        self.remove_from_deployment_set = remove_from_deployment_set
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether the instance is deployed on a dedicated host. Valid values: host. The instance is deployed only on a dedicated host.
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


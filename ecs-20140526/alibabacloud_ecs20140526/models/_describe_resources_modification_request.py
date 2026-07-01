# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeResourcesModificationRequest(DaraModel):
    def __init__(
        self,
        conditions: List[str] = None,
        cores: int = None,
        destination_resource: str = None,
        instance_type: str = None,
        memory: float = None,
        migrate_across_zone: bool = None,
        operation_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The list of conditions.
        self.conditions = conditions
        # The number of vCPU kernels of the target instance type. For valid values, see [Instance family](https://help.aliyun.com/document_detail/25378.html).
        # 
        # This parameter takes effect only when DestinationResource is set to InstanceType.
        self.cores = cores
        # The type of the resource to be changed. Valid values: 
        #          
        # - InstanceType: instance type.
        # - SystemDisk: system disk type.
        # 
        #   If you set this parameter to SystemDisk, you must also specify the InstanceType parameter to indicate the disk type required by the target instance type.
        # 
        # This parameter is required.
        self.destination_resource = destination_resource
        # The target instance type. For more information, see [Instance family](https://help.aliyun.com/document_detail/25378.html). You can also call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the most recent instance type list.
        # 
        # If DestinationResource is set to SystemDisk, you must also specify the InstanceType parameter to indicate the disk type required by the target instance type.
        self.instance_type = instance_type
        # The memory size of the target instance type. Unit: GiB. For valid values, see [Instance family](https://help.aliyun.com/document_detail/25378.html).
        # 
        # This parameter takes effect only when DestinationResource is set to InstanceType.
        self.memory = memory
        # Specifies whether cross-cluster instance type changes are supported. Valid values: 
        #         
        # - true: Supported.
        # - false: Not supported.
        # 
        # Default value: false.
        # 
        # If the MigrateAcrossZone parameter is set to true and you upgrade or downgrade the Elastic Compute Service instance based on the returned information, take note of the following items: 
        #             
        # - VPC-type instances: For [retired instance types](https://help.aliyun.com/document_detail/55263.html), when a non-I/O optimized instance is changed to an I/O optimized instance, the disk device names and software authorization codes of the server are changed. For Linux instances, basic disks (cloud) are identified as xvda or xvdb. Ultra disks (cloud_efficiency) and standard SSDs (cloud_ssd) are identified as vda or vdb.
        self.migrate_across_zone = migrate_across_zone
        # The type of the Upgrade/Downgrade operation.
        # 
        # - Valid values for subscription resources: 
        # 
        #     - Upgrade: upgrades resources.
        #     - Downgrade: downgrades resources.
        #     - RenewDowngrade: downgrades resources upon renewal.
        #     - RenewModify: renewal with specification change for expired instances.
        # 
        # - Valid value for pay-as-you-go resources: Upgrade.
        # 
        # Default value: Upgrade.
        self.operation_type = operation_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance whose configuration you want to change. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instance ID (InstanceId) of the instance whose instance type or system disk type you want to change.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the target zone.
        # 
        # Specify this parameter when you want to change the instance type across zones.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditions is not None:
            result['Conditions'] = self.conditions

        if self.cores is not None:
            result['Cores'] = self.cores

        if self.destination_resource is not None:
            result['DestinationResource'] = self.destination_resource

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.migrate_across_zone is not None:
            result['MigrateAcrossZone'] = self.migrate_across_zone

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('DestinationResource') is not None:
            self.destination_resource = m.get('DestinationResource')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MigrateAcrossZone') is not None:
            self.migrate_across_zone = m.get('MigrateAcrossZone')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


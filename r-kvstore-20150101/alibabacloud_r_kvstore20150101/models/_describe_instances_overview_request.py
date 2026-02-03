# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstancesOverviewRequest(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        charge_type: str = None,
        edition_type: str = None,
        engine_version: str = None,
        instance_class: str = None,
        instance_ids: str = None,
        instance_status: str = None,
        instance_type: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        private_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        search_key: str = None,
        security_token: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The architecture of the instance. Valid values:
        # 
        # *   **cluster**: cluster architecture
        # *   **standard**: standard architecture
        # *   **rwsplit**: read/write splitting architecture
        self.architecture_type = architecture_type
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The edition of the instance. Valid values:
        # 
        # *   **Community**: Redis Open-Source Edition
        # *   **Enterprise**: Tair (Enterprise Edition)
        self.edition_type = edition_type
        # The engine version of the instance. Valid values: **2.8**, **4.0**, **5.0**, **6.0**, and **7.0**.
        # 
        # Valid values:
        # 
        # *   1.0
        # *   2.8
        # *   4.0
        # *   5.0
        # *   6.0
        # *   7.0
        self.engine_version = engine_version
        # The instance type of the instance. For more information, see [Instance types](https://help.aliyun.com/document_detail/107984.html).
        self.instance_class = instance_class
        # The IDs of instances.
        # 
        # > By default, all instances that belong to this account are queried. If you specify multiple instance IDs, separate the instance IDs with commas (,).
        self.instance_ids = instance_ids
        # The state of the instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Creating**: The instance is being created.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Inactive**: The instance is disabled.
        # *   **Flushing**: The instance is being released.
        # *   **Released**: The instance is released.
        # *   **Transforming**: The billing method of the instance is being changed.
        # *   **Unavailable**: The instance is unavailable.
        # *   **Error**: The instance failed to be created.
        # *   **Migrating**: The instance is being migrated.
        # *   **BackupRecovering**: The instance is being restored from a backup.
        # *   **MinorVersionUpgrading**: The minor version of the instance is being updated.
        # *   **NetworkModifying**: The network type of the instance is being changed.
        # *   **SSLModifying**: The SSL certificate of the instance is being changed.
        # *   **MajorVersionUpgrading**: The major version of the instance is being upgraded. The instance remains accessible during the upgrade.
        # 
        # > For more information about instance states, see [Instance states and impacts](https://help.aliyun.com/document_detail/200740.html).
        self.instance_status = instance_status
        # The category of the instance. Valid values:
        # 
        # *   **Tair**
        # *   **Redis**
        # *   **Memcache**
        self.instance_type = instance_type
        # The network type of the instance. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: Virtual Private Cloud (VPC)
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The private IP address of the instance.
        self.private_ip = private_ip
        # The ID of the region in which the instances you want to query reside. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instances you want to query belong.
        # 
        # > You can query resource group IDs by using the Tair (Redis OSS-compatible) console or by calling the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation. For more information, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The keyword used for fuzzy search. The keyword can be based on an instance ID or an instance description.
        self.search_key = search_key
        self.security_token = security_token
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.edition_type is not None:
            result['EditionType'] = self.edition_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EditionType') is not None:
            self.edition_type = m.get('EditionType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


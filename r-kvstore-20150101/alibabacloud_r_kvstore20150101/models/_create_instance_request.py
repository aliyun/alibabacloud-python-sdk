# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        appendonly: str = None,
        auto_renew: str = None,
        auto_renew_period: str = None,
        auto_use_coupon: str = None,
        backup_id: str = None,
        business_info: str = None,
        capacity: int = None,
        charge_type: str = None,
        cluster_backup_id: str = None,
        connection_string_prefix: str = None,
        coupon_no: str = None,
        dedicated_host_group_id: str = None,
        dry_run: bool = None,
        engine_version: str = None,
        global_instance: bool = None,
        global_instance_id: str = None,
        global_security_group_ids: str = None,
        instance_class: str = None,
        instance_endpoint_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        network_type: str = None,
        node_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        param_group_id: str = None,
        password: str = None,
        period: str = None,
        port: str = None,
        private_ip_address: str = None,
        read_only_count: int = None,
        recover_config_mode: str = None,
        region_id: str = None,
        replica_count: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        secondary_zone_id: str = None,
        security_token: str = None,
        shard_count: int = None,
        slave_read_only_count: int = None,
        slave_replica_count: int = None,
        src_dbinstance_id: str = None,
        tag: List[main_models.CreateInstanceRequestTag] = None,
        token: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable AOF persistence for the new instance. Valid values:
        # 
        # - **yes** (default): Enables AOF persistence.
        # 
        # - **no**: Disables AOF persistence.
        # 
        # > This parameter is available only for classic edition instances. AOF persistence cannot be configured for cloud native edition instances at creation.
        self.appendonly = appendonly
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # - **true**: Enables auto-renewal.
        # 
        # - **false** (default): Disables auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration, in months. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # > This parameter is required when **AutoRenew** is set to **true**.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to use a coupon. Valid values:
        # 
        # - **true**: Uses a coupon.
        # 
        # - **false** (default): Does not use a coupon.
        self.auto_use_coupon = auto_use_coupon
        # The ID of the backup that you want to use to create the new instance. You can obtain backup IDs by calling the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation. If the source instance has a cluster architecture, you must specify the backup IDs of all its shards, separated by commas (for example, "10\\*\\*,11\\*\\*,15\\*\\*").
        # 
        # > If your source instance is a cloud native cluster instance, it is recommended to call [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) to get a cluster backup ID (for example, "cb-xx") and use the `ClusterBackupId` parameter instead. This avoids the need to specify the backup ID for each shard.
        self.backup_id = backup_id
        # The campaign ID or business information.
        self.business_info = business_info
        # The storage capacity of the instance, in MB.
        # 
        # > You must specify either the **Capacity** or the **InstanceClass** parameter.
        self.capacity = capacity
        # The billing method. Valid values:
        # 
        # - **PrePaid**: subscription.
        # 
        # - **PostPaid** (default): pay-as-you-go.
        self.charge_type = charge_type
        # The ID of the cluster backup. You can get this ID by calling the [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) operation. This parameter is available for some cloud native cluster instances.
        # 
        # - This parameter is mutually exclusive with `BackupId`.
        # 
        # - If this parameter is not available for your instance, you must specify the backup ID of each shard in the `BackupId` parameter (for example, "2158\\*\\*\\*\\*20,2158\\*\\*\\*\\*22").
        self.cluster_backup_id = cluster_backup_id
        # The prefix of the connection string. The prefix must be 8 to 40 characters long, start with a lowercase letter, and contain only lowercase letters and digits.
        # 
        # > The full connection string is in the format: \\<prefix>.redis.rds.aliyuncs.com.
        self.connection_string_prefix = connection_string_prefix
        # The coupon code. Default value: `default`.
        self.coupon_no = coupon_no
        # The ID of the dedicated host group. This parameter is required when you create a Redis instance in a dedicated host group.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Checks the request for validity without creating the instance. The system verifies required parameters, request format, and service limits. If the request is valid, the `DryRunOperation` error code is returned. If the request is invalid, an error message is returned.
        # 
        # - **false** (default): Sends the request. If the request is valid, the instance is created.
        self.dry_run = dry_run
        # The Redis engine version. Valid values for **classic edition** instances:
        # 
        # - **2.8** (Not recommended. [Support for this version is scheduled to be discontinued](https://help.aliyun.com/document_detail/2674657.html).)
        # 
        # - **4.0** (Not recommended.)
        # 
        # - **5.0**
        # 
        # Valid values for **cloud native edition** instances:
        # 
        # - **5.0**
        # 
        # - **6.0** (Recommended)
        # 
        # - **7.0**
        # 
        # > The default value is **5.0**.
        self.engine_version = engine_version
        # Specifies whether to create the new instance as the first child instance of a distributed instance. Valid values:
        # 
        # - **true**: Creates the instance as the first child instance.
        # 
        # - **false** (default): Does not create the instance as the first child instance.
        # 
        # > * If you set this parameter to **true**, the new instance must be a Tair memory-enhanced instance that runs Redis 5.0.
        # >
        # > * This parameter is available only in Chinese mainland.
        self.global_instance = global_instance
        # The ID of the distributed instance. This parameter is available only in Chinese mainland.
        # 
        # <props="china">
        # 
        # This parameter is required to add the new instance as a child of a distributed instance. For more information and the console procedure, see [Add a child instance to a distributed instance](https://help.aliyun.com/document_detail/106885.html).
        self.global_instance_id = global_instance_id
        # The IDs of the security groups to associate with the instance. You can specify multiple security group IDs, separated by commas (,). IDs cannot be repeated.
        # >Notice: This parameter is available only for cloud native edition instances. Security groups are not supported for classic edition instances.
        self.global_security_group_ids = global_security_group_ids
        # The instance type. For example, `redis.master.small.default` specifies a 1 GB Community Edition (classic edition) instance with a standard, dual-replica architecture. For more information, see [Instance specifications](https://help.aliyun.com/document_detail/26350.html).
        # 
        # > You must specify either the **Capacity** or the **InstanceClass** parameter.
        self.instance_class = instance_class
        # The connection endpoint type. This parameter is applicable only when you create a dual-zone, read/write splitting instance of the cloud native edition. If this parameter is not specified, `AzIndependentEndpoint` is used. Valid values:
        # 
        # - **AzIndependentEndpoint**: (**Default**) Zone-Independent Endpoint. The primary and secondary zones each provide an independent connection string for zone-local access.
        # 
        # - **UnifiedEndpoint**: Unified Endpoint. Provides a single connection string to access nodes in both zones, which may result in cross-zone access.
        # 
        # >Notice: 
        # 
        # This parameter is applicable only to dual-zone, read/write splitting instances of the cloud native edition. For other instance types, only zone-independent endpoints are supported, and specifying `UnifiedEndpoint` has no effect.
        # 
        # 
        # 
        # >Notice: 
        # 
        # The `UnifiedEndpoint` parameter is currently available only to allowlisted users. API calls will fail if you are not on the allowlist. To be added to the allowlist, submit a ticket.
        self.instance_endpoint_type = instance_endpoint_type
        # The name of the instance. The name must be 2 to 80 characters long, start with a letter (uppercase or lowercase) or a Chinese character, and not contain spaces or the characters `@/:=”<>{[]}`.
        self.instance_name = instance_name
        # The instance type. Valid values:
        # 
        # - **Redis** (default)
        # 
        # - **Memcache**
        self.instance_type = instance_type
        # The end time of the maintenance window. Specify the time in the *HH:mm*Z format (UTC). For example, to set the end time to 02:00 (UTC+8), specify `18:00Z`.
        # 
        # > The duration of the maintenance window must be at least one hour.
        # 
        # > If this parameter is not specified, the maintenance window ends at 06:00 (UTC+8), which is 22:00 (UTC).
        self.maintain_end_time = maintain_end_time
        # The start of the maintenance window. Specify the time in the *HH:mm*Z format (UTC). For example, to set the start time to 01:00 (UTC+8), specify `17:00Z`.
        # 
        # > If this parameter is not specified, the maintenance window starts at 02:00 (UTC+8), which is 18:00 (UTC).
        self.maintain_start_time = maintain_start_time
        # The network type. Valid value:
        # 
        # - **VPC**: Deploys the instance in a Virtual Private Cloud. This is the default value.
        self.network_type = network_type
        # The node type. Valid values:
        # 
        # - **MASTER_SLAVE**: high-availability (primary-replica)
        # 
        # - **STAND_ALONE**: standalone (single-node)
        # 
        # - **double**: primary-replica
        # 
        # - **single**: standalone (single-node)
        # 
        # > Set this parameter to **MASTER_SLAVE** or **STAND_ALONE** for cloud native edition instances. Set this parameter to **double** or **single** for classic edition instances.
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the parameter group. This ID must be globally unique.>Notice:  This parameter is available only for cloud native edition instances.
        self.param_group_id = param_group_id
        # The password for the instance. The password must be 8 to 32 characters long and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The allowed special characters are `!@#$%^&*()_+-=`.
        self.password = password
        # The subscription duration, in months. Valid values: **1** to **9**, **12**, **24**, **36**, and **60**.
        # 
        # > This parameter is available and required only when **ChargeType** is set to **PrePaid**.
        self.period = period
        # The service port of the instance. The port number must be between **1** and **65535**. The default value is **6379**.
        self.port = port
        # The private IP address of the new instance.
        # 
        # > The IP address must be within the CIDR block of the specified vSwitch.
        self.private_ip_address = private_ip_address
        # The number of read-only replicas in the primary zone. This parameter is available only when creating a read/write splitting instance of the cloud native edition.
        # 
        # - For a standard-architecture instance, the value must be an integer from 1 to 9.
        # 
        # - For a cluster-architecture instance, the value must be an integer from 1 to 4. This specifies the number of read-only replicas for each data shard.
        # 
        # > If you create a multi-zone instance, you can use this parameter and `SlaveReadOnlyCount` to customize the number of read-only replicas in the primary and secondary zones.
        # >
        # > - The sum of this parameter and `SlaveReadOnlyCount` cannot exceed 9 for a standard-architecture instance.
        # >
        # > - The sum of this parameter and `SlaveReadOnlyCount` cannot exceed 4 for a cluster-architecture instance.
        self.read_only_count = read_only_count
        # Specifies which configurations to restore from the backup when creating an instance. Valid values include `account`, `config`, and `whitelist`. For example, to restore account settings, specify `account`. To restore multiple configurations, separate them with commas.
        # 
        # By default, this parameter is empty, which means no configurations are restored.
        # 
        # > This parameter is applicable only to cloud native edition instances. The source backup must contain the specified configurations. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation and check the `RecoverConfigMode` field in the response to determine which configurations a backup contains.
        self.recover_config_mode = recover_config_mode
        # The ID of the region in which to create the instance. Call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to get a list of region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of replicas in the primary zone. This parameter is available only for multi-replica cluster instances of the cloud native edition. You can specify a value from 1 to 4.
        # 
        # > When creating a multi-zone instance, you can use this parameter and `SlaveReplicaCount` to customize the number of replicas in the primary and secondary zones. The sum of `ReplicaCount` and `SlaveReplicaCount` cannot exceed 4.
        self.replica_count = replica_count
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data, specified in the *yyyy-MM-dd*T*HH:mm:ss*Z (UTC) format.
        self.restore_time = restore_time
        # The ID of the secondary zone. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473764.html) operation to query the latest list of zones.
        # 
        # > The value of this parameter cannot be the same as the value of the `ZoneId` parameter, and you cannot specify a multi-zone ID.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of shards. This parameter is available only for cloud native edition instances.
        # 
        # - A value of **1** creates an instance with a standard architecture.
        # 
        # - A value greater than **1** creates an instance with a cluster architecture.
        self.shard_count = shard_count
        # The number of read-only replicas in the secondary zone.
        self.slave_read_only_count = slave_read_only_count
        # The number of replicas in the secondary zone.
        self.slave_replica_count = slave_replica_count
        # To create an instance from a backup, specify the ID of the source instance.
        # 
        # > This parameter must be used in conjunction with one of the following parameters: **BackupId**, **ClusterBackupId** (recommended for cloud native, cluster-architecture instances), or **RestoreTime**.
        self.src_dbinstance_id = src_dbinstance_id
        # The tags of the instance.
        self.tag = tag
        # A client-generated token to ensure the idempotence of the request. The token must be unique across requests, case-sensitive, and cannot exceed 64 ASCII characters.
        self.token = token
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The ID of the primary zone for the instance. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473763.html) operation to query available zones.
        # 
        # > You can also specify a secondary zone by using the `SecondaryZoneId` parameter. The primary and replica nodes are then deployed in the specified primary and secondary zones to create a dual-zone architecture for in-city disaster recovery. For example, you can set the `ZoneId` parameter to "cn-hangzhou-h" and the `SecondaryZoneId` parameter to "cn-hangzhou-g".
        self.zone_id = zone_id

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
        if self.appendonly is not None:
            result['Appendonly'] = self.appendonly

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_backup_id is not None:
            result['ClusterBackupId'] = self.cluster_backup_id

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.global_instance is not None:
            result['GlobalInstance'] = self.global_instance

        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id

        if self.global_security_group_ids is not None:
            result['GlobalSecurityGroupIds'] = self.global_security_group_ids

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_endpoint_type is not None:
            result['InstanceEndpointType'] = self.instance_endpoint_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.param_group_id is not None:
            result['ParamGroupId'] = self.param_group_id

        if self.password is not None:
            result['Password'] = self.password

        if self.period is not None:
            result['Period'] = self.period

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.read_only_count is not None:
            result['ReadOnlyCount'] = self.read_only_count

        if self.recover_config_mode is not None:
            result['RecoverConfigMode'] = self.recover_config_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_count is not None:
            result['ReplicaCount'] = self.replica_count

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.slave_read_only_count is not None:
            result['SlaveReadOnlyCount'] = self.slave_read_only_count

        if self.slave_replica_count is not None:
            result['SlaveReplicaCount'] = self.slave_replica_count

        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.token is not None:
            result['Token'] = self.token

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Appendonly') is not None:
            self.appendonly = m.get('Appendonly')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterBackupId') is not None:
            self.cluster_backup_id = m.get('ClusterBackupId')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('GlobalInstance') is not None:
            self.global_instance = m.get('GlobalInstance')

        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')

        if m.get('GlobalSecurityGroupIds') is not None:
            self.global_security_group_ids = m.get('GlobalSecurityGroupIds')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceEndpointType') is not None:
            self.instance_endpoint_type = m.get('InstanceEndpointType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParamGroupId') is not None:
            self.param_group_id = m.get('ParamGroupId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ReadOnlyCount') is not None:
            self.read_only_count = m.get('ReadOnlyCount')

        if m.get('RecoverConfigMode') is not None:
            self.recover_config_mode = m.get('RecoverConfigMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaCount') is not None:
            self.replica_count = m.get('ReplicaCount')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('SlaveReadOnlyCount') is not None:
            self.slave_read_only_count = m.get('SlaveReadOnlyCount')

        if m.get('SlaveReplicaCount') is not None:
            self.slave_replica_count = m.get('SlaveReplicaCount')

        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # > - `N` represents the sequence number of the tag, from 1 to 20. You can add a maximum of 20 tags to an instance.
        # >
        # > - If the tag key does not exist, it is automatically created.
        self.key = key
        # The value for tag `N`.
        # 
        # > The N in **Tag.N.Value** specifies the sequence number of the tag. For example, **Tag.1.Value** specifies the value of the first tag, and **Tag.2.Value** specifies the value of the second tag.
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


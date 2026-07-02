# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class CreateTairInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        auto_renew_period: str = None,
        auto_use_coupon: str = None,
        backup_id: str = None,
        business_info: str = None,
        charge_type: str = None,
        client_token: str = None,
        cluster_backup_id: str = None,
        connection_string_prefix: str = None,
        coupon_no: str = None,
        dry_run: bool = None,
        engine_version: str = None,
        global_instance_id: str = None,
        global_security_group_ids: str = None,
        instance_class: str = None,
        instance_endpoint_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        param_group_id: str = None,
        password: str = None,
        period: int = None,
        port: int = None,
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
        shard_type: str = None,
        slave_read_only_count: int = None,
        slave_replica_count: int = None,
        src_dbinstance_id: str = None,
        storage: int = None,
        storage_type: str = None,
        tag: List[main_models.CreateTairInstanceRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Set the value to **true**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # - **true**: Enable auto-renewal.
        # 
        # - **false** (default): Disable auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: month. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # > This parameter is required only when the **AutoRenew** parameter is set to **true**.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to use a coupon. Valid values:
        # 
        # - **true**: Use a coupon.
        # 
        # - **false** (default): Do not use a coupon.
        self.auto_use_coupon = auto_use_coupon
        # The ID of the backup set from the source instance. The system creates a new instance based on the data in this backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation to query the backup set ID. If the source instance is a cluster instance, you must specify the backup ID for each shard, separated by commas, for example, "10\\*\\*,11\\*\\*,15\\*\\*".
        # 
        # > If your instance is a cloud-native cluster instance, we recommend that you call the [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) operation to query the cluster backup ID, such as `cb-xx`. Then, specify the cluster backup ID for the `ClusterBackupId` parameter to clone the cluster instance. This avoids the need to specify the backup ID of each shard.
        self.backup_id = backup_id
        # The business information. This can be the ID of a promotion or a business context.
        self.business_info = business_info
        # The billing method of the instance. Valid values:
        # 
        # - **PrePaid** (default): The subscription billing method.
        # 
        # - **PostPaid**: The pay-as-you-go billing method.
        self.charge_type = charge_type
        # A client-generated token that ensures the idempotence of the request. The token must be unique among different requests. It is case-sensitive and cannot exceed 64 ASCII characters in length.
        self.client_token = client_token
        # The ID of the cluster backup set. Some instances that use the cluster architecture support cluster backup sets. You can call the [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) operation to query for cluster backup set IDs.
        # 
        # - If this feature is supported, you can specify this parameter and leave the **BackupId** parameter empty.
        # 
        # - If this feature is not supported, you must specify the backup ID of each shard of the source instance for the `BackupId` parameter. Separate the backup IDs with commas, for example, "2158\\*\\*\\*\\*20,2158\\*\\*\\*\\*22".
        self.cluster_backup_id = cluster_backup_id
        # The prefix of the connection string. It must start with a lowercase letter, consist of lowercase letters and digits, and be 8 to 40 characters in length.
        # 
        # > The full connection string is in the format of `<prefix>-<instance ID>.redis.rds.aliyuncs.com`.
        self.connection_string_prefix = connection_string_prefix
        # The coupon code.
        self.coupon_no = coupon_no
        # Specifies whether to perform a precheck for this request. Valid values:
        # 
        # - **true**: Performs a precheck and does not create the instance. The system checks the request parameters, request format, service limits, and available inventory. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): Sends a normal request and creates the instance after the request passes the precheck.
        self.dry_run = dry_run
        # The database version. Default value: **1.0**. The valid values depend on the Tair instance series:
        # 
        # - **tair_rdb**: Tair memory-enhanced instances are compatible with Redis 5.0, Redis 6.0, and Redis 7.0. Set the value to **5.0**, **6.0**, or **7.0**.
        # 
        # - **tair_scm**: Tair persistent memory-optimized instances are compatible with Redis 6.0. Set the value to **1.0**.
        # 
        # - **tair_essd**: Tair disk-based instances (ESSD/SSD) are compatible with Redis 6.0. Set the value to **1.0** to create an ESSD-based instance or **2.0** to create an SSD-based instance.
        self.engine_version = engine_version
        # Specifies whether to create the instance as a child instance in a distributed instance. By using this parameter, you can create a distributed instance.
        # 
        # - To create the first child instance, set this parameter to **true**.
        # 
        # - To create the second or third child instance, specify the ID of the distributed instance, such as `gr-bp14rkqrhac****`.
        # 
        # - If you do not want to create a distributed instance, do not specify this parameter.
        # 
        # > To be created as a child instance of a distributed instance, the new instance must be a Tair memory-enhanced instance.
        self.global_instance_id = global_instance_id
        # The IDs of the global IP whitelist templates for the instance. To specify multiple template IDs, separate them with commas. The IDs cannot be repeated.
        self.global_security_group_ids = global_security_group_ids
        # The instance type. For more information, see the following topics:
        # 
        # - [Memory-enhanced instance types](https://help.aliyun.com/document_detail/2527112.html)
        # 
        # - [Persistent memory-optimized instance types](https://help.aliyun.com/document_detail/2527110.html)
        # 
        # - [Disk-based instance types](https://help.aliyun.com/document_detail/2527111.html)
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The type of connection string to use when creating a cloud-native, dual-zone instance with the read/write splitting architecture. If you do not specify this parameter, the default value `AzIndependentEndpoint` is used.
        # 
        # - **AzIndependentEndpoint** (**default**): Zone-specific connection string. The primary and secondary zones each provide an independent connection string, allowing clients to connect to the nearest zone.
        # 
        # - **UnifiedEndpoint**: Unified connection string. A single connection string is provided to access nodes in both the primary and secondary zones, but this may cause cross-zone access.
        # 
        # >Notice: 
        # 
        # This parameter applies only to cloud-native, dual-zone instances with the read/write splitting architecture. Other instance types support only zone-specific connection strings.
        # 
        # 
        # 
        # >Notice: 
        # 
        # The `UnifiedEndpoint` option is available only to users on a whitelist. If a non-whitelisted user specifies this value, the request fails. To request access, submit a ticket.
        self.instance_endpoint_type = instance_endpoint_type
        # The name of the instance. The name must meet the following requirements:
        # 
        # - It must be 2 to 80 characters in length.
        # 
        # - It must start with an uppercase or lowercase letter or a Chinese character. It cannot contain spaces or the following special characters: `@/:=”<>{[]}`.
        self.instance_name = instance_name
        # The Tair instance series, which determines the storage medium. Valid values:
        # 
        # - **tair_rdb**: memory-enhanced
        # 
        # - **tair_scm**: persistent memory-optimized
        # 
        # - **tair_essd**: disk-based
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The end time of the maintenance window. Specify the time in the *HH:mm*Z format (UTC). For example, to end the maintenance at 02:00 (UTC+8), set this parameter to `18:00Z`.
        # 
        # > The maintenance window must be at least one hour long.
        # 
        # > If this parameter is not specified, the maintenance window ends at 22:00 UTC (06:00 UTC+8) by default.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window. Specify the time in the *HH:mm*Z format (UTC). For example, to start the maintenance at 01:00 (UTC+8), set this parameter to `17:00Z`.
        # 
        # > If this parameter is not specified, the maintenance window starts at 18:00 UTC (02:00 UTC+8) by default.
        self.maintain_start_time = maintain_start_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the parameter template. The instance is created by using the parameters defined in this template.
        self.param_group_id = param_group_id
        # The password of the instance. The password must meet the following requirements:
        # 
        # - It must be 8 to 32 characters in length.
        # 
        # - It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The supported special characters are `!@#$%^&*()_+-=`.
        self.password = password
        # The subscription duration, in months. Valid values: **1**, **2**, **3**, **4**, **5**, **6**, 7, 8, 9, 12, 24, 36, and 60.
        # 
        # > This parameter is required only when you set the `ChargeType` parameter to `PrePaid`.
        self.period = period
        # The service port of the instance. Valid values: 1 to 65535. Default value: 6379.
        self.port = port
        # The private IP address of the instance.
        # 
        # > The IP address must be within the CIDR block of the vSwitch to which the instance belongs. You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation to query the CIDR block information.
        self.private_ip_address = private_ip_address
        # The number of read-only nodes in the primary zone. This parameter is applicable only to cloud-native instances that use the read/write splitting architecture.
        # 
        # - If the instance uses the standard architecture, the valid values are 1 to 9.
        # 
        # - If the instance uses the cluster architecture, specify the number of read-only nodes per shard. The valid values are 1 to 4.
        # 
        # > If you create a multi-zone instance, you can use this parameter and the `SlaveReadOnlyCount` parameter to customize the number of read-only nodes in the primary and secondary zones.
        # >
        # > - If the instance uses the standard architecture, the sum of `ReadOnlyCount` and `SlaveReadOnlyCount` cannot exceed 9.
        # >
        # > - If the instance uses the cluster architecture, the sum of `ReadOnlyCount` and `SlaveReadOnlyCount` cannot exceed 4.
        self.read_only_count = read_only_count
        # When creating an instance from a backup set, specifies whether to restore configurations such as account information (`account`), kernel parameters (`config`), and whitelists (`whitelist`) from the source backup set. To restore a specific configuration, specify its keyword. To restore multiple configurations, separate the keywords with commas.
        # 
        # If this parameter is not specified, no configurations are restored from the source backup set.
        # 
        # > This parameter applies only to cloud-native instances, and the source backup set must contain the specified configuration information. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation and check the `RecoverConfigMode` parameter in the response to check if the backup set contains the information.
        self.recover_config_mode = recover_config_mode
        # The ID of the region where you want to create the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of replica nodes in the primary zone. This parameter is applicable only to cloud-native, multi-replica cluster instances. You can use this parameter to customize the number of replica nodes. Valid values: 1 to 4.
        # 
        # > If you create a multi-zone instance, you can use this parameter and the `SlaveReplicaCount` parameter to customize the number of replica nodes in the primary and secondary zones. The sum of `ReplicaCount` and `SlaveReplicaCount` cannot exceed 4.
        self.replica_count = replica_count
        # The ID of the resource group to which the instance belongs.
        # 
        # > - You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation or use the Resource Management console to query the IDs of resource groups. For more information, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        # >
        # > - Before you change the resource group of an instance, you can call the [ListResources](https://help.aliyun.com/document_detail/158866.html) operation to view the current resource group of the instance.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # If point-in-time recovery (PITR) is enabled for the source instance, you can specify a point in time within the backup retention period. The system creates a new instance by using the backup data of the source instance at that point in time. Specify the time in the *yyyy-MM-dd*T*HH:mm:ss*Z format (UTC).
        self.restore_time = restore_time
        # The ID of the secondary zone. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query available zones.
        # 
        # > The value of this parameter cannot be the same as the value of the `ZoneId` parameter. You cannot specify a multi-zone ID.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of shards in the instance. Valid values:
        # 
        # - **1** (default): Creates a standard architecture instance with a single shard.
        # 
        # - From **2** to **32**: Creates a cluster architecture instance with the specified number of shards.
        # 
        # > You can specify a value from **2** to **32** for this parameter only when you set the **InstanceType** parameter to `tair_rdb` or `tair_scm`. Only memory-enhanced and persistent memory-optimized instances support the cluster architecture.
        self.shard_count = shard_count
        # The architecture type of the instance. Valid values:
        # 
        # - **MASTER_SLAVE** (default): The primary/replica architecture, which provides high availability.
        # 
        # - **STAND_ALONE**: single-replica. This architecture uses a single node. If the node fails, data is lost, and the system automatically creates a new, empty instance. This architecture is supported only for **single-zone** deployments and does not support cluster or read/write splitting architectures.
        self.shard_type = shard_type
        # The number of read-only nodes in the secondary zone.
        self.slave_read_only_count = slave_read_only_count
        # The number of replica nodes in the secondary zone.
        self.slave_replica_count = slave_replica_count
        # To create an instance from a backup set of an existing instance, specify the ID of the source instance.
        # 
        # > You must also specify the backup data by using one of the following parameters: **BackupId**, **ClusterBackupId**, or **RestoreTime**. We recommend that you use `ClusterBackupId` for cloud-native instances that use a cluster architecture.
        self.src_dbinstance_id = src_dbinstance_id
        # The storage space of the disk-based instance. The valid values of this parameter vary based on the instance type. For more information, see [Disk-based instance types](https://help.aliyun.com/document_detail/2527111.html).
        # 
        # > This parameter is required only when you set the **InstanceType** parameter to `tair_essd` to create a Tair instance that uses an ESSD. For Tair instances that use standard `SSD`s, the storage capacity is determined by the instance type and you do not need to specify this parameter.
        self.storage = storage
        # The storage type. Valid values: **essd_pl1**, **essd_pl2**, and **essd_pl3**.
        # 
        # > This parameter is required only when you set the **InstanceType** parameter to `tair_essd` to create a Tair instance that uses an Enhanced SSD (ESSD).
        self.storage_type = storage_type
        # The tags of the instance.
        self.tag = tag
        # The ID of the vSwitch in the specified VPC. You can call the VPC API operation [DescribeVSwitches](https://help.aliyun.com/document_detail/35739.html) to obtain the vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the Virtual Private Cloud (VPC) where you want to create the instance. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query available VPCs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the primary zone where you want to create the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query available zones.
        # 
        # > You can also specify a secondary zone by using the `SecondaryZoneId` parameter. This deploys the primary and replica nodes in different zones within the same region for a high-availability primary/replica architecture. For example, you can set `ZoneId` to `cn-hangzhou-h` and `SecondaryZoneId` to `cn-hangzhou-g`.
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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

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

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_backup_id is not None:
            result['ClusterBackupId'] = self.cluster_backup_id

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

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

        if self.shard_type is not None:
            result['ShardType'] = self.shard_type

        if self.slave_read_only_count is not None:
            result['SlaveReadOnlyCount'] = self.slave_read_only_count

        if self.slave_replica_count is not None:
            result['SlaveReplicaCount'] = self.slave_replica_count

        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

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

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterBackupId') is not None:
            self.cluster_backup_id = m.get('ClusterBackupId')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

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

        if m.get('ShardType') is not None:
            self.shard_type = m.get('ShardType')

        if m.get('SlaveReadOnlyCount') is not None:
            self.slave_read_only_count = m.get('SlaveReadOnlyCount')

        if m.get('SlaveReplicaCount') is not None:
            self.slave_replica_count = m.get('SlaveReplicaCount')

        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTairInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateTairInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # > A single request can contain up to five key-value pairs.
        self.key = key
        # The value of the tag.
        # 
        # > **N** specifies the Nth tag in the request. For example, **Tag.1.Value** specifies the value of the first tag, and **Tag.2.Value** specifies the value of the second tag.
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


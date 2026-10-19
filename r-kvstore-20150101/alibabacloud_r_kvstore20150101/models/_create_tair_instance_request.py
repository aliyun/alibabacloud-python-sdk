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
        # Specifies whether to enable auto-renewal. Valid values:
        # * **true**: enables auto-renewal.
        # * **false**: disables auto-renewal. This is the default value.
        self.auto_renew = auto_renew
        # The auto-renewal epoch. Unit: months. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # > This parameter is required when the **AutoRenew** parameter is set to **true**.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to use a voucher. Valid values:
        # * **true**: uses a voucher.
        # * **false**: does not use a voucher. This is the default value.
        self.auto_use_coupon = auto_use_coupon
        # The ID of the backup set of the source instance. The system uses the data in the specified backup set to create the instance. You can invoke the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation to query the backup set ID. If the source instance is a cluster instance, you must enter the backup set IDs of all shards in the source instance and separate them with commas, such as "10**,11**,15**".
        # > If your instance is a cloud-native architecture instance, we recommend that you invoke the [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) operation to query the cluster backup set ID, such as "cb-xx", and then specify the ClusterBackupId request parameter to clone the cluster instance. This saves you the trouble of entering the backup set ID of each shard.
        self.backup_id = backup_id
        # The activity ID and business information.
        self.business_info = business_info
        # The billing method. Valid values:
        # - **PrePaid**: subscription. This is the default value.
        # - **PostPaid**: pay-as-you-go.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token is case-sensitive and can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The ID of the cluster backup set. Some new cluster architectures support cluster backup set IDs. You can call the [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) operation to obtain the ID.
        # * If the cluster architecture supports cluster backup sets, you can enter the specified cluster backup set ID. You do not need to specify the **BackupId** parameter.
        # * If the cluster architecture does not support cluster backup sets, enter the backup set IDs of all shards in the source instance in the BackupId parameter and separate them with commas, such as "2158\\*\\*\\*\\*20,2158\\*\\*\\*\\*22".
        self.cluster_backup_id = cluster_backup_id
        # The prefix of the endpoint. The prefix must be 8 to 40 characters in length and can contain lowercase letters and digits. It must start with a lowercase letter.
        # 
        # > 
        # > The endpoint is in the following format: <Prefix-Instance ID>.redis.rds.aliyuncs.com.
        self.connection_string_prefix = connection_string_prefix
        # The coupon code.
        self.coupon_no = coupon_no
        # Specifies whether to perform a dry run before you create the instance. Valid values:
        # * **true**: performs a dry run without creating the instance. The system checks the request parameters, request format, service limits, and available resources. If the request fails the dry run, the system returns an error. If the request passes the dry run, the system returns the `DryRunOperation` error code.
        # * **false**: sends the request. If the request passes the check, the instance is created. This is the default value.
        self.dry_run = dry_run
        # The database engine version. Default value: **1.0**. The value varies based on the Tair instance type:
        # - Tair_rdb: Tair memory-enhanced instances are compatible with Redis 5.0, Redis 6.0, and Redis 7.0 protocols. Set the value to **5.0**, **6.0**, or **7.0**.
        # - Tair_scm: Tair persistent memory-optimized instances are compatible with the Redis 6.0 protocol. Set the value to **1.0**.
        # - Tair_essd: Tair disk-based (ESSD/SSD) instances are compatible with the Redis 6.0 protocol. Set the value to **1.0** for ESSD-based instances and **2.0** for SSD-based instances.
        self.engine_version = engine_version
        # Specifies whether to use the new instance as a child instance in a distributed instance. You can use this parameter to create a distributed instance.
        # * To use the new instance as the first child instance, set the value to **true**.
        # * To use the new instance as the second or third child instance, set the value to the ID of the distributed instance, such as gr-bp14rkqrhac****.
        # * If you do not want to use the new instance as a child instance in a distributed instance, leave this parameter empty.
        # > The new instance must be a Tair memory-enhanced instance if you want to use it as a child instance in a distributed instance.
        self.global_instance_id = global_instance_id
        # The global IP address whitelist templates of the instance. Separate multiple whitelist templates with commas (,). Each template must be unique.
        self.global_security_group_ids = global_security_group_ids
        # The instance type. For more information, see:
        # - [Memory-enhanced instance types](https://help.aliyun.com/document_detail/2527112.html).
        # - [Persistent memory-optimized instance types](https://help.aliyun.com/document_detail/2527110.html).
        # - [Disk-based instance types](https://help.aliyun.com/document_detail/2527111.html).
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The endpoint type used when you create a cloud-native Dual-active-zone deployment read/write splitting instance. If you do not specify this parameter, the default value is AzIndependentEndpoint.
        # 
        # - **AzIndependentEndpoint**: active zone-independent endpoint. This is the **default value**. Independent endpoints are provided for the primary and secondary active zones. You can use different endpoints to achieve nearest access.
        # - **UnifiedEndpoint**: unified endpoint. A unified endpoint is provided to access nodes in both the primary and secondary active zones. However, cross-active-zone access may occur.
        # 
        # >Notice: This parameter applies only to cloud-native Dual-active-zone deployment read/write splitting instances. For other types of instances, only active zone-independent endpoints are supported. Even if you specify UnifiedEndpoint, it does not take effect.
        # 
        # >Notice: The UnifiedEndpoint parameter is currently available only to whitelisted users. If you are not a whitelisted user and specify this parameter, an invoke error is returned. To request access, commit a ticket.
        self.instance_endpoint_type = instance_endpoint_type
        # The instance name. The name must meet the following requirements:
        # * The name must be 2 to 80 characters in length.
        # * The name must start with a letter or a Chinese character. It cannot contain spaces or the following special characters: `@/:=”<>{[]}`.
        self.instance_name = instance_name
        # The storage medium. Valid values:
        # * **tair_rdb**: memory-enhanced.
        # * **tair_scm**: persistent memory-optimized.
        # * **tair_essd**: disk-based.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The end time of the maintenance window. Specify the time in the <i>HH:mm</i>Z format. The time must be in UTC. For example, if you want the maintenance window to end at 02:00 (UTC+8), set the value to `18:00Z`.
        # 
        # > The interval between the start time and the end time must be at least 1 hour.
        # 
        # > If you do not specify this parameter, the default value is 22:00 (UTC), which is 06:00 (UTC+8).
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window. Specify the time in the <i>HH:mm</i>Z format. The time must be in UTC. For example, if you want the maintenance window to start at 01:00 (UTC+8), set the value to `17:00Z`.
        # 
        # > If you do not specify this parameter, the default value is 18:00 (UTC), which is 02:00 (UTC+8).
        self.maintain_start_time = maintain_start_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the parameter template. The instance is created based on the parameters in the specified template. Each template ID must be unique.
        self.param_group_id = param_group_id
        # The instance password. The password must meet the following requirements:
        # * The password must be 8 to 32 characters in length.
        # * The password must contain at least three of the following character types: uppercase letters, lowercase letters, special characters, and digits. Supported special characters are `!@#$%^&*()_+-=`.
        self.password = password
        # The subscription duration. Unit: months. Valid values: **1** to **9**, **12**, **24**, **36**, and **60**.
        # > This parameter is required when the **ChargeType** parameter is set to **PrePaid**.
        self.period = period
        # The service port of the instance. Valid values: 1 to 65535. Default value: 6379.
        self.port = port
        # The internal IP address of the instance.
        # 
        # > The IP address must fall within the CIDR block of the vSwitch to which the instance belongs. You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation of the VPC API to query the CIDR block information.
        self.private_ip_address = private_ip_address
        # The number of read-only nodes in the primary zone. This parameter applies only when you create a cloud-native read/write splitting instance.
        # * If the instance uses the standard architecture, valid values are 1 to 9.
        # * If the instance uses the cluster architecture, valid values are 1 to 4, which indicate the number of read-only nodes per data shard.
        # > If you create a multi-zone instance, you can use this parameter and the SlaveReadOnlyCount parameter to specify the number of read-only nodes in the primary and secondary zones.
        # > * If the instance uses the standard architecture, the sum of the values of this parameter and the SlaveReadOnlyCount parameter cannot exceed 9.
        # > * If the instance uses the cluster architecture, the sum of the values of this parameter and the SlaveReadOnlyCount parameter cannot exceed 4.
        self.read_only_count = read_only_count
        # Specifies whether to restore the account, kernel parameters, and whitelist from the original backup set when you create an instance by using a specified backup set. For example, to restore the account information, set the value to account.
        # 
        # Default value: empty. An empty value indicates that the account, kernel parameters, and whitelist are not restored from the original backup set.
        # > This parameter applies only to cloud-native instances and requires that the original backup set contains the account, kernel parameters, and whitelist information. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation to query whether the RecoverConfigMode parameter of a specified backup set contains the preceding information.
        self.recover_config_mode = recover_config_mode
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent region list. Use this parameter to specify the region where you want to create the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of secondary nodes in the primary zone. This parameter applies only when you create a cloud-native cluster instance with multiple replicas. You can use this parameter to specify the number of secondary nodes. Valid values: 1 to 4.
        # > If you create a multi-zone instance, you can use this parameter and the SlaveReplicaCount parameter to specify the number of secondary nodes in the primary and secondary zones. The sum of the values of this parameter and the SlaveReplicaCount parameter cannot exceed 4.
        self.replica_count = replica_count
        # The ID of the destination resource group.
        # 
        # > * You can invoke the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation or use the console to obtain the resource group ID list. For related operations, see [View the basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        # > * Before you change the resource group to which the instance belongs, you can invoke the [ListResources](https://help.aliyun.com/document_detail/158866.html) operation to view the current resource group of the instance.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore the source instance. If the data flashback feature is enabled for the source instance, you can specify a point in time within the backup retention period of the source instance. The system uses the backup data of the source instance at the specified point in time to create the instance. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time must be in UTC.
        self.restore_time = restore_time
        # The secondary zone ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent zone list.
        # 
        # > The value of this parameter cannot be the same as the value of the ZoneId parameter, and you cannot specify the ID of a multi-zone deployment.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of data nodes in the instance. Valid values:
        # * **1**: creates a [standard instance](https://help.aliyun.com/document_detail/52228.html) that has only one data node. This is the default value.
        # * **2** to **32**: creates a [cluster instance](https://help.aliyun.com/document_detail/52228.html) that has the specified number of data nodes.
        # 
        # > You can set this parameter to a value from **2** to **32** only when the **InstanceType** parameter is set to **tair_rdb** or **tair_scm**. This means that only memory-enhanced and persistent memory-optimized instances support the cluster architecture.
        self.shard_count = shard_count
        # The instance edition. Valid values:
        # - **MASTER_SLAVE**: High-availability Edition. This edition uses a primary/secondary architecture to ensure high availability. This is the default value.
        # - **STAND_ALONE**: Standalone Edition. This edition uses a single-node architecture. If a node fails, data is lost and the system automatically creates a new empty instance. This edition is supported only in **single-zone** deployments and does not support cluster or read/write splitting architectures.
        self.shard_type = shard_type
        # The number of read-only nodes in the secondary zone.
        self.slave_read_only_count = slave_read_only_count
        # The number of secondary nodes in the secondary zone.
        self.slave_replica_count = slave_replica_count
        # Instance ID of the source instance. If you want to create an instance based on the backup set of an existing instance, specify instance ID of the source instance in this parameter.
        # > Then, specify the backup set or point in time by using the **BackupId**, **ClusterBackupId** (recommended for cloud-native cluster architectures), or **RestoreTime** parameter. This parameter must be used in combination with one of the preceding three parameters.
        self.src_dbinstance_id = src_dbinstance_id
        # The storage capacity of the disk-based instance. The valid values vary based on the instance type. For more information, see [Disk-based instance types](https://help.aliyun.com/document_detail/2527111.html).
        # > This parameter is required only when the **InstanceType** parameter is set to **tair_essd** and you create an ESSD-based instance. If you create a Tair disk-based **SSD** instance, the capacity field is defined as a fixed value based on the instance type, and you do not need to specify this field.
        self.storage = storage
        # The storage type. Valid values: **essd_pl1**, **essd_pl2**, and **essd_pl3**.
        # > This parameter is required only when the **InstanceType** parameter is set to **tair_essd** and you create an ESSD-based instance.
        self.storage_type = storage_type
        # The tag information of the instance.
        self.tag = tag
        # The ID of the vSwitch in the VPC. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation of the VPC API to obtain the vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC). You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation of the VPC API to query the VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The primary active zone ID. You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent active zone list. Use this parameter to specify the active zone where you want to create the instance.
        # > You can also specify the SecondaryZoneId parameter to set the secondary active zone. The primary and secondary nodes will be placed in the specified primary and secondary active zones to implement a dual-active-zone primary/secondary architecture deployment. For example, set the ZoneId parameter to "cn-hangzhou-h" and the SecondaryZoneId parameter to "cn-hangzhou-g".
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
        # The tag key. A tag key and a tag value form a key-value pair.
        # > You can specify up to 5 tag key-value pairs at a time.
        self.key = key
        # The tag value.
        # > **N** indicates the sequence number of the tag. For example, **Tag.1.Value** indicates the value of the first tag, and **Tag.2.Value** indicates the value of the second tag.
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


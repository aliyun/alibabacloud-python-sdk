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
        # *   **true**: enables auto-renewal.
        # *   **false** (default): disables auto-renewal.
        self.auto_renew = auto_renew
        # The subscription duration that is supported by auto-renewal. Unit: month. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # >  This parameter is required if the **AutoRenew** parameter is set to **true**.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to use a coupon. Valid values:
        # 
        # *   **true**: uses a coupon.
        # *   **false** (default): does not use a coupon.
        self.auto_use_coupon = auto_use_coupon
        # You can set the BackupId parameter to the backup set ID of the source instance. The system uses the data stored in the backup set to create an instance. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation to query the backup set ID. If the source instance is a cluster instance, set the BackupId parameter to the backup set IDs of all shards of the source instance, separated by commas (,). Example: "10\\*\\*,11\\*\\*,15\\*\\*".
        # 
        # >  If your instance is a cloud-native cluster instance, we recommend that you use [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) to query the backup set ID of the cluster instance, such as cb-xx. Then, set the ClusterBackupId request parameter to the backup set ID to clone the cluster instance. This eliminates the need to specify the backup set ID of each shard.
        self.backup_id = backup_id
        # The ID of the promotional event or the business information.
        self.business_info = business_info
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid** (default): subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests and is case-sensitive. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # This parameter is supported for specific new cluster instances. You can query the backup set ID by calling the [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) operation.
        # 
        # *   If this parameter is supported, you can specify the backup set ID. In this case, you do not need to specify the **BackupId** parameter.
        # *   If this parameter is not supported, set the BackupId parameter to the IDs of backup sets in all shards of the source instance, separated by commas (,). Example: "2158\\*\\*\\*\\*20,2158\\*\\*\\*\\*22".
        self.cluster_backup_id = cluster_backup_id
        # The prefix of the endpoint. The prefix must be 8 to 40 characters in length and can contain lowercase letters and digits. It must start with a lowercase letter.
        # 
        # >  The endpoint must be in the \\<prefix>.redis.rds.aliyuncs.com format.
        self.connection_string_prefix = connection_string_prefix
        # The coupon code.
        self.coupon_no = coupon_no
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs a dry run and does not create the instance. The system prechecks the request parameters, request format, service limits, and available resources. If the request fails the dry run, an error code is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (false): performs a dry run and performs the actual request. If the request passes the dry run, the instance is directly created.
        self.dry_run = dry_run
        # The database engine version. Default value: **1.0**. The parameter value varies based on the Tair instance series.
        # 
        # *   To create a Tair DRAM-based instance (Tair_rdb) that is compatible with Redis 5.0, 6.0, or 7.0, set this parameter to **5.0**, **6.0**, or **7.0**.
        # *   To create a Tair persistent memory-optimized instance (tair_scm) that is compatible with Redis 6.0, set this parameter to **1.0**.
        # *   To create a Tair ESSD-based instance (tair_essd) that is compatible with Redis 6.0, set this parameter to **1.0**. To create a Tair SSD-based instance that is compatible with Redis 6.0, set this parameter to **2.0**.
        self.engine_version = engine_version
        # Specifies whether to use the created instance as a child instance of a distributed instance.
        # 
        # *   If you want the created instance to be used as the first child instance, enter **true**.
        # *   If you want the created instance to be used as the second or third child instance, enter the ID of the distributed instance, such as gr-bp14rkqrhac\\*\\*\\*\\*.
        # *   If you do not want the created instance to be used as a distributed instance, leave the parameter empty.
        # 
        # >  If you want the created instance to be used as a distributed instance, the created instance must be a Tair DRAM-based instance.
        self.global_instance_id = global_instance_id
        # The global IP whitelist templates of the instance. Separate multiple IP whitelist templates with commas (,). Each IP whitelist template must be unique.
        self.global_security_group_ids = global_security_group_ids
        # The instance series. For more information, see the following topics:
        # 
        # *   [DRAM-based instances](https://help.aliyun.com/document_detail/2527112.html)
        # *   [Persistent memory-optimized instances](https://help.aliyun.com/document_detail/2527110.html)
        # *   [ESSD/SSD-based instances](https://help.aliyun.com/document_detail/2527111.html)
        # 
        # This parameter is required.
        self.instance_class = instance_class
        self.instance_endpoint_type = instance_endpoint_type
        # The name of the instance. The name must meet the following requirements:
        # 
        # *   The name must be 2 to 80 characters in length.
        # *   The name must start with a letter and cannot contain spaces or special characters. Special characters include `@ / : = " < > { [ ] }`
        self.instance_name = instance_name
        # The instance series. Valid values:
        # 
        # *   **tair_rdb**: Tair DRAM-based instance
        # *   **tair_scm**: Tair persistent memory-optimized instance
        # *   **tair_essd**: Tair ESSD/SSD-based instance
        # 
        # This parameter is required.
        self.instance_type = instance_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the parameter template. The instance is created based on the parameters in the parameter template. The ID must be unique.
        self.param_group_id = param_group_id
        # The password that is used to connect to the instance. The password must meet the following requirements:
        # 
        # *   The password must be 8 to 32 characters in length.
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `! @ # $ % ^ & * ( ) _ + - =`
        self.password = password
        # The subscription duration. Valid values: **1**, 2, 3, 4, 5, 6, 7, 8, **9**, **12**, **24**,**36**, and **60**. Unit: month.
        # 
        # >  This parameter is required only if the **ChargeType** parameter is set to **PrePaid**.
        self.period = period
        # The service port number of the instance. Valid values: 1024 to 65535. Default value: 6379.
        self.port = port
        # The internal IP address of the instance.
        # 
        # >  The IP address must be within the CIDR block of the vSwitch to which you want the instance to connect. You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation of VPC to query the CIDR block information.
        self.private_ip_address = private_ip_address
        # The number of read replicas in the primary zone. This parameter applies only to cloud-native read/write splitting instances. Valid values: 1 to 9.
        # 
        # >  The sum of the values of this parameter and the SlaveReadOnlyCount parameter cannot exceed 9.
        self.read_only_count = read_only_count
        # Specifies whether to restore the account, kernel parameter, and whitelist information from the original backup set when you create an instance from the specified backup set. For example, if you want to restore the account information, set the parameter to `{"account":true}`.
        # 
        # This parameter is empty by default, which indicates that the account, kernel parameter, and whitelist information is not restored from the original backup set.
        # 
        # >  This parameter applies only to cloud-native cluster instances. The account, kernel parameter, and whitelist information must be stored in the original backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation to check whether the RecoverConfigMode configurations in the specified backup set contain the preceding information.
        self.recover_config_mode = recover_config_mode
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of replica nodes in the primary zone. This parameter applies only to cloud-native multi-replica cluster instances. Valid values: 1 to 4.
        # 
        # > 
        # 
        # *   The sum of the values of this parameter and the SlaveReplicaCount parameter cannot exceed 4.
        # 
        # *   You can specify only one of the ReplicaCount and ReadOnlyCount parameters.
        # 
        # *   Master-replica instances do not support multiple replicas.
        self.replica_count = replica_count
        # The ID of the resource group that you want to manage.
        # 
        # > 
        # 
        # *   You can query resource group IDs in the console or by calling the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation. For more information, see [View the basic information about a resource group](https://help.aliyun.com/document_detail/151181.html).
        # 
        # *   Before you modify the resource group to which an instance belongs, you can call the [ListResources](https://help.aliyun.com/document_detail/158866.html) operation to view the current resource group of the instance.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # If data flashback is enabled for the source instance, you can use this parameter to specify a point in time within the backup retention period of the source instance. The system uses the backup data of the source instance at the point in time to create an instance. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.restore_time = restore_time
        # The ID of the secondary zone. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the ID of the secondary zone.
        # 
        # >  You cannot specify multiple zone IDs or set this parameter to a value that is the same as that of the ZoneId parameter.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of data nodes in the instance. Valid values:
        # 
        # *   **1** (default): You can create a [standard instance](https://help.aliyun.com/document_detail/52228.html) that contains only one data node.
        # *   **2** to **32**: You can create a [cluster instance](https://help.aliyun.com/document_detail/52228.html) that contains the specified number of data nodes.
        # 
        # >  When the **InstanceType** parameter is set to **tair_rdb** or **tair_scm**, this parameter can be set to a value in the range of **2** to **32**. Only DRAM-based and persistent memory-optimized instances support the cluster architecture.
        self.shard_count = shard_count
        # The shard type of the instance. Valid values:
        # 
        # *   **MASTER_SLAVE** (default): runs in a master-replica architecture that provides high availability.
        # *   **STAND_ALONE**: runs in a standalone architecture. If the only node fails, the system creates a new instance and switches the workloads to the new instance. This may cause data loss. You can set the ShardType parameter to this value only if the instance uses the **single-zone** deployment mode. If you set the ShardType parameter to this value, you cannot create cluster or read/write splitting instances.
        self.shard_type = shard_type
        # The number of read replicas in the secondary zone when you create a multi-zone read/write splitting instance. The sum of the values of this parameter and the ReadOnlyCount parameter cannot exceed 9.
        # 
        # > When you create a multi-zone read/write splitting instance, you must specify both SlaveReadOnlyCount and SecondaryZoneId.
        self.slave_read_only_count = slave_read_only_count
        # The number of replica nodes in the secondary zone when you create a cloud-native multi-replica cluster instance deployed across multiple zones. The sum of the values of this parameter and the ReplicaCount parameter cannot exceed 4.
        # 
        # >  When you create a cloud-native multi-replica cluster instance deployed across multiple zones, you must specify both SlaveReplicaCount and SecondaryZoneId.
        self.slave_replica_count = slave_replica_count
        # If you want to create an instance based on the backup set of an existing instance, set this parameter to the ID of the source instance.
        # 
        # >  After you specify the SrcDBInstanceId parameter, use the **BackupId**, **ClusterBackupId** (recommended for cloud-native cluster instances), or **RestoreTime** parameter to specify the backup set or the specific point in time that you want to use to create an instance. The SrcDBInstanceId parameter must be used in combination with one of the preceding three parameters.
        self.src_dbinstance_id = src_dbinstance_id
        # The storage capacity of the ESSD/SSD-based instance. The valid values vary based on the instance type. For more information, see [ESSD/SSD-based instances](https://help.aliyun.com/document_detail/2527111.html).
        # 
        # >  This parameter is required only when you set the **InstanceType** parameter to **tair_essd** to create an ESSD-based instance. If you create a Tair **SSD**-based instance, the Storage parameter is automatically specified based on predefined specifications. You do not need to specify this parameter.
        self.storage = storage
        # The storage type. Valid values: **essd_pl1**, **essd_pl2**, and **essd_pl3**.
        # 
        # >  This parameter is required only when you set the **InstanceType** parameter to **tair_essd** to create an ESSD-based instance.
        # 
        # Enumerated values:
        # 
        # *   essd_pl0
        # *   essd_pl1
        # *   essd_pl2
        # *   essd_pl3
        self.storage_type = storage_type
        # Details of the tags.
        self.tag = tag
        # The ID of the vSwitch that belongs to the VPC. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query vSwitch IDs.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the VPC. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query VPC IDs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the primary zone. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent zone list.
        # 
        # >  You can also set the SecondaryZoneId parameter to specify the secondary zone. The primary and secondary nodes will then be deployed in the specified primary and secondary zones to implement the master-replica zone-disaster recovery architecture. For example, you can set the ZoneId parameter to cn-hangzhou-h and the SecondaryZoneId parameter to cn-hangzhou-g.
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
        # The tag key. A tag is a key-value pair.
        # 
        # >  A maximum of five key-value pairs can be specified at a time.
        self.key = key
        # The value of the tag.
        # 
        # >  **N** specifies the value of the nth tag. For example, **Tag.1.Value** specifies the value of the first tag, and **Tag.2.Value** specifies the value of the second tag.
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


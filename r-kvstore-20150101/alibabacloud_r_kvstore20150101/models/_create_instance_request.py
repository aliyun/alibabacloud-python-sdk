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
        # Specifies whether to enable append-only file (AOF) persistence for the instance. Valid values:
        # 
        # *   **yes** (default): enables AOF persistence.
        # *   **no**: disables AOF persistence.
        # 
        # **
        # 
        # **Description** This parameter is applicable to classic instances, and is unavailable for cloud-native instances.
        self.appendonly = appendonly
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
        # If your instance is a cloud-native cluster instance, we recommend that you use [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) to query the backup set ID of the cluster instance, such as cb-xx. Then, set the ClusterBackupId request parameter to the backup set ID to clone the cluster instance. This eliminates the need to specify the backup set ID of each shard.
        # 
        # You can set the BackupId parameter to the backup set ID of the source instance. The system uses the data stored in the backup set to create an instance. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) operation to query backup set IDs. If the source instance is a cluster instance, set the BackupId parameter to the backup set IDs of all shards of the source instance, separated by commas (,). Example: "10\\*\\*,11\\*\\*,15\\*\\*".
        self.backup_id = backup_id
        # The ID of the promotional event or business information.
        self.business_info = business_info
        # The storage capacity of the instance. Unit: MB.
        # 
        # > You must specify at least one of the **Capacity** and **InstanceClass** parameters when you call this operation.
        self.capacity = capacity
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid** (default): pay-as-you-go
        self.charge_type = charge_type
        # This parameter is supported for specific new cluster instances. You can query the backup set ID by using the [DescribeClusterBackupList](https://help.aliyun.com/document_detail/2679168.html) operation.
        # 
        # *   If this parameter is supported, you can specify the backup set ID. In this case, you do not need to specify the **BackupId** parameter.
        # *   If this parameter is not supported, set the BackupId parameter to the IDs of backup sets for all shards of the source instance, separated by commas (,). Example: "2158\\*\\*\\*\\*20,2158\\*\\*\\*\\*22".
        self.cluster_backup_id = cluster_backup_id
        # The operation that you want to perform. Set the value to **AllocateInstancePublicConnection**.
        self.connection_string_prefix = connection_string_prefix
        # The coupon code. Default value: `default`.
        self.coupon_no = coupon_no
        # The ID of the dedicated cluster. This parameter is required if you create an instance in a dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs a dry run and does not create the instance. The system prechecks the request parameters, request format, service limits, and available resources. If the request fails to pass the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, the instance is created.
        self.dry_run = dry_run
        # The engine version. Valid values for **classic instances**:
        # 
        # *   **2.8** (not recommended due to [scheduled EOFS](https://help.aliyun.com/document_detail/2674657.html))
        # *   **4.0** (not recommended)
        # *   **5.0**
        # 
        # Valid values for **cloud-native instances**:
        # 
        # *   **5.0**
        # *   **6.0** (recommended)
        # *   **7.0**
        # 
        # >  The default value is **5.0**.
        self.engine_version = engine_version
        # Specifies whether to use the new instance as the first child instance of a distributed instance. Valid values:
        # 
        # *   **true**: uses the new instance as the first child instance.
        # *   **false** (default): does not use the new instance as the first child instance.
        # 
        # > 
        # 
        # *   If you want to create a Tair DRAM-based instance that runs Redis 5.0, you must set this parameter to **true**.
        # 
        # *   This parameter is available only on the China site (aliyun.com).
        self.global_instance = global_instance
        # The ID of the distributed instance. This parameter is available only on the China site (aliyun.com).
        self.global_instance_id = global_instance_id
        # The global IP whitelist template for the instance. Multiple IP whitelist templates should be separated by English commas (,) and cannot be duplicated.
        self.global_security_group_ids = global_security_group_ids
        # The instance type. For example, redis.master.small.default indicates a Community Edition standard master-replica instance that has 1 GB of memory. For more information, see [Overview](https://help.aliyun.com/document_detail/26350.html).
        # 
        # **
        # 
        # **Description** You must specify at least one of the **Capacity** and **InstanceClass** parameters when you call the CreateInstance operation.
        self.instance_class = instance_class
        self.instance_endpoint_type = instance_endpoint_type
        # The name of the instance. The name must be 2 to 80 characters in length and must start with a letter. It cannot contain spaces or specific special characters. These special characters include `@ / : = " < > { [ ] }`
        self.instance_name = instance_name
        # The database engine of the instance. Valid values:
        # 
        # *   **Redis** (default)
        # *   **Memcache**
        self.instance_type = instance_type
        # The network type. Valid value:
        # 
        # *   **VPC** (default)
        self.network_type = network_type
        # The node type. Valid values:
        # 
        # *   **MASTER_SLAVE**: high availability (master-replica)
        # *   **STAND_ALONE**: standalone
        # *   **double**: master-replica
        # *   **single**: standalone
        # 
        # >  To create a cloud-native instance, set this parameter to **MASTER_SLAVE** or **STAND_ALONE**. To create a classic instance, set this parameter to **double** or **single**.
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The parameter template ID, which must be globally unique.
        self.param_group_id = param_group_id
        # The password that is used to connect to the instance. The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. These special characters include `! @ # $ % ^ & * ( ) _ + - =`
        self.password = password
        # The subscription duration. Valid values: **1**, 2, 3, 4, 5, 6, 7, 8, **9**, **12**, **24**,**36**, and **60**. Unit: months.
        # 
        # > This parameter is available and required only if the **ChargeType** parameter is set to **PrePaid**.
        self.period = period
        # The port number that is used to connect to the instance. Valid values: **1024** to **65535**. Default value: **6379**.
        self.port = port
        # The private IP address of the instance.
        # 
        # > The private IP address must be available within the CIDR block of the vSwitch to which to connect the instance.
        self.private_ip_address = private_ip_address
        # The number of read replicas in the primary zone. This parameter applies only to read/write splitting instances that use cloud disks. You can use this parameter to customize the number of read replicas. Valid values: 1 to 9.
        # 
        # >  The sum of the values of this parameter and SlaveReadOnlyCount cannot be greater than 9.
        self.read_only_count = read_only_count
        # When creating an instance using a specified backup set, whether to restore account, kernel parameter (whitelist), and whitelist (config) information from the original backup set. For example, if you need to restore account information, the value should be `{"account":true}`.
        # By default, it is empty, indicating that no account, kernel parameter, or whitelist information will be restored from the original backup set. 
        # > This parameter applies only to cloud-native instances and requires that the original backup set has saved the account, kernel parameter, and whitelist information. You can use the [DescribeBackups](https://help.aliyun.com/document_detail/473823.html) API to check if the RecoverConfigMode parameter in the specified backup set contains the above information.
        self.recover_config_mode = recover_config_mode
        # The ID of the region where you want to create the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of slave replicas in the primary availability zone. This parameter is applicable only for creating cloud-native cluster edition multi-replica instances, allowing you to customize the number of slave replicas. The value range is 1 to 4.
        # > > - The sum of this parameter and SlaveReplicaCount cannot exceed 4. 
        # >> - Only one of this parameter and ReadOnlyCount can be passed; there are no instances that simultaneously include both replicas and read-only nodes. 
        # >> - Primary-secondary instances do not support multiple replicas.
        self.replica_count = replica_count
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # If data flashback is enabled for the source instance, you can use this parameter to specify a point in time within the backup retention period of the source instance. The system uses the backup data of the source instance at the point in time to create an instance. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.restore_time = restore_time
        # The secondary zone ID of the instance. You can call the [DescribeZones](https://help.aliyun.com/document_detail/473764.html) operation to query the most recent zone list.
        # 
        # > If you specify this parameter, the master node and replica node of the instance can be deployed in different zones and disaster recovery is implemented across zones. The instance can withstand failures in data centers.
        self.secondary_zone_id = secondary_zone_id
        self.security_token = security_token
        # The number of shards. This parameter applies only to cloud-native cluster instances.
        self.shard_count = shard_count
        # The number of read replicas in the secondary zone. This parameter is used to create a read/write splitting instance that is deployed across multiple zones. The sum of the values of this parameter and ReadOnlyCount cannot be greater than 9.
        # 
        # > When you create a multi-zone read/write splitting instance, you must specify both SlaveReadOnlyCount and SecondaryZoneId.
        self.slave_read_only_count = slave_read_only_count
        # Used for specifying the number of slave replicas in the secondary availability zone when creating a multi-AZ cloud-native cluster edition with multiple replicas. The sum of this parameter and ReplicaCount cannot exceed 4. <notice>When creating a multi-AZ cloud-native cluster edition with multiple replicas, both SlaveReplicaCount and SecondaryZoneId parameters must be specified.</notice>
        self.slave_replica_count = slave_replica_count
        # If you want to create an instance based on the backup set of an existing instance, set this parameter to the ID of the source instance.
        # 
        # >  After you specify the SrcDBInstanceId parameter, use the **BackupId**, **ClusterBackupId** (recommended for cloud-native cluster instances), or **RestoreTime** parameter to specify the backup set or the specific point in time that you want to use to create an instance. The SrcDBInstanceId parameter must be used in combination with one of the preceding three parameters.
        self.src_dbinstance_id = src_dbinstance_id
        # The tags of the instance.
        self.tag = tag
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the token is unique among different requests. The token is case-sensitive. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.token = token
        # The ID of the vSwitch to which you want the instance to connect.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The primary zone ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the most recent zone list.
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
        # The keys of the tags that are added to the instance.
        # 
        # > *   **N** specifies the serial number of the tag. Up to 20 tags can be added to a single instance. For example, Tag.1.Key specifies the key of the first tag and Tag.2.Key specifies the key of the second tag.
        # > *   If the key of the tag does not exist, the tag is automatically created.
        self.key = key
        # The values of the tags that are added to the instance.
        # 
        # > **N** specifies the serial number of the tag. For example, **Tag.1.Value** specifies the value of the first tag and **Tag.2.Value** specifies the value of the second tag.
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


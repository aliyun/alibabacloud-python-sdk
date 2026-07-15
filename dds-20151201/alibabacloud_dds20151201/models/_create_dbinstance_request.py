# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class CreateDBInstanceRequest(DaraModel):
    def __init__(
        self,
        account_password: str = None,
        auto_renew: str = None,
        backup_id: str = None,
        business_info: str = None,
        charge_type: str = None,
        client_token: str = None,
        cluster_id: str = None,
        coupon_no: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_storage: int = None,
        database_names: str = None,
        encrypted: bool = None,
        encryption_key: str = None,
        engine: str = None,
        engine_version: str = None,
        global_security_group_ids: str = None,
        hidden_zone_id: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        provisioned_iops: int = None,
        readonly_replicas: str = None,
        region_id: str = None,
        replication_factor: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        restore_type: str = None,
        secondary_zone_id: str = None,
        security_iplist: str = None,
        src_dbinstance_id: str = None,
        src_region: str = None,
        storage_engine: str = None,
        storage_type: str = None,
        tag: List[main_models.CreateDBInstanceRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The password for the root account. The password must meet the following requirements:
        # 
        # - It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # - The special characters are !@#$%^&\\*()_+-=
        # 
        # - It must be 8 to 32 characters long.
        # 
        # > For more information about connection failures caused by special characters in passwords, see [How do I fix a connection failure that is caused by special characters in a password?]().
        self.account_password = account_password
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # - **true**: Enables auto-renewal.
        # 
        # - **false**: The default value. Disables auto-renewal. You must manually renew the instance.
        # 
        # > This parameter is optional and takes effect only when you set the **ChargeType** parameter to **PrePaid**.
        self.auto_renew = auto_renew
        # The backup point ID. To query the backup point ID, call the [DescribeBackups]() operation.
        # 
        # > You must specify this parameter and the **SrcDBInstanceId** parameter only when you clone an instance based on a backup point.
        self.backup_id = backup_id
        # The business information. This is an optional parameter.
        self.business_info = business_info
        # The billing method of the instance. Valid values:
        # 
        # - **PostPaid**: The default value. Pay-as-you-go.
        # 
        # - **PrePaid**: Subscription.
        # 
        # > If you set this parameter to **PrePaid**, you must also specify the **Period** parameter.
        self.charge_type = charge_type
        # A client token that is used to ensure the idempotence of the request. You can use the client to generate the token. Make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot be more than 64 characters long.
        self.client_token = client_token
        self.cluster_id = cluster_id
        # Specifies whether to use a coupon. Valid values:
        # 
        # - **default** or **null** (default): Uses a coupon.
        # 
        # - **youhuiquan_promotion_option_id_for_blank**: Does not use a coupon.
        self.coupon_no = coupon_no
        # The instance type. To query instance types, call the [DescribeAvailableResource]() operation.
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # The instance name. The name must meet the following requirements:
        # 
        # - It must start with a letter or a Chinese character.
        # 
        # - It can contain letters, Chinese characters, digits, underscores (_), periods (.), and hyphens (-).
        # 
        # - It must be 2 to 256 characters long.
        self.dbinstance_description = dbinstance_description
        # The storage space of the instance in GB.
        # 
        # The value of this parameter varies based on the instance type. For more information, see [Replica set instance types]().
        # 
        # This parameter is required.
        self.dbinstance_storage = dbinstance_storage
        # The database name.
        # 
        # > When you clone an instance, you can specify this parameter to clone specific databases. If you do not specify this parameter, all databases of the instance are cloned.
        self.database_names = database_names
        # Specifies whether to enable disk encryption.
        self.encrypted = encrypted
        # The custom key ID.
        self.encryption_key = encryption_key
        # The database engine. The value is fixed as **MongoDB**.
        self.engine = engine
        # The database engine version. Valid values:
        # 
        # - **8.0**
        # 
        # - **7.0**
        # 
        # - **6.0**
        # 
        # - **5.0**
        # 
        # - **4.4**
        # 
        # - **4.2**
        # 
        # - **4.0**
        # 
        # > When you clone an instance or restore an instance from the recycle bin, this parameter must be the same as the engine version of the source instance.
        # 
        # >Warning: 
        # 
        # Versions 3.4 and earlier are discontinued.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The global IP address whitelist templates for the instance. Separate multiple templates with commas (,). The templates cannot be repeated. This feature is in canary release.
        self.global_security_group_ids = global_security_group_ids
        # The zone where the hidden node is deployed. This parameter is used for multi-zone deployment. Valid values:
        # 
        # - **cn-hangzhou-g**: Zone G in Hangzhou.
        # 
        # - **cn-hangzhou-h**: Zone H in Hangzhou.
        # 
        # - **cn-hangzhou-i**: Zone I in Hangzhou.
        # 
        # - **cn-hongkong-b**: Zone B in Hong Kong (China).
        # 
        # - **cn-hongkong-c**: Zone C in Hong Kong (China).
        # 
        # - **cn-hongkong-d**: Zone D in Hong Kong (China).
        # 
        # - **cn-wulanchabu-a**: Zone A in Ulanqab.
        # 
        # - **cn-wulanchabu-b**: Zone B in Ulanqab.
        # 
        # - **cn-wulanchabu-c**: Zone C in Ulanqab.
        # 
        # - **ap-southeast-1a**: Zone A in Singapore.
        # 
        # - **ap-southeast-1b**: Zone B in Singapore.
        # 
        # - **ap-southeast-1c**: Zone C in Singapore.
        # 
        # - **ap-southeast-5a**: Zone A in Jakarta.
        # 
        # - **ap-southeast-5b**: Zone B in Jakarta.
        # 
        # - **ap-southeast-5c**: Zone C in Jakarta.
        # 
        # - **eu-central-1a**: Zone A in Frankfurt.
        # 
        # - **eu-central-1b**: Zone B in Frankfurt.
        # 
        # - **eu-central-1c**: Zone C in Frankfurt.
        # 
        # > * This parameter is available when the instance uses disks.
        # >
        # > * The value of this parameter cannot be the same as the value of the **ZoneId** or **SecondaryZoneId** parameter.
        self.hidden_zone_id = hidden_zone_id
        # The network type of the instance. Valid values:
        # 
        # **VPC**: virtual private cloud (VPC).
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration of the instance in months.
        # 
        # Valid values: **1** to **9** (integers), **12**, **24**, **36**, and **60**.
        # 
        # > This parameter is required and takes effect only when you set the **ChargeType** parameter to **PrePaid**.
        self.period = period
        # The provisioned IOPS (input/output operations per second). Valid values: 0 to 50000.
        self.provisioned_iops = provisioned_iops
        # The number of **read-only nodes** in the replica set instance. Valid values are integers from **0** to **5**. The default value is **0**.
        self.readonly_replicas = readonly_replicas
        # The region ID. To query the region ID, call the [DescribeRegions]() operation.
        # 
        # > When you clone an instance or restore an instance from the recycle bin, this parameter must be the same as the region ID of the source instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of **primary and secondary nodes** in the replica set instance. Valid values:
        # 
        # - **3** (default)
        # 
        # - **5**
        # 
        # - **7**
        # 
        # >Notice: 
        # 
        # You do not need to specify this parameter for standalone instances.
        self.replication_factor = replication_factor
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore the instance. You can specify any point in time within the last seven days. The time must be in the *yyyy-MM-dd*T*HH:mm:ss*Z format and in UTC.
        # 
        # > You must specify this parameter and the **SrcDBInstanceId** parameter only when you clone an instance based on a point in time.
        self.restore_time = restore_time
        # The method to restore an instance from a backup.
        # 
        # - 0: Restores the instance to a specified backup set.
        # 
        # - 1: Restores the instance to a specified point in time.
        # 
        # - 2: Restores a released instance to a specified backup set.
        # 
        # - 3: Restores the instance to a specified geo-redundant backup set.
        self.restore_type = restore_type
        # The zone where the secondary node is deployed. This parameter is used for multi-zone deployment. Valid values:
        # 
        # - **cn-hangzhou-g**: Zone G in Hangzhou.
        # 
        # - **cn-hangzhou-h**: Zone H in Hangzhou.
        # 
        # - **cn-hangzhou-i**: Zone I in Hangzhou.
        # 
        # - **cn-hongkong-b**: Zone B in Hong Kong (China).
        # 
        # - **cn-hongkong-c**: Zone C in Hong Kong (China).
        # 
        # - **cn-hongkong-d**: Zone D in Hong Kong (China).
        # 
        # - **cn-wulanchabu-a**: Zone A in Ulanqab.
        # 
        # - **cn-wulanchabu-b**: Zone B in Ulanqab.
        # 
        # - **cn-wulanchabu-c**: Zone C in Ulanqab.
        # 
        # - **ap-southeast-1a**: Zone A in Singapore.
        # 
        # - **ap-southeast-1b**: Zone B in Singapore.
        # 
        # - **ap-southeast-1c**: Zone C in Singapore.
        # 
        # - **ap-southeast-5a**: Zone A in Jakarta.
        # 
        # - **ap-southeast-5b**: Zone B in Jakarta.
        # 
        # - **ap-southeast-5c**: Zone C in Jakarta.
        # 
        # - **eu-central-1a**: Zone A in Frankfurt.
        # 
        # - **eu-central-1b**: Zone B in Frankfurt.
        # 
        # - **eu-central-1c**: Zone C in Frankfurt.
        # 
        # > * This parameter is available when the instance uses disks.
        # >
        # > * The value of this parameter cannot be the same as the value of the **ZoneId** or **HiddenZoneId** parameter.
        self.secondary_zone_id = secondary_zone_id
        # The IP address whitelist of the instance. Separate multiple IP addresses with commas (,). Each IP address in the whitelist must be unique. The whitelist can be in one of the following formats:
        # 
        # - 0.0.0.0/0
        # 
        # - An IP address, for example, 10.23.12.24.
        # 
        # - A CIDR block, for example, 10.23.12.0/24. The /24 indicates that the prefix of the CIDR block is 24 bits in length. You can set the prefix to a value from 1 to 32.
        # 
        # > * You can add a maximum of 1,000 IP addresses or CIDR blocks to all IP address whitelists.
        # >
        # > * If you set the whitelist to 0.0.0.0/0, all IP addresses can access the instance. This is a high-risk setting. Use this with caution.
        self.security_iplist = security_iplist
        # The source instance ID.
        # 
        # > When you clone an instance, you must specify this parameter and the **BackupId** or **RestoreTime** parameter. When you restore an instance from the recycle bin, you only need to specify this parameter. You do not need to specify the **BackupId** or **RestoreTime** parameter.
        self.src_dbinstance_id = src_dbinstance_id
        # The region where the source instance is located.
        # 
        # > - This parameter is required when RestoreType is set to 2 or 3.
        self.src_region = src_region
        # The storage engine of the instance. The value is fixed as **WiredTiger**.
        # 
        # > - When you clone an instance or restore an instance from the recycle bin, this parameter must be the same as the storage engine of the source instance.
        # >
        # > - For more information about the constraints on storage engines and database versions, see [Versions and storage engines]().
        self.storage_engine = storage_engine
        # The storage class. Valid values:
        # 
        # - **cloud_essd1**: ESSD PL1 disk.
        # 
        # - **cloud_essd2**: ESSD PL2 disk.
        # 
        # - **cloud_essd3**: ESSD PL3 disk.
        # 
        # - **cloud_auto**: ESSD AutoPL disk.
        # 
        # - **local_ssd**: Local SSD.
        # 
        # > * For standalone instances, if you pass the value cloud_essd1, an ESSD disk is used.
        # >
        # > * ESSD AutoPL disks are available only on the China site (aliyun.com).
        # >
        # > * For instances of version 4.4 or later, the default value is **cloud_essd1**.
        # >
        # > * For instances of version 4.2 or earlier, the default value is **local_ssd**.
        self.storage_type = storage_type
        # The custom tags.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID. To query the zone ID, call the [DescribeRegions]() operation.
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
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.global_security_group_ids is not None:
            result['GlobalSecurityGroupIds'] = self.global_security_group_ids

        if self.hidden_zone_id is not None:
            result['HiddenZoneId'] = self.hidden_zone_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.src_dbinstance_id is not None:
            result['SrcDBInstanceId'] = self.src_dbinstance_id

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.storage_engine is not None:
            result['StorageEngine'] = self.storage_engine

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
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('GlobalSecurityGroupIds') is not None:
            self.global_security_group_ids = m.get('GlobalSecurityGroupIds')

        if m.get('HiddenZoneId') is not None:
            self.hidden_zone_id = m.get('HiddenZoneId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SrcDBInstanceId') is not None:
            self.src_dbinstance_id = m.get('SrcDBInstanceId')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('StorageEngine') is not None:
            self.storage_engine = m.get('StorageEngine')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self



class CreateDBInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # > - **N** specifies the Nth tag. For example, **Tag.1.Key** specifies the key of the first tag, and **Tag.2.Key** specifies the key of the second tag.
        self.key = key
        # The tag value.
        # 
        # > **N** specifies the Nth tag. For example, **Tag.1.Value** specifies the value of the first tag, and **Tag.2.Value** specifies the value of the second tag.
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


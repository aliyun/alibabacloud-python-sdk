# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class CreateShardingDBInstanceRequest(DaraModel):
    def __init__(
        self,
        account_password: str = None,
        auto_renew: str = None,
        backup_id: str = None,
        charge_type: str = None,
        client_token: str = None,
        config_server: List[main_models.CreateShardingDBInstanceRequestConfigServer] = None,
        dbinstance_description: str = None,
        dest_region: str = None,
        encrypted: bool = None,
        encryption_key: str = None,
        engine: str = None,
        engine_version: str = None,
        global_security_group_ids: str = None,
        hidden_zone_id: str = None,
        mongos: List[main_models.CreateShardingDBInstanceRequestMongos] = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        protocol_type: str = None,
        provisioned_iops: int = None,
        region_id: str = None,
        replica_set: List[main_models.CreateShardingDBInstanceRequestReplicaSet] = None,
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
        tag: List[main_models.CreateShardingDBInstanceRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The password of the root account. The password must meet the following requirements:
        # 
        # *   The password contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   The following special characters are supported: ! @ # $ % ^ & \\* ( ) _ + - =.
        # *   The password must be 8 to 32 characters in length.
        # 
        # >  For more information about how to resolve failed database connections due to special characters, see [What do I do if my instance is not connected due to special characters in the password in the connection string of the instance?](https://help.aliyun.com/document_detail/471568.html)
        self.account_password = account_password
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > This parameter is available and optional if you set the value of **ChargeType** to **PrePaid**.
        self.auto_renew = auto_renew
        # The ID of the backup set. 
        # 
        # > When you call this operation to clone an instance based on the backup set, this parameter is required. The **SrcDBInstanceId** parameter is also required.
        self.backup_id = backup_id
        # The billing method of the instance. Valid values:
        # 
        # *   **PostPaid** (default): pay-as-you-go
        # *   **PrePaid**: subscription
        # 
        # >  If you set this parameter to **PrePaid**, you must also configure the **Period** parameter.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ConfigServer nodes of the instance.
        # 
        # This parameter is required.
        self.config_server = config_server
        # The name of the instance. The name of the instance must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   It can contain digits, letters, underscores (_), and hyphens (-).
        # *   It must be 2 to 256 characters in length.
        self.dbinstance_description = dbinstance_description
        # The region of the backup set used for the cross-region backup and restoration.
        # 
        # >  This parameter is required when you set the RestoreType parameter to 3.
        self.dest_region = dest_region
        # Specifies whether to enable disk encryption.
        self.encrypted = encrypted
        # The ID of the custom key.
        self.encryption_key = encryption_key
        # The database engine of the instance. Set the value to **MongoDB**.
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version of the instance. Valid values:
        # 
        # *   **7.0**
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # 
        # > 
        # 
        # *   For more information about the limits on database versions and storage engines, see [MongoDB versions and storage engines](https://help.aliyun.com/document_detail/61906.html).
        # 
        # *   If you call this operation to clone an instance, set the value of this parameter to the database engine version of the source instance.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The global IP address whitelist template of the instance. Separate multiple templates with commas (,). The template name must be globally unique.
        self.global_security_group_ids = global_security_group_ids
        # The ID of secondary zone 2 for multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hong Kong Zone B
        # *   **cn-hongkong-c**: Hong Kong Zone C
        # *   **cn-hongkong-d**: Hong Kong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > *   This parameter is available and required if you set the value of **EngineVersion** to **4.4** or **5.0**.
        # > *   The value of this parameter cannot be the same as the value of **ZoneId** or **SecondaryZoneId**.
        # > *   For more information about the multi-zone deployment policy of a sharded cluster instance, see [Create a multi-zone sharded cluster instance](https://help.aliyun.com/document_detail/117865.html).
        self.hidden_zone_id = hidden_zone_id
        # The mongos nodes of the instance.
        # 
        # This parameter is required.
        self.mongos = mongos
        # The network type of the instance. Set the value to VPC.
        # 
        # ****
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription period of the instance. Unit: months.
        # 
        # Valid values: **1** to **9**, **12**, **24**, **36**, and **60**.
        # 
        # > When you set the **ChargeType** parameter to **PrePaid**, this parameter is valid and required.
        self.period = period
        # The access protocol type of the instance. Valid values:
        # 
        # *   **mongodb**
        # *   **dynamodb**
        self.protocol_type = protocol_type
        # The provisioned IOPS of the instance:
        self.provisioned_iops = provisioned_iops
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The information of the shard component.
        # 
        # This parameter is required.
        self.replica_set = replica_set
        # The resource group ID. For more information, see [View the basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to restore the instance, which must be within seven days. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in Coordinated Universal Time (UTC).
        # 
        # > This parameter is required only if you call this operation to clone an instance. If you specify this parameter, you must also specify **SrcDBInstanceId**.
        self.restore_time = restore_time
        # The restoration type of the instance. Valid values:
        # 
        # *   1: restores the instance data to the specified point in time.
        # *   2: restores the data of the released instance to the specified backup set.
        # *   3: restores the instance data to the specified cross-region backup set.
        self.restore_type = restore_type
        # The ID of secondary zone 1 for multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G
        # *   **cn-hangzhou-h**: Hangzhou Zone H
        # *   **cn-hangzhou-i**: Hangzhou Zone I
        # *   **cn-hongkong-b**: Hong Kong Zone B
        # *   **cn-hongkong-c**: Hong Kong Zone C
        # *   **cn-hongkong-d**: Hong Kong Zone D
        # *   **cn-wulanchabu-a**: Ulanqab Zone A
        # *   **cn-wulanchabu-b**: Ulanqab Zone B
        # *   **cn-wulanchabu-c**: Ulanqab Zone C
        # *   **ap-southeast-1a**: Singapore Zone A
        # *   **ap-southeast-1b**: Singapore Zone B
        # *   **ap-southeast-1c**: Singapore Zone C
        # *   **ap-southeast-5a**: Jakarta Zone A
        # *   **ap-southeast-5b**: Jakarta Zone B
        # *   **ap-southeast-5c**: Jakarta Zone C
        # *   **eu-central-1a**: Frankfurt Zone A
        # *   **eu-central-1b**: Frankfurt Zone B
        # *   **eu-central-1c**: Frankfurt Zone C
        # 
        # > *   This parameter is available and required if you set the value of **EngineVersion** to **4.4** or **5.0**.
        # > *   The value of this parameter cannot be the same as the value of **ZoneId** or **HiddenZoneId**.
        # > *   For more information about the multi-zone deployment policy of a sharded cluster instance, see [Create a multi-zone sharded cluster instance](https://help.aliyun.com/document_detail/117865.html).
        self.secondary_zone_id = secondary_zone_id
        # The IP addresses in an IP address whitelist of the instance. Multiple IP addresses are separated by commas (,), and each IP address in the IP address whitelist must be unique. The following types of values are supported:
        # 
        # *   0.0.0.0/0
        # *   IP addresses, such as 10.23.12.24.
        # *   CIDR blocks, such as 10.23.12.0/24. In this case, 24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32.
        # 
        # > *   A maximum of 1,000 IP addresses and CIDR blocks can be configured for each instance.
        # > *   If you enter 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. Proceed with caution.
        self.security_iplist = security_iplist
        # The source instance ID.
        # 
        # > This parameter is required only if you call this operation to clone an instance. If you specify this parameter, you must also specify **RestoreTime**.
        self.src_dbinstance_id = src_dbinstance_id
        # The region ID of the instance.
        # 
        # > This parameter is required when restore type is set to 2 or 3.
        self.src_region = src_region
        # The storage engine of the instance. Set the value to **WiredTiger**.
        # 
        # > 
        # 
        # *   If you call this operation to clone an instance, set the value of this parameter to the storage engine of the source instance.
        # 
        # *   For more information about the limits on database versions and storage engines, see [MongoDB versions and storage engines](https://help.aliyun.com/document_detail/61906.html).
        self.storage_engine = storage_engine
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd1**: ESSD PL1
        # *   **cloud_essd2**: ESSD PL2
        # *   **cloud_essd3**: ESSD PL3
        # *   **local_ssd**: local SSD
        # 
        # > *   Instances of MongoDB 4.4 and later support only cloud disks. **cloud_essd1** is selected if you leave this parameter empty.
        # > *   Instances of MongoDB 4.2 and earlier support only local disks. **local_ssd** is selected if you leave this parameter empty.
        self.storage_type = storage_type
        # The custom tags that you want to add to the instance.
        self.tag = tag
        # The vSwitch ID of the instance.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The zone ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.config_server:
            for v1 in self.config_server:
                 if v1:
                    v1.validate()
        if self.mongos:
            for v1 in self.mongos:
                 if v1:
                    v1.validate()
        if self.replica_set:
            for v1 in self.replica_set:
                 if v1:
                    v1.validate()
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

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['ConfigServer'] = []
        if self.config_server is not None:
            for k1 in self.config_server:
                result['ConfigServer'].append(k1.to_map() if k1 else None)

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

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

        result['Mongos'] = []
        if self.mongos is not None:
            for k1 in self.mongos:
                result['Mongos'].append(k1.to_map() if k1 else None)

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ReplicaSet'] = []
        if self.replica_set is not None:
            for k1 in self.replica_set:
                result['ReplicaSet'].append(k1.to_map() if k1 else None)

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

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.config_server = []
        if m.get('ConfigServer') is not None:
            for k1 in m.get('ConfigServer'):
                temp_model = main_models.CreateShardingDBInstanceRequestConfigServer()
                self.config_server.append(temp_model.from_map(k1))

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

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

        self.mongos = []
        if m.get('Mongos') is not None:
            for k1 in m.get('Mongos'):
                temp_model = main_models.CreateShardingDBInstanceRequestMongos()
                self.mongos.append(temp_model.from_map(k1))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.replica_set = []
        if m.get('ReplicaSet') is not None:
            for k1 in m.get('ReplicaSet'):
                temp_model = main_models.CreateShardingDBInstanceRequestReplicaSet()
                self.replica_set.append(temp_model.from_map(k1))

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
                temp_model = main_models.CreateShardingDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateShardingDBInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # >  **N** specifies the serial number of the tag. For example, **Tag.1.Key** specifies the key of the first tag and **Tag.2.Key** specifies the key of the second tag.
        self.key = key
        # The tag value.
        # 
        # >  **N** specifies the serial number of the tag. For example, **Tag.1.Value** specifies the value of the first tag and Tag.2.Value specifies the value of the second tag.
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

class CreateShardingDBInstanceRequestReplicaSet(DaraModel):
    def __init__(
        self,
        class_: str = None,
        readonly_replicas: int = None,
        storage: int = None,
    ):
        # The instance type of the shard component. For more information, see [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html).
        # 
        # > 
        # 
        # *   **N** specifies the serial number of the shard component for which the instance type is specified. For example, **ReplicaSet.2.Class** specifies the instance type of the second shard component.
        # 
        # *   Valid values of **N**: **2** to **32**.
        # 
        # This parameter is required.
        self.class_ = class_
        # The number of read-only nodes in the shard component.
        # 
        # Valid values: **0**, **1, 2, 3, 4, and 5**. Default value: **0**.
        # 
        # >  **N** specifies the serial number of the shard component for which you want to set the number of read-only nodes. **ReplicaSet.2.ReadonlyReplicas** specifies the number of read-only nodes in the second shard component.
        self.readonly_replicas = readonly_replicas
        # The storage capacity of the shard component. Unit: GB.
        # 
        # > 
        # 
        # *   The values that can be specified for this parameter vary based on the instance types. For more information, see [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html).
        # 
        # *   **N** specifies the serial number of the shard component for which the storage capacity is specified. For example, **ReplicaSet.2.Storage** specifies the storage capacity of the second shard component.
        # 
        # This parameter is required.
        self.storage = storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['Class'] = self.class_

        if self.readonly_replicas is not None:
            result['ReadonlyReplicas'] = self.readonly_replicas

        if self.storage is not None:
            result['Storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('ReadonlyReplicas') is not None:
            self.readonly_replicas = m.get('ReadonlyReplicas')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        return self

class CreateShardingDBInstanceRequestMongos(DaraModel):
    def __init__(
        self,
        class_: str = None,
    ):
        # The instance type of the mongos node. For more information, see [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html).
        # 
        # > *   **N** specifies the serial number of the mongos node for which the instance type is specified. For example, **Mongos.2.Class** specifies the instance type of the second mongos node.
        # > *   Valid values for **N**: **2** to **32**.
        # 
        # This parameter is required.
        self.class_ = class_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['Class'] = self.class_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        return self

class CreateShardingDBInstanceRequestConfigServer(DaraModel):
    def __init__(
        self,
        class_: str = None,
        storage: int = None,
    ):
        # The instance type of the ConfigServer node. Valid values:
        # 
        # *   **mdb.shard.2x.xlarge.d**: 4 cores, 8 GB (dedicated). Only instances that run MongoDB 4.4 and later support this instance type.
        # *   **dds.cs.mid** :1 core, 2 GB (general-purpose). Only instances that run MongoDB 4.2 and earlier support this instance type.
        # 
        # This parameter is required.
        self.class_ = class_
        # The storage space of the ConfigServer node. Unit: GB.
        # 
        # > The values that can be specified for this parameter vary based on the instance types. For more information, see [Sharded cluster instance types](https://help.aliyun.com/document_detail/311414.html).
        # 
        # This parameter is required.
        self.storage = storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['Class'] = self.class_

        if self.storage is not None:
            result['Storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        return self


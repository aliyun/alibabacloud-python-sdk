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
        # The password of the root account. The password must meet the following requirements:
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   Special characters include ! # $ % ^ & \\* ( ) _ + - =
        # *   The password of the account must be 8 to 32 characters in length.
        self.account_password = account_password
        # Specifies whether to enable auto-renewal for the instance. Default value: false. Valid values:
        # 
        # *   **true**: The instance is automatically renewed.
        # *   **false**: The instance is manually renewed.
        # 
        # > This parameter is valid and optional when the **ChargeType** parameter is set to **PrePaid**.
        self.auto_renew = auto_renew
        # The ID of the backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/62172.html) operation to query the backup set ID.
        # 
        # > When you call this operation to clone an instance based on the backup set, this parameter is required. The **SrcDBInstanceId** parameter is also required.
        self.backup_id = backup_id
        # The business information. This is an additional parameter.
        self.business_info = business_info
        # The billing method of the instance. Valid values:
        # 
        # *   **PostPaid**: pay-as-you-go. This is the default value.
        # *   **PrePaid**: subscription.
        # 
        # > If you set this parameter to **PrePaid**, you must also specify the **Period** parameter.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the dedicated cluster to which the instance belongs.
        self.cluster_id = cluster_id
        # Specifies whether to use coupons. Default value: null. Valid values:
        # - **default** or **null**: uses coupons.
        # - **youhuiquan_promotion_option_id_for_blank**: does not use coupons.
        self.coupon_no = coupon_no
        # The instance type. You can also call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/149719.html) operation to query the instance type.
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # The name of the instance. The name of the instance must meet the following requirements:
        # 
        # *   The name must start with a letter.
        # *   The name can contain digits, letters, underscores (_), and hyphens (-).
        # *   The name must be 2 to 256 characters in length.
        self.dbinstance_description = dbinstance_description
        # The storage capacity of the instance. Unit: GB.
        # 
        # The values that can be specified for this parameter vary based on the instance types. For more information, see [Replica set instance types](https://help.aliyun.com/document_detail/311410.html).
        # 
        # This parameter is required.
        self.dbinstance_storage = dbinstance_storage
        # The name of the database.
        # 
        # > When you call this operation to clone an instance, you can set this parameter to specify the database to clone. Otherwise, all databases of the instance are cloned.
        self.database_names = database_names
        # Specifies whether to enable disk encryption.
        self.encrypted = encrypted
        # The ID of the custom key.
        self.encryption_key = encryption_key
        # The database engine of the instance. Set the value to **MongoDB**.
        self.engine = engine
        # The version of the database engine. Valid values:
        # 
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # 
        # > When you call this operation to clone an instance or restore an instance from the recycle bin, set the value of this parameter to the engine version of the source instance.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The global IP address whitelist template name of the instance. Multiple IP address whitelist template names are separated by commas (,) and each template name must be unique. (The template feature is available only in canary release.)
        self.global_security_group_ids = global_security_group_ids
        # The zone where the hidden node resides for multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G.
        # *   **cn-hangzhou-h**: Hangzhou Zone H.
        # *   **cn-hangzhou-i**: Hangzhou Zone I.
        # *   **cn-hongkong-b**: Hongkong Zone B.
        # *   **cn-hongkong-c**: Hongkong Zone C.
        # *   **cn-hongkong-d**: Hongkong Zone D.
        # *   **cn-wulanchabu-a**: Ulanqab Zone A.
        # *   **cn-wulanchabu-b**: Ulanqab Zone B.
        # *   **cn-wulanchabu-c**: Ulanqab Zone C.
        # *   **ap-southeast-1a**: Singapore Zone A.
        # *   **ap-southeast-1b**: Singapore Zone B.
        # *   **ap-southeast-1c**: Singapore Zone C.
        # *   **ap-southeast-5a**: Jakarta Zone A.
        # *   **ap-southeast-5b**: Jakarta Zone B.
        # *   **ap-southeast-5c**: Jakarta Zone C.
        # *   **eu-central-1a**: Frankfurt Zone A.
        # *   **eu-central-1b**: Frankfurt Zone B.
        # *   **eu-central-1c**: Frankfurt Zone C.
        # 
        # >  *   This parameter is valid and required when the **EngineVersion** parameter is set to **4.4** or **5.0**.
        # >  *   The value of this parameter cannot be the same as the value of the **ZoneId** or **SecondaryZoneId** parameter.
        self.hidden_zone_id = hidden_zone_id
        # The network type of the instance. Valid value:
        # 
        # **VPC**: Virtual Private Cloud (VPC)
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription period of the instance. Unit: months.
        # 
        # Valid values: **1** to **9**, **12**, **24**, **36**, and **60**.
        # 
        # > When you set the **ChargeType** parameter to **PrePaid**, this parameter is valid and required.
        self.period = period
        # The provisioned IOPS. Valid values: 0 to 50000.
        self.provisioned_iops = provisioned_iops
        # The number of **read-only nodes** in the replica set instance. Default value: **0**. Valid values: **0** to **5**.
        self.readonly_replicas = readonly_replicas
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of **nodes** in the replica set instance. Default value: 3. Valid values:
        # 
        # *   **3**
        # *   **5**
        # *   **7**
        self.replication_factor = replication_factor
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The point in time to which the instance is restored, which must be within seven days. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format (UTC time).
        # 
        # > When you call this operation to restore an instance to the specified time, this parameter is required. The **SrcDBInstanceId** parameter is also required.
        self.restore_time = restore_time
        # The backup restore type of the instance.
        # - 0: restore an instance to the specified backup set.
        # - 1:  restore an instance to the specified time.
        # - 2: restore an  released instance to the specified backup set.
        # - 3：restore an instance to the specified cross-regional backup set.
        self.restore_type = restore_type
        # The zone where the secondary node resides for multi-zone deployment. Valid values:
        # 
        # *   **cn-hangzhou-g**: Hangzhou Zone G.
        # *   **cn-hangzhou-h**: Hangzhou Zone H.
        # *   **cn-hangzhou-i**: Hangzhou Zone I.
        # *   **cn-hongkong-b**: Hongkong Zone B.
        # *   **cn-hongkong-c**: Hongkong Zone C.
        # *   **cn-hongkong-d**: Hongkong Zone D.
        # *   **cn-wulanchabu-a**: Ulanqab Zone A.
        # *   **cn-wulanchabu-b**: Ulanqab Zone B.
        # *   **cn-wulanchabu-c**: Ulanqab Zone C.
        # *   **ap-southeast-1a**: Singapore Zone A.
        # *   **ap-southeast-1b**: Singapore Zone B.
        # *   **ap-southeast-1c**: Singapore Zone C.
        # *   **ap-southeast-5a**: Jakarta Zone A.
        # *   **ap-southeast-5b**: Jakarta Zone B.
        # *   **ap-southeast-5c**: Jakarta Zone C.
        # *   **eu-central-1a**: Frankfurt Zone A.
        # *   **eu-central-1b**: Frankfurt Zone B.
        # *   **eu-central-1c**: Frankfurt Zone C.
        # 
        # >  *   This parameter is valid and required when the **EngineVersion** parameter is set to **4.4** or **5.0**.
        # >  *   The value of this parameter cannot be the same as the value of the **ZoneId** or **HiddenZoneId** parameter.
        self.secondary_zone_id = secondary_zone_id
        # The IP addresses in an IP address whitelist. Multiple IP addresses are separated by commas (,), and each IP address in the IP address whitelist must be unique. The following types of values are supported:
        # 
        # *   0.0.0.0/0
        # *   IP addresses, such as 10.23.12.24.
        # *   Classless Inter-Domain Routing (CIDR) blocks, such as 10.23.12.0/24. In this case, /24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32.
        # 
        # > *   A maximum of 1,000 IP addresses or CIDR blocks can be configured for each instance.
        # > *   If you enter 0.0.0.0/0, all IP addresses can access the instance. This may introduce security risks to the instance. Proceed with caution.
        self.security_iplist = security_iplist
        # The ID of the source instance.
        # 
        # > When you call this operation to clone an instance, this parameter is required. The **BackupId** or **RestoreTime** parameter is also required. When you call this operation to restore an instance from the recycle bin, this parameter is required. The **BackupId** or **RestoreTime** parameter is not required.
        self.src_dbinstance_id = src_dbinstance_id
        # The region ID of the instance.
        # 
        # > -  This parameter is required when restore type is set to 2 or 3.
        self.src_region = src_region
        # The storage engine of the instance. Set the value to **WiredTiger**.
        # 
        # > * If you call this operation to clone an instance or restore an instance from the recycle bin, set this parameter to the storage engine of the source instance.
        # > * For more information about the limits on database versions and storage engines of an instance, see [MongoDB versions and storage engines](https://help.aliyun.com/document_detail/61906.html).
        self.storage_engine = storage_engine
        # The storage type of the instance. Valid values:
        # 
        # *   **cloud_essd1** :ESSD PL1.
        # *   **cloud_essd2**: ESSD PL2.
        # *   **cloud_essd3**: ESSD PL3.
        # *   **local_ssd**: local SSD.
        self.storage_type = storage_type
        # The custom tags added to the instance.
        self.tag = tag
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The zone ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent zone list.
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
        # The key of the tag.
        # 
        # > **N** specifies the serial number of the tag. For example, **Tag.1.Key** specifies the key of the first tag and **Tag.2.Key** specifies the key of the second tag.
        self.key = key
        # The value of the tag.
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


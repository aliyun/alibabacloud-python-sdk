# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CloneDBInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        backup_id: str = None,
        backup_type: str = None,
        bpe_enabled: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        client_token: str = None,
        custom_extra_info: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        db_names: str = None,
        dedicated_host_group_id: str = None,
        deletion_protection: bool = None,
        instance_network_type: str = None,
        io_acceleration_enabled: str = None,
        pay_type: str = None,
        period: str = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        restore_table: str = None,
        restore_time: str = None,
        serverless_config: main_models.CloneDBInstanceRequestServerlessConfig = None,
        table_meta: str = None,
        tag: List[main_models.CloneDBInstanceRequestTag] = None,
        used_time: int = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
        zone_id_slave_2: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # 1. **true**: enables automatic payment. Make sure that your account balance is sufficient.
        # 
        # 1. **false**: generates an order but does not deduct fees.
        # 
        # > Default value: true. If your payment method has an insufficient balance, you can set the AutoPay parameter to false. In this case, an unpaid order is generated, and you can log on to the ApsaraDB RDS console to complete the payment.
        self.auto_pay = auto_pay
        # The ID of the backup set.
        # 
        # You can call the DescribeBackups operation to query the backup sets.
        # 
        # >You must specify at least one of the **BackupId** and **RestoreTime** parameters.
        self.backup_id = backup_id
        # The backup type. Valid values:
        # 
        # * **FullBackup**: full backup.
        # * **IncrementalBackup**: incremental backup.
        self.backup_type = backup_type
        self.bpe_enabled = bpe_enabled
        # Specifies whether to enable the I/O performance burst feature for Premium ESSD cloud disks. Valid values:
        # * **true**: enables the feature.
        # * **false**: shutdown.
        # > For more information about the I/O performance burst feature, see [What is a premium performance disk](https://help.aliyun.com/document_detail/2340501.html).
        self.bursting_enabled = bursting_enabled
        # The instance edition. Valid values:
        # 
        # - **Basic**: Basic Edition.
        # - **HighAvailability**: high availability Edition (active).
        # - **AlwaysOn**: Cluster Edition (SQL Server).
        # - **cluster**: Cluster Edition (MySQL).
        # - **Finance**: Finance Edition (supported only on the China site).
        # 
        # **Serverless instances**
        # - **serverless_basic**: Serverless Basic Edition (applicable only to MySQL and PostgreSQL).
        # - **serverless_standard**: MySQL Serverless high availability Edition (active).
        # - **serverless_ha**: SQL Server Serverless high availability Edition (active).
        # > You do not need to specify this parameter. The cloned instance inherits the edition of the source instance.
        self.category = category
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The value can be up to 64 ASCII characters in length and cannot contain non-ASCII characters.
        self.client_token = client_token
        # The internal reserved field. You do not need to specify this parameter.
        self.custom_extra_info = custom_extra_info
        # The instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # >Default value: the instance type of the primary instance.
        self.dbinstance_class = dbinstance_class
        # The instance name. It must be 2 to 255 characters in length. It must start with a letter or a Chinese character and can contain letters, digits, Chinese characters, underscores (_), and hyphens (-).
        # >It cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Instance storage capacity of the instance. Unit: GB. Instance storage capacity increases in increments of 5 GB. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        # >Default value: instance storage capacity of the primary instance.
        self.dbinstance_storage = dbinstance_storage
        # The instance storage type. Valid values:
        # 
        # * **general_essd**: Premium ESSD (recommended).
        # * **local_ssd**: premium local disk.
        # * **cloud_ssd**: standard SSD.
        # * **cloud_essd**: PL1 ESSD.
        # * **cloud_essd2**: PL2 ESSD.
        # * **cloud_essd3**: PL3 ESSD.
        # 
        # > Serverless instances support only PL1 ESSD and Premium ESSD.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The names of the databases. Format: `Original database name 1,Original database name 2`.
        self.db_names = db_names
        # The ID of the dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to enable the release protection feature. Valid values:
        # * **true**: enables the feature.
        # * **false** (default): disables the feature.
        self.deletion_protection = deletion_protection
        # The network type of the instance. Valid values:
        # * **VPC**: Virtual Private Cloud (VPC).
        # * **Classic**: classic network.
        # 
        # >Default value: the network type of the primary instance.
        self.instance_network_type = instance_network_type
        # Specifies whether to enable the Buffer Pool Extension (BPE) feature for Premium ESSD cloud disks. Valid values:
        # 
        #  - **1**: enables the feature.
        #  - **0**: disables the feature.
        # 
        # > For more information about the BPE feature, see [Buffer Pool Extension (BPE)](https://help.aliyun.com/document_detail/2527067.html).
        self.io_acceleration_enabled = io_acceleration_enabled
        # The billing method of the instance. Valid values:
        # * **Postpaid**: pay-as-you-go.
        # * **Prepaid**: subscription.
        # * **Serverless**: serverless. This value is not supported for ApsaraDB RDS for MariaDB instances. For more information, see [Overview of serverless ApsaraDB RDS for MySQL instances](https://help.aliyun.com/document_detail/411291.html), [Overview of serverless ApsaraDB RDS for SQL Server instances](https://help.aliyun.com/document_detail/604344.html), and [Overview of serverless ApsaraDB RDS for PostgreSQL instances](https://help.aliyun.com/document_detail/607742.html).
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription period of the subscription instance. Valid values:
        # * **Year**: yearly subscription.
        # * **Month**: monthly subscription.
        # 
        # > This parameter is required when the billing method is set to **Prepaid**.
        self.period = period
        # The internal network IP address of the new instance. The IP address must be within the IP address range of the specified vSwitch. By default, the system automatically allocates an IP address based on the **VPCId** and **VSwitchId** parameters.
        self.private_ip_address = private_ip_address
        # The region ID. You can call the DescribeRegions operation to view the region ID.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # Specifies whether to restore individual databases and tables. A value of **true** specifies that individual databases and tables are restored. If you do not want to restore individual databases and tables, leave this parameter empty.
        self.restore_table = restore_table
        # The point in time to which you want to restore the instance. The point in time must be within the backup retention period. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time must be in UTC.
        # 
        # >You must specify at least one of the **BackupId** and **RestoreTime** parameters.
        self.restore_time = restore_time
        self.serverless_config = serverless_config
        # The information about the databases and tables that you want to restore. This parameter is required when you restore individual databases and tables. Format:
        # ```[{"type":"db","name":"Name of database 1","newname":"New name of database 1","tables":[{"type":"table","name":"Name of table 1 in database 1","newname":"New name of table 1"},{"type":"table","name":"Name of table 2 in database 1","newname":"New name of table 2"}]},{"type":"db","name":"Name of database 2","newname":"New name of database 2","tables":[{"type":"table","name":"Name of table 1 in database 2","newname":"New name of table 1"},{"type":"table","name":"Name of table 2 in database 2","newname":"New name of table 2"}]}]```
        self.table_meta = table_meta
        # The list of tags.
        self.tag = tag
        # The subscription duration. Valid values:
        # * Valid values when the **Period** parameter is set to **Year**: **1**, **2**, and **3**.
        # * Valid values when the **Period** parameter is set to **Month**: **1** to **9**.
        # 
        # > This parameter is required when the billing method is set to **Prepaid**.
        self.used_time = used_time
        # The VPC ID.
        # >Make sure that the VPC belongs to the region where the instance is deployed.
        self.vpcid = vpcid
        # The vSwitch ID. The zone (active zone) where the vSwitch is located must match the zone (active zone) ID specified in **ZoneId**.
        # 
        # - The network type **InstanceNetworkType** must be set to **VPC**.
        # - If you specify **ZoneSlaveId1** (the secondary active zone ID), you must specify two vSwitch IDs and separate them with commas (,).
        self.v_switch_id = v_switch_id
        # The primary zone ID. You can call the DescribeRegions operation to view the zone ID.
        # 
        # >Default value: the zone ID of the source instance.
        self.zone_id = zone_id
        # The secondary zone (active zone) ID. If this parameter is set to the same value as the **ZoneId** parameter, the instance uses a single-zone (active zone) deployment. If this parameter is set to a different value from the **ZoneId** parameter, the instance uses a multi-zone (active zone) deployment.
        self.zone_id_slave_1 = zone_id_slave_1
        # <props="intl">The logger zone (active zone) ID. If this parameter is set to the same value as the **ZoneId** parameter, the instance uses a single-zone (active zone) deployment. If this parameter is set to a different value from the **ZoneId** parameter, the instance uses a multi-zone (active zone) deployment.
        # 
        # <props="china">The secondary zone (active zone) ID or logger zone (active zone) ID. If this parameter is set to the same value as the **ZoneId** parameter, the instance uses a single-zone (active zone) deployment. If this parameter is set to a different value from the **ZoneId** parameter, the instance uses a multi-zone (active zone) deployment.
        self.zone_id_slave_2 = zone_id_slave_2

    def validate(self):
        if self.serverless_config:
            self.serverless_config.validate()
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

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.bpe_enabled is not None:
            result['BpeEnabled'] = self.bpe_enabled

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.custom_extra_info is not None:
            result['CustomExtraInfo'] = self.custom_extra_info

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.db_names is not None:
            result['DbNames'] = self.db_names

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.io_acceleration_enabled is not None:
            result['IoAccelerationEnabled'] = self.io_acceleration_enabled

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_table is not None:
            result['RestoreTable'] = self.restore_table

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.serverless_config is not None:
            result['ServerlessConfig'] = self.serverless_config.to_map()

        if self.table_meta is not None:
            result['TableMeta'] = self.table_meta

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_id_slave_1 is not None:
            result['ZoneIdSlave1'] = self.zone_id_slave_1

        if self.zone_id_slave_2 is not None:
            result['ZoneIdSlave2'] = self.zone_id_slave_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BpeEnabled') is not None:
            self.bpe_enabled = m.get('BpeEnabled')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CustomExtraInfo') is not None:
            self.custom_extra_info = m.get('CustomExtraInfo')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('IoAccelerationEnabled') is not None:
            self.io_acceleration_enabled = m.get('IoAccelerationEnabled')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTable') is not None:
            self.restore_table = m.get('RestoreTable')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('ServerlessConfig') is not None:
            temp_model = main_models.CloneDBInstanceRequestServerlessConfig()
            self.serverless_config = temp_model.from_map(m.get('ServerlessConfig'))

        if m.get('TableMeta') is not None:
            self.table_meta = m.get('TableMeta')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CloneDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneIdSlave1') is not None:
            self.zone_id_slave_1 = m.get('ZoneIdSlave1')

        if m.get('ZoneIdSlave2') is not None:
            self.zone_id_slave_2 = m.get('ZoneIdSlave2')

        return self

class CloneDBInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify this parameter to bind a tag to the instance.
        # 
        # * If the specified tag key already exists, the tag key is directly bound to the instance. You can call the ListTagResources operation to query the created tags.
        # * If the specified tag key does not exist, the tag key is created and then bound to the instance.
        # * Empty strings are not allowed.
        # * This parameter must be used together with the **Tag.Value** parameter and cannot be used alone.
        self.key = key
        # The tag value that corresponds to the tag key. You can specify this parameter to bind a tag to the instance.
        # 
        # * If the specified tag value already exists for the corresponding tag key, the tag value is directly bound to the instance. You can call the ListTagResources operation to query the created tags.
        # * If the specified tag value does not exist for the corresponding tag key, the tag value is created and then bound to the instance.
        # * This parameter must be used together with the **Tag.Key** parameter and cannot be used alone.
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

class CloneDBInstanceRequestServerlessConfig(DaraModel):
    def __init__(
        self,
        auto_pause: bool = None,
        max_capacity: float = None,
        min_capacity: float = None,
        switch_force: bool = None,
    ):
        self.auto_pause = auto_pause
        self.max_capacity = max_capacity
        self.min_capacity = min_capacity
        self.switch_force = switch_force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pause is not None:
            result['AutoPause'] = self.auto_pause

        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        if self.switch_force is not None:
            result['SwitchForce'] = self.switch_force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPause') is not None:
            self.auto_pause = m.get('AutoPause')

        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        if m.get('SwitchForce') is not None:
            self.switch_force = m.get('SwitchForce')

        return self


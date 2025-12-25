# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneDBInstanceShrinkRequest(DaraModel):
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
        serverless_config_shrink: str = None,
        table_meta: str = None,
        used_time: int = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        zone_id_slave_1: str = None,
        zone_id_slave_2: str = None,
    ):
        # Specifies whether to enable the automatic payment feature for the new instance. Valid values:
        # 
        # 1.  **true**: enables the feature. You must make sure that your account balance is sufficient.
        # 2.  **false**: disables the feature. An unpaid order is generated.
        # 
        # >  Default value: true. If your account balance is insufficient, you can set the AutoPay parameter to false to generate an unpaid order. Then, you can log on to the ApsaraDB RDS console to complete the payment.
        self.auto_pay = auto_pay
        # The backup set ID.
        # 
        # You can call the DescribeBackups operation to query the backup set ID.
        # 
        # >  You must specify at least one of the **BackupId** or **RestoreTime** parameters.
        self.backup_id = backup_id
        # The type of backup that is used to restore the data of the original instance. Valid values:
        # 
        # *   **FullBackup**
        # *   **IncrementalBackup**
        self.backup_type = backup_type
        # A reserved parameter. You do not need to specify this parameter.
        self.bpe_enabled = bpe_enabled
        # An invalid parameter. You do not need to specify this parameter.
        self.bursting_enabled = bursting_enabled
        # The RDS edition of the instance. Valid values:
        # 
        # *   **Basic**: RDS Basic Edition.
        # *   **HighAvailability**: RDS High-availability Edition.
        # *   **AlwaysOn**: RDS Cluster Edition for ApsaraDB RDS for SQL Server.
        # *   **cluster**: RDS Cluster Edition for ApsaraDB RDS for MySQL.
        # *   **Finance**: RDS Enterprise Edition. This edition is available only on the China site (aliyun.com).
        # 
        # **Serverless instances**
        # 
        # *   **serverless_basic**: RDS Basic Edition. This edition is available only for serverless instances that run MySQL and PostgreSQL.
        # *   **serverless_standard**: RDS High-availability Edition for ApsaraDB RDS for MySQL
        # *   **serverless_ha**: RDS High-availability Edition for ApsaraDB RDS for SQL Server
        # 
        # >  You do not need to configure this parameter. The value of this parameter is the same as that of the original instance.
        self.category = category
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.custom_extra_info = custom_extra_info
        # The instance type of the new instance. For information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # > By default, the new instance uses the same instance type as the original primary instance.
        self.dbinstance_class = dbinstance_class
        # The instance name. The value must be 2 to 255 characters in length The value can contain letters, digits, underscores (_), and hyphens (-), and must start with a letter.
        # 
        # >  The value cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The storage capacity of the new instance. Unit: GB. You can increase the storage capacity in increments of 5 GB. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # > By default, the new instance has the same storage capacity as the original primary instance.
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the new instance. Valid values:
        # 
        # *   **general_essd** (recommend): general Enterprise SSD (ESSD)
        # *   **local_ssd**: local SSD
        # *   **cloud_ssd**: standard SSD
        # *   **cloud_essd**: performance level 1 (PL1) ESSD
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        # 
        # >  Serverless instances support only PL1 ESSDs and general ESSDs.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The name of the database. If you specify more than one database, the value is in the following format: `Original database name 1,Original database name 2`.
        self.db_names = db_names
        # The ID of the dedicated cluster.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to enable the release protection feature for the new instance. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.deletion_protection = deletion_protection
        # The network type of the new instance. Valid values:
        # 
        # *   **VPC**
        # *   **Classic**
        # 
        # > By default, the new instance has the same network type as the original primary instance.
        self.instance_network_type = instance_network_type
        # A reserved parameter.
        self.io_acceleration_enabled = io_acceleration_enabled
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        # *   **Serverless**: serverless. This value is not supported for instances that run MariaDB. For more information, see [Overview of serverless ApsaraDB RDS for MySQL instances](https://help.aliyun.com/document_detail/411291.html), [Overview of serverless ApsaraDB RDS for SQL Server instances](https://help.aliyun.com/document_detail/604344.html), and [Overview of serverless ApsaraDB RDS for PostgreSQL instances](https://help.aliyun.com/document_detail/607742.html).
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit that is used to calculate the billing cycle of the new instance. This parameter takes effect only when you select the subscription billing method for the new instance. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        # 
        # >  If you set the PayType parameter to **Prepaid**, you must specify this parameter.
        self.period = period
        # The internal IP address of the new instance, which must be within the CIDR block supported by the specified vSwitch. The system automatically assigns an internal IP address based on the values of the **VPCId** and **VSwitchId** parameters.
        self.private_ip_address = private_ip_address
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # Specifies whether to restore only the databases and tables that you specify. The value **1** specifies to restore only the specified databases and tables. If you do not want to restore only the specified databases or tables, you do not need to specify this parameter.
        self.restore_table = restore_table
        # The point in time to which you want to restore data. The point in time must fall within the specified backup retention period. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # > You must specify at least one of the **BackupId** and **RestoreTime** parameters.
        self.restore_time = restore_time
        # The specifications for the serverless instance. You must specify this parameter only when you restore data to a new serverless instance.
        # 
        # >  This parameter is available only on the China site (aliyun.com).
        self.serverless_config_shrink = serverless_config_shrink
        # The information about the database and table that you want to restore. The value is in the following format: `[{"type":"db","name":"Name of Database 1","newname":"New name of Database 1","tables":[{"type":"table","name":"Name of Table 1 in Database 1","newname":"New name of Table 1"},{"type":"table","name":"Name of Table 2 in Database 1","newname":"New name of Table 2"}]},{"type":"db","name":"Name of Database 2","newname":"New name of Database 2","tables":[{"type":"table","name":"Name of Table 1 in Database 2","newname":"New name of Table 1"},{"type":"table","name":"Name of Table 2 in Database 2","newname":"New name of Table 2"}]}]`
        self.table_meta = table_meta
        # The subscription duration of the new instance. Valid values:
        # 
        # *   If you set the **Period** parameter to **Year**, the value of the UsedTime parameter ranges from **1 to 3**.
        # *   If you set the **Period** parameter to **Month**, the value of the UsedTime parameter ranges from **1 to 9**.
        # 
        # > If you set the PayType parameter to **Prepaid**, you must also specify this parameter.
        self.used_time = used_time
        # The ID of the virtual private cloud (VPC).
        # 
        # >  Make sure that the VPC belongs to the required region.
        self.vpcid = vpcid
        # The ID of the vSwitch. The vSwitch must belong to the zone that is specified by **ZoneId**.
        # 
        # *   If you set **InstanceNetworkType** to **VPC**, you must also specify this parameter.
        # *   If you specify the **ZoneSlaveId1** parameter, you must specify the IDs of two vSwitches for this parameter and separate the IDs with a comma (,).
        self.v_switch_id = v_switch_id
        # The zone ID of the primary instance. You can call the DescribeRegions operation to query the zone ID.
        # 
        # >  Set this value to the zone ID of the original instance.
        self.zone_id = zone_id
        # The zone ID of the secondary instance. If you set the ZoneIdSlave1 parameter and the **ZoneId** parameter to the same value, the single-zone deployment method is used. If you set the ZoneIdSlave1 parameter and the **ZoneId** parameter to different values, the multi-zone deployment method is used.
        self.zone_id_slave_1 = zone_id_slave_1
        # The zone ID of the logger instance. If you set the ZoneIdSlave2 parameter to the same value as the **ZoneId** parameter, the single-zone deployment method is used. If you set the ZoneIdSlave2 parameter to a different value from the **ZoneId** parameter, the multi-zone deployment method is used.
        self.zone_id_slave_2 = zone_id_slave_2

    def validate(self):
        pass

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

        if self.serverless_config_shrink is not None:
            result['ServerlessConfig'] = self.serverless_config_shrink

        if self.table_meta is not None:
            result['TableMeta'] = self.table_meta

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
            self.serverless_config_shrink = m.get('ServerlessConfig')

        if m.get('TableMeta') is not None:
            self.table_meta = m.get('TableMeta')

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


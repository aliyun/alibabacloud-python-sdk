# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
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
        tag: List[main_models.CloneDBInstanceShrinkRequestTag] = None,
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
        # 1. **false**: generates an order without charging the account.
        # 
        # 
        # 
        # 
        # > Default value: true. If your payment method has insufficient balance, set AutoPay to false. In this case, an unpaid order is generated. You can log on to the ApsaraDB RDS console to pay for the order.
        # >
        self.auto_pay = auto_pay
        # The backup set ID.
        # 
        # You can call the DescribeBackups operation to query the backup set list.
        # 
        # > You must specify at least one of **BackupId** and **RestoreTime**.
        self.backup_id = backup_id
        # The backup type. Valid values:
        # 
        # * **FullBackup**: full backup.
        # * **IncrementalBackup**: incremental backup.
        self.backup_type = backup_type
        self.bpe_enabled = bpe_enabled
        # Specifies whether to enable the I/O burst feature for the Premium ESSD cloud disk. Valid values:
        # * **true**: enables the feature.
        # * **false**: disables the feature.
        # > For more information about the I/O burst feature, see [What is Premium ESSD?](https://help.aliyun.com/document_detail/2340501.html).
        self.bursting_enabled = bursting_enabled
        # The instance edition. Valid values:
        # 
        # - **Basic**: Basic Edition.
        # - **HighAvailability**: High-availability Edition.
        # - **AlwaysOn**: Cluster Edition (SQL Server).
        # - **cluster**: Cluster Edition (MySQL).
        # - **Finance**: Enterprise Edition. This value is supported only on the China site (aliyun.com).
        # 
        # **Serverless instances**
        # - **serverless_basic**: Serverless Basic Edition. This value is valid only for ApsaraDB RDS for MySQL and ApsaraDB RDS for PostgreSQL instances.
        # - **serverless_standard**: MySQL Serverless High-availability Edition.
        # - **serverless_ha**: SQL Server Serverless High-availability Edition.
        # > You do not need to specify this parameter. The clone instance uses the same edition as the source instance.
        self.category = category
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.custom_extra_info = custom_extra_info
        # The instance type. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # > Default value: the instance type of the source instance.
        self.dbinstance_class = dbinstance_class
        # The name of the instance. The name must be 2 to 255 characters in length. It must start with a letter or a Chinese character and can contain digits, Chinese characters, letters, underscores (_), and hyphens (-).
        # > The name cannot start with http:// or https://.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Instance storage capacity of the instance. Unit: GB. The value increases in increments of 5 GB. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        # > Default value: instance storage capacity of the source instance.
        self.dbinstance_storage = dbinstance_storage
        # The instance storage type. Valid values:
        # 
        # * **general_essd**: Premium ESSD (recommended).
        # * **local_ssd**: local SSD.
        # * **cloud_ssd**: standard SSD.
        # * **cloud_essd**: PL1 ESSD.
        # * **cloud_essd2**: PL2 ESSD.
        # * **cloud_essd3**: PL3 ESSD.
        # 
        # > Serverless instances support only PL1 ESSDs and Premium ESSDs.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The database names in the following format: `OriginalDatabaseName1,OriginalDatabaseName2`.
        self.db_names = db_names
        # The dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # Specifies whether to enable the release protection feature. Valid values:
        # * **true**: enables the feature.
        # * **false** (default): disables the feature.
        self.deletion_protection = deletion_protection
        # The network type of the instance. Valid values:
        # * **VPC**: virtual private cloud (VPC).
        # * **Classic**: classic network.
        # 
        # > Default value: the network type of the source instance.
        self.instance_network_type = instance_network_type
        # Specifies whether to enable the Buffer Pool Extension (BPE) feature for the Premium ESSD cloud disk. Valid values:
        # 
        #  - **1**: enables the feature.
        #  - **0**: disables the feature.
        # 
        # > For more information about the BPE feature, see [Buffer Pool Extension (BPE)](https://help.aliyun.com/document_detail/2527067.html).
        self.io_acceleration_enabled = io_acceleration_enabled
        # The billing method. Valid values:
        # * **Postpaid**: pay-as-you-go.
        # * **Prepaid**: subscription.
        # * **Serverless**: serverless. This value is not supported for ApsaraDB RDS for MariaDB instances. For more information, see [Overview of MySQL Serverless instances](https://help.aliyun.com/document_detail/411291.html), [Overview of SQL Server Serverless instances](https://help.aliyun.com/document_detail/604344.html), and [Overview of PostgreSQL Serverless instances](https://help.aliyun.com/document_detail/607742.html).
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # * **Year**
        # * **Month**
        # 
        # > This parameter is required if PayType is set to **Prepaid**.
        self.period = period
        # The internal IP address of the new instance. The IP address must be within the IP address range of the specified vSwitch. The system automatically assigns an internal IP address based on the values of **VPCId** and **VSwitchId**.
        self.private_ip_address = private_ip_address
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # Specifies whether to restore individual databases and tables. Set this parameter to **true** to restore individual databases and tables. Otherwise, leave this parameter empty.
        self.restore_table = restore_table
        # Any point in time within the backup retention period. Specify the time in the format of <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # 
        # > You must specify at least one of **BackupId** and **RestoreTime**.
        self.restore_time = restore_time
        self.serverless_config_shrink = serverless_config_shrink
        # The information about the databases and tables that you want to restore. Format:
        # ```[{"type":"db","name":"Database1Name","newname":"NewDatabase1Name","tables":[{"type":"table","name":"Table1NameInDatabase1","newname":"NewTable1Name"},{"type":"table","name":"Table2NameInDatabase1","newname":"NewTable2Name"}]},{"type":"db","name":"Database2Name","newname":"NewDatabase2Name","tables":[{"type":"table","name":"Table1NameInDatabase2","newname":"NewTable1Name"},{"type":"table","name":"Table2NameInDatabase2","newname":"NewTable2Name"}]}]```
        self.table_meta = table_meta
        # The tag list.
        self.tag = tag
        # The subscription duration. Valid values:
        # * If **Period** is set to **Year**, the value of UsedTime ranges from **1 to 3**.
        # * If **Period** is set to **Month**, the value of UsedTime ranges from **1 to 9**.
        # 
        # > This parameter is required if PayType is set to **Prepaid**.
        self.used_time = used_time
        # The VPC ID.
        # > Make sure that the VPC belongs to the corresponding region.
        self.vpcid = vpcid
        # The vSwitch ID. The zone of the vSwitch must correspond to the active zone ID specified in **ZoneId**.
        # 
        # - The network type (**InstanceNetworkType**) must be set to **VPC**.
        # - If you specify **ZoneSlaveId1** (secondary zone ID), you must specify two vSwitch IDs separated by a comma (,).
        self.v_switch_id = v_switch_id
        # The primary zone ID. You can call the DescribeRegions operation to query the zone ID.
        # 
        # > Default value: the zone of the source instance.
        self.zone_id = zone_id
        # The zone ID of the secondary node. If this parameter is set to the same value as **ZoneId**, the single-zone deployment method is used. If this parameter is set to a different value from **ZoneId**, the multi-zone deployment method is used.
        self.zone_id_slave_1 = zone_id_slave_1
        # <props="intl">The zone ID of the logger node. If this parameter is set to the same value as **ZoneId**, the single-zone deployment method is used. If this parameter is set to a different value from **ZoneId**, the multi-zone deployment method is used.
        # 
        # <props="china">The zone ID of the secondary node or logger node. If this parameter is set to the same value as **ZoneId**, the single-zone deployment method is used. If this parameter is set to a different value from **ZoneId**, the multi-zone deployment method is used.
        self.zone_id_slave_2 = zone_id_slave_2

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
            self.serverless_config_shrink = m.get('ServerlessConfig')

        if m.get('TableMeta') is not None:
            self.table_meta = m.get('TableMeta')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CloneDBInstanceShrinkRequestTag()
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

class CloneDBInstanceShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Specify this parameter to attach a tag to the instance.
        # 
        # * If the specified tag key already exists, the tag is directly attached to the instance. You can call the ListTagResources operation to query existing tags.
        # * If the specified tag key does not exist, the tag key is created and then attached to the instance.
        # * Empty strings are not allowed.
        # * This parameter must be used together with **Tag.Value**.
        self.key = key
        # The tag value that corresponds to the tag key. Specify this parameter to attach a tag to the instance.
        # 
        # * If the specified tag value already exists for the corresponding tag key, the tag value is directly attached to the instance. You can call the ListTagResources operation to query existing tags.
        # * If the specified tag value does not exist for the corresponding tag key, the tag value is created and then attached to the instance.
        # * This parameter must be used together with **Tag.Key**.
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


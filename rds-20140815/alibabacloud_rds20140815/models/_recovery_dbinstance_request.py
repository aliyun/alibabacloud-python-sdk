# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecoveryDBInstanceRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        db_names: str = None,
        instance_network_type: str = None,
        pay_type: str = None,
        period: str = None,
        private_ip_address: str = None,
        resource_owner_id: int = None,
        restore_time: str = None,
        target_dbinstance_id: str = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The backup set ID. You can call the DescribeBackups operation to query the backup set ID.
        # 
        # If you specify this parameter, you do not need to specify **DBInstanceId**.
        # 
        # >  You must specify at least one of the **BackupId** or **RestoreTime** parameters.
        self.backup_id = backup_id
        # The instance type of the new instance. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_class = dbinstance_class
        # The ID of the original instance.
        # 
        # > *   If you specify BackupId, you do not need to specify this parameter.
        # > *   If you specify RestoreTime, you must also specify this parameter.
        self.dbinstance_id = dbinstance_id
        # The storage capacity of the new instance. Unit: GB. For more information, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # >  You must set this parameter to a value that is greater than or equal to the storage capacity of the original instance.
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the new instance. Valid values:
        # 
        # *   **local_ssd/ephemeral_ssd**: local SSD
        # *   **cloud_ssd**: standard SSD.
        # *   **cloud_essd**: enhanced SSD (ESSD)
        self.dbinstance_storage_type = dbinstance_storage_type
        # The name of the database. When you restore data to a new instance, the format of the database name is `Original database name 1,New database name 2`.
        # 
        # >  For more information about how to restore data to an existing instance, see [CopyDatabaseBetweenInstances](https://help.aliyun.com/document_detail/2628854.html).
        # 
        # This parameter is required.
        self.db_names = db_names
        # The network type of the new instance. Valid values:
        # 
        # *   **Classic**
        # *   **VPC**
        # 
        # By default, the new instance uses the same network type as the original instance.
        self.instance_network_type = instance_network_type
        # The billing method of the new instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.pay_type = pay_type
        # The unit that is used to calculate the billing cycle of the new instance. This parameter takes effect only when you select the subscription billing method for the new instance. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        # 
        # > This parameter must be specified when **PayType** is set to **Prepaid**.
        self.period = period
        # The internal IP address of the new instance. The internal IP address must be within the CIDR block that is supported by the specified vSwitch. The system automatically assigns an internal IP address based on the values of the **VPCId** and **VSwitchId** parameters.
        self.private_ip_address = private_ip_address
        self.resource_owner_id = resource_owner_id
        # The point in time to which you want to restore data. The point in time must fall within the specified log backup retention period. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # If you specify this parameter, you must also specify **DBInstanceId**.
        # 
        # > You must specify at least one of **BackupId** and **RestoreTime**.
        self.restore_time = restore_time
        # The ID of the destination instance.
        self.target_dbinstance_id = target_dbinstance_id
        # The subscription duration of the instance. Valid values:
        # 
        # *   Valid values when **Period** is set to **Year**: **1 to 3**.****
        # *   Valid values when **Period** is set to **Month**: **1 to 9**.****
        # 
        # > This parameter must be specified when PayType is set to **Prepaid**.
        self.used_time = used_time
        # The VPC ID of the new instance.
        self.vpcid = vpcid
        # The vSwitch ID of the new instance. If you specify more than one vSwitch ID, you must separate the IDs with commas (,).
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.db_names is not None:
            result['DbNames'] = self.db_names

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time

        if self.target_dbinstance_id is not None:
            result['TargetDBInstanceId'] = self.target_dbinstance_id

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')

        if m.get('TargetDBInstanceId') is not None:
            self.target_dbinstance_id = m.get('TargetDBInstanceId')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self


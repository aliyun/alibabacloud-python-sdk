# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBackupPlanRequest(DaraModel):
    def __init__(
        self,
        backup_method: str = None,
        client_token: str = None,
        database_region: str = None,
        database_type: str = None,
        from_app: str = None,
        instance_class: str = None,
        instance_type: str = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        region: str = None,
        resource_group_id: str = None,
        storage_region: str = None,
        storage_type: str = None,
        used_time: int = None,
    ):
        # The backup method. Valid values:
        # 
        # - **logical**: logical backup
        # 
        # - **physical**: physical backup
        # 
        # This parameter is required.
        self.backup_method = backup_method
        # A client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The region of the database.
        self.database_region = database_region
        # The database type. Valid values:
        # 
        # - **MySQL**
        # 
        # - **MSSQL**
        # 
        # - **Oracle**
        # 
        # - **MariaDB**
        # 
        # - **PostgreSQL**
        # 
        # - **DRDS**
        # 
        # - **MongoDB**
        # 
        # - **Redis**
        # 
        # This parameter is required.
        self.database_type = database_type
        # The source of the request. The default value is OpenAPI. You do not need to set this parameter.
        self.from_app = from_app
        # The instance class. Valid values:
        # 
        # - **micro**: Entry
        # 
        # - **small**: Basic
        # 
        # - **medium**: Standard
        # 
        # - **large**: Enhanced
        # 
        # - **xlarge**: Enhanced (no traffic limit)
        # 
        # > The higher the instance class, the better the performance of backup and recovery. For more information, see [Specifications](https://help.aliyun.com/document_detail/84372.html).
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The database instance type. Valid values:
        # 
        # - **RDS**
        # 
        # - **PolarDB**
        # 
        # - **DDS**: Alibaba Cloud MongoDB
        # 
        # - **Kvstore**: Alibaba Cloud Redis
        # 
        # - **Other**: A database that is connected over the Internet.
        # 
        # - **dg**: A self-managed database without a public IP address and port that is connected through Database Gateway (DG).
        self.instance_type = instance_type
        self.owner_id = owner_id
        # The payment method. Valid value:
        # 
        # **prepay**: subscription
        self.pay_type = pay_type
        # The billing cycle of the subscription instance. Valid values:
        # 
        # - **Year**
        # 
        # - **Month**
        self.period = period
        # The region ID of the DBS instance. This parameter is required. Call the [DescribeRegions](https://help.aliyun.com/document_detail/2869853.html) operation to view the regions that DBS supports.
        # 
        # > For more information, see [Endpoints](https://help.aliyun.com/document_detail/2869810.html).
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The storage region.
        self.storage_region = storage_region
        # This parameter is not used.
        self.storage_type = storage_type
        # The subscription duration. Valid values:
        # 
        # - If you set the **Period** parameter to **Year**, the value of **UsedTime** can be 1 to 5.
        # 
        # - If you set the **Period** parameter to **Month**, the value of **UsedTime** can be 1 to 11.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.database_region is not None:
            result['DatabaseRegion'] = self.database_region

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.from_app is not None:
            result['FromApp'] = self.from_app

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.storage_region is not None:
            result['StorageRegion'] = self.storage_region

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DatabaseRegion') is not None:
            self.database_region = m.get('DatabaseRegion')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StorageRegion') is not None:
            self.storage_region = m.get('StorageRegion')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self


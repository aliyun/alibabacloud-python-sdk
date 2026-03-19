# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAndStartBackupPlanRequest(DaraModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_log_interval_seconds: int = None,
        backup_method: str = None,
        backup_objects: str = None,
        backup_period: str = None,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        backup_rate_limit: int = None,
        backup_retention_period: int = None,
        backup_speed_limit: int = None,
        backup_start_time: str = None,
        backup_storage_type: str = None,
        backup_strategy_type: str = None,
        client_token: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        database_region: str = None,
        database_type: str = None,
        duplication_archive_period: int = None,
        duplication_infrequent_access_period: int = None,
        enable_backup_log: bool = None,
        from_app: str = None,
        instance_class: str = None,
        instance_type: str = None,
        ossbucket_name: str = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        region: str = None,
        resource_group_id: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: int = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
        storage_region: str = None,
        storage_type: str = None,
        used_time: int = None,
    ):
        # The ID of the backup gateway.
        # 
        # > - This parameter is required if **SourceEndpoint**.**InstanceType** is set to **agent**.
        # >
        # > - For more information about how to create a backup gateway, see [Add a backup gateway](https://help.aliyun.com/document_detail/93250.html).
        # >
        # > - You can call the [DescribeBackupGatewayList](https://help.aliyun.com/document_detail/2869840.html) operation to view the list of existing backup gateways.
        self.backup_gateway_id = backup_gateway_id
        # The interval for incremental backups, in seconds.
        # 
        # > This parameter is required only for **physical backups**.
        self.backup_log_interval_seconds = backup_log_interval_seconds
        # The backup method. Valid values:
        # 
        # - **logical**: logical backup
        # 
        # - **physical**: physical backup
        # 
        # This parameter is required.
        self.backup_method = backup_method
        # The backup objects.
        self.backup_objects = backup_objects
        # The full backup cycle. Valid values:
        # 
        # - **Monday**
        # 
        # - **Tuesday**
        # 
        # - **Wednesday**
        # 
        # - **Thursday**
        # 
        # - **Friday**
        # 
        # - **Saturday**
        # 
        # - **Sunday**
        # 
        # > You can select multiple values. Separate them with commas (,).
        self.backup_period = backup_period
        # The ID of the backup plan.
        self.backup_plan_id = backup_plan_id
        # The custom name of the backup plan.
        # 
        # This parameter is required.
        self.backup_plan_name = backup_plan_name
        # The network bandwidth throttling limit, in KB/s. The maximum allowed value is 10 GB.
        # 
        # > This parameter is valid only for MySQL physical backups.
        self.backup_rate_limit = backup_rate_limit
        # The retention period for backup data, in days. Valid values: 0 to 1825. Default value: 730.
        self.backup_retention_period = backup_retention_period
        # The disk I/O limit, in KB/s.
        # 
        # > This parameter is valid only for MySQL physical backups.
        self.backup_speed_limit = backup_speed_limit
        # The start time for the full backup. The time is in the *HH:mm* format and is in UTC.
        self.backup_start_time = backup_start_time
        # The built-in storage type:
        # 
        # - Empty (default): Backup data is stored in your OSS bucket.
        # 
        # - system: Backup data is stored in the built-in OSS bucket of DBS.
        self.backup_storage_type = backup_storage_type
        # The full backup strategy. Valid values:
        # 
        # - **simple**: periodic backup. Use this value with BackupPeriod and BackupStartTime.
        # 
        # - **manual**: manual backup.
        # 
        # > The default value is **simple**.
        self.backup_strategy_type = backup_strategy_type
        # A client token used to ensure the idempotence of the request. This prevents duplicate requests.
        self.client_token = client_token
        # The UID of the Alibaba Cloud account for cross-account backup.
        self.cross_aliyun_id = cross_aliyun_id
        # The name of the RAM role for cross-account backup.
        self.cross_role_name = cross_role_name
        # The region where the database is located.
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
        # The time after which backup data is converted to archive storage, in days. Default value: 365.
        self.duplication_archive_period = duplication_archive_period
        # The time after which backup data is converted to Infrequent Access (IA) storage, in days. Default value: 180.
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        # Specifies whether to enable incremental log backup. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.enable_backup_log = enable_backup_log
        # The source of the request. The default value is OpenApi. You do not need to set this parameter.
        self.from_app = from_app
        # The specification of the backup plan. Valid values:
        # 
        # - **micro**
        # 
        # - **small**
        # 
        # - **medium**
        # 
        # - **large**
        # 
        # - **xlarge**
        # 
        # > Higher specifications provide better backup and recovery performance. For more information, see [Specifications](https://help.aliyun.com/document_detail/84372.html).
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
        # - **Other**: A database connected over an IP address and port.
        # 
        # - **dg**: A self-managed database without a public IP address or port, connected through Database Gateway (DG).
        self.instance_type = instance_type
        # The name of the Object Storage Service (OSS) bucket.
        # Default: The system automatically generates a new name.
        self.ossbucket_name = ossbucket_name
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
        # The region where DBS is available. To view the available regions, call the [DescribeRegions](https://help.aliyun.com/document_detail/2869853.html) operation.
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The database name.
        # 
        # > This parameter is required if the database type is **PostgreSQL** or **MongoDB**.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The database endpoint.
        # 
        # > This parameter is required if **SourceEndpoint**.**InstanceType** is set to **express**, **agent**, or **other**.
        self.source_endpoint_ip = source_endpoint_ip
        # The ID of the database instance.
        # 
        # > This parameter is required if **SourceEndpoint**.**InstanceType** is set to **RDS**, **ECS**, **DDS**, or **Express**.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The location of the database. Valid values:
        # 
        # - **RDS**
        # 
        # - **ECS**
        # 
        # - **Express**: A database connected through a leased line, VPN Gateway, or Smart Access Gateway.
        # 
        # - **Agent**: A database connected through a backup gateway.
        # 
        # - **DDS**: Alibaba Cloud MongoDB
        # 
        # - **Other**: A database connected directly over an IP address and port.
        # 
        # - **dg**: A self-managed database without a public IP address or port, connected through Database Gateway (DG).
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The Oracle system ID (SID). This parameter is required if the database type is Oracle.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The password for the database account.
        # 
        # > This parameter is optional if the database type is **Redis**, or if the database location is **agent** and the database type is **MSSQL**. In all other cases, this parameter is required.
        self.source_endpoint_password = source_endpoint_password
        # The database port.
        # 
        # > This parameter is required if **SourceEndpoint**.**InstanceType** is set to **express**, **agent**, **other**, or **ECS**.
        self.source_endpoint_port = source_endpoint_port
        # The region where the database is located.
        # 
        # > This parameter is required if **SourceEndpoint**.**InstanceType** is set to **RDS**, **ECS**, **DDS**, **Express**, or **Agent**.
        self.source_endpoint_region = source_endpoint_region
        # The database account.
        # 
        # > This parameter is optional if the database type is **Redis**, or if the database location is **agent** and the database type is **MSSQL**. In all other cases, this parameter is required.
        self.source_endpoint_user_name = source_endpoint_user_name
        # The storage region.
        self.storage_region = storage_region
        # This parameter is not yet available.
        self.storage_type = storage_type
        # The subscription duration. Valid values:
        # 
        # - If **Period** is set to **Year**, the value of **UsedTime** can be 1 to 5.
        # 
        # - If **Period** is set to **Month**, the value of **UsedTime** can be 1 to 11.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id

        if self.backup_log_interval_seconds is not None:
            result['BackupLogIntervalSeconds'] = self.backup_log_interval_seconds

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects

        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name

        if self.backup_rate_limit is not None:
            result['BackupRateLimit'] = self.backup_rate_limit

        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period

        if self.backup_speed_limit is not None:
            result['BackupSpeedLimit'] = self.backup_speed_limit

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_storage_type is not None:
            result['BackupStorageType'] = self.backup_storage_type

        if self.backup_strategy_type is not None:
            result['BackupStrategyType'] = self.backup_strategy_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id

        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name

        if self.database_region is not None:
            result['DatabaseRegion'] = self.database_region

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period

        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.from_app is not None:
            result['FromApp'] = self.from_app

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ossbucket_name is not None:
            result['OSSBucketName'] = self.ossbucket_name

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

        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name

        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type

        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid

        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password

        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name

        if self.storage_region is not None:
            result['StorageRegion'] = self.storage_region

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('BackupLogIntervalSeconds') is not None:
            self.backup_log_interval_seconds = m.get('BackupLogIntervalSeconds')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')

        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')

        if m.get('BackupRateLimit') is not None:
            self.backup_rate_limit = m.get('BackupRateLimit')

        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')

        if m.get('BackupSpeedLimit') is not None:
            self.backup_speed_limit = m.get('BackupSpeedLimit')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStorageType') is not None:
            self.backup_storage_type = m.get('BackupStorageType')

        if m.get('BackupStrategyType') is not None:
            self.backup_strategy_type = m.get('BackupStrategyType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')

        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')

        if m.get('DatabaseRegion') is not None:
            self.database_region = m.get('DatabaseRegion')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')

        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OSSBucketName') is not None:
            self.ossbucket_name = m.get('OSSBucketName')

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

        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')

        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')

        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')

        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')

        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')

        if m.get('StorageRegion') is not None:
            self.storage_region = m.get('StorageRegion')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigureBackupPlanRequest(DaraModel):
    def __init__(
        self,
        auto_start_backup: bool = None,
        backup_gateway_id: int = None,
        backup_log_interval_seconds: int = None,
        backup_objects: str = None,
        backup_period: str = None,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        backup_rate_limit: int = None,
        backup_retention_period: int = None,
        backup_speed_limit: int = None,
        backup_start_time: str = None,
        backup_storage_encrypt_method: str = None,
        backup_storage_type: str = None,
        backup_strategy_type: str = None,
        client_token: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        duplication_archive_period: int = None,
        duplication_infrequent_access_period: int = None,
        enable_backup_log: bool = None,
        enable_mysql_physical_backup_binlog: str = None,
        enable_source_endpoint_ssl: str = None,
        ossbucket_name: str = None,
        owner_id: str = None,
        resource_group_id: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_home: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: int = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
        ssl_ca_pem: str = None,
    ):
        # Enable automatic backup. Valid values:
        # 
        # - **true**: Enable
        # 
        # - **false**: Disable
        self.auto_start_backup = auto_start_backup
        # The backup gateway ID. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        # 
        # > This parameter is required when **SourceEndpointInstanceType** is **agent**.
        self.backup_gateway_id = backup_gateway_id
        # The incremental interval in seconds (s).
        # 
        # > Only physical backup is supported.
        self.backup_log_interval_seconds = backup_log_interval_seconds
        # The backup objects. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        self.backup_objects = backup_objects
        # The full backup period. Valid values:
        # 
        # - **Monday**: Monday
        # 
        # - **Tuesday**: Tuesday
        # 
        # - **Wednesday**: Wednesday
        # 
        # - **Thursday**: Thursday
        # 
        # - **Friday**: Friday
        # 
        # - **Saturday**: Saturday
        # 
        # - **Sunday**: Sunday
        self.backup_period = backup_period
        # The backup plan ID. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The custom backup plan name. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        # 
        # This parameter is required.
        self.backup_plan_name = backup_plan_name
        # The network bandwidth throttling in KB/s. The maximum value is 10 GB.
        # 
        # > This parameter is valid only for MySQL physical backup.
        self.backup_rate_limit = backup_rate_limit
        # The retention period for backup data. Valid values: 0 to 1825. Default value: 730 days.
        self.backup_retention_period = backup_retention_period
        # The disk I/O limit in KB/s.
        # 
        # > This parameter is valid only for MySQL physical backup.
        self.backup_speed_limit = backup_speed_limit
        # The full backup start time in *HH:mm*Z (UTC) format. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        self.backup_start_time = backup_start_time
        self.backup_storage_encrypt_method = backup_storage_encrypt_method
        # The built-in storage type:
        # 
        # - Empty (default): Backup data is stored on your OSS.
        # 
        # - system: Backup data is stored on the built-in OSS of DBS.
        self.backup_storage_type = backup_storage_type
        # The full backup period. Valid values:
        # 
        # - **simple**: Periodic backup. Use this value with BackupPeriod and BackupStartTime.
        # 
        # - **manual**: Manual backup.
        # 
        # > Default value: **simple**.
        self.backup_strategy_type = backup_strategy_type
        # Ensure the idempotence of the request to prevent duplicate submissions. The client generates this parameter value. Ensure its uniqueness across different requests. The maximum length is 64 ASCII characters, and the value cannot contain non-ASCII characters.
        self.client_token = client_token
        # The UID for cross-Alibaba Cloud account backup. Call the [DescribeRestoreTaskList](https://help.aliyun.com/document_detail/2869838.html) API to get this parameter\\"s value.
        self.cross_aliyun_id = cross_aliyun_id
        # The RAM role name for cross-Alibaba Cloud account backup. Call the [DescribeRestoreTaskList](https://help.aliyun.com/document_detail/2869838.html) API to get this parameter\\"s value.
        self.cross_role_name = cross_role_name
        # The period after which data is converted to archive cold storage. Default value: 365 days.
        self.duplication_archive_period = duplication_archive_period
        # The period after which data is converted to Infrequent Access storage. Default value: 180 days.
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        # Enable incremental log backup. Valid values:
        # 
        # - **true**: Enable
        # 
        # - **false**: Disable
        self.enable_backup_log = enable_backup_log
        self.enable_mysql_physical_backup_binlog = enable_mysql_physical_backup_binlog
        self.enable_source_endpoint_ssl = enable_source_endpoint_ssl
        # The OSS bucket name.
        # 
        # > The system automatically generates a new name by default.
        self.ossbucket_name = ossbucket_name
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The database name. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        # 
        # > This parameter is required when the database type is **PostgreSQL** or **MongoDB**.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The database endpoint. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        # 
        # > This parameter is required when **SourceEndpointInstanceType** is **express**, **agent**, or **other**.
        self.source_endpoint_ip = source_endpoint_ip
        # The database instance ID. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        # 
        # > This parameter is required when **SourceEndpoint**.**InstanceType** is **RDS**, **ECS**, **DDS**, or **Express**.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The location of the database. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value. Valid values:
        # 
        # - **RDS**
        # 
        # - **ECS**
        # 
        # - **Express**: A database connected through a leased line, VPN Gateway, or Smart Gateway.
        # 
        # - **Agent**: A database connected through a backup gateway.
        # 
        # - **DDS**: Cloud MongoDB.
        # 
        # - **Other**: A database directly connected through IP:Port.
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_oracle_home = source_endpoint_oracle_home
        # The Oracle SID name.
        # 
        # > This parameter is required when the database type is Oracle.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The password.
        # 
        # > This parameter is optional when the database type is **Redis**, or when the database location is **agent** and the database type is **SQL Server**. It is required in other scenarios.
        self.source_endpoint_password = source_endpoint_password
        # The database port. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        # 
        # > This parameter is required when **SourceEndpoint**.**InstanceType** is **express**, **agent**, **other**, or **ECS**.
        self.source_endpoint_port = source_endpoint_port
        # The region of the database. Call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) API to get this parameter\\"s value.
        # 
        # > This parameter is required when **SourceEndpointInstanceType** is RDS, ECS, DDS, Express, or Agent.
        self.source_endpoint_region = source_endpoint_region
        # The database account.
        # 
        # > This parameter is optional when the database type is **Redis**, or when the database location is **agent** and the database type is **SQL Server**. It is required in other scenarios.
        self.source_endpoint_user_name = source_endpoint_user_name
        self.ssl_ca_pem = ssl_ca_pem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_start_backup is not None:
            result['AutoStartBackup'] = self.auto_start_backup

        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id

        if self.backup_log_interval_seconds is not None:
            result['BackupLogIntervalSeconds'] = self.backup_log_interval_seconds

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

        if self.backup_storage_encrypt_method is not None:
            result['BackupStorageEncryptMethod'] = self.backup_storage_encrypt_method

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

        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period

        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.enable_mysql_physical_backup_binlog is not None:
            result['EnableMysqlPhysicalBackupBinlog'] = self.enable_mysql_physical_backup_binlog

        if self.enable_source_endpoint_ssl is not None:
            result['EnableSourceEndpointSsl'] = self.enable_source_endpoint_ssl

        if self.ossbucket_name is not None:
            result['OSSBucketName'] = self.ossbucket_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if self.source_endpoint_oracle_home is not None:
            result['SourceEndpointOracleHome'] = self.source_endpoint_oracle_home

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

        if self.ssl_ca_pem is not None:
            result['SslCaPem'] = self.ssl_ca_pem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStartBackup') is not None:
            self.auto_start_backup = m.get('AutoStartBackup')

        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('BackupLogIntervalSeconds') is not None:
            self.backup_log_interval_seconds = m.get('BackupLogIntervalSeconds')

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

        if m.get('BackupStorageEncryptMethod') is not None:
            self.backup_storage_encrypt_method = m.get('BackupStorageEncryptMethod')

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

        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')

        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('EnableMysqlPhysicalBackupBinlog') is not None:
            self.enable_mysql_physical_backup_binlog = m.get('EnableMysqlPhysicalBackupBinlog')

        if m.get('EnableSourceEndpointSsl') is not None:
            self.enable_source_endpoint_ssl = m.get('EnableSourceEndpointSsl')

        if m.get('OSSBucketName') is not None:
            self.ossbucket_name = m.get('OSSBucketName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

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

        if m.get('SourceEndpointOracleHome') is not None:
            self.source_endpoint_oracle_home = m.get('SourceEndpointOracleHome')

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

        if m.get('SslCaPem') is not None:
            self.ssl_ca_pem = m.get('SslCaPem')

        return self


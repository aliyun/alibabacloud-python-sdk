# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ConfigureBackupPlanRequest(TeaModel):
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
        backup_storage_type: str = None,
        backup_strategy_type: str = None,
        client_token: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        duplication_archive_period: int = None,
        duplication_infrequent_access_period: int = None,
        enable_backup_log: bool = None,
        ossbucket_name: str = None,
        owner_id: str = None,
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
    ):
        # Specifies whether to enable the automatic backup feature.
        # 
        # *   **true**: enables the automatic backup feature.
        # *   **false**: disables the automatic backup feature.
        self.auto_start_backup = auto_start_backup
        # The backup gateway ID. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain it.
        # 
        # >  If you set **SourceEndpointInstanceType** to **Agent**, this parameter is required.
        self.backup_gateway_id = backup_gateway_id
        # The interval at which you want to perform incremental log backups. Unit: seconds.
        # 
        # >  Only physical backup supports this parameter.
        self.backup_log_interval_seconds = backup_log_interval_seconds
        # The objects to be backed up. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the objects.
        self.backup_objects = backup_objects
        # The day of each week when the full backup task runs. Valid values:
        # 
        # *   **Monday**\
        # *   **Tuesday**\
        # *   **Wednesday**\
        # *   **Thursday**\
        # *   **Friday**\
        # *   **Saturday**\
        # *   **Sunday**\
        self.backup_period = backup_period
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain it.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The name of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the name.
        # 
        # This parameter is required.
        self.backup_plan_name = backup_plan_name
        # The network bandwidth throttling. Unit: KB/s. DBS allows a maximum bandwidth of 10 GB/s.
        # 
        # > This parameter takes effect only when physical backups for MySQL databases are performed.
        self.backup_rate_limit = backup_rate_limit
        # The number of days for which the backup data is retained. Valid values: 0 to 1825. Default value: 730.
        self.backup_retention_period = backup_retention_period
        # The disk I/O limit. Unit: KB/s.
        # 
        # >  This parameter takes effect only during the physical backup of a MySQL database.
        self.backup_speed_limit = backup_speed_limit
        # The start time of the full backup. Specify the time in the *HH:mm*Z format. The time must be in UTC. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the start time of full backup tasks.
        self.backup_start_time = backup_start_time
        # The storage type. Valid values:
        # 
        # *   Empty: If you do not specify this parameter, the system stores backup data in your OSS bucket.
        # *   system: The system stores backup data in the built-in OSS bucket of DBS.
        self.backup_storage_type = backup_storage_type
        # The backup method that you want to use for full backups. Valid values:
        # 
        # *   **simple**: scheduled backup. If you specify this value for the BackupStrategyType parameter, you must also specify the BackupPeriod and BackupStartTime parameters.
        # *   **Manual**: manual backup.
        # 
        # > Default value: **simple**.
        self.backup_strategy_type = backup_strategy_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The unique ID (UID) of the Alibaba Cloud account to which the backup schedule belongs. You can call the [DescribeRestoreTaskList](https://help.aliyun.com/document_detail/2869838.html) operation to obtain the UID.
        self.cross_aliyun_id = cross_aliyun_id
        # The name of the RAM role that is used to perform backup across Alibaba Cloud accounts. You can call the [DescribeRestoreTaskList](https://help.aliyun.com/document_detail/2869838.html) operation to obtain the RAM role.
        self.cross_role_name = cross_role_name
        # The number of days after which the storage class of the backup data is changed to Archive. Default value: 365.
        self.duplication_archive_period = duplication_archive_period
        # The number of days after which the storage class of the backup data is changed to Infrequent Access (IA). Default value: 180.
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        # Specifies whether to enable the incremental log backup feature. Valid values:
        # 
        # *   **true**: enables the incremental log backup feature.
        # *   **false**: disables the incremental log backup feature.
        self.enable_backup_log = enable_backup_log
        # The name of the OSS bucket.
        # 
        # >  By default, the system automatically generates an OSS bucket name.
        self.ossbucket_name = ossbucket_name
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The source database name. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain it.
        # 
        # >  If the source database runs the **PostgreSQL** database engine or **MongoDB** database engine, this parameter is required.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The source database endpoint. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain it.
        # 
        # >  If you set **SourceEndpointInstanceType** to **Express**, **Agent**, or **Other**, this parameter is required.
        self.source_endpoint_ip = source_endpoint_ip
        # The database instance ID. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the ID.
        # 
        # >  If you set **SourceEndpoint****InstanceType** to **RDS**, **ECS**, **DDS**, or **Express**, this parameter is required.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The location of the database. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the location. Valid values:
        # 
        # *   **RDS**\
        # *   **ECS**\
        # *   **Express**: The database is connected to Database Backup (DBS) via Express Connect, VPN Gateway, or Smart Access Gateway.
        # *   **Agent**: The database is connected over a DBS backup gateway.
        # *   **DDS**: The database is an ApsaraDB for MongoDB database.
        # *   **Other**: The database is connected to DBS by using the IP address and port of the database.
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The system ID (SID) of the Oracle database.
        # 
        # > This parameter is required if the database is an Oracle database.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The password of the account that is used to connect to the database.
        # 
        # > This parameter is required except that the database is an **SQL Server** database that is connected to DBS over a DBS backup gateway or a **Redis** database.
        self.source_endpoint_password = source_endpoint_password
        # The port that is used to connect to the source database. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the port.
        # 
        # >  If you set **SourceEndpoint****InstanceType** to **Express**, **Agent**, **Other**, or **ECS**, this parameter is required.
        self.source_endpoint_port = source_endpoint_port
        # The region in which the source database resides. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the region.
        # 
        # >  If you set **SourceEndpointInstanceType** to RDS, ECS, DDS, Express, or Agent, this parameter is required.
        self.source_endpoint_region = source_endpoint_region
        # The username of the account that is used to connect to the database.
        # 
        # > This parameter is required except that the database is an **SQL Server** database that is connected to DBS over a DBS backup gateway or a **Redis** database.
        self.source_endpoint_user_name = source_endpoint_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        return self


class ConfigureBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigureBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConfigureBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAndStartBackupPlanRequest(TeaModel):
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
        # The backup gateway ID.
        # 
        # > 
        # 
        # *   If **SourceEndpointInstanceType** is set to **Agent**, this parameter is required.****\
        # 
        # *   For more information about how to install a backup gateway, see [Install a backup gateway](https://help.aliyun.com/document_detail/93250.html).
        # 
        # *   You can query a list of existing backup gateways by calling the [DescribeBackupGatewayList](https://help.aliyun.com/document_detail/2869840.html) operation.
        self.backup_gateway_id = backup_gateway_id
        # The interval at which you want to perform incremental log backups. Unit: seconds.
        # 
        # >  This parameter is required only if you set BackupMethod to **physical**.
        self.backup_log_interval_seconds = backup_log_interval_seconds
        # The method that is used to generate the backup file. Valid values:
        # 
        # *   **logical**: logical backup
        # *   **physical**: physical backup
        # *   **duplication**: dump backup
        # 
        # This parameter is required.
        self.backup_method = backup_method
        # The object to be backed up.
        self.backup_objects = backup_objects
        # The day of the week on which you want to perform full backup. Valid values:
        # 
        # *   **Monday**\
        # *   **Tuesday**\
        # *   **Wednesday**\
        # *   **Thursday**\
        # *   **Friday**\
        # *   **Saturday**\
        # *   **Sunday**\
        # 
        # >  You can specify multiple values. Separate multiple values with commas (,).
        self.backup_period = backup_period
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The name of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_name = backup_plan_name
        # The network bandwidth throttling. Unit: KB/s. DBS allows a maximum bandwidth of 10 GB/s.
        # 
        # >  This parameter takes effect only when physical backups for MySQL databases are performed.
        self.backup_rate_limit = backup_rate_limit
        # The number of days for which the backup data is retained. Valid values: 0 to 1825. Default value: 730.
        self.backup_retention_period = backup_retention_period
        # The I/O limit for the disk. Unit: KB/s.
        # 
        # >  This parameter takes effect only when physical backups for MySQL databases are performed.
        self.backup_speed_limit = backup_speed_limit
        # The start time of full backup tasks. Specify the value in the *HH:mm* format. The time must be in UTC.
        self.backup_start_time = backup_start_time
        # The storage type. Valid values:
        # 
        # *   Empty: If you do not specify this parameter, the system stores backup data in your OSS bucket.
        # *   system : The system stores backup data in the built-in OSS bucket of DBS.
        self.backup_storage_type = backup_storage_type
        # The backup method that you want to use for full backups. Valid values:
        # 
        # *   **simple**: scheduled backup. If you specify this value for the BackupStrategyType parameter, you must also specify the BackupPeriod and BackupStartTime parameters.
        # *   **Manual**: manual backup.
        # 
        # > Default value: **simple**.
        self.backup_strategy_type = backup_strategy_type
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The unique ID (UID) of the Alibaba Cloud account to which the source database belongs.
        self.cross_aliyun_id = cross_aliyun_id
        # The name of the RAM role that is used to perform backups across Alibaba Cloud accounts.
        self.cross_role_name = cross_role_name
        # The region in which the database that you want to back up resides.
        # 
        # > This parameter is required if the **PayType** parameter is set to **postpay**.
        self.database_region = database_region
        # The type of the source database. Valid values:
        # 
        # *   **MySQL**\
        # *   **MSSQL**\
        # *   **Oracle**\
        # *   **MariaDB**\
        # *   **PostgreSQL**\
        # *   **DRDS**\
        # *   **MongoDB**\
        # *   **Redis**\
        # 
        # This parameter is required.
        self.database_type = database_type
        # The number of days after which the storage class of the backup data is changed to Archive. Default value: 365.
        self.duplication_archive_period = duplication_archive_period
        # The number of days after which the storage class of the backup data is changed to Infrequent Access (IA). Default value: 180.
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        # Specifies whether to enable the incremental log backup feature. Valid values:
        # 
        # *   **true**: enables the incremental log backup feature.
        # *   **false**: disables the incremental log backup feature.
        self.enable_backup_log = enable_backup_log
        # The request source. Default value: OpenApi. You do not need to set this parameter.
        self.from_app = from_app
        # The type of the backup schedule. Valid values:
        # 
        # *   **micro**\
        # *   **small**\
        # *   **medium**\
        # *   **large**\
        # *   **xlarge**\
        # 
        # >  A backup schedule type with higher specifications offers higher backup and restoration performance. For more information, see [Select a backup schedule type](https://help.aliyun.com/document_detail/84372.html).
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The type of the source database instance. Valid values:
        # 
        # *   **RDS**: ApsaraDB RDS.
        # *   **PolarDB**: PolarDB.
        # *   **DDS**: ApsaraDB for MongoDB.
        # *   **Kvstore**: ApsaraDB for Redis.
        # *   **Other**: Database connected by using an IP address and a port number.
        # *   **dg**: Self-managed database that has no public IP address or port number and is connected over Database Gateway.
        # 
        # >  If **PayType** is set to **postpay**, this parameter is required.
        self.instance_type = instance_type
        # The name of the Object Storage Service (OSS) bucket used to store backup files. By default, the system automatically generates a name for the OSS bucket.
        self.ossbucket_name = ossbucket_name
        self.owner_id = owner_id
        # The billing method. Valid values:
        # 
        # *   **postpay**: pay-as-you-go.
        # *   **prepay**: subscription.
        # 
        # >  The default value is **prepay**. You can set this parameter to **postpay** only if you set **BackupMethod** to **duplication**.
        self.pay_type = pay_type
        # Specifies whether to use yearly subscription or monthly subscription for the instance. Valid values:
        # 
        # *   **Year**: yearly subscription
        # *   **Month**: monthly subscription
        self.period = period
        # The ID of the region in which you want to store the backup data. You can query the supported regions of DBS by calling the [DescribeRegions](https://help.aliyun.com/document_detail/2869853.html) operation.
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the database.
        # 
        # > This parameter is required if the DatabaseType parameter is set to **PostgreSQL** or **MongoDB**.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The endpoint of the database.
        # 
        # > This parameter is required if the **SourceEndpointInstanceType** parameter is set to **Express**, **Agent**, or **Other**.
        self.source_endpoint_ip = source_endpoint_ip
        # The ID of the database instance.
        # 
        # > This parameter is required if the **SourceEndpointInstanceType** parameter is set to **RDS**, **ECS**, **DDS**, or **Express**.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The location of the source database. Valid values:
        # 
        # *   **RDS**: The database is on an ApsaraDB RDS instance.
        # *   **ECS**: The database is on an Elastic Compute Service (ECS) instance.
        # *   **Express**: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway.
        # *   **Agent**: The database is connected to DBS over a DBS backup gateway.
        # *   **DDS**: The database is on an ApsaraDB for MongoDB instance.
        # *   **Other**: The database is connected to DBS by using an IP address and a port number.
        # *   **dg**: The database is a self-managed database that has no public IP address or port number and is connected to DBS over Database Gateway.
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The system ID (SID) of the Oracle database. This parameter is required if the source database is an Oracle database.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The password of the account that is used to connect to the database.
        # 
        # > This parameter is required except that the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database.
        self.source_endpoint_password = source_endpoint_password
        # The port of the database.
        # 
        # > This parameter is required if the **SourceEndpointInstanceType** parameter is set to **Express**, **Agent**, **Other**, or **ECS**.
        self.source_endpoint_port = source_endpoint_port
        # The region in which the database that you want to back up resides.
        # 
        # > This parameter is required if the **SourceEndpointInstanceType** parameter is set to **RDS**, **ECS**, **DDS**, **Express**, or **Agent**.
        self.source_endpoint_region = source_endpoint_region
        # The username of the account that is used to connect to the database.
        # 
        # > This parameter is required except that the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database.
        self.source_endpoint_user_name = source_endpoint_user_name
        # The region in which you want to store the backup data.
        # 
        # > This parameter is required if the **PayType** parameter is set to **postpay**.
        self.storage_region = storage_region
        # This parameter is unavailable.
        self.storage_type = storage_type
        # The subscription duration. Valid values:
        # 
        # *   If **Period** is set to **Year**, the valid values of **UsedTime** range from 1 to 5.
        # *   If **Period** is set to **Month**, the valid values of **UsedTime** range from 1 to 11.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateAndStartBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        create_backup_set: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backup schedule ID.
        self.backup_plan_id = backup_plan_id
        # Indicates whether a backup is performed immediately after the backup schedule is configured. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.create_backup_set = create_backup_set
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.create_backup_set is not None:
            result['CreateBackupSet'] = self.create_backup_set
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('CreateBackupSet') is not None:
            self.create_backup_set = m.get('CreateBackupSet')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAndStartBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAndStartBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAndStartBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPlanRequest(TeaModel):
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
        # The backup method of the backup schedule. Valid values:
        # 
        # *   **logical**: logical backup
        # *   **physical**: physical backup
        # *   **duplication**: dump backup
        # 
        # This parameter is required.
        self.backup_method = backup_method
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The region in which the database you want to back up resides.
        # 
        # > This parameter is required if the **PayType** parameter is set to **postpay**.
        self.database_region = database_region
        # The type of the source database. Valid values:
        # 
        # *   **MySQL**\
        # *   **MSSQL**\
        # *   **Oracle**\
        # *   **MariaDB**\
        # *   **PostgreSQL**\
        # *   **DRDS**\
        # *   **MongoDB**\
        # *   **Redis**\
        # 
        # This parameter is required.
        self.database_type = database_type
        # The source of the request. The default value is OpenAPI and cannot be changed.
        self.from_app = from_app
        # The type of the backup schedule. Valid values:
        # 
        # *   **micro**\
        # *   **small**\
        # *   **medium**\
        # *   **large**\
        # *   **xlarge**\
        # 
        # >  A backup schedule type with higher specifications offers higher backup and restoration performance. For more information, see [Select a backup schedule type](https://help.aliyun.com/document_detail/84372.html).
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The type of the source database instance. Valid values:
        # 
        # *   **RDS**: ApsaraDB RDS.
        # *   **PolarDB**: PolarDB.
        # *   **DDS**: ApsaraDB for MongoDB.
        # *   **Kvstore**: ApsaraDB for Redis.
        # *   **Other**: Database connected by using an IP address and a port number.
        # *   **dg**: Self-managed database that has no public IP address or port number and is connected over Database Gateway.
        # 
        # >  If **PayType** is set to **postpay**, this parameter is required.
        self.instance_type = instance_type
        self.owner_id = owner_id
        # The billing method of the backup schedule. Valid values:
        # 
        # *   **postpay**: pay-as-you-go
        # *   **prepay**: subscription
        # 
        # > The default value is **prepay**. If the **BackupMethod** parameter is set to **duplication**, **postpay** is supported.
        self.pay_type = pay_type
        # The unit of the subscription period. Valid values:
        # 
        # *   **Year**: yearly subscription
        # *   **Month**: monthly subscription
        self.period = period
        # The ID of the region in which you can activate Data Disaster Recovery. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/2869853.html) operation to query the regions supported by Data Disaster Recovery.
        # 
        # >  For more information, see [Endpoints](https://help.aliyun.com/document_detail/2869810.html).
        self.region = region
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The region in which you want to store the backup data.
        # 
        # > This parameter is required if the **PayType** parameter is set to **postpay**.
        self.storage_region = storage_region
        # This parameter is unavailable.
        self.storage_type = storage_type
        # The subscription period. Valid values:
        # 
        # *   If **Period** is set to **Year**, the valid values of **UsedTime** range from 1 to 5.
        # *   If **Period** is set to **Month**, the valid values of **UsedTime** range from 1 to 11.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFullBackupSetDownloadRequest(TeaModel):
    def __init__(
        self,
        backup_set_data_format: str = None,
        backup_set_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The format in which the full backup set is downloaded. Valid values:
        # 
        # *   **Native**\
        # *   **SQL**\
        # *   **CSV**(Default value)
        # *   **JSON**\
        self.backup_set_data_format = backup_set_data_format
        # The ID of the full backup set.
        # 
        # This parameter is required.
        self.backup_set_id = backup_set_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_data_format is not None:
            result['BackupSetDataFormat'] = self.backup_set_data_format
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetDataFormat') is not None:
            self.backup_set_data_format = m.get('BackupSetDataFormat')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateFullBackupSetDownloadResponseBody(TeaModel):
    def __init__(
        self,
        backup_set_download_task_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup set download task.
        self.backup_set_download_task_id = backup_set_download_task_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFullBackupSetDownloadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFullBackupSetDownloadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFullBackupSetDownloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGetDBListFromAgentTaskRequest(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        client_token: str = None,
        database_type: str = None,
        owner_id: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_port: int = None,
        source_endpoint_region: str = None,
    ):
        # The ID of the backup gateway. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to query the ID.
        # 
        # >  This parameter is required.
        self.backup_gateway_id = backup_gateway_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The type of the database. Valid values:
        # 
        # *   **MySQL**\
        # *   **MSSQL**\
        # *   **Oracle**\
        # *   **MariaDB**\
        # *   **PostgreSQL**\
        # *   **DRDS**\
        # *   **MongoDB**\
        # *   **Redis**\
        self.database_type = database_type
        self.owner_id = owner_id
        # The URL that is used to access the database.
        self.source_endpoint_ip = source_endpoint_ip
        # The port that is used to connect to the database.
        self.source_endpoint_port = source_endpoint_port
        # The region in which the backup gateway resides.
        self.source_endpoint_region = source_endpoint_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        return self


class CreateGetDBListFromAgentTaskResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        task_id: int = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The ID of the asynchronous task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateGetDBListFromAgentTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGetDBListFromAgentTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGetDBListFromAgentTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIncrementBackupSetDownloadRequest(TeaModel):
    def __init__(
        self,
        backup_set_data_format: str = None,
        backup_set_id: str = None,
        backup_set_name: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The format in which the incremental backup set is downloaded. Valid values:
        # 
        # *   **Native**\
        # *   **SQL**\
        # *   **CSV**\
        # *   **JSON**\
        # 
        # > Default value: Native.
        self.backup_set_data_format = backup_set_data_format
        # The ID of the incremental backup task. To obtain the task ID, you can call the [DescribeIncrementBackupList](https://help.aliyun.com/document_detail/2869833.html) operation and view the value of the **BackupSetJobId** parameter in the response.
        # 
        # This parameter is required.
        self.backup_set_id = backup_set_id
        # The ID of the incremental backup set. To obtain the backup set ID, you can call the [DescribeIncrementBackupList](https://help.aliyun.com/document_detail/2869833.html) operation and view the value of the **BackupSetId** parameter in the response.
        # 
        # This parameter is required.
        self.backup_set_name = backup_set_name
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_data_format is not None:
            result['BackupSetDataFormat'] = self.backup_set_data_format
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_set_name is not None:
            result['BackupSetName'] = self.backup_set_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetDataFormat') is not None:
            self.backup_set_data_format = m.get('BackupSetDataFormat')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSetName') is not None:
            self.backup_set_name = m.get('BackupSetName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateIncrementBackupSetDownloadResponseBody(TeaModel):
    def __init__(
        self,
        backup_set_download_task_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup set download task.
        self.backup_set_download_task_id = backup_set_download_task_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateIncrementBackupSetDownloadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIncrementBackupSetDownloadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIncrementBackupSetDownloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRestoreTaskRequest(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_plan_id: str = None,
        backup_set_id: str = None,
        client_token: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_password: str = None,
        destination_endpoint_port: int = None,
        destination_endpoint_region: str = None,
        destination_endpoint_user_name: str = None,
        duplicate_conflict: str = None,
        owner_id: str = None,
        restore_dir: str = None,
        restore_home: str = None,
        restore_objects: str = None,
        restore_task_name: str = None,
        restore_time: int = None,
    ):
        # The ID of the backup gateway.
        # 
        # > This parameter is required if the DestinationEndpointInstanceType parameter is set to Agent.
        self.backup_gateway_id = backup_gateway_id
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The ID of the full backup set.
        self.backup_set_id = backup_set_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The unique ID (UID) of the Alibaba Cloud account to which the source database belongs.
        self.cross_aliyun_id = cross_aliyun_id
        # The name of the RAM role that is used to perform backups across Alibaba Cloud accounts.
        self.cross_role_name = cross_role_name
        # The name of the database.
        # 
        # 
        # 
        # > This parameter is required if the database is a PostgreSQL database or a MongoDB database.
        self.destination_endpoint_database_name = destination_endpoint_database_name
        # The endpoint that is used to connect to the database.
        # 
        # > This parameter is required if the DestinationEndpointInstanceType parameter is set to Express, Agent, or Other.
        self.destination_endpoint_ip = destination_endpoint_ip
        # The ID of the database instance.
        # 
        # > This parameter is required if the DestinationEndpointInstanceType parameter is set to RDS, ECS, DDS, or Express.
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        # The location of the database. Valid values:
        # 
        # *   **RDS**: The database is deployed on an ApsaraDB RDS instance.
        # *   **ECS**: The database is deployed on an Elastic Compute Service (ECS) instance.
        # *   **Express**: The database is connected to Database Backup (DBS) by using Express Connect, VPN Gateway, or Smart Access Gateway.
        # *   **Agent**: The database is connected over a DBS backup gateway.
        # *   **DDS**: The database is an ApsaraDB for MongoDB database.
        # *   **Other**: The database is connected to DBS by using the IP address and port of the database.
        # *   **dg**: The database is a self-managed database that does not have public IP addresses or port numbers and is connected to DBS over Database Gateway.
        # 
        # This parameter is required.
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        # The system ID (SID) of the Oracle database.
        # 
        # 
        # 
        # > This parameter is required if the source database is an Oracle database.
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        # The password of the account that is used to connect to the source database.
        # 
        # 
        # 
        # > This parameter is required except that the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database.
        self.destination_endpoint_password = destination_endpoint_password
        # The port of the database.
        # > This parameter is required if the DestinationEndpointInstanceType parameter is set to Express, Agent, Other, or ECS.
        self.destination_endpoint_port = destination_endpoint_port
        # The region ID of the destination database instance.
        # 
        # >  You must specify this parameter if **DestinationEndpointInstanceType** is set to RDS, ECS, DDS, Express, or Agent.
        self.destination_endpoint_region = destination_endpoint_region
        # The username of the account that is used to connect to the database.
        # 
        # 
        # > This parameter is required except that the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database.
        self.destination_endpoint_user_name = destination_endpoint_user_name
        # The method of processing objects with the same name. Valid values:
        # 
        # - failure: The restore task fails if the system detects objects with the same name. This is the default value.
        # - renamenew: The restore task renames objects with the same name starting from the second occurrence.
        self.duplicate_conflict = duplicate_conflict
        self.owner_id = owner_id
        # This parameter is required if the DestinationEndpointInstanceType parameter is set to Agent and the backup object of the backup schedule is a MySQL database.
        self.restore_dir = restore_dir
        # The program directory of the database.
        self.restore_home = restore_home
        # The objects to be restored.
        # 
        # 
        # 
        # > This parameter is required except that the DestinationEndpointInstanceType parameter is set to Agent. For information about the parameter definition, see RestoreObjects.
        self.restore_objects = restore_objects
        # The name of the restore task.
        # 
        # This parameter is required.
        self.restore_task_name = restore_task_name
        # The time to run the restore task, such as 1554560477000.
        self.restore_time = restore_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name
        if self.destination_endpoint_ip is not None:
            result['DestinationEndpointIP'] = self.destination_endpoint_ip
        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id
        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type
        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid
        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password
        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name
        if self.duplicate_conflict is not None:
            result['DuplicateConflict'] = self.duplicate_conflict
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.restore_dir is not None:
            result['RestoreDir'] = self.restore_dir
        if self.restore_home is not None:
            result['RestoreHome'] = self.restore_home
        if self.restore_objects is not None:
            result['RestoreObjects'] = self.restore_objects
        if self.restore_task_name is not None:
            result['RestoreTaskName'] = self.restore_task_name
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')
        if m.get('DestinationEndpointIP') is not None:
            self.destination_endpoint_ip = m.get('DestinationEndpointIP')
        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')
        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')
        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')
        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')
        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')
        if m.get('DuplicateConflict') is not None:
            self.duplicate_conflict = m.get('DuplicateConflict')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RestoreDir') is not None:
            self.restore_dir = m.get('RestoreDir')
        if m.get('RestoreHome') is not None:
            self.restore_home = m.get('RestoreHome')
        if m.get('RestoreObjects') is not None:
            self.restore_objects = m.get('RestoreObjects')
        if m.get('RestoreTaskName') is not None:
            self.restore_task_name = m.get('RestoreTaskName')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        return self


class CreateRestoreTaskResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        restore_task_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # The ID of the restore task.
        self.restore_task_id = restore_task_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRestoreTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRestoreTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRestoreTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupGatewayListRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        identifier: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The unique identifier of the backup gateway. You can query multiple backup gateways. Separate multiple identifiers with commas (,).
        self.identifier = identifier
        self.owner_id = owner_id
        # The number of the page to return. The value must be a positive integer. Default value: 0.
        self.page_num = page_num
        # The number of entries to return on each page. Valid values:
        # 
        # *   **30**\
        # *   **50**\
        # *   **100**\
        # 
        # > Default value: 30.
        self.page_size = page_size
        # The region in which Database Backup (DBS) is activated. Valid values:
        # 
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-qingdao**: China (Qingdao)
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        # *   **ap-southeast-1**: Singapore (Singapore)
        # *   **cn-hangzhou-finance**: China East 1 Finance
        # *   **cn-shanghai-finance**: China East 2 Finance
        # *   **cn-shenzhen-finance**: China South 1 Finance
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeBackupGatewayListResponseBodyItemsBackupGateway(TeaModel):
    def __init__(
        self,
        backup_gateway_create_time: int = None,
        backup_gateway_id: str = None,
        backup_gateway_status: str = None,
        display_name: str = None,
        identifier: str = None,
        last_heartbeat_time: int = None,
        region: str = None,
        source_endpoint_hostname: str = None,
        source_endpoint_internet_ip: str = None,
        source_endpoint_intranet_ip: str = None,
    ):
        # The time when the backup gateway was created, such as 1554560477000.
        self.backup_gateway_create_time = backup_gateway_create_time
        # The ID of the backup gateway.
        self.backup_gateway_id = backup_gateway_id
        # The status of the backup gateway. Valid values:
        # 
        # *   ONLINE: The backup gateway is online.
        # *   OFFLINE: The backup gateway is offline.
        # *   STOPPED: The backup gateway is stopped.
        # *   UPGRADING: The backup gateway is being upgraded.
        self.backup_gateway_status = backup_gateway_status
        # The display name of the backup gateway.
        self.display_name = display_name
        # The unique identifier of the backup gateway.
        self.identifier = identifier
        # The last time when a heartbeat message was sent, such as 1554560477000.
        self.last_heartbeat_time = last_heartbeat_time
        # The ID of the region.
        self.region = region
        # The name of the host on which the backup gateway is installed.
        self.source_endpoint_hostname = source_endpoint_hostname
        # The public IP address of the host on which the backup gateway is installed.
        self.source_endpoint_internet_ip = source_endpoint_internet_ip
        # The private IP address of the host on which the backup gateway is installed.
        self.source_endpoint_intranet_ip = source_endpoint_intranet_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_create_time is not None:
            result['BackupGatewayCreateTime'] = self.backup_gateway_create_time
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_gateway_status is not None:
            result['BackupGatewayStatus'] = self.backup_gateway_status
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.last_heartbeat_time is not None:
            result['LastHeartbeatTime'] = self.last_heartbeat_time
        if self.region is not None:
            result['Region'] = self.region
        if self.source_endpoint_hostname is not None:
            result['SourceEndpointHostname'] = self.source_endpoint_hostname
        if self.source_endpoint_internet_ip is not None:
            result['SourceEndpointInternetIP'] = self.source_endpoint_internet_ip
        if self.source_endpoint_intranet_ip is not None:
            result['SourceEndpointIntranetIP'] = self.source_endpoint_intranet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayCreateTime') is not None:
            self.backup_gateway_create_time = m.get('BackupGatewayCreateTime')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupGatewayStatus') is not None:
            self.backup_gateway_status = m.get('BackupGatewayStatus')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('LastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('LastHeartbeatTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SourceEndpointHostname') is not None:
            self.source_endpoint_hostname = m.get('SourceEndpointHostname')
        if m.get('SourceEndpointInternetIP') is not None:
            self.source_endpoint_internet_ip = m.get('SourceEndpointInternetIP')
        if m.get('SourceEndpointIntranetIP') is not None:
            self.source_endpoint_intranet_ip = m.get('SourceEndpointIntranetIP')
        return self


class DescribeBackupGatewayListResponseBodyItems(TeaModel):
    def __init__(
        self,
        backup_gateway: List[DescribeBackupGatewayListResponseBodyItemsBackupGateway] = None,
    ):
        self.backup_gateway = backup_gateway

    def validate(self):
        if self.backup_gateway:
            for k in self.backup_gateway:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupGateway'] = []
        if self.backup_gateway is not None:
            for k in self.backup_gateway:
                result['BackupGateway'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_gateway = []
        if m.get('BackupGateway') is not None:
            for k in m.get('BackupGateway'):
                temp_model = DescribeBackupGatewayListResponseBodyItemsBackupGateway()
                self.backup_gateway.append(temp_model.from_map(k))
        return self


class DescribeBackupGatewayListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: DescribeBackupGatewayListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of backup gateways.
        self.items = items
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of backup gateways.
        self.total_elements = total_elements
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribeBackupGatewayListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeBackupGatewayListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupGatewayListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupGatewayListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlanBillingRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        show_storage_type: bool = None,
    ):
        # The ID of the backup gateway.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.owner_id = owner_id
        # Indicates whether the storage type is displayed.
        self.show_storage_type = show_storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.show_storage_type is not None:
            result['ShowStorageType'] = self.show_storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ShowStorageType') is not None:
            self.show_storage_type = m.get('ShowStorageType')
        return self


class DescribeBackupPlanBillingResponseBodyItem(TeaModel):
    def __init__(
        self,
        buy_charge_type: str = None,
        buy_create_timestamp: int = None,
        buy_expired_timestamp: int = None,
        buy_spec: str = None,
        cont_storage_size: int = None,
        full_storage_size: int = None,
        is_expired: bool = None,
        is_free_bytes_unlimited: bool = None,
        paied_bytes: int = None,
        quota_end_timestamp: int = None,
        quota_start_timestamp: int = None,
        total_free_bytes: int = None,
        used_full_bytes: int = None,
        used_increment_bytes: int = None,
    ):
        # The billing method. Valid values:
        # 
        # *   PREPAY
        # *   POSTPAY
        self.buy_charge_type = buy_charge_type
        # The timestamp that indicates when the instance was purchased.
        self.buy_create_timestamp = buy_create_timestamp
        # The timestamp that indicates when the instance expires.
        # 
        # > This parameter is available only if the value of the BuyChargeType parameter is PREPAY.
        self.buy_expired_timestamp = buy_expired_timestamp
        # The specifications of the instance.
        self.buy_spec = buy_spec
        # The size of the built-in storage for storing incremental backup data.
        self.cont_storage_size = cont_storage_size
        # The size of the built-in storage for storing full backup data.
        self.full_storage_size = full_storage_size
        # Indicates whether the instance expired.
        # 
        # > This parameter is available only if the value of the BuyChargeType parameter is PREPAY.
        self.is_expired = is_expired
        # Indicates whether the instance has no backup traffic limit.
        self.is_free_bytes_unlimited = is_free_bytes_unlimited
        # The total paid backup traffic in the current month.
        self.paied_bytes = paied_bytes
        # The timestamp that indicates when the billing cycle of free backup traffic ends.
        self.quota_end_timestamp = quota_end_timestamp
        # The timestamp that indicates when the billing cycle of free backup traffic starts.
        self.quota_start_timestamp = quota_start_timestamp
        # The total free backup traffic in the current month.
        # 
        # > This parameter is available only if the value of the BuyChargeType parameter is PREPAY and the value of the IsFreeBytesUnlimited parameter is false.
        self.total_free_bytes = total_free_bytes
        # The paid full backup traffic in the current month.
        self.used_full_bytes = used_full_bytes
        # The paid incremental backup traffic in the current month.
        self.used_increment_bytes = used_increment_bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_charge_type is not None:
            result['BuyChargeType'] = self.buy_charge_type
        if self.buy_create_timestamp is not None:
            result['BuyCreateTimestamp'] = self.buy_create_timestamp
        if self.buy_expired_timestamp is not None:
            result['BuyExpiredTimestamp'] = self.buy_expired_timestamp
        if self.buy_spec is not None:
            result['BuySpec'] = self.buy_spec
        if self.cont_storage_size is not None:
            result['ContStorageSize'] = self.cont_storage_size
        if self.full_storage_size is not None:
            result['FullStorageSize'] = self.full_storage_size
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.is_free_bytes_unlimited is not None:
            result['IsFreeBytesUnlimited'] = self.is_free_bytes_unlimited
        if self.paied_bytes is not None:
            result['PaiedBytes'] = self.paied_bytes
        if self.quota_end_timestamp is not None:
            result['QuotaEndTimestamp'] = self.quota_end_timestamp
        if self.quota_start_timestamp is not None:
            result['QuotaStartTimestamp'] = self.quota_start_timestamp
        if self.total_free_bytes is not None:
            result['TotalFreeBytes'] = self.total_free_bytes
        if self.used_full_bytes is not None:
            result['UsedFullBytes'] = self.used_full_bytes
        if self.used_increment_bytes is not None:
            result['UsedIncrementBytes'] = self.used_increment_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyChargeType') is not None:
            self.buy_charge_type = m.get('BuyChargeType')
        if m.get('BuyCreateTimestamp') is not None:
            self.buy_create_timestamp = m.get('BuyCreateTimestamp')
        if m.get('BuyExpiredTimestamp') is not None:
            self.buy_expired_timestamp = m.get('BuyExpiredTimestamp')
        if m.get('BuySpec') is not None:
            self.buy_spec = m.get('BuySpec')
        if m.get('ContStorageSize') is not None:
            self.cont_storage_size = m.get('ContStorageSize')
        if m.get('FullStorageSize') is not None:
            self.full_storage_size = m.get('FullStorageSize')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('IsFreeBytesUnlimited') is not None:
            self.is_free_bytes_unlimited = m.get('IsFreeBytesUnlimited')
        if m.get('PaiedBytes') is not None:
            self.paied_bytes = m.get('PaiedBytes')
        if m.get('QuotaEndTimestamp') is not None:
            self.quota_end_timestamp = m.get('QuotaEndTimestamp')
        if m.get('QuotaStartTimestamp') is not None:
            self.quota_start_timestamp = m.get('QuotaStartTimestamp')
        if m.get('TotalFreeBytes') is not None:
            self.total_free_bytes = m.get('TotalFreeBytes')
        if m.get('UsedFullBytes') is not None:
            self.used_full_bytes = m.get('UsedFullBytes')
        if m.get('UsedIncrementBytes') is not None:
            self.used_increment_bytes = m.get('UsedIncrementBytes')
        return self


class DescribeBackupPlanBillingResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        item: DescribeBackupPlanBillingResponseBodyItem = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The billing information of the backup schedule.
        self.item = item
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.item is not None:
            result['Item'] = self.item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Item') is not None:
            temp_model = DescribeBackupPlanBillingResponseBodyItem()
            self.item = temp_model.from_map(m['Item'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBackupPlanBillingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPlanBillingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupPlanBillingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlanListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        backup_plan_status: str = None,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the backup schedule. You can query multiple backup schedule IDs. Separate multiple IDs with commas (,).
        self.backup_plan_id = backup_plan_id
        # Backup plan name.
        self.backup_plan_name = backup_plan_name
        # Backup plan status, the values are as follows:
        # 
        # * **wait**: Not configured
        # * **init**: Not started (pre-check failed)
        # * **running**: Running
        # * **stop**: Failed
        # * **pause**: Paused
        # * **locked**: Locked
        # * **check_pass**: Pre-check passed
        self.backup_plan_status = backup_plan_status
        # Used to ensure the idempotence of the request, preventing duplicate submissions.
        self.client_token = client_token
        self.owner_id = owner_id
        # Page number, must be greater than or equal to 0 and not exceed the maximum value of Integer. The default value is 0.
        self.page_num = page_num
        # Number of records per page, the value should be between 1 and 100.
        # 
        # > The default is **30**.
        self.page_size = page_size
        # DBS region, you can view the supported DBS regions by calling the [DescribeRegions](https://help.aliyun.com/document_detail/2869853.html) interface.
        self.region = region
        # Resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name
        if self.backup_plan_status is not None:
            result['BackupPlanStatus'] = self.backup_plan_status
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')
        if m.get('BackupPlanStatus') is not None:
            self.backup_plan_status = m.get('BackupPlanStatus')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeBackupPlanListResponseBodyItemsBackupPlanDetail(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_method: str = None,
        backup_objects: str = None,
        backup_period: str = None,
        backup_plan_create_time: int = None,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        backup_plan_status: str = None,
        backup_retention_period: int = None,
        backup_set_download_dir: str = None,
        backup_set_download_full_data_format: str = None,
        backup_set_download_gateway_id: int = None,
        backup_set_download_increment_data_format: str = None,
        backup_set_download_target_type: str = None,
        backup_start_time: str = None,
        backup_storage_type: str = None,
        begin_timestamp_for_restore: int = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        database_type: str = None,
        duplication_archive_period: int = None,
        duplication_infrequent_access_period: int = None,
        enable_backup_log: bool = None,
        end_timestamp_for_restore: int = None,
        err_message: str = None,
        instance_class: str = None,
        ossbucket_name: str = None,
        ossbucket_region: str = None,
        open_backup_set_auto_download: bool = None,
        resource_group_id: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_ip_port: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
    ):
        # Backup gateway ID.
        self.backup_gateway_id = backup_gateway_id
        # Backup method. The return values are as follows:
        # - **logical**: Logical backup
        # - **physical**: Physical backup
        # - **duplication**: Replication backup
        self.backup_method = backup_method
        # Backup objects.
        self.backup_objects = backup_objects
        # Full backup cycle. The return values are as follows:
        # - **Monday**: Monday
        # - **Tuesday**: Tuesday
        # - **Wednesday**: Wednesday
        # - **Thursday**: Thursday
        # - **Friday**: Friday
        # - **Saturday**: Saturday
        # - **Sunday**: Sunday
        self.backup_period = backup_period
        # Timestamp of the backup plan creation.
        self.backup_plan_create_time = backup_plan_create_time
        # Backup plan ID.
        self.backup_plan_id = backup_plan_id
        # Backup plan name.
        self.backup_plan_name = backup_plan_name
        # Backup plan status. The return values are as follows:
        # - **wait**: Not configured
        # - **init**: Not started (pre-check failed)
        # - **running**: Running
        # - **stop**: Failed
        # - **pause**: Paused
        # - **locked**: Locked
        # - **check_pass**: Pre-check passed
        self.backup_plan_status = backup_plan_status
        # Backup data retention period, with a value range of 0 to 1825 days.
        self.backup_retention_period = backup_retention_period
        # Download server directory of the backup set
        self.backup_set_download_dir = backup_set_download_dir
        # Full data format for backup set download:
        # * **Native**\
        # * **SQL**\
        # * **CSV**\
        # * **JSON**\
        self.backup_set_download_full_data_format = backup_set_download_full_data_format
        # Backup set download backup gateway ID.
        self.backup_set_download_gateway_id = backup_set_download_gateway_id
        # Backup set download full data format:
        # * **Native**\
        # * **SQL**\
        # * **CSV**\
        # * **JSON**\
        self.backup_set_download_increment_data_format = backup_set_download_increment_data_format
        # Backup set download target type.
        # 
        # > The only value is: agent, indicating that the backup gateway is installed.
        self.backup_set_download_target_type = backup_set_download_target_type
        # Full backup start time, in the format HH:mm.
        self.backup_start_time = backup_start_time
        # Built-in storage type. The return values are as follows:
        # 
        # - Empty (default): Backup data is stored on the user\\"s OSS.
        # - system: Backup data is stored on the built-in OSS of DBS.
        self.backup_storage_type = backup_storage_type
        # Start time for the database restore period, with a return value of 1554560477000.
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        # UID for cross-Aliyun account backup.
        self.cross_aliyun_id = cross_aliyun_id
        # RAM role name for cross-Aliyun account backup.
        self.cross_role_name = cross_role_name
        # Database type.
        self.database_type = database_type
        # Time (in days) to convert to archive cold backup storage.
        self.duplication_archive_period = duplication_archive_period
        # Time (in days) to convert to infrequent access storage.
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        # Indicates whether incremental log backup is enabled, with return values as follows:
        # - **true**: Enabled
        # - **false**: Disabled
        self.enable_backup_log = enable_backup_log
        # End time of the database restorable period, in timestamp format.
        self.end_timestamp_for_restore = end_timestamp_for_restore
        # Pre-check task error message.
        self.err_message = err_message
        # Instance class, with return values as follows:
        # 
        # - **micro**: Entry-level
        # - **small**: Low-spec
        # - **medium**: Medium-spec
        # - **large**: High-spec
        # - **xlarge**: High-spec (no traffic limit)
        self.instance_class = instance_class
        # OSS Bucket name.
        self.ossbucket_name = ossbucket_name
        # OSS Bucket region.
        self.ossbucket_region = ossbucket_region
        # Indicates whether the automatic backup set download feature is enabled.
        self.open_backup_set_auto_download = open_backup_set_auto_download
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Database name.
        self.source_endpoint_database_name = source_endpoint_database_name
        # Database instance ID.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # Location of the database, the return values are as follows:
        # - **rds**\
        # - **ecs**\
        # - **express**: Database connected via dedicated line/VPN gateway/smart gateway
        # - **agent**: Database connected via backup gateway
        # - **dds**: Cloud MongoDB
        # - **other**: Database connected directly via IP:Port
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # Database connection address.
        self.source_endpoint_ip_port = source_endpoint_ip_port
        # Oracle SID name.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # Database region.
        self.source_endpoint_region = source_endpoint_region
        # Database username.
        self.source_endpoint_user_name = source_endpoint_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_create_time is not None:
            result['BackupPlanCreateTime'] = self.backup_plan_create_time
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name
        if self.backup_plan_status is not None:
            result['BackupPlanStatus'] = self.backup_plan_status
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.backup_set_download_dir is not None:
            result['BackupSetDownloadDir'] = self.backup_set_download_dir
        if self.backup_set_download_full_data_format is not None:
            result['BackupSetDownloadFullDataFormat'] = self.backup_set_download_full_data_format
        if self.backup_set_download_gateway_id is not None:
            result['BackupSetDownloadGatewayId'] = self.backup_set_download_gateway_id
        if self.backup_set_download_increment_data_format is not None:
            result['BackupSetDownloadIncrementDataFormat'] = self.backup_set_download_increment_data_format
        if self.backup_set_download_target_type is not None:
            result['BackupSetDownloadTargetType'] = self.backup_set_download_target_type
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_storage_type is not None:
            result['BackupStorageType'] = self.backup_storage_type
        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period
        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.ossbucket_name is not None:
            result['OSSBucketName'] = self.ossbucket_name
        if self.ossbucket_region is not None:
            result['OSSBucketRegion'] = self.ossbucket_region
        if self.open_backup_set_auto_download is not None:
            result['OpenBackupSetAutoDownload'] = self.open_backup_set_auto_download
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_ip_port is not None:
            result['SourceEndpointIpPort'] = self.source_endpoint_ip_port
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanCreateTime') is not None:
            self.backup_plan_create_time = m.get('BackupPlanCreateTime')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')
        if m.get('BackupPlanStatus') is not None:
            self.backup_plan_status = m.get('BackupPlanStatus')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('BackupSetDownloadDir') is not None:
            self.backup_set_download_dir = m.get('BackupSetDownloadDir')
        if m.get('BackupSetDownloadFullDataFormat') is not None:
            self.backup_set_download_full_data_format = m.get('BackupSetDownloadFullDataFormat')
        if m.get('BackupSetDownloadGatewayId') is not None:
            self.backup_set_download_gateway_id = m.get('BackupSetDownloadGatewayId')
        if m.get('BackupSetDownloadIncrementDataFormat') is not None:
            self.backup_set_download_increment_data_format = m.get('BackupSetDownloadIncrementDataFormat')
        if m.get('BackupSetDownloadTargetType') is not None:
            self.backup_set_download_target_type = m.get('BackupSetDownloadTargetType')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStorageType') is not None:
            self.backup_storage_type = m.get('BackupStorageType')
        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')
        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('OSSBucketName') is not None:
            self.ossbucket_name = m.get('OSSBucketName')
        if m.get('OSSBucketRegion') is not None:
            self.ossbucket_region = m.get('OSSBucketRegion')
        if m.get('OpenBackupSetAutoDownload') is not None:
            self.open_backup_set_auto_download = m.get('OpenBackupSetAutoDownload')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointIpPort') is not None:
            self.source_endpoint_ip_port = m.get('SourceEndpointIpPort')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        return self


class DescribeBackupPlanListResponseBodyItems(TeaModel):
    def __init__(
        self,
        backup_plan_detail: List[DescribeBackupPlanListResponseBodyItemsBackupPlanDetail] = None,
    ):
        self.backup_plan_detail = backup_plan_detail

    def validate(self):
        if self.backup_plan_detail:
            for k in self.backup_plan_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupPlanDetail'] = []
        if self.backup_plan_detail is not None:
            for k in self.backup_plan_detail:
                result['BackupPlanDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_plan_detail = []
        if m.get('BackupPlanDetail') is not None:
            for k in m.get('BackupPlanDetail'):
                temp_model = DescribeBackupPlanListResponseBodyItemsBackupPlanDetail()
                self.backup_plan_detail.append(temp_model.from_map(k))
        return self


class DescribeBackupPlanListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: DescribeBackupPlanListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # Error code.
        self.err_code = err_code
        # Error message.
        self.err_message = err_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Details of the backup plans.
        self.items = items
        # Page number.
        self.page_num = page_num
        # Number of records per page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Whether the operation was successful.
        self.success = success
        # Total number of backup plans.
        self.total_elements = total_elements
        # Total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribeBackupPlanListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeBackupPlanListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPlanListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupPlanListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupSetDownloadTaskListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_set_download_task_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The backup schedule ID. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the ID.
        # 
        # >  You must configure the **BackupPlanId** or **BackupSetDownloadTaskId** parameter.
        self.backup_plan_id = backup_plan_id
        # The ID of the backup set download task.
        # 
        # *   Full backup set download task: You can call the [CreateFullBackupSetDownload](https://help.aliyun.com/document_detail/2869842.html) operation to create a full backup set download task and obtain the task ID.
        # *   Incremental backup set download task: You can call the [CreateIncrementBackupSetDownload](https://help.aliyun.com/document_detail/2869843.html) operation to create an incremental backup set download task and obtain the task ID.
        self.backup_set_download_task_id = backup_set_download_task_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # The number of the page to return. The value must be a positive integer. Default value: 0.
        self.page_num = page_num
        # The number of entries to return on each page. Valid values: 30, 50, and 100.
        # 
        # > Default value: 30.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeBackupSetDownloadTaskListResponseBodyItemsBackupSetDownloadTaskDetail(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_plan_id: str = None,
        backup_set_code: str = None,
        backup_set_data_format: str = None,
        backup_set_data_size: int = None,
        backup_set_db_type: str = None,
        backup_set_download_create_time: int = None,
        backup_set_download_dir: str = None,
        backup_set_download_finish_time: int = None,
        backup_set_download_internet_url: str = None,
        backup_set_download_intranet_url: str = None,
        backup_set_download_status: str = None,
        backup_set_download_target_type: str = None,
        backup_set_download_task_id: str = None,
        backup_set_download_task_name: str = None,
        backup_set_download_way: str = None,
        backup_set_id: str = None,
        backup_set_job_type: str = None,
        err_message: str = None,
    ):
        # The backup gateway that is used to download the backup set. This parameter is available only if the value of the BackupSetDownloadWay parameter is auto.
        self.backup_gateway_id = backup_gateway_id
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The code of the backup set.
        self.backup_set_code = backup_set_code
        # The format in which the backup set is downloaded. Valid values:
        # 
        # *   **Native**\
        # *   **SQL**\
        # *   **CSV**\
        # *   **JSON**\
        self.backup_set_data_format = backup_set_data_format
        # The size of the data in the backup set.
        self.backup_set_data_size = backup_set_data_size
        # The type of the database.
        self.backup_set_db_type = backup_set_db_type
        # The timestamp that indicates when the backup set download task was created.
        self.backup_set_download_create_time = backup_set_download_create_time
        # The server directory to which the backup set is downloaded.
        # 
        # > This parameter is available only if the value of the BackupSetDownloadWay parameter is auto.
        self.backup_set_download_dir = backup_set_download_dir
        # The timestamp that indicates when the backup set download task is complete.
        self.backup_set_download_finish_time = backup_set_download_finish_time
        # The public download URL of the backup set.
        # 
        # > This parameter is available only if the value of the BackupSetDownloadWay parameter is manual and the conversion is complete.
        self.backup_set_download_internet_url = backup_set_download_internet_url
        # The internal download URL of the backup set.
        # 
        # > This parameter is available only if the value of the BackupSetDownloadWay parameter is manual and the conversion is complete.
        self.backup_set_download_intranet_url = backup_set_download_intranet_url
        # The status of the backup set download task. Valid values:
        # 
        # *   **checking**: The backup set download task is being prechecked.
        # *   **init**: The backup set download task is not started and fails to pass the precheck.
        # *   **check_pass**: The backup set download task passes the precheck.
        # *   **pause**: The backup set download task is paused.
        # *   **schedule**: The backup set download task is waiting to be scheduled
        # *   **running**: The backup set download task is running.
        # *   **stop**: The backup set download task fails.
        # *   **finish**: The backup set download task is complete.
        self.backup_set_download_status = backup_set_download_status
        # The type of the destination server to which the backup set is downloaded.
        # 
        # > This parameter is available only if the value of the BackupSetDownloadWay parameter is auto. A value of agent indicates a server on which a backup gateway is installed.
        self.backup_set_download_target_type = backup_set_download_target_type
        # The ID of the backup set download task.
        self.backup_set_download_task_id = backup_set_download_task_id
        # The name of the backup set download task.
        self.backup_set_download_task_name = backup_set_download_task_name
        # The method in which the backup set is downloaded. Valid values:
        # 
        # *   **manual**: The backup set is manually downloaded.
        # *   **auto**: The backup set is automatically downloaded.
        self.backup_set_download_way = backup_set_download_way
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        # The type of the backup set task. Valid values:
        # 
        # *   **cbs_backup_sub_full**: logical full backup set download task
        # *   **cbs_backup_sub_cont**: logical incremental backup set download task
        self.backup_set_job_type = backup_set_job_type
        # The error message.
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_set_code is not None:
            result['BackupSetCode'] = self.backup_set_code
        if self.backup_set_data_format is not None:
            result['BackupSetDataFormat'] = self.backup_set_data_format
        if self.backup_set_data_size is not None:
            result['BackupSetDataSize'] = self.backup_set_data_size
        if self.backup_set_db_type is not None:
            result['BackupSetDbType'] = self.backup_set_db_type
        if self.backup_set_download_create_time is not None:
            result['BackupSetDownloadCreateTime'] = self.backup_set_download_create_time
        if self.backup_set_download_dir is not None:
            result['BackupSetDownloadDir'] = self.backup_set_download_dir
        if self.backup_set_download_finish_time is not None:
            result['BackupSetDownloadFinishTime'] = self.backup_set_download_finish_time
        if self.backup_set_download_internet_url is not None:
            result['BackupSetDownloadInternetUrl'] = self.backup_set_download_internet_url
        if self.backup_set_download_intranet_url is not None:
            result['BackupSetDownloadIntranetUrl'] = self.backup_set_download_intranet_url
        if self.backup_set_download_status is not None:
            result['BackupSetDownloadStatus'] = self.backup_set_download_status
        if self.backup_set_download_target_type is not None:
            result['BackupSetDownloadTargetType'] = self.backup_set_download_target_type
        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id
        if self.backup_set_download_task_name is not None:
            result['BackupSetDownloadTaskName'] = self.backup_set_download_task_name
        if self.backup_set_download_way is not None:
            result['BackupSetDownloadWay'] = self.backup_set_download_way
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_set_job_type is not None:
            result['BackupSetJobType'] = self.backup_set_job_type
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetCode') is not None:
            self.backup_set_code = m.get('BackupSetCode')
        if m.get('BackupSetDataFormat') is not None:
            self.backup_set_data_format = m.get('BackupSetDataFormat')
        if m.get('BackupSetDataSize') is not None:
            self.backup_set_data_size = m.get('BackupSetDataSize')
        if m.get('BackupSetDbType') is not None:
            self.backup_set_db_type = m.get('BackupSetDbType')
        if m.get('BackupSetDownloadCreateTime') is not None:
            self.backup_set_download_create_time = m.get('BackupSetDownloadCreateTime')
        if m.get('BackupSetDownloadDir') is not None:
            self.backup_set_download_dir = m.get('BackupSetDownloadDir')
        if m.get('BackupSetDownloadFinishTime') is not None:
            self.backup_set_download_finish_time = m.get('BackupSetDownloadFinishTime')
        if m.get('BackupSetDownloadInternetUrl') is not None:
            self.backup_set_download_internet_url = m.get('BackupSetDownloadInternetUrl')
        if m.get('BackupSetDownloadIntranetUrl') is not None:
            self.backup_set_download_intranet_url = m.get('BackupSetDownloadIntranetUrl')
        if m.get('BackupSetDownloadStatus') is not None:
            self.backup_set_download_status = m.get('BackupSetDownloadStatus')
        if m.get('BackupSetDownloadTargetType') is not None:
            self.backup_set_download_target_type = m.get('BackupSetDownloadTargetType')
        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')
        if m.get('BackupSetDownloadTaskName') is not None:
            self.backup_set_download_task_name = m.get('BackupSetDownloadTaskName')
        if m.get('BackupSetDownloadWay') is not None:
            self.backup_set_download_way = m.get('BackupSetDownloadWay')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSetJobType') is not None:
            self.backup_set_job_type = m.get('BackupSetJobType')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DescribeBackupSetDownloadTaskListResponseBodyItems(TeaModel):
    def __init__(
        self,
        backup_set_download_task_detail: List[DescribeBackupSetDownloadTaskListResponseBodyItemsBackupSetDownloadTaskDetail] = None,
    ):
        self.backup_set_download_task_detail = backup_set_download_task_detail

    def validate(self):
        if self.backup_set_download_task_detail:
            for k in self.backup_set_download_task_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackupSetDownloadTaskDetail'] = []
        if self.backup_set_download_task_detail is not None:
            for k in self.backup_set_download_task_detail:
                result['BackupSetDownloadTaskDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_set_download_task_detail = []
        if m.get('BackupSetDownloadTaskDetail') is not None:
            for k in m.get('BackupSetDownloadTaskDetail'):
                temp_model = DescribeBackupSetDownloadTaskListResponseBodyItemsBackupSetDownloadTaskDetail()
                self.backup_set_download_task_detail.append(temp_model.from_map(k))
        return self


class DescribeBackupSetDownloadTaskListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: DescribeBackupSetDownloadTaskListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backup schedules.
        self.items = items
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success
        # The total number of backup set download tasks.
        self.total_elements = total_elements
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribeBackupSetDownloadTaskListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeBackupSetDownloadTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupSetDownloadTaskListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBackupSetDownloadTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDLAServiceRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDLAServiceResponseBody(TeaModel):
    def __init__(
        self,
        auto_add: bool = None,
        err_code: str = None,
        err_message: str = None,
        have_job_failed: bool = None,
        http_status_code: int = None,
        request_id: str = None,
        state: str = None,
        success: bool = None,
    ):
        # Specifies whether to enable the feature of automatically adding incremental data to a data lake. If this feature is enabled, DBS adds the backup sets that are newly generated to the data lake that is created for the backup schedule. Valid values:
        # 
        # *   **true**: enables the feature.
        # *   **false**: disables the feature.
        self.auto_add = auto_add
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # Indicates whether a failed DLA task exists in the return result. Valid values:
        # 
        # *   **true**: A failed DLA task exists.
        # *   **false**: No failed DLA task exists.
        self.have_job_failed = have_job_failed
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # The status of the DLA service for the backup schedule. Valid values:
        # 
        # *   **Running**: DLA is running.
        # *   **Closing**: DLA is being disabled.
        # *   **Closed**: DLA is disabled.
        self.state = state
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_add is not None:
            result['AutoAdd'] = self.auto_add
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.have_job_failed is not None:
            result['HaveJobFailed'] = self.have_job_failed
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAdd') is not None:
            self.auto_add = m.get('AutoAdd')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HaveJobFailed') is not None:
            self.have_job_failed = m.get('HaveJobFailed')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDLAServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDLAServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDLAServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFullBackupListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_set_id: str = None,
        client_token: str = None,
        end_timestamp: int = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        show_storage_type: bool = None,
        start_timestamp: int = None,
    ):
        # The error code.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The end time of the backup task, such as 1554560477000.
        self.backup_set_id = backup_set_id
        # The number of entries returned on each page.
        self.client_token = client_token
        self.end_timestamp = end_timestamp
        self.owner_id = owner_id
        # The client token that is used to ensure the idempotence of the request.
        self.page_num = page_num
        # The error message.
        self.page_size = page_size
        # The ID of the request.
        self.show_storage_type = show_storage_type
        # Queries full backup tasks.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.show_storage_type is not None:
            result['ShowStorageType'] = self.show_storage_type
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShowStorageType') is not None:
            self.show_storage_type = m.get('ShowStorageType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeFullBackupListResponseBodyItemsFullBackupFile(TeaModel):
    def __init__(
        self,
        backup_objects: str = None,
        backup_set_expired_time: int = None,
        backup_set_id: str = None,
        backup_size: int = None,
        backup_status: str = None,
        create_time: int = None,
        end_time: int = None,
        err_message: str = None,
        finish_time: int = None,
        source_endpoint_ip_port: str = None,
        start_time: int = None,
        storage_method: str = None,
    ):
        self.backup_objects = backup_objects
        self.backup_set_expired_time = backup_set_expired_time
        self.backup_set_id = backup_set_id
        self.backup_size = backup_size
        self.backup_status = backup_status
        self.create_time = create_time
        self.end_time = end_time
        self.err_message = err_message
        self.finish_time = finish_time
        self.source_endpoint_ip_port = source_endpoint_ip_port
        self.start_time = start_time
        self.storage_method = storage_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.backup_set_expired_time is not None:
            result['BackupSetExpiredTime'] = self.backup_set_expired_time
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.source_endpoint_ip_port is not None:
            result['SourceEndpointIpPort'] = self.source_endpoint_ip_port
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage_method is not None:
            result['StorageMethod'] = self.storage_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('BackupSetExpiredTime') is not None:
            self.backup_set_expired_time = m.get('BackupSetExpiredTime')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('SourceEndpointIpPort') is not None:
            self.source_endpoint_ip_port = m.get('SourceEndpointIpPort')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StorageMethod') is not None:
            self.storage_method = m.get('StorageMethod')
        return self


class DescribeFullBackupListResponseBodyItems(TeaModel):
    def __init__(
        self,
        full_backup_file: List[DescribeFullBackupListResponseBodyItemsFullBackupFile] = None,
    ):
        self.full_backup_file = full_backup_file

    def validate(self):
        if self.full_backup_file:
            for k in self.full_backup_file:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FullBackupFile'] = []
        if self.full_backup_file is not None:
            for k in self.full_backup_file:
                result['FullBackupFile'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.full_backup_file = []
        if m.get('FullBackupFile') is not None:
            for k in m.get('FullBackupFile'):
                temp_model = DescribeFullBackupListResponseBodyItemsFullBackupFile()
                self.full_backup_file.append(temp_model.from_map(k))
        return self


class DescribeFullBackupListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: DescribeFullBackupListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.items = items
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribeFullBackupListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeFullBackupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFullBackupListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFullBackupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIncrementBackupListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        end_timestamp: int = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        show_storage_type: bool = None,
        start_timestamp: int = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The end of the time range to query.
        self.end_timestamp = end_timestamp
        self.owner_id = owner_id
        # The number of the page to return. The value must be a positive integer. Default value: 0.
        self.page_num = page_num
        # The number of entries to return on each page. Valid values: 30, 50, and 100.
        # 
        # > Default value: 30.
        self.page_size = page_size
        # Specifies whether to return the storage class. Valid values:
        # 
        # *   true
        # *   false
        # 
        # > Default value: true.
        self.show_storage_type = show_storage_type
        # The beginning of the time range to query.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.show_storage_type is not None:
            result['ShowStorageType'] = self.show_storage_type
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShowStorageType') is not None:
            self.show_storage_type = m.get('ShowStorageType')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeIncrementBackupListResponseBodyItemsIncrementBackupFile(TeaModel):
    def __init__(
        self,
        backup_set_expired_time: int = None,
        backup_set_id: str = None,
        backup_set_job_id: str = None,
        backup_size: int = None,
        backup_status: str = None,
        end_time: int = None,
        source_endpoint_ip_port: str = None,
        start_time: int = None,
        storage_method: str = None,
    ):
        # The point in time when the backup set expires.
        self.backup_set_expired_time = backup_set_expired_time
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        # The ID of the incremental backup task.
        self.backup_set_job_id = backup_set_job_id
        # The size of the backup set.
        self.backup_size = backup_size
        # The status of the incremental backup task. Valid values:
        # 
        # *   **INIT**: The incremental backup task is not started.
        # *   **FILLING**: The incremental backup task is in progress.
        # *   **COMPLETED**: The incremental backup task is complete.
        # *   **UNCOMPLETED**: The incremental backup task is not complete.
        self.backup_status = backup_status
        # The end time of the incremental backup task.
        self.end_time = end_time
        # The endpoint that is used to connect to the database.
        self.source_endpoint_ip_port = source_endpoint_ip_port
        # The start time of the incremental backup task.
        self.start_time = start_time
        # The storage class of the backup data. Valid values:
        # 
        # *   **Standard**: The storage class is Standard.
        # *   **IA**: The storage class is Infrequent Access (IA).
        # *   **Archive**: The storage class is Archive.
        # *   **UNKNOWN**: The storage class is unknown. This value is returned because the task is not complete.
        self.storage_method = storage_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_expired_time is not None:
            result['BackupSetExpiredTime'] = self.backup_set_expired_time
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_set_job_id is not None:
            result['BackupSetJobId'] = self.backup_set_job_id
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_endpoint_ip_port is not None:
            result['SourceEndpointIpPort'] = self.source_endpoint_ip_port
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage_method is not None:
            result['StorageMethod'] = self.storage_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetExpiredTime') is not None:
            self.backup_set_expired_time = m.get('BackupSetExpiredTime')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSetJobId') is not None:
            self.backup_set_job_id = m.get('BackupSetJobId')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceEndpointIpPort') is not None:
            self.source_endpoint_ip_port = m.get('SourceEndpointIpPort')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StorageMethod') is not None:
            self.storage_method = m.get('StorageMethod')
        return self


class DescribeIncrementBackupListResponseBodyItems(TeaModel):
    def __init__(
        self,
        increment_backup_file: List[DescribeIncrementBackupListResponseBodyItemsIncrementBackupFile] = None,
    ):
        self.increment_backup_file = increment_backup_file

    def validate(self):
        if self.increment_backup_file:
            for k in self.increment_backup_file:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IncrementBackupFile'] = []
        if self.increment_backup_file is not None:
            for k in self.increment_backup_file:
                result['IncrementBackupFile'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.increment_backup_file = []
        if m.get('IncrementBackupFile') is not None:
            for k in m.get('IncrementBackupFile'):
                temp_model = DescribeIncrementBackupListResponseBodyItemsIncrementBackupFile()
                self.increment_backup_file.append(temp_model.from_map(k))
        return self


class DescribeIncrementBackupListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: DescribeIncrementBackupListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of incremental backup tasks.
        self.items = items
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success
        # The total number of incremental backup tasks.
        self.total_elements = total_elements
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribeIncrementBackupListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeIncrementBackupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIncrementBackupListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIncrementBackupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobErrorCodeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        language: str = None,
        owner_id: str = None,
        task_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The language of the error message. Valid values:
        # 
        # *   **en** (default): English
        # *   **cn**: Chinese
        self.language = language
        self.owner_id = owner_id
        # The ID of the full backup or restore task.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeJobErrorCodeResponseBodyItem(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_id: str = None,
        job_state: str = None,
        job_type: str = None,
        language: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The standard error message.
        self.error_message = error_message
        # The ID of the full backup or restore task.
        self.job_id = job_id
        # The status of the task.
        self.job_state = job_state
        # The internal ID of the DBS task type.
        self.job_type = job_type
        # The language of the error message.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_state is not None:
            result['JobState'] = self.job_state
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class DescribeJobErrorCodeResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        item: DescribeJobErrorCodeResponseBodyItem = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error information.
        self.item = item
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.item is not None:
            result['Item'] = self.item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Item') is not None:
            temp_model = DescribeJobErrorCodeResponseBodyItem()
            self.item = temp_model.from_map(m['Item'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeJobErrorCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeJobErrorCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeJobErrorCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeCidrListRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        region: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # The region in which DBS is activated. Valid values:
        # 
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-qingdao**: China (Qingdao)
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        # *   **ap-southeast-1**: Singapore (Singapore)
        # *   **cn-hangzhou-finance**: China East 1 Finance
        # *   **cn-shanghai-finance**: China East 2 Finance
        # *   **cn-shenzhen-finance**: China South 1 Finance
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeNodeCidrListResponseBodyInternetIPs(TeaModel):
    def __init__(
        self,
        internet_ip: List[str] = None,
    ):
        self.internet_ip = internet_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')
        return self


class DescribeNodeCidrListResponseBodyIntranetIPs(TeaModel):
    def __init__(
        self,
        intranet_ip: List[str] = None,
    ):
        self.intranet_ip = intranet_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')
        return self


class DescribeNodeCidrListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        internet_ips: DescribeNodeCidrListResponseBodyInternetIPs = None,
        intranet_ips: DescribeNodeCidrListResponseBodyIntranetIPs = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The public CIDR blocks.
        self.internet_ips = internet_ips
        # The internal CIDR blocks.
        self.intranet_ips = intranet_ips
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.internet_ips:
            self.internet_ips.validate()
        if self.intranet_ips:
            self.intranet_ips.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.internet_ips is not None:
            result['InternetIPs'] = self.internet_ips.to_map()
        if self.intranet_ips is not None:
            result['IntranetIPs'] = self.intranet_ips.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InternetIPs') is not None:
            temp_model = DescribeNodeCidrListResponseBodyInternetIPs()
            self.internet_ips = temp_model.from_map(m['InternetIPs'])
        if m.get('IntranetIPs') is not None:
            temp_model = DescribeNodeCidrListResponseBodyIntranetIPs()
            self.intranet_ips = temp_model.from_map(m['IntranetIPs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeNodeCidrListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodeCidrListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodeCidrListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePreCheckProgressListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        restore_task_id: str = None,
    ):
        # The backup schedule ID.
        # 
        # >  You must specify one of BackupPlanId and RestoreTaskId.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # The restoration task ID.
        self.restore_task_id = restore_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        return self


class DescribePreCheckProgressListResponseBodyItemsPreCheckProgressDetail(TeaModel):
    def __init__(
        self,
        boot_time: int = None,
        err_msg: str = None,
        finish_time: int = None,
        item: str = None,
        job_id: str = None,
        names: str = None,
        order_num: str = None,
        state: str = None,
    ):
        # The time when the check for the item started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.boot_time = boot_time
        # The error message.
        self.err_msg = err_msg
        # The time when the check for the item was complete. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.finish_time = finish_time
        # The name of the check item.
        self.item = item
        # The ID of the job for the check item.
        self.job_id = job_id
        # The name of the group to which the check item belongs.
        self.names = names
        # The sequence number of the check item.
        self.order_num = order_num
        # The state of the check for the item. Valid values:
        # 
        # *   **init**: The check for the item is being initialized.
        # *   **warning**: A warning is reported.
        # *   **catched**: An exception occurs.
        # *   **running**: The check for the item is in progress.
        # *   **failed**: The check for the item fails.
        # *   **finish**: The check for the item is completed.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.item is not None:
            result['Item'] = self.item
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.names is not None:
            result['Names'] = self.names
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribePreCheckProgressListResponseBodyItems(TeaModel):
    def __init__(
        self,
        pre_check_progress_detail: List[DescribePreCheckProgressListResponseBodyItemsPreCheckProgressDetail] = None,
    ):
        self.pre_check_progress_detail = pre_check_progress_detail

    def validate(self):
        if self.pre_check_progress_detail:
            for k in self.pre_check_progress_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PreCheckProgressDetail'] = []
        if self.pre_check_progress_detail is not None:
            for k in self.pre_check_progress_detail:
                result['PreCheckProgressDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pre_check_progress_detail = []
        if m.get('PreCheckProgressDetail') is not None:
            for k in m.get('PreCheckProgressDetail'):
                temp_model = DescribePreCheckProgressListResponseBodyItemsPreCheckProgressDetail()
                self.pre_check_progress_detail.append(temp_model.from_map(k))
        return self


class DescribePreCheckProgressListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: DescribePreCheckProgressListResponseBodyItems = None,
        progress: int = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of check items.
        self.items = items
        # The precheck progress. Valid values: 0 to 100.
        self.progress = progress
        # The ID of the request.
        self.request_id = request_id
        # The status of the precheck. Valid values:
        # 
        # *   **running**: The precheck is in progress.
        # *   **failed**: The precheck failed.
        # *   **finish**: The precheck is complete.
        self.status = status
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribePreCheckProgressListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePreCheckProgressListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePreCheckProgressListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePreCheckProgressListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_code: List[str] = None,
    ):
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The regions that DBS supports.
        self.regions = regions
        # The request ID.
        self.request_id = request_id
        # The status of the request.
        self.success = success

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreRangeInfoRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        begin_timestamp_for_restore: int = None,
        client_token: str = None,
        end_timestamp_for_restore: int = None,
        owner_id: str = None,
        recently_restore: bool = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain it.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The earliest point in time to which you can restore data. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the value of the parameter for each backup schedule.
        # 
        # This parameter is required.
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The latest point in time to which you can restore data. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the value of the parameter for each backup schedule.
        # 
        # This parameter is required.
        self.end_timestamp_for_restore = end_timestamp_for_restore
        self.owner_id = owner_id
        # Specifies whether to query the most recent point in time to which you can restore data.
        self.recently_restore = recently_restore

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.recently_restore is not None:
            result['RecentlyRestore'] = self.recently_restore
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RecentlyRestore') is not None:
            self.recently_restore = m.get('RecentlyRestore')
        return self


class DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupListFullBackupDetail(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        # The end time of the full backup task. Example: 1646760308000.
        self.end_time = end_time
        # The start time of the full backup task. Example: 1646760282000.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupList(TeaModel):
    def __init__(
        self,
        full_backup_detail: List[DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupListFullBackupDetail] = None,
    ):
        self.full_backup_detail = full_backup_detail

    def validate(self):
        if self.full_backup_detail:
            for k in self.full_backup_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FullBackupDetail'] = []
        if self.full_backup_detail is not None:
            for k in self.full_backup_detail:
                result['FullBackupDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.full_backup_detail = []
        if m.get('FullBackupDetail') is not None:
            for k in m.get('FullBackupDetail'):
                temp_model = DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupListFullBackupDetail()
                self.full_backup_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRange(TeaModel):
    def __init__(
        self,
        begin_timestamp_for_restore: int = None,
        end_timestamp_for_restore: int = None,
        full_backup_list: DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupList = None,
        range_type: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
    ):
        # The beginning of the time range to which you can restore data.
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        # The end of the time range to which you can restore data.
        self.end_timestamp_for_restore = end_timestamp_for_restore
        # If the value of the RangeType parameter is point, this parameter is returned. The value of this parameter describes information about all backup points in the time range.
        self.full_backup_list = full_backup_list
        # The type of the time range to which you can restore data.
        # 
        # *   **point**: The time range contains discrete points in time at which full backups were performed.
        # *   **range**: The time range is a period of time for which continuous backup is performed. You can specify a random point in time in the time range to restore data.
        self.range_type = range_type
        # The ID of the database instance.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The location of the database.
        self.source_endpoint_instance_type = source_endpoint_instance_type

    def validate(self):
        if self.full_backup_list:
            self.full_backup_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore
        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore
        if self.full_backup_list is not None:
            result['FullBackupList'] = self.full_backup_list.to_map()
        if self.range_type is not None:
            result['RangeType'] = self.range_type
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')
        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')
        if m.get('FullBackupList') is not None:
            temp_model = DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupList()
            self.full_backup_list = temp_model.from_map(m['FullBackupList'])
        if m.get('RangeType') is not None:
            self.range_type = m.get('RangeType')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        return self


class DescribeRestoreRangeInfoResponseBodyItems(TeaModel):
    def __init__(
        self,
        dbsrecover_range: List[DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRange] = None,
    ):
        self.dbsrecover_range = dbsrecover_range

    def validate(self):
        if self.dbsrecover_range:
            for k in self.dbsrecover_range:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBSRecoverRange'] = []
        if self.dbsrecover_range is not None:
            for k in self.dbsrecover_range:
                result['DBSRecoverRange'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbsrecover_range = []
        if m.get('DBSRecoverRange') is not None:
            for k in m.get('DBSRecoverRange'):
                temp_model = DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRange()
                self.dbsrecover_range.append(temp_model.from_map(k))
        return self


class DescribeRestoreRangeInfoResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: DescribeRestoreRangeInfoResponseBodyItems = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The information about the time ranges to which you can restore data.
        self.items = items
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribeRestoreRangeInfoResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRestoreRangeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRestoreRangeInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRestoreRangeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreTaskListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        end_timestamp: int = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        restore_task_id: str = None,
        start_timestamp: int = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The end of the time range to query.
        self.end_timestamp = end_timestamp
        self.owner_id = owner_id
        # The number of the page to return. The value must be a positive integer. Default value: 0.
        self.page_num = page_num
        # The number of entries to return on each page. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        # 
        # > Default value: 30.
        self.page_size = page_size
        # The restoration task ID. Separate multiple IDs with commas (,). You can call the [CreateRestoreTask](https://help.aliyun.com/document_detail/2869836.html) operation to obtain the ID.
        # 
        # >  Configure the BackupPlanId or RestoreTaskId parameter. If you configure the two parameters, an error is returned.
        self.restore_task_id = restore_task_id
        # The beginning of the time range to query.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeRestoreTaskListResponseBodyItemsRestoreTaskDetail(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_plan_id: str = None,
        backup_set_id: str = None,
        continuous_restore_progress: int = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_ip_port: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_user_name: str = None,
        err_message: str = None,
        full_data_restore_progress: int = None,
        full_stru_after_restore_progress: int = None,
        full_strufore_restore_progress: int = None,
        restore_dir: str = None,
        restore_objects: str = None,
        restore_status: str = None,
        restore_task_create_time: int = None,
        restore_task_finish_time: int = None,
        restore_task_id: str = None,
        restore_task_name: str = None,
        restore_time: int = None,
    ):
        # The ID of the backup gateway.
        self.backup_gateway_id = backup_gateway_id
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The ID of the full backup set that is used in the restore task.
        self.backup_set_id = backup_set_id
        # The restore progress of the incremental log files.
        self.continuous_restore_progress = continuous_restore_progress
        # The unique ID (UID) of the Alibaba Cloud account to which the backup schedule belongs.
        self.cross_aliyun_id = cross_aliyun_id
        # The name of the RAM role that can be used to perform backups across Alibaba Cloud accounts.
        self.cross_role_name = cross_role_name
        # The name of the database.
        self.destination_endpoint_database_name = destination_endpoint_database_name
        # The ID of the database instance.
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        # The location of the database. Valid values:
        # 
        # *   RDS
        # *   ECS
        # *   Express: The database is connected to DBS by using Express Connect, VPN Gateway, or Smart Access Gateway.
        # *   Agent: The database is connected to DBS over a DBS backup gateway.
        # *   DDS: The database is an ApsaraDB for MongoDB database.
        # *   Other: The database is connected to DBS by using the IP address and port of the database.
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        # The endpoint that is used to connect to the database.
        self.destination_endpoint_ip_port = destination_endpoint_ip_port
        # The SID of the Oracle database.
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        # The region in which the database is deployed.
        self.destination_endpoint_region = destination_endpoint_region
        # The username of the account that is used to connect to the database.
        self.destination_endpoint_user_name = destination_endpoint_user_name
        # The error message.
        self.err_message = err_message
        # The restore progress of the full backup data.
        self.full_data_restore_progress = full_data_restore_progress
        # The progress of schema restore after full data restore.
        self.full_stru_after_restore_progress = full_stru_after_restore_progress
        # The progress of schema restore before full data restore.
        self.full_strufore_restore_progress = full_strufore_restore_progress
        # The directory of the destination database to which the objects were restored.
        self.restore_dir = restore_dir
        # The objects to be restored.
        self.restore_objects = restore_objects
        # The status of the restore task. Valid values:
        # 
        # *   init: The restore task is not started or does not pass the precheck.
        # *   running: The restore task is running.
        # *   stop: The restore task failed.
        # *   pause: The restore task is stopped.
        # *   check_pass: The restore task passed the precheck.
        self.restore_status = restore_status
        # The time when the restore task was created, such as 1554560477000.
        self.restore_task_create_time = restore_task_create_time
        # The time when the restore task was complete, such as 1554560477000.
        self.restore_task_finish_time = restore_task_finish_time
        # The ID of the restore task.
        self.restore_task_id = restore_task_id
        # The name of the restore task.
        self.restore_task_name = restore_task_name
        # The time to run the restore task, such as 1554560477000.
        self.restore_time = restore_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.continuous_restore_progress is not None:
            result['ContinuousRestoreProgress'] = self.continuous_restore_progress
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name
        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id
        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type
        if self.destination_endpoint_ip_port is not None:
            result['DestinationEndpointIpPort'] = self.destination_endpoint_ip_port
        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.full_data_restore_progress is not None:
            result['FullDataRestoreProgress'] = self.full_data_restore_progress
        if self.full_stru_after_restore_progress is not None:
            result['FullStruAfterRestoreProgress'] = self.full_stru_after_restore_progress
        if self.full_strufore_restore_progress is not None:
            result['FullStruforeRestoreProgress'] = self.full_strufore_restore_progress
        if self.restore_dir is not None:
            result['RestoreDir'] = self.restore_dir
        if self.restore_objects is not None:
            result['RestoreObjects'] = self.restore_objects
        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status
        if self.restore_task_create_time is not None:
            result['RestoreTaskCreateTime'] = self.restore_task_create_time
        if self.restore_task_finish_time is not None:
            result['RestoreTaskFinishTime'] = self.restore_task_finish_time
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.restore_task_name is not None:
            result['RestoreTaskName'] = self.restore_task_name
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('ContinuousRestoreProgress') is not None:
            self.continuous_restore_progress = m.get('ContinuousRestoreProgress')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')
        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')
        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')
        if m.get('DestinationEndpointIpPort') is not None:
            self.destination_endpoint_ip_port = m.get('DestinationEndpointIpPort')
        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('FullDataRestoreProgress') is not None:
            self.full_data_restore_progress = m.get('FullDataRestoreProgress')
        if m.get('FullStruAfterRestoreProgress') is not None:
            self.full_stru_after_restore_progress = m.get('FullStruAfterRestoreProgress')
        if m.get('FullStruforeRestoreProgress') is not None:
            self.full_strufore_restore_progress = m.get('FullStruforeRestoreProgress')
        if m.get('RestoreDir') is not None:
            self.restore_dir = m.get('RestoreDir')
        if m.get('RestoreObjects') is not None:
            self.restore_objects = m.get('RestoreObjects')
        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')
        if m.get('RestoreTaskCreateTime') is not None:
            self.restore_task_create_time = m.get('RestoreTaskCreateTime')
        if m.get('RestoreTaskFinishTime') is not None:
            self.restore_task_finish_time = m.get('RestoreTaskFinishTime')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('RestoreTaskName') is not None:
            self.restore_task_name = m.get('RestoreTaskName')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        return self


class DescribeRestoreTaskListResponseBodyItems(TeaModel):
    def __init__(
        self,
        restore_task_detail: List[DescribeRestoreTaskListResponseBodyItemsRestoreTaskDetail] = None,
    ):
        self.restore_task_detail = restore_task_detail

    def validate(self):
        if self.restore_task_detail:
            for k in self.restore_task_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RestoreTaskDetail'] = []
        if self.restore_task_detail is not None:
            for k in self.restore_task_detail:
                result['RestoreTaskDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_task_detail = []
        if m.get('RestoreTaskDetail') is not None:
            for k in m.get('RestoreTaskDetail'):
                temp_model = DescribeRestoreTaskListResponseBodyItemsRestoreTaskDetail()
                self.restore_task_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreTaskListResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: DescribeRestoreTaskListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backup schedule.
        self.items = items
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of restore tasks.
        self.total_elements = total_elements
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribeRestoreTaskListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeRestoreTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRestoreTaskListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRestoreTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableBackupLogRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The backup schedule ID. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to query the ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DisableBackupLogResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        need_precheck: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backup schedule ID.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether a precheck is triggered. Valid values:
        # 
        # *   true: A precheck is triggered. You must call the [StartBackupPlan](https://help.aliyun.com/document_detail/2869816.html) operation to start the backup schedule.
        # *   false: No precheck is triggered.
        self.need_precheck = need_precheck
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableBackupLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableBackupLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableBackupLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableBackupLogRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The backup schedule ID. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class EnableBackupLogResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        need_precheck: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backup schedule ID.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether a precheck is triggered. Valid values:
        # 
        # *   true: A precheck is triggered. You must call the [StartBackupPlan](https://help.aliyun.com/document_detail/2869816.html) operation to start the backup schedule.
        # *   false: No precheck is triggered.
        self.need_precheck = need_precheck
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableBackupLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableBackupLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableBackupLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDBListFromAgentRequest(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        client_token: str = None,
        owner_id: str = None,
        source_endpoint_region: str = None,
        task_id: int = None,
    ):
        # The ID of the backup gateway.
        self.backup_gateway_id = backup_gateway_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.owner_id = owner_id
        # The region in which the backup gateway resides.
        self.source_endpoint_region = source_endpoint_region
        # The ID of the asynchronous task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetDBListFromAgentResponseBodyDbList(TeaModel):
    def __init__(
        self,
        db_name: List[str] = None,
    ):
        self.db_name = db_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['dbName'] = self.db_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        return self


class GetDBListFromAgentResponseBody(TeaModel):
    def __init__(
        self,
        db_list: GetDBListFromAgentResponseBodyDbList = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the databases.
        self.db_list = db_list
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.db_list:
            self.db_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_list is not None:
            result['DbList'] = self.db_list.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbList') is not None:
            temp_model = GetDBListFromAgentResponseBodyDbList()
            self.db_list = temp_model.from_map(m['DbList'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDBListFromAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDBListFromAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDBListFromAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeDbsServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_message: str = None,
        error_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The value is null.
        self.data = data
        # The error message returned if the request failed.
        self.err_message = err_message
        # The error code returned.
        self.error_code = error_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InitializeDbsServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitializeDbsServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitializeDbsServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupObjectsRequest(TeaModel):
    def __init__(
        self,
        backup_objects: str = None,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The backup objects that are defined in a JSON string in the following format:
        # 
        #     [
        #         {
        #             "DBName":"The name of the database that you want to back up",
        #             "SchemaName":"The name of the schema that you want to back up",
        #             "TableIncludes":[{
        #             	"TableName":"The name of the table that you want to back up"
        #             }],
        #             "TableExcludes":[{
        #                 "TableName":"The name of the table that you want to exclude during the backup"
        #             }]
        #         }
        #     ]
        # 
        # *   If you specify only `DBName` and do not specify objects of lower levels, all objects in the database are backed up.
        # 
        # *   If you specify `DBName` and some objects of lower levels, only the specified objects are backed up by default. You can use the following regular expressions to define object names:
        # 
        #     *   A period `.` matches any single character except `\\r\\n`.
        #     *   An asterisk `*` matches zero or more occurrences of a preceding subexpression. For example, `h.*llo` matches strings such as `hllo` and `heeeello`.
        #     *   A question mark `?` matches zero or one occurrence of a preceding subexpression. For example, `h.?llo` matches strings such as `hllo` and `hello`, but not `haello`.
        #     *   Character set `[Characters]` matches a character included in the brackets ([ ]). For example, `h[ae]llo` matches `hallo` and `hello`.
        #     *   Negative character set `[^Characters]` does not match a character in the brackets ([ ]). For example, `h[^ae]llo` matches `hcllo` and `hdllo`, but not `hallo` or `hello`.
        #     *   Character range `[character1-character2]` matches any character included in the range from `character1 to character2`, such as `[0-9]` and `[a-z]`.
        # 
        # >  `SchemaName` and `NewSchemaName` apply only to SQL Server databases. Use `DBName` and `NewDBName` to specify the names of other databases.
        # 
        # This parameter is required.
        self.backup_objects = backup_objects
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyBackupObjectsResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        need_precheck: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether a precheck is triggered. If true is returned, you must call the [StartBackupPlan](https://help.aliyun.com/document_detail/2869816.html) operation to start the backup schedule.
        self.need_precheck = need_precheck
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyBackupObjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBackupObjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBackupObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPlanNameRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The name of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_name = backup_plan_name
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyBackupPlanNameResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyBackupPlanNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBackupPlanNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBackupPlanNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupSetDownloadRulesRequest(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_plan_id: str = None,
        backup_set_download_dir: str = None,
        backup_set_download_target_type: str = None,
        backup_set_download_target_type_location: str = None,
        client_token: str = None,
        full_data_format: str = None,
        increment_data_format: str = None,
        open_auto_download: bool = None,
        owner_id: str = None,
    ):
        # The ID of the backup gateway that is used to download the backup set.
        self.backup_gateway_id = backup_gateway_id
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The server directory to which the backup set is downloaded.
        self.backup_set_download_dir = backup_set_download_dir
        # The type of the destination server to which the backup set is downloaded.
        # 
        # > Set the value to agent, which indicates a server on which a backup gateway is installed.
        self.backup_set_download_target_type = backup_set_download_target_type
        # The type of the destination directory to which the backup set is downloaded. This parameter is required if the automatic download feature is enabled. Valid values:
        # 
        # *   local
        # *   nas
        # *   ftp
        # *   minio
        # 
        # > Default value: local.
        self.backup_set_download_target_type_location = backup_set_download_target_type_location
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The format in which the full backup set is downloaded. Valid values:
        # 
        # *   Native
        # *   SQL
        # *   CSV
        # *   JSON
        # 
        # > Default value: CSV.
        self.full_data_format = full_data_format
        # The format in which the incremental backup set is downloaded. Valid values:
        # 
        # *   Native
        # *   SQL
        # *   CSV
        # *   JSON
        # 
        # > Default value: Native.
        self.increment_data_format = increment_data_format
        # Specifies whether to enable the automatic download feature. Default value: false.
        self.open_auto_download = open_auto_download
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_set_download_dir is not None:
            result['BackupSetDownloadDir'] = self.backup_set_download_dir
        if self.backup_set_download_target_type is not None:
            result['BackupSetDownloadTargetType'] = self.backup_set_download_target_type
        if self.backup_set_download_target_type_location is not None:
            result['BackupSetDownloadTargetTypeLocation'] = self.backup_set_download_target_type_location
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.full_data_format is not None:
            result['FullDataFormat'] = self.full_data_format
        if self.increment_data_format is not None:
            result['IncrementDataFormat'] = self.increment_data_format
        if self.open_auto_download is not None:
            result['OpenAutoDownload'] = self.open_auto_download
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetDownloadDir') is not None:
            self.backup_set_download_dir = m.get('BackupSetDownloadDir')
        if m.get('BackupSetDownloadTargetType') is not None:
            self.backup_set_download_target_type = m.get('BackupSetDownloadTargetType')
        if m.get('BackupSetDownloadTargetTypeLocation') is not None:
            self.backup_set_download_target_type_location = m.get('BackupSetDownloadTargetTypeLocation')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FullDataFormat') is not None:
            self.full_data_format = m.get('FullDataFormat')
        if m.get('IncrementDataFormat') is not None:
            self.increment_data_format = m.get('IncrementDataFormat')
        if m.get('OpenAutoDownload') is not None:
            self.open_auto_download = m.get('OpenAutoDownload')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyBackupSetDownloadRulesResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyBackupSetDownloadRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBackupSetDownloadRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBackupSetDownloadRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupSourceEndpointRequest(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        backup_objects: str = None,
        backup_plan_id: str = None,
        client_token: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        owner_id: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: int = None,
        source_endpoint_region: str = None,
        source_endpoint_user_name: str = None,
    ):
        # The backup gateway ID. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the ID.
        # 
        # >  If you set **SourceEndpointInstanceType** to Agent, this parameter is required.
        self.backup_gateway_id = backup_gateway_id
        # The backup object. If you set SourceEndpointInstanceType to Agent, this parameter is optional. Otherwise, it is required. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the backup object.
        self.backup_objects = backup_objects
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain it.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The unique ID (UID) of the Alibaba Cloud account to which the backup schedule belongs. You can call the [DescribeRestoreTaskList](https://help.aliyun.com/document_detail/2869838.html) operation to obtain the UID.
        self.cross_aliyun_id = cross_aliyun_id
        # The name of the RAM role that is used to perform backups across Alibaba Cloud accounts. You can call the [DescribeRestoreTaskList](https://help.aliyun.com/document_detail/2869838.html) operation to obtain the RAM role.
        self.cross_role_name = cross_role_name
        self.owner_id = owner_id
        # The name of the database.
        # 
        # *   This parameter is required if the database is a PostgreSQL or MongoDB database.
        # *   This parameter is required if the database is an SQL Server database that is connected to DBS over a DBS backup gateway.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The endpoint of the database. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the endpoint.
        # 
        # >  If you set **SourceEndpointInstanceType** to Express, Agent, or Other, this parameter is required.
        self.source_endpoint_ip = source_endpoint_ip
        # The database instance ID. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the ID.
        # 
        # >  If you set **SourceEndpointInstanceType** to RDS, ECS, DDS, or Express, this parameter is required.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The location of the database. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain it. Valid values:
        # 
        # *   **RDS**\
        # *   **ECS**\
        # *   **Express**: The database is connected to DBS via Express Connect, VPN Gateway, or Smart Access Gateway.
        # *   **Agent**: The database is connected to DBS over a DBS backup gateway.
        # *   **DDS**: The database is an ApsaraDB for MongoDB database.
        # *   **Other**: The database is connected to DBS using the IP address and port of the database.
        # 
        # This parameter is required.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The SID of the Oracle source database. If the database is an Oracle database, this parameter is required.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The password of the account that is used to connect to the database.
        # 
        # This parameter is required except that the database is an SQL Server database that is connected to DBS over a DBS backup gateway or a Redis database.
        self.source_endpoint_password = source_endpoint_password
        # The port that is used to connect to the database. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the port.
        # 
        # >  If you set **SourceEndpointInstanceType** to Express, Agent, Other, or ECS, this parameter is required.
        self.source_endpoint_port = source_endpoint_port
        # The region in which the database you want to back up resides. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the region.
        # 
        # >  If you set **SourceEndpointInstanceType** to RDS, ECS, DDS, Express, or Agent, this parameter is required.
        self.source_endpoint_region = source_endpoint_region
        # The account that is used to log on to the database. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the account.
        # 
        # If the database is an SQL Server database connected to DBS over a DBS backup gateway or a Redis database, this parameter is optional. Otherwise, it is required.
        self.source_endpoint_user_name = source_endpoint_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
        return self


class ModifyBackupSourceEndpointResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        need_precheck: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether a precheck is triggered. If the value of this parameter is true, you must start the backup schedule by calling the StartBackupPlan operation.
        self.need_precheck = need_precheck
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyBackupSourceEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBackupSourceEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBackupSourceEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupStrategyRequest(TeaModel):
    def __init__(
        self,
        backup_log_interval_seconds: int = None,
        backup_period: str = None,
        backup_plan_id: str = None,
        backup_start_time: str = None,
        backup_strategy_type: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The interval at which you want to perform incremental log backups. Unit: seconds.
        # 
        # > This parameter takes effect only when physical backups are performed.
        self.backup_log_interval_seconds = backup_log_interval_seconds
        # The day of each week when the full backup task runs. Valid values:
        # 
        # *   Monday
        # *   Tuesday
        # *   Wednesday
        # *   Thursday
        # *   Friday
        # *   Saturday
        # *   Sunday
        # 
        # This parameter is required.
        self.backup_period = backup_period
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The start time of the full backup task. Specify the time in the HH:mm format.
        self.backup_start_time = backup_start_time
        # The backup method that you want to use for full backups. Valid values:
        # 
        # *   **simple**: scheduled backup. If you specify this value for the BackupStrategyType parameter, you must also specify the BackupPeriod and BackupStartTime parameters.
        # *   **Manual**: manual backup.
        # 
        # > Default value: **simple**.
        self.backup_strategy_type = backup_strategy_type
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_log_interval_seconds is not None:
            result['BackupLogIntervalSeconds'] = self.backup_log_interval_seconds
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_strategy_type is not None:
            result['BackupStrategyType'] = self.backup_strategy_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupLogIntervalSeconds') is not None:
            self.backup_log_interval_seconds = m.get('BackupLogIntervalSeconds')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStrategyType') is not None:
            self.backup_strategy_type = m.get('BackupStrategyType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyBackupStrategyResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        need_precheck: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether a precheck is triggered. If the value of this parameter is true, you must start the backup schedule by calling the StartBackupPlan operation.
        self.need_precheck = need_precheck
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyBackupStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBackupStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyBackupStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyStorageStrategyRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_retention_period: int = None,
        client_token: str = None,
        duplication_archive_period: int = None,
        duplication_infrequent_access_period: int = None,
        owner_id: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The number of days for which the backup data is retained. Valid values: 0 to 1825.
        # 
        # > Default value: 730.
        # 
        # This parameter is required.
        self.backup_retention_period = backup_retention_period
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The number of days after which the storage class of the backup data is changed to Archive. The value of this parameter must be smaller than the value of the BackupRetentionPeriod parameter. For more information about the Archive storage class, see [Storage class overview](https://help.aliyun.com/document_detail/51374.html).
        # 
        # > Default value: 365.
        # 
        # This parameter is required.
        self.duplication_archive_period = duplication_archive_period
        # The number of days after which the storage class of the backup data is changed to Infrequent Access (IA). The value of this parameter must be smaller than the value of the DuplicationArchivePeriod parameter. For more information about the IA storage class, see [Storage class overview](https://help.aliyun.com/document_detail/51374.html).
        # 
        # > Default value: 180.
        # 
        # This parameter is required.
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period
        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')
        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyStorageStrategyResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        need_precheck: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether a precheck is triggered. Valid values:
        # 
        # *   **true**: A precheck is triggered. You must manually call the [StartBackupPlan](https://help.aliyun.com/document_detail/2869818.html) operation to start the backup schedule.
        # *   **false**: No precheck is triggered.
        self.need_precheck = need_precheck
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyStorageStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyStorageStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyStorageStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The backup schedule ID. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to query the ID.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ReleaseBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request succeeded. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReleaseBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        period: str = None,
        used_time: int = None,
    ):
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # Specifies whether to use yearly subscription or monthly subscription for the instance. Valid values:
        # 
        # *   Year
        # *   Month
        # 
        # This parameter is required.
        self.period = period
        # The subscription duration of the instance. Valid values:
        # 
        # *   If the Period parameter is set to Year, the value of the UsedTime parameter ranges from 1 to 9.
        # *   If the Period parameter is set to Month, the value of the UsedTime parameter ranges from 1 to 11.
        # 
        # This parameter is required.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class RenewBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenewBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) operation to obtain it.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class StartBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        created_full_backupset_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The ID of the full backup set.
        self.created_full_backupset_id = created_full_backupset_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.created_full_backupset_id is not None:
            result['CreatedFullBackupsetId'] = self.created_full_backupset_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('CreatedFullBackupsetId') is not None:
            self.created_full_backupset_id = m.get('CreatedFullBackupsetId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRestoreTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        restore_task_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # The ID of the restore task.
        # 
        # This parameter is required.
        self.restore_task_id = restore_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        return self


class StartRestoreTaskResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        restore_task_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # The ID of the restore task.
        self.restore_task_id = restore_task_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartRestoreTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartRestoreTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartRestoreTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        stop_method: str = None,
    ):
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        self.owner_id = owner_id
        # The method that is used to stop the backup schedule. Valid values:
        # 
        # *   ALL: stops the backup schedule, full data backup tasks, incremental log backup tasks, and restore tasks
        # *   PLAN: stops only the backup schedule.
        # 
        # This parameter is required.
        self.stop_method = stop_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stop_method is not None:
            result['StopMethod'] = self.stop_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StopMethod') is not None:
            self.stop_method = m.get('StopMethod')
        return self


class StopBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        instance_class: str = None,
        owner_id: str = None,
    ):
        # The ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The specifications of the instance. Valid values:
        # 
        # *   micro
        # *   small
        # *   medium
        # *   large
        # *   xlarge
        # 
        # This parameter is required.
        self.instance_class = instance_class
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UpgradeBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



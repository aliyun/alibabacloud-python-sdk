# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ConfigureBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_region: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_port: int = None,
        source_endpoint_database_name: str = None,
        source_endpoint_user_name: str = None,
        source_endpoint_password: str = None,
        backup_gateway_id: int = None,
        ossbucket_name: str = None,
        backup_objects: str = None,
        backup_period: str = None,
        backup_start_time: str = None,
        enable_backup_log: bool = None,
        backup_log_interval_seconds: int = None,
        backup_retention_period: int = None,
        duplication_infrequent_access_period: int = None,
        duplication_archive_period: int = None,
        backup_plan_name: str = None,
        source_endpoint_oracle_sid: str = None,
        backup_storage_type: str = None,
        backup_speed_limit: int = None,
        backup_rate_limit: int = None,
        backup_strategy_type: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        auto_start_backup: bool = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_user_name = source_endpoint_user_name
        self.source_endpoint_password = source_endpoint_password
        self.backup_gateway_id = backup_gateway_id
        self.ossbucket_name = ossbucket_name
        self.backup_objects = backup_objects
        self.backup_period = backup_period
        self.backup_start_time = backup_start_time
        self.enable_backup_log = enable_backup_log
        self.backup_log_interval_seconds = backup_log_interval_seconds
        self.backup_retention_period = backup_retention_period
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        self.duplication_archive_period = duplication_archive_period
        self.backup_plan_name = backup_plan_name
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.backup_storage_type = backup_storage_type
        self.backup_speed_limit = backup_speed_limit
        self.backup_rate_limit = backup_rate_limit
        self.backup_strategy_type = backup_strategy_type
        self.cross_aliyun_id = cross_aliyun_id
        self.cross_role_name = cross_role_name
        self.auto_start_backup = auto_start_backup
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.ossbucket_name is not None:
            result['OSSBucketName'] = self.ossbucket_name
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        if self.backup_log_interval_seconds is not None:
            result['BackupLogIntervalSeconds'] = self.backup_log_interval_seconds
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period
        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period
        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.backup_storage_type is not None:
            result['BackupStorageType'] = self.backup_storage_type
        if self.backup_speed_limit is not None:
            result['BackupSpeedLimit'] = self.backup_speed_limit
        if self.backup_rate_limit is not None:
            result['BackupRateLimit'] = self.backup_rate_limit
        if self.backup_strategy_type is not None:
            result['BackupStrategyType'] = self.backup_strategy_type
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.auto_start_backup is not None:
            result['AutoStartBackup'] = self.auto_start_backup
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('OSSBucketName') is not None:
            self.ossbucket_name = m.get('OSSBucketName')
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
        if m.get('BackupLogIntervalSeconds') is not None:
            self.backup_log_interval_seconds = m.get('BackupLogIntervalSeconds')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')
        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')
        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('BackupStorageType') is not None:
            self.backup_storage_type = m.get('BackupStorageType')
        if m.get('BackupSpeedLimit') is not None:
            self.backup_speed_limit = m.get('BackupSpeedLimit')
        if m.get('BackupRateLimit') is not None:
            self.backup_rate_limit = m.get('BackupRateLimit')
        if m.get('BackupStrategyType') is not None:
            self.backup_strategy_type = m.get('BackupStrategyType')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('AutoStartBackup') is not None:
            self.auto_start_backup = m.get('AutoStartBackup')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ConfigureBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class ConfigureBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigureBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPlanRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        instance_class: str = None,
        database_type: str = None,
        backup_method: str = None,
        period: str = None,
        used_time: int = None,
        pay_type: str = None,
        database_region: str = None,
        storage_region: str = None,
        instance_type: str = None,
        storage_type: str = None,
        from_app: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.region = region
        self.instance_class = instance_class
        self.database_type = database_type
        self.backup_method = backup_method
        self.period = period
        self.used_time = used_time
        self.pay_type = pay_type
        self.database_region = database_region
        self.storage_region = storage_region
        self.instance_type = instance_type
        self.storage_type = storage_type
        self.from_app = from_app
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.database_region is not None:
            result['DatabaseRegion'] = self.database_region
        if self.storage_region is not None:
            result['StorageRegion'] = self.storage_region
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('DatabaseRegion') is not None:
            self.database_region = m.get('DatabaseRegion')
        if m.get('StorageRegion') is not None:
            self.storage_region = m.get('StorageRegion')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        order_id: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.order_id = order_id
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class CreateBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFullBackupSetDownloadRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        backup_set_data_format: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_set_id = backup_set_id
        self.backup_set_data_format = backup_set_data_format
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_set_data_format is not None:
            result['BackupSetDataFormat'] = self.backup_set_data_format
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSetDataFormat') is not None:
            self.backup_set_data_format = m.get('BackupSetDataFormat')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateFullBackupSetDownloadResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        backup_set_download_task_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.backup_set_download_task_id = backup_set_download_task_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class CreateFullBackupSetDownloadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFullBackupSetDownloadResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFullBackupSetDownloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGetDBListFromAgentTaskRequest(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        database_type: str = None,
        source_endpoint_region: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_port: int = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_gateway_id = backup_gateway_id
        self.database_type = database_type
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_port = source_endpoint_port
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateGetDBListFromAgentTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        request_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class CreateGetDBListFromAgentTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGetDBListFromAgentTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGetDBListFromAgentTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIncrementBackupSetDownloadRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        backup_set_name: str = None,
        backup_set_data_format: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_set_id = backup_set_id
        self.backup_set_name = backup_set_name
        self.backup_set_data_format = backup_set_data_format
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_set_name is not None:
            result['BackupSetName'] = self.backup_set_name
        if self.backup_set_data_format is not None:
            result['BackupSetDataFormat'] = self.backup_set_data_format
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSetName') is not None:
            self.backup_set_name = m.get('BackupSetName')
        if m.get('BackupSetDataFormat') is not None:
            self.backup_set_data_format = m.get('BackupSetDataFormat')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateIncrementBackupSetDownloadResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        backup_set_download_task_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.backup_set_download_task_id = backup_set_download_task_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class CreateIncrementBackupSetDownloadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIncrementBackupSetDownloadResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIncrementBackupSetDownloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRestoreTaskRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_port: int = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_user_name: str = None,
        destination_endpoint_password: str = None,
        backup_gateway_id: int = None,
        restore_objects: str = None,
        restore_time: int = None,
        backup_set_id: str = None,
        restore_task_name: str = None,
        destination_endpoint_oracle_sid: str = None,
        restore_dir: str = None,
        restore_home: str = None,
        duplicate_conflict: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        self.destination_endpoint_region = destination_endpoint_region
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        self.destination_endpoint_ip = destination_endpoint_ip
        self.destination_endpoint_port = destination_endpoint_port
        self.destination_endpoint_database_name = destination_endpoint_database_name
        self.destination_endpoint_user_name = destination_endpoint_user_name
        self.destination_endpoint_password = destination_endpoint_password
        self.backup_gateway_id = backup_gateway_id
        self.restore_objects = restore_objects
        self.restore_time = restore_time
        self.backup_set_id = backup_set_id
        self.restore_task_name = restore_task_name
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        self.restore_dir = restore_dir
        self.restore_home = restore_home
        self.duplicate_conflict = duplicate_conflict
        self.cross_aliyun_id = cross_aliyun_id
        self.cross_role_name = cross_role_name
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id
        if self.destination_endpoint_ip is not None:
            result['DestinationEndpointIP'] = self.destination_endpoint_ip
        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port
        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name
        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name
        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.restore_objects is not None:
            result['RestoreObjects'] = self.restore_objects
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.restore_task_name is not None:
            result['RestoreTaskName'] = self.restore_task_name
        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid
        if self.restore_dir is not None:
            result['RestoreDir'] = self.restore_dir
        if self.restore_home is not None:
            result['RestoreHome'] = self.restore_home
        if self.duplicate_conflict is not None:
            result['DuplicateConflict'] = self.duplicate_conflict
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')
        if m.get('DestinationEndpointIP') is not None:
            self.destination_endpoint_ip = m.get('DestinationEndpointIP')
        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')
        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')
        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')
        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('RestoreObjects') is not None:
            self.restore_objects = m.get('RestoreObjects')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('RestoreTaskName') is not None:
            self.restore_task_name = m.get('RestoreTaskName')
        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')
        if m.get('RestoreDir') is not None:
            self.restore_dir = m.get('RestoreDir')
        if m.get('RestoreHome') is not None:
            self.restore_home = m.get('RestoreHome')
        if m.get('DuplicateConflict') is not None:
            self.duplicate_conflict = m.get('DuplicateConflict')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateRestoreTaskResponseBody(TeaModel):
    def __init__(
        self,
        restore_task_id: str = None,
        request_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.restore_task_id = restore_task_id
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class CreateRestoreTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRestoreTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRestoreTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupGatewayListRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        identifier: str = None,
        page_size: int = None,
        page_num: int = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.region = region
        self.identifier = identifier
        self.page_size = page_size
        self.page_num = page_num
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeBackupGatewayListResponseBodyItemsBackupGateway(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        backup_gateway_create_time: int = None,
        backup_gateway_id: str = None,
        region: str = None,
        identifier: str = None,
        source_endpoint_internet_ip: str = None,
        backup_gateway_status: str = None,
        source_endpoint_intranet_ip: str = None,
        last_heartbeat_time: int = None,
        source_endpoint_hostname: str = None,
    ):
        self.display_name = display_name
        self.backup_gateway_create_time = backup_gateway_create_time
        self.backup_gateway_id = backup_gateway_id
        self.region = region
        self.identifier = identifier
        self.source_endpoint_internet_ip = source_endpoint_internet_ip
        self.backup_gateway_status = backup_gateway_status
        self.source_endpoint_intranet_ip = source_endpoint_intranet_ip
        self.last_heartbeat_time = last_heartbeat_time
        self.source_endpoint_hostname = source_endpoint_hostname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.backup_gateway_create_time is not None:
            result['BackupGatewayCreateTime'] = self.backup_gateway_create_time
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.region is not None:
            result['Region'] = self.region
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.source_endpoint_internet_ip is not None:
            result['SourceEndpointInternetIP'] = self.source_endpoint_internet_ip
        if self.backup_gateway_status is not None:
            result['BackupGatewayStatus'] = self.backup_gateway_status
        if self.source_endpoint_intranet_ip is not None:
            result['SourceEndpointIntranetIP'] = self.source_endpoint_intranet_ip
        if self.last_heartbeat_time is not None:
            result['LastHeartbeatTime'] = self.last_heartbeat_time
        if self.source_endpoint_hostname is not None:
            result['SourceEndpointHostname'] = self.source_endpoint_hostname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('BackupGatewayCreateTime') is not None:
            self.backup_gateway_create_time = m.get('BackupGatewayCreateTime')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('SourceEndpointInternetIP') is not None:
            self.source_endpoint_internet_ip = m.get('SourceEndpointInternetIP')
        if m.get('BackupGatewayStatus') is not None:
            self.backup_gateway_status = m.get('BackupGatewayStatus')
        if m.get('SourceEndpointIntranetIP') is not None:
            self.source_endpoint_intranet_ip = m.get('SourceEndpointIntranetIP')
        if m.get('LastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('LastHeartbeatTime')
        if m.get('SourceEndpointHostname') is not None:
            self.source_endpoint_hostname = m.get('SourceEndpointHostname')
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
        page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        http_status_code: int = None,
        total_elements: int = None,
        total_pages: int = None,
        items: DescribeBackupGatewayListResponseBodyItems = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.page_num = page_num
        self.request_id = request_id
        self.page_size = page_size
        self.http_status_code = http_status_code
        self.total_elements = total_elements
        self.total_pages = total_pages
        self.items = items
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('Items') is not None:
            temp_model = DescribeBackupGatewayListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeBackupGatewayListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupGatewayListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupGatewayListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlanBillingRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        owner_id: str = None,
        client_token: str = None,
        show_storage_type: bool = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.owner_id = owner_id
        self.client_token = client_token
        self.show_storage_type = show_storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.show_storage_type is not None:
            result['ShowStorageType'] = self.show_storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ShowStorageType') is not None:
            self.show_storage_type = m.get('ShowStorageType')
        return self


class DescribeBackupPlanBillingResponseBodyItem(TeaModel):
    def __init__(
        self,
        full_storage_size: int = None,
        buy_create_timestamp: int = None,
        buy_expired_timestamp: int = None,
        quota_end_timestamp: int = None,
        buy_spec: str = None,
        quota_start_timestamp: int = None,
        is_expired: bool = None,
        paied_bytes: int = None,
        total_free_bytes: int = None,
        used_full_bytes: int = None,
        is_free_bytes_unlimited: bool = None,
        cont_storage_size: int = None,
        buy_charge_type: str = None,
        used_increment_bytes: int = None,
    ):
        self.full_storage_size = full_storage_size
        self.buy_create_timestamp = buy_create_timestamp
        self.buy_expired_timestamp = buy_expired_timestamp
        self.quota_end_timestamp = quota_end_timestamp
        self.buy_spec = buy_spec
        self.quota_start_timestamp = quota_start_timestamp
        self.is_expired = is_expired
        self.paied_bytes = paied_bytes
        self.total_free_bytes = total_free_bytes
        self.used_full_bytes = used_full_bytes
        self.is_free_bytes_unlimited = is_free_bytes_unlimited
        self.cont_storage_size = cont_storage_size
        self.buy_charge_type = buy_charge_type
        self.used_increment_bytes = used_increment_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.full_storage_size is not None:
            result['FullStorageSize'] = self.full_storage_size
        if self.buy_create_timestamp is not None:
            result['BuyCreateTimestamp'] = self.buy_create_timestamp
        if self.buy_expired_timestamp is not None:
            result['BuyExpiredTimestamp'] = self.buy_expired_timestamp
        if self.quota_end_timestamp is not None:
            result['QuotaEndTimestamp'] = self.quota_end_timestamp
        if self.buy_spec is not None:
            result['BuySpec'] = self.buy_spec
        if self.quota_start_timestamp is not None:
            result['QuotaStartTimestamp'] = self.quota_start_timestamp
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.paied_bytes is not None:
            result['PaiedBytes'] = self.paied_bytes
        if self.total_free_bytes is not None:
            result['TotalFreeBytes'] = self.total_free_bytes
        if self.used_full_bytes is not None:
            result['UsedFullBytes'] = self.used_full_bytes
        if self.is_free_bytes_unlimited is not None:
            result['IsFreeBytesUnlimited'] = self.is_free_bytes_unlimited
        if self.cont_storage_size is not None:
            result['ContStorageSize'] = self.cont_storage_size
        if self.buy_charge_type is not None:
            result['BuyChargeType'] = self.buy_charge_type
        if self.used_increment_bytes is not None:
            result['UsedIncrementBytes'] = self.used_increment_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullStorageSize') is not None:
            self.full_storage_size = m.get('FullStorageSize')
        if m.get('BuyCreateTimestamp') is not None:
            self.buy_create_timestamp = m.get('BuyCreateTimestamp')
        if m.get('BuyExpiredTimestamp') is not None:
            self.buy_expired_timestamp = m.get('BuyExpiredTimestamp')
        if m.get('QuotaEndTimestamp') is not None:
            self.quota_end_timestamp = m.get('QuotaEndTimestamp')
        if m.get('BuySpec') is not None:
            self.buy_spec = m.get('BuySpec')
        if m.get('QuotaStartTimestamp') is not None:
            self.quota_start_timestamp = m.get('QuotaStartTimestamp')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('PaiedBytes') is not None:
            self.paied_bytes = m.get('PaiedBytes')
        if m.get('TotalFreeBytes') is not None:
            self.total_free_bytes = m.get('TotalFreeBytes')
        if m.get('UsedFullBytes') is not None:
            self.used_full_bytes = m.get('UsedFullBytes')
        if m.get('IsFreeBytesUnlimited') is not None:
            self.is_free_bytes_unlimited = m.get('IsFreeBytesUnlimited')
        if m.get('ContStorageSize') is not None:
            self.cont_storage_size = m.get('ContStorageSize')
        if m.get('BuyChargeType') is not None:
            self.buy_charge_type = m.get('BuyChargeType')
        if m.get('UsedIncrementBytes') is not None:
            self.used_increment_bytes = m.get('UsedIncrementBytes')
        return self


class DescribeBackupPlanBillingResponseBody(TeaModel):
    def __init__(
        self,
        item: DescribeBackupPlanBillingResponseBodyItem = None,
        request_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.item = item
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        result = dict()
        if self.item is not None:
            result['Item'] = self.item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            temp_model = DescribeBackupPlanBillingResponseBodyItem()
            self.item = temp_model.from_map(m['Item'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeBackupPlanBillingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupPlanBillingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupPlanBillingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlanListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        region: str = None,
        page_size: int = None,
        page_num: int = None,
        backup_plan_name: str = None,
        backup_plan_status: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.region = region
        self.page_size = page_size
        self.page_num = page_num
        self.backup_plan_name = backup_plan_name
        self.backup_plan_status = backup_plan_status
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.region is not None:
            result['Region'] = self.region
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name
        if self.backup_plan_status is not None:
            result['BackupPlanStatus'] = self.backup_plan_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')
        if m.get('BackupPlanStatus') is not None:
            self.backup_plan_status = m.get('BackupPlanStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeBackupPlanListResponseBodyItemsBackupPlanDetail(TeaModel):
    def __init__(
        self,
        cross_role_name: str = None,
        source_endpoint_instance_type: str = None,
        backup_set_download_dir: str = None,
        source_endpoint_ip_port: str = None,
        cross_aliyun_id: str = None,
        duplication_archive_period: int = None,
        backup_plan_id: str = None,
        end_timestamp_for_restore: int = None,
        backup_plan_status: str = None,
        backup_set_download_full_data_format: str = None,
        backup_retention_period: int = None,
        ossbucket_region: str = None,
        source_endpoint_oracle_sid: str = None,
        backup_storage_type: str = None,
        backup_method: str = None,
        source_endpoint_region: str = None,
        source_endpoint_database_name: str = None,
        backup_period: str = None,
        backup_set_download_gateway_id: int = None,
        instance_class: str = None,
        backup_plan_create_time: int = None,
        backup_start_time: str = None,
        duplication_infrequent_access_period: int = None,
        backup_set_download_target_type: str = None,
        err_message: str = None,
        backup_objects: str = None,
        begin_timestamp_for_restore: int = None,
        source_endpoint_instance_id: str = None,
        open_backup_set_auto_download: bool = None,
        backup_plan_name: str = None,
        ossbucket_name: str = None,
        backup_gateway_id: int = None,
        source_endpoint_user_name: str = None,
        backup_set_download_increment_data_format: str = None,
        enable_backup_log: bool = None,
    ):
        self.cross_role_name = cross_role_name
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.backup_set_download_dir = backup_set_download_dir
        self.source_endpoint_ip_port = source_endpoint_ip_port
        self.cross_aliyun_id = cross_aliyun_id
        self.duplication_archive_period = duplication_archive_period
        self.backup_plan_id = backup_plan_id
        self.end_timestamp_for_restore = end_timestamp_for_restore
        self.backup_plan_status = backup_plan_status
        self.backup_set_download_full_data_format = backup_set_download_full_data_format
        self.backup_retention_period = backup_retention_period
        self.ossbucket_region = ossbucket_region
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.backup_storage_type = backup_storage_type
        self.backup_method = backup_method
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_database_name = source_endpoint_database_name
        self.backup_period = backup_period
        self.backup_set_download_gateway_id = backup_set_download_gateway_id
        self.instance_class = instance_class
        self.backup_plan_create_time = backup_plan_create_time
        self.backup_start_time = backup_start_time
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        self.backup_set_download_target_type = backup_set_download_target_type
        self.err_message = err_message
        self.backup_objects = backup_objects
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.open_backup_set_auto_download = open_backup_set_auto_download
        self.backup_plan_name = backup_plan_name
        self.ossbucket_name = ossbucket_name
        self.backup_gateway_id = backup_gateway_id
        self.source_endpoint_user_name = source_endpoint_user_name
        self.backup_set_download_increment_data_format = backup_set_download_increment_data_format
        self.enable_backup_log = enable_backup_log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.backup_set_download_dir is not None:
            result['BackupSetDownloadDir'] = self.backup_set_download_dir
        if self.source_endpoint_ip_port is not None:
            result['SourceEndpointIpPort'] = self.source_endpoint_ip_port
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore
        if self.backup_plan_status is not None:
            result['BackupPlanStatus'] = self.backup_plan_status
        if self.backup_set_download_full_data_format is not None:
            result['BackupSetDownloadFullDataFormat'] = self.backup_set_download_full_data_format
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.ossbucket_region is not None:
            result['OSSBucketRegion'] = self.ossbucket_region
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.backup_storage_type is not None:
            result['BackupStorageType'] = self.backup_storage_type
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_set_download_gateway_id is not None:
            result['BackupSetDownloadGatewayId'] = self.backup_set_download_gateway_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.backup_plan_create_time is not None:
            result['BackupPlanCreateTime'] = self.backup_plan_create_time
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period
        if self.backup_set_download_target_type is not None:
            result['BackupSetDownloadTargetType'] = self.backup_set_download_target_type
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.open_backup_set_auto_download is not None:
            result['OpenBackupSetAutoDownload'] = self.open_backup_set_auto_download
        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name
        if self.ossbucket_name is not None:
            result['OSSBucketName'] = self.ossbucket_name
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        if self.backup_set_download_increment_data_format is not None:
            result['BackupSetDownloadIncrementDataFormat'] = self.backup_set_download_increment_data_format
        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('BackupSetDownloadDir') is not None:
            self.backup_set_download_dir = m.get('BackupSetDownloadDir')
        if m.get('SourceEndpointIpPort') is not None:
            self.source_endpoint_ip_port = m.get('SourceEndpointIpPort')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')
        if m.get('BackupPlanStatus') is not None:
            self.backup_plan_status = m.get('BackupPlanStatus')
        if m.get('BackupSetDownloadFullDataFormat') is not None:
            self.backup_set_download_full_data_format = m.get('BackupSetDownloadFullDataFormat')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('OSSBucketRegion') is not None:
            self.ossbucket_region = m.get('OSSBucketRegion')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('BackupStorageType') is not None:
            self.backup_storage_type = m.get('BackupStorageType')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupSetDownloadGatewayId') is not None:
            self.backup_set_download_gateway_id = m.get('BackupSetDownloadGatewayId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('BackupPlanCreateTime') is not None:
            self.backup_plan_create_time = m.get('BackupPlanCreateTime')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')
        if m.get('BackupSetDownloadTargetType') is not None:
            self.backup_set_download_target_type = m.get('BackupSetDownloadTargetType')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('OpenBackupSetAutoDownload') is not None:
            self.open_backup_set_auto_download = m.get('OpenBackupSetAutoDownload')
        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')
        if m.get('OSSBucketName') is not None:
            self.ossbucket_name = m.get('OSSBucketName')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        if m.get('BackupSetDownloadIncrementDataFormat') is not None:
            self.backup_set_download_increment_data_format = m.get('BackupSetDownloadIncrementDataFormat')
        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')
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
        page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        http_status_code: int = None,
        total_elements: int = None,
        total_pages: int = None,
        items: DescribeBackupPlanListResponseBodyItems = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.page_num = page_num
        self.request_id = request_id
        self.page_size = page_size
        self.http_status_code = http_status_code
        self.total_elements = total_elements
        self.total_pages = total_pages
        self.items = items
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('Items') is not None:
            temp_model = DescribeBackupPlanListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeBackupPlanListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupPlanListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupPlanListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupSetDownloadTaskListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_set_download_task_id: str = None,
        page_size: int = None,
        page_num: int = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.backup_set_download_task_id = backup_set_download_task_id
        self.page_size = page_size
        self.page_num = page_num
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeBackupSetDownloadTaskListResponseBodyItemsBackupSetDownloadTaskDetail(TeaModel):
    def __init__(
        self,
        backup_set_download_status: str = None,
        backup_set_data_size: int = None,
        backup_set_download_dir: str = None,
        backup_set_download_target_type: str = None,
        err_message: str = None,
        backup_plan_id: str = None,
        backup_set_download_create_time: int = None,
        backup_set_db_type: str = None,
        backup_set_download_internet_url: str = None,
        backup_set_id: str = None,
        backup_gateway_id: int = None,
        backup_set_download_intranet_url: str = None,
        backup_set_download_way: str = None,
        backup_set_download_finish_time: int = None,
        backup_set_job_type: str = None,
        backup_set_download_task_id: str = None,
        backup_set_download_task_name: str = None,
        backup_set_data_format: str = None,
        backup_set_code: str = None,
    ):
        self.backup_set_download_status = backup_set_download_status
        self.backup_set_data_size = backup_set_data_size
        self.backup_set_download_dir = backup_set_download_dir
        self.backup_set_download_target_type = backup_set_download_target_type
        self.err_message = err_message
        self.backup_plan_id = backup_plan_id
        self.backup_set_download_create_time = backup_set_download_create_time
        self.backup_set_db_type = backup_set_db_type
        self.backup_set_download_internet_url = backup_set_download_internet_url
        self.backup_set_id = backup_set_id
        self.backup_gateway_id = backup_gateway_id
        self.backup_set_download_intranet_url = backup_set_download_intranet_url
        self.backup_set_download_way = backup_set_download_way
        self.backup_set_download_finish_time = backup_set_download_finish_time
        self.backup_set_job_type = backup_set_job_type
        self.backup_set_download_task_id = backup_set_download_task_id
        self.backup_set_download_task_name = backup_set_download_task_name
        self.backup_set_data_format = backup_set_data_format
        self.backup_set_code = backup_set_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_set_download_status is not None:
            result['BackupSetDownloadStatus'] = self.backup_set_download_status
        if self.backup_set_data_size is not None:
            result['BackupSetDataSize'] = self.backup_set_data_size
        if self.backup_set_download_dir is not None:
            result['BackupSetDownloadDir'] = self.backup_set_download_dir
        if self.backup_set_download_target_type is not None:
            result['BackupSetDownloadTargetType'] = self.backup_set_download_target_type
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_set_download_create_time is not None:
            result['BackupSetDownloadCreateTime'] = self.backup_set_download_create_time
        if self.backup_set_db_type is not None:
            result['BackupSetDbType'] = self.backup_set_db_type
        if self.backup_set_download_internet_url is not None:
            result['BackupSetDownloadInternetUrl'] = self.backup_set_download_internet_url
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_set_download_intranet_url is not None:
            result['BackupSetDownloadIntranetUrl'] = self.backup_set_download_intranet_url
        if self.backup_set_download_way is not None:
            result['BackupSetDownloadWay'] = self.backup_set_download_way
        if self.backup_set_download_finish_time is not None:
            result['BackupSetDownloadFinishTime'] = self.backup_set_download_finish_time
        if self.backup_set_job_type is not None:
            result['BackupSetJobType'] = self.backup_set_job_type
        if self.backup_set_download_task_id is not None:
            result['BackupSetDownloadTaskId'] = self.backup_set_download_task_id
        if self.backup_set_download_task_name is not None:
            result['BackupSetDownloadTaskName'] = self.backup_set_download_task_name
        if self.backup_set_data_format is not None:
            result['BackupSetDataFormat'] = self.backup_set_data_format
        if self.backup_set_code is not None:
            result['BackupSetCode'] = self.backup_set_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetDownloadStatus') is not None:
            self.backup_set_download_status = m.get('BackupSetDownloadStatus')
        if m.get('BackupSetDataSize') is not None:
            self.backup_set_data_size = m.get('BackupSetDataSize')
        if m.get('BackupSetDownloadDir') is not None:
            self.backup_set_download_dir = m.get('BackupSetDownloadDir')
        if m.get('BackupSetDownloadTargetType') is not None:
            self.backup_set_download_target_type = m.get('BackupSetDownloadTargetType')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetDownloadCreateTime') is not None:
            self.backup_set_download_create_time = m.get('BackupSetDownloadCreateTime')
        if m.get('BackupSetDbType') is not None:
            self.backup_set_db_type = m.get('BackupSetDbType')
        if m.get('BackupSetDownloadInternetUrl') is not None:
            self.backup_set_download_internet_url = m.get('BackupSetDownloadInternetUrl')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupSetDownloadIntranetUrl') is not None:
            self.backup_set_download_intranet_url = m.get('BackupSetDownloadIntranetUrl')
        if m.get('BackupSetDownloadWay') is not None:
            self.backup_set_download_way = m.get('BackupSetDownloadWay')
        if m.get('BackupSetDownloadFinishTime') is not None:
            self.backup_set_download_finish_time = m.get('BackupSetDownloadFinishTime')
        if m.get('BackupSetJobType') is not None:
            self.backup_set_job_type = m.get('BackupSetJobType')
        if m.get('BackupSetDownloadTaskId') is not None:
            self.backup_set_download_task_id = m.get('BackupSetDownloadTaskId')
        if m.get('BackupSetDownloadTaskName') is not None:
            self.backup_set_download_task_name = m.get('BackupSetDownloadTaskName')
        if m.get('BackupSetDataFormat') is not None:
            self.backup_set_data_format = m.get('BackupSetDataFormat')
        if m.get('BackupSetCode') is not None:
            self.backup_set_code = m.get('BackupSetCode')
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
        page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        http_status_code: int = None,
        total_elements: int = None,
        total_pages: int = None,
        items: DescribeBackupSetDownloadTaskListResponseBodyItems = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.page_num = page_num
        self.request_id = request_id
        self.page_size = page_size
        self.http_status_code = http_status_code
        self.total_elements = total_elements
        self.total_pages = total_pages
        self.items = items
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('Items') is not None:
            temp_model = DescribeBackupSetDownloadTaskListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeBackupSetDownloadTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupSetDownloadTaskListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBackupSetDownloadTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFullBackupListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        page_size: int = None,
        page_num: int = None,
        owner_id: str = None,
        client_token: str = None,
        show_storage_type: bool = None,
        backup_set_id: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.page_size = page_size
        self.page_num = page_num
        self.owner_id = owner_id
        self.client_token = client_token
        self.show_storage_type = show_storage_type
        self.backup_set_id = backup_set_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.show_storage_type is not None:
            result['ShowStorageType'] = self.show_storage_type
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ShowStorageType') is not None:
            self.show_storage_type = m.get('ShowStorageType')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        return self


class DescribeFullBackupListResponseBodyItemsFullBackupFile(TeaModel):
    def __init__(
        self,
        finish_time: int = None,
        backup_status: str = None,
        create_time: int = None,
        source_endpoint_ip_port: str = None,
        backup_objects: str = None,
        err_message: str = None,
        end_time: int = None,
        backup_set_expired_time: int = None,
        start_time: int = None,
        storage_method: str = None,
        backup_set_id: str = None,
        backup_size: int = None,
    ):
        self.finish_time = finish_time
        self.backup_status = backup_status
        self.create_time = create_time
        self.source_endpoint_ip_port = source_endpoint_ip_port
        self.backup_objects = backup_objects
        self.err_message = err_message
        self.end_time = end_time
        self.backup_set_expired_time = backup_set_expired_time
        self.start_time = start_time
        self.storage_method = storage_method
        self.backup_set_id = backup_set_id
        self.backup_size = backup_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_endpoint_ip_port is not None:
            result['SourceEndpointIpPort'] = self.source_endpoint_ip_port
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.backup_set_expired_time is not None:
            result['BackupSetExpiredTime'] = self.backup_set_expired_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage_method is not None:
            result['StorageMethod'] = self.storage_method
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceEndpointIpPort') is not None:
            self.source_endpoint_ip_port = m.get('SourceEndpointIpPort')
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BackupSetExpiredTime') is not None:
            self.backup_set_expired_time = m.get('BackupSetExpiredTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StorageMethod') is not None:
            self.storage_method = m.get('StorageMethod')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
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
        page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        http_status_code: int = None,
        total_elements: int = None,
        total_pages: int = None,
        items: DescribeFullBackupListResponseBodyItems = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.page_num = page_num
        self.request_id = request_id
        self.page_size = page_size
        self.http_status_code = http_status_code
        self.total_elements = total_elements
        self.total_pages = total_pages
        self.items = items
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('Items') is not None:
            temp_model = DescribeFullBackupListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeFullBackupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFullBackupListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFullBackupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIncrementBackupListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        page_size: int = None,
        page_num: int = None,
        owner_id: str = None,
        client_token: str = None,
        show_storage_type: bool = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.page_size = page_size
        self.page_num = page_num
        self.owner_id = owner_id
        self.client_token = client_token
        self.show_storage_type = show_storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.show_storage_type is not None:
            result['ShowStorageType'] = self.show_storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ShowStorageType') is not None:
            self.show_storage_type = m.get('ShowStorageType')
        return self


class DescribeIncrementBackupListResponseBodyItemsIncrementBackupFile(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        backup_set_expired_time: int = None,
        start_time: int = None,
        storage_method: str = None,
        backup_set_job_id: str = None,
        backup_set_id: str = None,
        backup_status: str = None,
        source_endpoint_ip_port: str = None,
        backup_size: int = None,
    ):
        self.end_time = end_time
        self.backup_set_expired_time = backup_set_expired_time
        self.start_time = start_time
        self.storage_method = storage_method
        self.backup_set_job_id = backup_set_job_id
        self.backup_set_id = backup_set_id
        self.backup_status = backup_status
        self.source_endpoint_ip_port = source_endpoint_ip_port
        self.backup_size = backup_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.backup_set_expired_time is not None:
            result['BackupSetExpiredTime'] = self.backup_set_expired_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage_method is not None:
            result['StorageMethod'] = self.storage_method
        if self.backup_set_job_id is not None:
            result['BackupSetJobId'] = self.backup_set_job_id
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.source_endpoint_ip_port is not None:
            result['SourceEndpointIpPort'] = self.source_endpoint_ip_port
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BackupSetExpiredTime') is not None:
            self.backup_set_expired_time = m.get('BackupSetExpiredTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StorageMethod') is not None:
            self.storage_method = m.get('StorageMethod')
        if m.get('BackupSetJobId') is not None:
            self.backup_set_job_id = m.get('BackupSetJobId')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('SourceEndpointIpPort') is not None:
            self.source_endpoint_ip_port = m.get('SourceEndpointIpPort')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
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
        page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        http_status_code: int = None,
        total_elements: int = None,
        total_pages: int = None,
        items: DescribeIncrementBackupListResponseBodyItems = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.page_num = page_num
        self.request_id = request_id
        self.page_size = page_size
        self.http_status_code = http_status_code
        self.total_elements = total_elements
        self.total_pages = total_pages
        self.items = items
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('Items') is not None:
            temp_model = DescribeIncrementBackupListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeIncrementBackupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIncrementBackupListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIncrementBackupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobErrorCodeRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        language: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.task_id = task_id
        self.language = language
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeJobErrorCodeResponseBodyItem(TeaModel):
    def __init__(
        self,
        job_state: str = None,
        error_message: str = None,
        error_code: str = None,
        job_id: str = None,
        job_type: str = None,
        language: str = None,
    ):
        self.job_state = job_state
        self.error_message = error_message
        self.error_code = error_code
        self.job_id = job_id
        self.job_type = job_type
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_state is not None:
            result['JobState'] = self.job_state
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class DescribeJobErrorCodeResponseBody(TeaModel):
    def __init__(
        self,
        item: DescribeJobErrorCodeResponseBodyItem = None,
        request_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.item = item
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        result = dict()
        if self.item is not None:
            result['Item'] = self.item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            temp_model = DescribeJobErrorCodeResponseBodyItem()
            self.item = temp_model.from_map(m['Item'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeJobErrorCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJobErrorCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeJobErrorCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeCidrListRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.region = region
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        request_id: str = None,
        internet_ips: DescribeNodeCidrListResponseBodyInternetIPs = None,
        http_status_code: int = None,
        intranet_ips: DescribeNodeCidrListResponseBodyIntranetIPs = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.internet_ips = internet_ips
        self.http_status_code = http_status_code
        self.intranet_ips = intranet_ips
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.internet_ips:
            self.internet_ips.validate()
        if self.intranet_ips:
            self.intranet_ips.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.internet_ips is not None:
            result['InternetIPs'] = self.internet_ips.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.intranet_ips is not None:
            result['IntranetIPs'] = self.intranet_ips.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InternetIPs') is not None:
            temp_model = DescribeNodeCidrListResponseBodyInternetIPs()
            self.internet_ips = temp_model.from_map(m['InternetIPs'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('IntranetIPs') is not None:
            temp_model = DescribeNodeCidrListResponseBodyIntranetIPs()
            self.intranet_ips = temp_model.from_map(m['IntranetIPs'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeNodeCidrListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNodeCidrListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNodeCidrListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePreCheckProgressListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        restore_task_id: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.restore_task_id = restore_task_id
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribePreCheckProgressListResponseBodyItemsPreCheckProgressDetail(TeaModel):
    def __init__(
        self,
        finish_time: int = None,
        state: str = None,
        boot_time: int = None,
        job_id: str = None,
        item: str = None,
        err_msg: str = None,
        order_num: str = None,
        names: str = None,
    ):
        self.finish_time = finish_time
        self.state = state
        self.boot_time = boot_time
        self.job_id = job_id
        self.item = item
        self.err_msg = err_msg
        self.order_num = order_num
        self.names = names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.state is not None:
            result['State'] = self.state
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.item is not None:
            result['Item'] = self.item
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('Names') is not None:
            self.names = m.get('Names')
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
        status: str = None,
        progress: int = None,
        request_id: str = None,
        http_status_code: int = None,
        items: DescribePreCheckProgressListResponseBodyItems = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.status = status
        self.progress = progress
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.items = items
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribePreCheckProgressListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribePreCheckProgressListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePreCheckProgressListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePreCheckProgressListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        request_id: str = None,
        http_status_code: int = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.regions = regions
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreRangeInfoRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        begin_timestamp_for_restore: int = None,
        end_timestamp_for_restore: int = None,
        owner_id: str = None,
        client_token: str = None,
        recently_restore: bool = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        self.end_timestamp_for_restore = end_timestamp_for_restore
        self.owner_id = owner_id
        self.client_token = client_token
        self.recently_restore = recently_restore

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore
        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.recently_restore is not None:
            result['RecentlyRestore'] = self.recently_restore
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')
        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RecentlyRestore') is not None:
            self.recently_restore = m.get('RecentlyRestore')
        return self


class DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupListFullBackupDetail(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        backup_set_id: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.backup_set_id = backup_set_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
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
        end_timestamp_for_restore: int = None,
        source_endpoint_instance_type: str = None,
        full_backup_list: DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupList = None,
        range_type: str = None,
        begin_timestamp_for_restore: int = None,
        source_endpoint_instance_id: str = None,
    ):
        self.end_timestamp_for_restore = end_timestamp_for_restore
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.full_backup_list = full_backup_list
        self.range_type = range_type
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        self.source_endpoint_instance_id = source_endpoint_instance_id

    def validate(self):
        if self.full_backup_list:
            self.full_backup_list.validate()

    def to_map(self):
        result = dict()
        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.full_backup_list is not None:
            result['FullBackupList'] = self.full_backup_list.to_map()
        if self.range_type is not None:
            result['RangeType'] = self.range_type
        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('FullBackupList') is not None:
            temp_model = DescribeRestoreRangeInfoResponseBodyItemsDBSRecoverRangeFullBackupList()
            self.full_backup_list = temp_model.from_map(m['FullBackupList'])
        if m.get('RangeType') is not None:
            self.range_type = m.get('RangeType')
        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
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
        request_id: str = None,
        http_status_code: int = None,
        items: DescribeRestoreRangeInfoResponseBodyItems = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.items = items
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Items') is not None:
            temp_model = DescribeRestoreRangeInfoResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeRestoreRangeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRestoreRangeInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRestoreRangeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreTaskListRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        restore_task_id: str = None,
        page_size: int = None,
        page_num: int = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.restore_task_id = restore_task_id
        self.page_size = page_size
        self.page_num = page_num
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DescribeRestoreTaskListResponseBodyItemsRestoreTaskDetail(TeaModel):
    def __init__(
        self,
        restore_status: str = None,
        full_stru_after_restore_progress: int = None,
        cross_role_name: str = None,
        restore_dir: str = None,
        cross_aliyun_id: str = None,
        restore_objects: str = None,
        backup_plan_id: str = None,
        destination_endpoint_region: str = None,
        restore_task_create_time: int = None,
        destination_endpoint_user_name: str = None,
        restore_task_finish_time: int = None,
        destination_endpoint_ip_port: str = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_instance_type: str = None,
        full_strufore_restore_progress: int = None,
        err_message: str = None,
        restore_task_id: str = None,
        full_data_restore_progress: int = None,
        continuous_restore_progress: int = None,
        destination_endpoint_instance_id: str = None,
        backup_set_id: str = None,
        restore_task_name: str = None,
        backup_gateway_id: int = None,
        restore_time: int = None,
    ):
        self.restore_status = restore_status
        self.full_stru_after_restore_progress = full_stru_after_restore_progress
        self.cross_role_name = cross_role_name
        self.restore_dir = restore_dir
        self.cross_aliyun_id = cross_aliyun_id
        self.restore_objects = restore_objects
        self.backup_plan_id = backup_plan_id
        self.destination_endpoint_region = destination_endpoint_region
        self.restore_task_create_time = restore_task_create_time
        self.destination_endpoint_user_name = destination_endpoint_user_name
        self.restore_task_finish_time = restore_task_finish_time
        self.destination_endpoint_ip_port = destination_endpoint_ip_port
        self.destination_endpoint_database_name = destination_endpoint_database_name
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        self.full_strufore_restore_progress = full_strufore_restore_progress
        self.err_message = err_message
        self.restore_task_id = restore_task_id
        self.full_data_restore_progress = full_data_restore_progress
        self.continuous_restore_progress = continuous_restore_progress
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        self.backup_set_id = backup_set_id
        self.restore_task_name = restore_task_name
        self.backup_gateway_id = backup_gateway_id
        self.restore_time = restore_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status
        if self.full_stru_after_restore_progress is not None:
            result['FullStruAfterRestoreProgress'] = self.full_stru_after_restore_progress
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.restore_dir is not None:
            result['RestoreDir'] = self.restore_dir
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.restore_objects is not None:
            result['RestoreObjects'] = self.restore_objects
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.restore_task_create_time is not None:
            result['RestoreTaskCreateTime'] = self.restore_task_create_time
        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name
        if self.restore_task_finish_time is not None:
            result['RestoreTaskFinishTime'] = self.restore_task_finish_time
        if self.destination_endpoint_ip_port is not None:
            result['DestinationEndpointIpPort'] = self.destination_endpoint_ip_port
        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name
        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid
        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type
        if self.full_strufore_restore_progress is not None:
            result['FullStruforeRestoreProgress'] = self.full_strufore_restore_progress
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.full_data_restore_progress is not None:
            result['FullDataRestoreProgress'] = self.full_data_restore_progress
        if self.continuous_restore_progress is not None:
            result['ContinuousRestoreProgress'] = self.continuous_restore_progress
        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.restore_task_name is not None:
            result['RestoreTaskName'] = self.restore_task_name
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')
        if m.get('FullStruAfterRestoreProgress') is not None:
            self.full_stru_after_restore_progress = m.get('FullStruAfterRestoreProgress')
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('RestoreDir') is not None:
            self.restore_dir = m.get('RestoreDir')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('RestoreObjects') is not None:
            self.restore_objects = m.get('RestoreObjects')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('RestoreTaskCreateTime') is not None:
            self.restore_task_create_time = m.get('RestoreTaskCreateTime')
        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')
        if m.get('RestoreTaskFinishTime') is not None:
            self.restore_task_finish_time = m.get('RestoreTaskFinishTime')
        if m.get('DestinationEndpointIpPort') is not None:
            self.destination_endpoint_ip_port = m.get('DestinationEndpointIpPort')
        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')
        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')
        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')
        if m.get('FullStruforeRestoreProgress') is not None:
            self.full_strufore_restore_progress = m.get('FullStruforeRestoreProgress')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('FullDataRestoreProgress') is not None:
            self.full_data_restore_progress = m.get('FullDataRestoreProgress')
        if m.get('ContinuousRestoreProgress') is not None:
            self.continuous_restore_progress = m.get('ContinuousRestoreProgress')
        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('RestoreTaskName') is not None:
            self.restore_task_name = m.get('RestoreTaskName')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
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
        page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        http_status_code: int = None,
        total_elements: int = None,
        total_pages: int = None,
        items: DescribeRestoreTaskListResponseBodyItems = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.page_num = page_num
        self.request_id = request_id
        self.page_size = page_size
        self.http_status_code = http_status_code
        self.total_elements = total_elements
        self.total_pages = total_pages
        self.items = items
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('Items') is not None:
            temp_model = DescribeRestoreTaskListResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DescribeRestoreTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRestoreTaskListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRestoreTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableBackupLogRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DisableBackupLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        need_precheck: bool = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.need_precheck = need_precheck
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class DisableBackupLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableBackupLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableBackupLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableBackupLogRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class EnableBackupLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        need_precheck: bool = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.need_precheck = need_precheck
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class EnableBackupLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableBackupLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableBackupLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDBListFromAgentRequest(TeaModel):
    def __init__(
        self,
        backup_gateway_id: int = None,
        source_endpoint_region: str = None,
        task_id: int = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_gateway_id = backup_gateway_id
        self.source_endpoint_region = source_endpoint_region
        self.task_id = task_id
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        request_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        db_list: GetDBListFromAgentResponseBodyDbList = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.db_list = db_list
        self.err_code = err_code

    def validate(self):
        if self.db_list:
            self.db_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.db_list is not None:
            result['DbList'] = self.db_list.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('DbList') is not None:
            temp_model = GetDBListFromAgentResponseBodyDbList()
            self.db_list = temp_model.from_map(m['DbList'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class GetDBListFromAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDBListFromAgentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDBListFromAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupObjectsRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_objects: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.backup_objects = backup_objects
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyBackupObjectsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        need_precheck: bool = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.need_precheck = need_precheck
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class ModifyBackupObjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupObjectsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBackupObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPlanNameRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_plan_name: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.backup_plan_name = backup_plan_name
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_plan_name is not None:
            result['BackupPlanName'] = self.backup_plan_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupPlanName') is not None:
            self.backup_plan_name = m.get('BackupPlanName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyBackupPlanNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class ModifyBackupPlanNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupPlanNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBackupPlanNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupSetDownloadRulesRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        open_auto_download: bool = None,
        backup_gateway_id: int = None,
        full_data_format: str = None,
        increment_data_format: str = None,
        backup_set_download_dir: str = None,
        backup_set_download_target_type: str = None,
        backup_set_download_target_type_location: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.open_auto_download = open_auto_download
        self.backup_gateway_id = backup_gateway_id
        self.full_data_format = full_data_format
        self.increment_data_format = increment_data_format
        self.backup_set_download_dir = backup_set_download_dir
        self.backup_set_download_target_type = backup_set_download_target_type
        self.backup_set_download_target_type_location = backup_set_download_target_type_location
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.open_auto_download is not None:
            result['OpenAutoDownload'] = self.open_auto_download
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.full_data_format is not None:
            result['FullDataFormat'] = self.full_data_format
        if self.increment_data_format is not None:
            result['IncrementDataFormat'] = self.increment_data_format
        if self.backup_set_download_dir is not None:
            result['BackupSetDownloadDir'] = self.backup_set_download_dir
        if self.backup_set_download_target_type is not None:
            result['BackupSetDownloadTargetType'] = self.backup_set_download_target_type
        if self.backup_set_download_target_type_location is not None:
            result['BackupSetDownloadTargetTypeLocation'] = self.backup_set_download_target_type_location
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('OpenAutoDownload') is not None:
            self.open_auto_download = m.get('OpenAutoDownload')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('FullDataFormat') is not None:
            self.full_data_format = m.get('FullDataFormat')
        if m.get('IncrementDataFormat') is not None:
            self.increment_data_format = m.get('IncrementDataFormat')
        if m.get('BackupSetDownloadDir') is not None:
            self.backup_set_download_dir = m.get('BackupSetDownloadDir')
        if m.get('BackupSetDownloadTargetType') is not None:
            self.backup_set_download_target_type = m.get('BackupSetDownloadTargetType')
        if m.get('BackupSetDownloadTargetTypeLocation') is not None:
            self.backup_set_download_target_type_location = m.get('BackupSetDownloadTargetTypeLocation')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyBackupSetDownloadRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class ModifyBackupSetDownloadRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupSetDownloadRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBackupSetDownloadRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupSourceEndpointRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_region: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_port: int = None,
        source_endpoint_database_name: str = None,
        source_endpoint_user_name: str = None,
        source_endpoint_password: str = None,
        backup_gateway_id: int = None,
        backup_objects: str = None,
        source_endpoint_oracle_sid: str = None,
        cross_aliyun_id: str = None,
        cross_role_name: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_user_name = source_endpoint_user_name
        self.source_endpoint_password = source_endpoint_password
        self.backup_gateway_id = backup_gateway_id
        self.backup_objects = backup_objects
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.cross_aliyun_id = cross_aliyun_id
        self.cross_role_name = cross_role_name
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password
        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id
        if self.backup_objects is not None:
            result['BackupObjects'] = self.backup_objects
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.cross_aliyun_id is not None:
            result['CrossAliyunId'] = self.cross_aliyun_id
        if self.cross_role_name is not None:
            result['CrossRoleName'] = self.cross_role_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')
        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')
        if m.get('BackupObjects') is not None:
            self.backup_objects = m.get('BackupObjects')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('CrossAliyunId') is not None:
            self.cross_aliyun_id = m.get('CrossAliyunId')
        if m.get('CrossRoleName') is not None:
            self.cross_role_name = m.get('CrossRoleName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyBackupSourceEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        need_precheck: bool = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.need_precheck = need_precheck
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class ModifyBackupSourceEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupSourceEndpointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBackupSourceEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupStrategyRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_period: str = None,
        backup_start_time: str = None,
        backup_strategy_type: str = None,
        backup_log_interval_seconds: int = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.backup_period = backup_period
        self.backup_start_time = backup_start_time
        self.backup_strategy_type = backup_strategy_type
        self.backup_log_interval_seconds = backup_log_interval_seconds
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_strategy_type is not None:
            result['BackupStrategyType'] = self.backup_strategy_type
        if self.backup_log_interval_seconds is not None:
            result['BackupLogIntervalSeconds'] = self.backup_log_interval_seconds
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStrategyType') is not None:
            self.backup_strategy_type = m.get('BackupStrategyType')
        if m.get('BackupLogIntervalSeconds') is not None:
            self.backup_log_interval_seconds = m.get('BackupLogIntervalSeconds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyBackupStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        need_precheck: bool = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.need_precheck = need_precheck
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class ModifyBackupStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupStrategyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBackupStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyStorageStrategyRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_retention_period: int = None,
        duplication_infrequent_access_period: int = None,
        duplication_archive_period: int = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.backup_retention_period = backup_retention_period
        self.duplication_infrequent_access_period = duplication_infrequent_access_period
        self.duplication_archive_period = duplication_archive_period
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.duplication_infrequent_access_period is not None:
            result['DuplicationInfrequentAccessPeriod'] = self.duplication_infrequent_access_period
        if self.duplication_archive_period is not None:
            result['DuplicationArchivePeriod'] = self.duplication_archive_period
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('DuplicationInfrequentAccessPeriod') is not None:
            self.duplication_infrequent_access_period = m.get('DuplicationInfrequentAccessPeriod')
        if m.get('DuplicationArchivePeriod') is not None:
            self.duplication_archive_period = m.get('DuplicationArchivePeriod')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyStorageStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        need_precheck: bool = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.need_precheck = need_precheck
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class ModifyStorageStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyStorageStrategyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyStorageStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ReleaseBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class ReleaseBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        period: str = None,
        used_time: int = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.period = period
        self.used_time = used_time
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RenewBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        order_id: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.order_id = order_id
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class RenewBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StartBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class StartBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRestoreTaskRequest(TeaModel):
    def __init__(
        self,
        restore_task_id: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.restore_task_id = restore_task_id
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StartRestoreTaskResponseBody(TeaModel):
    def __init__(
        self,
        restore_task_id: str = None,
        request_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.restore_task_id = restore_task_id
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.restore_task_id is not None:
            result['RestoreTaskId'] = self.restore_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreTaskId') is not None:
            self.restore_task_id = m.get('RestoreTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class StartRestoreTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartRestoreTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartRestoreTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.task_id = task_id
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StartTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        http_status_code: int = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
        job_type_name: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.err_message = err_message
        self.success = success
        self.err_code = err_code
        self.job_type_name = job_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.job_type_name is not None:
            result['JobTypeName'] = self.job_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('JobTypeName') is not None:
            self.job_type_name = m.get('JobTypeName')
        return self


class StartTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        stop_method: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.stop_method = stop_method
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.stop_method is not None:
            result['StopMethod'] = self.stop_method
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('StopMethod') is not None:
            self.stop_method = m.get('StopMethod')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class StopBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class StopBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeBackupPlanRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        instance_class: str = None,
        owner_id: str = None,
        client_token: str = None,
    ):
        self.backup_plan_id = backup_plan_id
        self.instance_class = instance_class
        self.owner_id = owner_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpgradeBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        backup_plan_id: str = None,
        err_message: str = None,
        order_id: str = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.backup_plan_id = backup_plan_id
        self.err_message = err_message
        self.order_id = order_id
        self.success = success
        self.err_code = err_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        return self


class UpgradeBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeBackupPlanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



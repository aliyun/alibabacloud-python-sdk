# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.client_token = client_token
        self.new_resource_group_id = new_resource_group_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDownloadRequest(TeaModel):
    def __init__(
        self,
        bak_set_id: str = None,
        bak_set_size: str = None,
        bak_set_type: str = None,
        download_point_in_time: str = None,
        format_type: str = None,
        instance_name: str = None,
        region_code: str = None,
        target_bucket: str = None,
        target_oss_region: str = None,
        target_path: str = None,
        target_type: str = None,
    ):
        # The ID of the backup set. You can call the [DescribeBackups](~~26273~~) operation to obtain the ID of the backup set.
        # 
        # >  This parameter is required if the BakSetType parameter is set to full.
        self.bak_set_id = bak_set_id
        # The size of the full backup set. You can call the [DescribeBackups](~~26273~~) operation to query the size of the full backup set. Unit: bytes.
        self.bak_set_size = bak_set_size
        # The type of the download task. Valid values:
        # 
        # *   **full**: downloads a full backup set.
        # *   **pitr**: downloads a backup set at a specific point in time.
        self.bak_set_type = bak_set_type
        # The point in time at which the backup set is downloaded. The UNIX timestamp of the LONG type. Unit: milliseconds.
        # 
        # >  This parameter is required if the BakSetType parameter is set to pitr.
        self.download_point_in_time = download_point_in_time
        # The destination format to which the downloaded backup set is converted. Valid values:
        # 
        # *   **csv**\
        # *   **SQL**\
        # *   **Parquet**\
        self.format_type = format_type
        # The ID of the instance.
        self.instance_name = instance_name
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](~~26231~~) operation to query the region ID of the instance.
        self.region_code = region_code
        # The name of the OSS bucket that is used to store the backup set.
        # 
        # *   This parameter is required if the TargetType parameter is set to OSS.
        # *   Make sure that your account has the **AliyunDBSDefaultRole** permission. For more information, see [Use RAM for resource authorization](~~26307~~). You can also grant permissions based on the operation instructions in the RAM console.
        self.target_bucket = target_bucket
        # The region in which the OSS bucket resides.
        # 
        # >  This parameter is required if the TargetType parameter is set to OSS.
        self.target_oss_region = target_oss_region
        # The destination path of the downloaded data.
        # 
        # >  This parameter is required if the TargetType parameter is set to OSS.
        self.target_path = target_path
        # The type of the method in which the backup set is downloaded. Valid values:
        # 
        # *   **OSS**\
        # *   **URL**\
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bak_set_id is not None:
            result['BakSetId'] = self.bak_set_id
        if self.bak_set_size is not None:
            result['BakSetSize'] = self.bak_set_size
        if self.bak_set_type is not None:
            result['BakSetType'] = self.bak_set_type
        if self.download_point_in_time is not None:
            result['DownloadPointInTime'] = self.download_point_in_time
        if self.format_type is not None:
            result['FormatType'] = self.format_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket
        if self.target_oss_region is not None:
            result['TargetOssRegion'] = self.target_oss_region
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BakSetId') is not None:
            self.bak_set_id = m.get('BakSetId')
        if m.get('BakSetSize') is not None:
            self.bak_set_size = m.get('BakSetSize')
        if m.get('BakSetType') is not None:
            self.bak_set_type = m.get('BakSetType')
        if m.get('DownloadPointInTime') is not None:
            self.download_point_in_time = m.get('DownloadPointInTime')
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')
        if m.get('TargetOssRegion') is not None:
            self.target_oss_region = m.get('TargetOssRegion')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateDownloadResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_set_time: int = None,
        bak_set_id: str = None,
        db_list: str = None,
        download_status: str = None,
        export_data_size: int = None,
        format: str = None,
        gmt_create: int = None,
        import_data_size: int = None,
        progress: str = None,
        region_code: str = None,
        target_path: str = None,
        target_type: str = None,
        task_id: str = None,
    ):
        # The point in time of the backup set if the task is used to download a backup set at a specific point in time. The value is a timestamp.
        self.backup_set_time = backup_set_time
        # The ID of the full backup set.
        self.bak_set_id = bak_set_id
        # The database and table information that is returned if the download task is a database and table filtering task.
        self.db_list = db_list
        # The status of the download task. Valid values:
        # 
        # *   Initializing: The download task is being initialized.
        # *   queuing: The download task is queuing.
        # *   running: The download task is running.
        # *   failed: The download task fails.
        # *   finished: The download task is complete.
        # *   expired: The download task expires.
        # 
        # >  The download task expires in three days after the task is complete if the TargetType parameter is set to URL.
        self.download_status = download_status
        # The amount of output data. Unit: bytes.
        self.export_data_size = export_data_size
        # The format to which the downloaded data is converted.
        self.format = format
        # The time when the download task was created. The value is a timestamp.
        self.gmt_create = gmt_create
        # The amount of data that is processed. Unit: bytes.
        self.import_data_size = import_data_size
        # The number of tables that have been downloaded and the total number of tables to be downloaded.
        # 
        # >  If the task is in the preparation stage, 0/0 is returned.
        self.progress = progress
        # The ID of the region in which the instance resides.
        self.region_code = region_code
        # The destination path of the downloaded data.
        # 
        # >  This parameter is returned if the TargetType parameter is set to OSS.
        self.target_path = target_path
        # The type of the method in which the backup set is downloaded.
        self.target_type = target_type
        # The ID of the download task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_time is not None:
            result['BackupSetTime'] = self.backup_set_time
        if self.bak_set_id is not None:
            result['BakSetId'] = self.bak_set_id
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.download_status is not None:
            result['DownloadStatus'] = self.download_status
        if self.export_data_size is not None:
            result['ExportDataSize'] = self.export_data_size
        if self.format is not None:
            result['Format'] = self.format
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.import_data_size is not None:
            result['ImportDataSize'] = self.import_data_size
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetTime') is not None:
            self.backup_set_time = m.get('BackupSetTime')
        if m.get('BakSetId') is not None:
            self.bak_set_id = m.get('BakSetId')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('DownloadStatus') is not None:
            self.download_status = m.get('DownloadStatus')
        if m.get('ExportDataSize') is not None:
            self.export_data_size = m.get('ExportDataSize')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ImportDataSize') is not None:
            self.import_data_size = m.get('ImportDataSize')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDownloadResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateDownloadResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The response parameters.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateDownloadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDownloadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDownloadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateDownloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSandboxInstanceRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_set_id: str = None,
        restore_time: str = None,
        sandbox_instance_name: str = None,
        sandbox_password: str = None,
        sandbox_specification: str = None,
        sandbox_type: str = None,
        sandbox_user: str = None,
        vpc_id: str = None,
        vpc_switch_id: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](~~437215~~) operation to obtain the ID of the backup schedule.
        # 
        # >  If your instance is an ApsaraDB RDS for MySQL instance, you can configure [automatic access to the instance](~~193091~~) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The ID of the backup set to be restored, which is the point in time when a snapshot was created. You can call the [DescribeSandboxBackupSets](~~437256~~) operation to obtain the ID.
        # 
        # >  You need to specify only one of the **BackupSetId** and **RestoreTime** parameters.
        self.backup_set_id = backup_set_id
        # The point in time of the sandbox instance to be restored. You can call the [DescribeSandboxRecoveryTime](~~437258~~) operation to view the recoverable time range. Specify the time in the format of *yyyy-MM-ddTHH:mm:ssZ*. The time must be in UTC.
        self.restore_time = restore_time
        # The name of the sandbox instance.
        self.sandbox_instance_name = sandbox_instance_name
        # The password of the privileged account created in the sandbox instance.
        self.sandbox_password = sandbox_password
        # The specifications of the sandbox instance. Valid values:
        # 
        # *   **MYSQL\_1C\_1M_SD**: 1 CPU core and 1 GB of memory.
        # *   **MYSQL\_1C\_2M_SD**: 1 CPU core and 2 GB of memory.
        # *   **MYSQL\_2C\_4M_SD**: 2 CPU cores and 4 GB of memory.
        # *   **MYSQL\_2C\_8M_SD**: 2 CPU cores and 8 GB of memory.
        # *   **MYSQL\_4C\_8M_SD**: 4 CPU cores and 8 GB of memory.
        # *   **MYSQL\_4C\_16M_SD**: 4 CPU cores and 16 GB of memory.
        # *   **MYSQL\_8C\_16M_SD**: 8 CPU cores and 16 GB of memory.
        # *   **MYSQL\_8C\_32M_SD**: 8 CPU cores and 32 GB of memory.
        # 
        # >  Different specifications have little impact on the recovery speed. High-specification instances provide better performance after restoration. For more information, see [Sandbox instance fees](~~201466~~).
        self.sandbox_specification = sandbox_specification
        # The type of the sandbox instance. You can call this operation only to create an instance of the **Sandbox** type. After the sandbox instance is created, the MySQL endpoint of the instance is provided.
        self.sandbox_type = sandbox_type
        # The privileged account created in the sandbox instance.
        # 
        # *   After you specify this parameter, the system creates a privileged account in the sandbox instance. The account has the permissions on all databases in the instance.
        # 
        # The account of the source database is retained in the sandbox instance.
        # 
        # *   If you do not specify this parameter, the database account is the same as that of the source database.
        self.sandbox_user = sandbox_user
        # The ID of the virtual private cloud (VPC) that is used to connect to the sandbox instance. If you want to connect to the sandbox instance by using Elastic Compute Service (ECS) instances, you must set this parameter to the VPC in which the ECS instances reside.
        # 
        # >  You can set this parameter if you want to use it in a recovery drill scenario.
        self.vpc_id = vpc_id
        # The ID of the VSwitch that is used to connect to the sandbox instance.
        self.vpc_switch_id = vpc_switch_id

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
        if self.restore_time is not None:
            result['RestoreTime'] = self.restore_time
        if self.sandbox_instance_name is not None:
            result['SandboxInstanceName'] = self.sandbox_instance_name
        if self.sandbox_password is not None:
            result['SandboxPassword'] = self.sandbox_password
        if self.sandbox_specification is not None:
            result['SandboxSpecification'] = self.sandbox_specification
        if self.sandbox_type is not None:
            result['SandboxType'] = self.sandbox_type
        if self.sandbox_user is not None:
            result['SandboxUser'] = self.sandbox_user
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_switch_id is not None:
            result['VpcSwitchId'] = self.vpc_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('RestoreTime') is not None:
            self.restore_time = m.get('RestoreTime')
        if m.get('SandboxInstanceName') is not None:
            self.sandbox_instance_name = m.get('SandboxInstanceName')
        if m.get('SandboxPassword') is not None:
            self.sandbox_password = m.get('SandboxPassword')
        if m.get('SandboxSpecification') is not None:
            self.sandbox_specification = m.get('SandboxSpecification')
        if m.get('SandboxType') is not None:
            self.sandbox_type = m.get('SandboxType')
        if m.get('SandboxUser') is not None:
            self.sandbox_user = m.get('SandboxUser')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcSwitchId') is not None:
            self.vpc_switch_id = m.get('VpcSwitchId')
        return self


class CreateSandboxInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The ID of the sandbox instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateSandboxInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateSandboxInstanceResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The response parameters.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateSandboxInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSandboxInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSandboxInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateSandboxInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSandboxInstanceRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](~~437215~~) operation to obtain the ID of the backup schedule.
        # 
        # >  If your instance is an ApsaraDB RDS for MySQL instance, you can configure [automatic access to the instance](~~193091~~) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The ID of the sandbox instance. You can call the [DescribeSandboxInstances](~~437257~~) operation to obtain the ID of the sandbox instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteSandboxInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The response parameters.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The error message.
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSandboxInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSandboxInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteSandboxInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBTablesRecoveryBackupSetRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_code: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_code = region_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBTablesRecoveryBackupSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDBTablesRecoveryBackupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBTablesRecoveryBackupSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDBTablesRecoveryBackupSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBTablesRecoveryStateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_code: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_code = region_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBTablesRecoveryStateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDBTablesRecoveryStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBTablesRecoveryStateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDBTablesRecoveryStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBTablesRecoveryTimeRangeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_code: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_code = region_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBTablesRecoveryTimeRangeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDBTablesRecoveryTimeRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBTablesRecoveryTimeRangeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDBTablesRecoveryTimeRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadBackupSetStorageInfoRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        duration: str = None,
        instance_name: str = None,
        region_code: str = None,
        task_id: str = None,
    ):
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        # Set this parameter if the Download Destination parameter is set to URL.
        # 
        # *   By default, a URL is valid for 2 hours, which is equal to 7,200 seconds.
        # *   The valid duration is 5 minutes (300 seconds) to 1 day (86,400 seconds).
        # *   Before you set this parameter, convert the time to seconds. For example, if you want to set the validity period of the link to 5 minutes, enter 300.
        self.duration = duration
        # The ID of the instance.
        # 
        # >  The **BackupSetId** parameter is required if you specify the **InstanceName** parameter.
        self.instance_name = instance_name
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](~~26231~~) operation to query the region ID of the instance.
        self.region_code = region_code
        # The ID of the download task.
        # 
        # *   The **BackupSetId** and **InstanceName** parameters are required if you do not specify the **TaskId** parameter.
        # *   You can find the instance and click **Backup and Restoration**. On the **Backup Download** tab, view the **task ID**.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDownloadBackupSetStorageInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        expiration_time: int = None,
        private_url: str = None,
        public_url: str = None,
    ):
        # The expiration time of the URL.
        # 
        # >  The return value is in the timestamp format.
        self.expiration_time = expiration_time
        # The private download URL of the backup set.
        self.private_url = private_url
        # The public download URL of the backup set.
        self.public_url = public_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        if self.private_url is not None:
            result['PrivateUrl'] = self.private_url
        if self.public_url is not None:
            result['PublicUrl'] = self.public_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        if m.get('PrivateUrl') is not None:
            self.private_url = m.get('PrivateUrl')
        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')
        return self


class DescribeDownloadBackupSetStorageInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeDownloadBackupSetStorageInfoResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The response parameters.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: the request is successful.
        # *   **false**: the request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeDownloadBackupSetStorageInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDownloadBackupSetStorageInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadBackupSetStorageInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDownloadBackupSetStorageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadSupportRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_code: str = None,
    ):
        # The ID of the instance.
        self.instance_name = instance_name
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](~~26231~~) operation to query the region ID of the instance.
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        return self


class DescribeDownloadSupportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # Indicates whether the advanced download feature is supported. Valid values:
        # 
        # *   **true**: The advanced download feature is supported.
        # *   **false**: The advanced download feature is not supported.
        self.data = data
        # The error code returned if the request fails.
        self.err_code = err_code
        # The error message returned if the request fails.
        self.err_message = err_message
        # The error message.
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDownloadSupportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadSupportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDownloadSupportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDownloadTaskRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        current_page: str = None,
        datasource_id: str = None,
        end_time: str = None,
        instance_name: str = None,
        order_column: str = None,
        order_direct: str = None,
        page_size: str = None,
        region_code: str = None,
        start_time: str = None,
        state: str = None,
        task_type: str = None,
    ):
        # The ID of the backup set generated when you create the download task. You can call the [DescribeBackups](~~26273~~) operation to query the backup set ID. Unit: bytes.
        self.backup_set_id = backup_set_id
        # The page number of the page to return.
        self.current_page = current_page
        # The ID of the Database Backup (DBS) data source. Specify the parameter in the format of *ds-${Instance ID}\_${regionId}*.
        self.datasource_id = datasource_id
        # The end of the time range to query. Specify this parameter as a timestamp of the LONG type. Unit: milliseconds.
        self.end_time = end_time
        # The ID of the instance.
        self.instance_name = instance_name
        # The column based on which the entries are sorted. By default, the entries are sorted by the creation time. Set the value to **gmt_create**.
        self.order_column = order_column
        # The order in which you want to sort the entries. Valid values:
        # 
        # *   **asc**: sorts the retrieved entries by time in ascending order.
        # *   **desc**: sorts the retrieved entries by time in descending order. This is the default value.
        self.order_direct = order_direct
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](~~26231~~) operation to query the region ID of the instance.
        self.region_code = region_code
        # The beginning of the time range to query. Specify this parameter as a timestamp of the LONG type. Unit: milliseconds.
        self.start_time = start_time
        # The status of the download task. Valid values:
        # 
        # *   **Initializing**: The download task is being initialized.
        # *   **queuing**: The download task is queuing.
        # *   **running**: The download task is running.
        # *   **failed**: The download task fails.
        # *   **finished**: The download task is complete.
        self.state = state
        # The type of the download task. Valid values:
        # 
        # *   **full**: downloads a full backup set.
        # *   **pitr**: downloads a backup set at a specific point in time.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.order_column is not None:
            result['OrderColumn'] = self.order_column
        if self.order_direct is not None:
            result['OrderDirect'] = self.order_direct
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')
        if m.get('OrderDirect') is not None:
            self.order_direct = m.get('OrderDirect')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeDownloadTaskResponseBodyDataContentList(TeaModel):
    def __init__(
        self,
        backup_set_time: str = None,
        bak_set_id: str = None,
        db_list: str = None,
        download_status: str = None,
        export_data_size: str = None,
        format: str = None,
        gmt_create: str = None,
        import_data_size: str = None,
        progress: str = None,
        region_code: str = None,
        target_path: str = None,
        target_type: str = None,
        task_id: str = None,
    ):
        # The point in time of the backup set if the task is used to download a backup set at a specific point in time. The value is a timestamp of the LONG type. Unit: milliseconds.
        self.backup_set_time = backup_set_time
        # The ID of the full backup set.
        self.bak_set_id = bak_set_id
        # The details of the databases.
        self.db_list = db_list
        # The status of the download task. Valid values:
        # 
        # *   **Initializing**: The download task is being initialized.
        # *   **queuing**: The download task is queuing.
        # *   **running**: The download task is running.
        # *   **failed**: The download task fails.
        # *   **finished**: The download task is complete.
        # *   **expired**: The download task expires.
        self.download_status = download_status
        # The amount of output data. Unit: bytes.
        self.export_data_size = export_data_size
        # The format to which the downloaded backup set is converted. Valid values:
        # 
        # *   **csv**\
        # *   **SQL**\
        # *   **Parquet**\
        self.format = format
        # The time when the download task was created. The value is a timestamp.
        self.gmt_create = gmt_create
        # The amount of data that is processed. Unit: bytes.
        self.import_data_size = import_data_size
        # The number of tables that have been downloaded and the total number of tables to be downloaded.
        self.progress = progress
        # The ID of the region in which the instance resides.
        self.region_code = region_code
        # The destination path to which the data is downloaded if the TargeType parameter is set to OSS.
        self.target_path = target_path
        # The type of the method in which the backup set is downloaded. Valid values:
        # 
        # *   **OSS**\
        # *   **URL**\
        self.target_type = target_type
        # The ID of the download task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_time is not None:
            result['BackupSetTime'] = self.backup_set_time
        if self.bak_set_id is not None:
            result['BakSetId'] = self.bak_set_id
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.download_status is not None:
            result['DownloadStatus'] = self.download_status
        if self.export_data_size is not None:
            result['ExportDataSize'] = self.export_data_size
        if self.format is not None:
            result['Format'] = self.format
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.import_data_size is not None:
            result['ImportDataSize'] = self.import_data_size
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetTime') is not None:
            self.backup_set_time = m.get('BackupSetTime')
        if m.get('BakSetId') is not None:
            self.bak_set_id = m.get('BakSetId')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('DownloadStatus') is not None:
            self.download_status = m.get('DownloadStatus')
        if m.get('ExportDataSize') is not None:
            self.export_data_size = m.get('ExportDataSize')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ImportDataSize') is not None:
            self.import_data_size = m.get('ImportDataSize')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDownloadTaskResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        list: List[DescribeDownloadTaskResponseBodyDataContentList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeDownloadTaskResponseBodyDataContentList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeDownloadTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        content: DescribeDownloadTaskResponseBodyDataContent = None,
        extra: str = None,
        page_number: int = None,
        page_size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The details of the download tasks.
        self.content = content
        # The extra description of the download task.
        self.extra = extra
        self.page_number = page_number
        self.page_size = page_size
        self.total_elements = total_elements
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = DescribeDownloadTaskResponseBodyDataContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeDownloadTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeDownloadTaskResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The details of the download tasks.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeDownloadTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDownloadTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDownloadTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeDownloadTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSandboxBackupSetsRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_set_id: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](~~437215~~) operation to obtain the ID of the backup schedule.
        # 
        # >  If your instance is an ApsaraDB RDS for MySQL instance, you can configure [automatic access to the instance](~~193091~~) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The ID of the backup set. If this parameter is specified, only the snapshot of the backup set is returned. If this parameter is not specified, all the snapshots of the backup schedule are returned.
        self.backup_set_id = backup_set_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   30 (default value)
        # *   50
        # *   100
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
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSandboxBackupSetsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The response parameters.
        # 
        # *   **backupSetTime**: the point in time when the snapshot was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        # *   **backupSetId**: the ID of the backup set.
        # *   **backupSetType**: the type of the snapshot. A value of **Full** indicates that the snapshot is a full backup snapshot. A value of **Inc** indicates that the snapshot is an incremental backup snapshot.
        # *   **backupPlanId**: the ID of the backup schedule.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The error message.
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSandboxBackupSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSandboxBackupSetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSandboxBackupSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSandboxInstancesRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](~~437215~~) operation to obtain the ID of the backup schedule.
        # 
        # >  If your instance is an ApsaraDB RDS for MySQL instance, you can configure [automatic access to the instance](~~193091~~) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        self.backup_plan_id = backup_plan_id
        # The ID of the sandbox instance. You can call the [CreateSandboxInstance](~~437252~~) parameter to obtain the ID of the sandbox instance.
        self.instance_id = instance_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   30 (default value)
        # *   50
        # *   100
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSandboxInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The response parameters.
        # 
        # *   **connectionString**: the connection string of the sandbox instance, in the format of IP address:Port number. This parameter indicates the endpoint of the sandbox instance if the value of the SandboxType parameter is **Sandbox**. This parameter indicates the Network File System (NFS) mount address if the value of the SandboxType parameter is **NFS**.
        # *   **restoreSeconds**: the time required to create the sandbox instance. Unit: seconds.
        # *   **restoreTime**: the point in time to which the sandbox instance is restored. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        # *   **instanceId**: the ID of the sandbox instance.
        # *   **backupSetId**: the ID of the backup set.
        # *   **createTime**: the point in time when the sandbox instance was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        # *   **backupPlanId**: the ID of the backup schedule.
        # *   **vpcId**: the ID of the virtual private cloud (VPC).
        # *   **vpcSwitchId**: the ID of the VSwitch.
        # *   **sandboxSpecification**: the specifications of the sandbox instance.
        # *   **status**: the status of the sandbox instance. Valid values: **running**, **check_pass**, and **stop**.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The error message.
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSandboxInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSandboxInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSandboxInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSandboxRecoveryTimeRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](~~437215~~) operation to obtain the ID of the backup schedule. If you set this parameter to the backup schedule ID obtained by calling the DescribeBackupPlanList operation, the dbs prefix must be removed. Otherwise, the call fails.
        # 
        # >  If your instance is an ApsaraDB RDS for MySQL instance, you can configure [automatic access to the instance](~~193091~~) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        self.backup_plan_id = backup_plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        return self


class DescribeSandboxRecoveryTimeResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        recovery_begin_time: str = None,
        recovery_end_time: str = None,
    ):
        # The backup schedule of the sandbox instance.
        self.backup_plan_id = backup_plan_id
        # The beginning of the time range during which the sandbox instance can be restored. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.recovery_begin_time = recovery_begin_time
        # The end of the time range during which the sandbox instance can be restored. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.recovery_end_time = recovery_end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id
        if self.recovery_begin_time is not None:
            result['RecoveryBeginTime'] = self.recovery_begin_time
        if self.recovery_end_time is not None:
            result['RecoveryEndTime'] = self.recovery_end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('RecoveryBeginTime') is not None:
            self.recovery_begin_time = m.get('RecoveryBeginTime')
        if m.get('RecoveryEndTime') is not None:
            self.recovery_end_time = m.get('RecoveryEndTime')
        return self


class DescribeSandboxRecoveryTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeSandboxRecoveryTimeResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.code = code
        # The response parameters.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeSandboxRecoveryTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSandboxRecoveryTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSandboxRecoveryTimeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSandboxRecoveryTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBTablesRecoveryStateRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        instance_id: str = None,
        region_code: str = None,
        region_id: str = None,
        retention: str = None,
    ):
        self.category = category
        self.instance_id = instance_id
        self.region_code = region_code
        self.region_id = region_id
        self.retention = retention

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retention is not None:
            result['Retention'] = self.retention
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        return self


class ModifyDBTablesRecoveryStateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDBTablesRecoveryStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBTablesRecoveryStateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyDBTablesRecoveryStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SupportDBTableRecoveryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_code: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_code = region_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SupportDBTableRecoveryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SupportDBTableRecoveryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SupportDBTableRecoveryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SupportDBTableRecoveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



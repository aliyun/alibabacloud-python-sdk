# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        new_resource_group_id: str = None,
        region_code: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the resource group to which you want to move the resource.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The region ID of the instance.
        self.region_code = region_code
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Set the value to backupplan.
        # 
        # This parameter is required.
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
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
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
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
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
        # The status code returned.
        self.code = code
        # Indicates whether the resource was successfully moved. Valid values:
        # 
        # *   **true**: The resource was successfully moved.
        # *   **false**: The resource failed to be moved.
        self.data = data
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The additional information.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
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
        # The ID of the backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the ID of the backup set.
        # 
        # > This parameter is required if the BakSetType parameter is set to full.
        self.bak_set_id = bak_set_id
        # The size of the full backup set. Unit: bytes. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the size of the full backup set.
        self.bak_set_size = bak_set_size
        # The type of the download task. Valid values:
        # 
        # *   **full**: downloads a full backup set.
        # *   **pitr**: downloads a backup set at a specific point in time.
        self.bak_set_type = bak_set_type
        # The point in time at which the backup set is downloaded. Specify a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # > This parameter is required if the BakSetType parameter is set to pitr.
        self.download_point_in_time = download_point_in_time
        # The format to which the downloaded backup set is converted. Valid values:
        # 
        # *   **CSV**\
        # *   **SQL**\
        # *   **Parquet**\
        # 
        # > This parameter is required.
        self.format_type = format_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/26231.html) operation to query the region ID of the instance.
        # 
        # This parameter is required.
        self.region_code = region_code
        # The name of the OSS bucket that is used to store the backup set.
        # 
        # *   This parameter is required if the TargetType parameter is set to OSS.
        # *   Make sure that your account is granted the **AliyunDBSDefaultRole** permission. For more information, see [Use RAM for resource authorization](https://help.aliyun.com/document_detail/26307.html). You can also grant permissions based on the operation instructions in the Resource Access Management (RAM) console.
        self.target_bucket = target_bucket
        # The region in which the OSS bucket resides.
        # 
        # > This parameter is required if the TargetType parameter is set to OSS.
        self.target_oss_region = target_oss_region
        # The destination path to which the backup set is downloaded.
        # 
        # > This parameter is required if the TargetType parameter is set to OSS.
        self.target_path = target_path
        # The type of the destination to which the backup set is downloaded. Valid values:
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
        # The point in time of the backup set if the task is used to download a backup set at a specific point in time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.backup_set_time = backup_set_time
        # The ID of the full backup set.
        self.bak_set_id = bak_set_id
        # The database and table information that is returned if databases and tables are filtered by the download task.
        self.db_list = db_list
        # The state of the download task. Valid values:
        # 
        # *   initializing: The download task was being initialized.
        # *   queuing: The download task was queuing.
        # *   running: The download task was running.
        # *   failed: The download task failed.
        # *   finished: The download task was complete.
        # *   expired: The download task expired.
        # 
        # > If the TargetType parameter is set to URL, the download task expires in three days after the task is complete.
        self.download_status = download_status
        # The size of the downloaded data. Unit: bytes.
        self.export_data_size = export_data_size
        # The format to which the downloaded data is converted.
        self.format = format
        # The time when the download task was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.gmt_create = gmt_create
        # The size of the processed data. Unit: bytes.
        self.import_data_size = import_data_size
        # The number of tables that have been downloaded and the total number of tables to be downloaded.
        # 
        # > If the task is in the preparation stage, 0/0 is returned.
        self.progress = progress
        # The ID of the region in which the instance resides.
        self.region_code = region_code
        # The destination path to which the backup set is downloaded.
        # 
        # >  This parameter is returned if the value of **TargetType is OSS**.
        self.target_path = target_path
        # The type of the destination to which the backup set is downloaded.
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
        # The status code returned.
        self.code = code
        # The information about the download task.
        self.data = data
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The error message returned if the request failed.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
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


class DeleteSandboxInstanceRequest(TeaModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        instance_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/437215.html) operation to query the ID of the backup schedule.
        # 
        # > If your instance is an ApsaraDB RDS for MySQL instance, you can [configure automatic access to a data source](https://help.aliyun.com/document_detail/193091.html) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The ID of the sandbox instance. You can call the [DescribeSandboxInstances](https://help.aliyun.com/document_detail/437257.html) operation to query the ID of the sandbox instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.zone_id = zone_id

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
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        # The error code returned if the request failed.
        self.code = code
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The error message returned if the request failed.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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


class DescribeBackupDataListRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_scale: str = None,
        backup_status: str = None,
        backup_type: str = None,
        data_source_id: str = None,
        end_time: str = None,
        instance_is_deleted: bool = None,
        instance_name: str = None,
        instance_region: str = None,
        page_number: int = None,
        page_size: int = None,
        region_code: str = None,
        scene_type: str = None,
        start_time: str = None,
    ):
        self.backup_id = backup_id
        self.backup_method = backup_method
        self.backup_mode = backup_mode
        self.backup_scale = backup_scale
        self.backup_status = backup_status
        self.backup_type = backup_type
        self.data_source_id = data_source_id
        self.end_time = end_time
        self.instance_is_deleted = instance_is_deleted
        self.instance_name = instance_name
        self.instance_region = instance_region
        self.page_number = page_number
        self.page_size = page_size
        self.region_code = region_code
        self.scene_type = scene_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_scale is not None:
            result['BackupScale'] = self.backup_scale
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_is_deleted is not None:
            result['InstanceIsDeleted'] = self.instance_is_deleted
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_region is not None:
            result['InstanceRegion'] = self.instance_region
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupScale') is not None:
            self.backup_scale = m.get('BackupScale')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIsDeleted') is not None:
            self.instance_is_deleted = m.get('InstanceIsDeleted')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceRegion') is not None:
            self.instance_region = m.get('InstanceRegion')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupDataListResponseBodyDataContentPolarSnapshot(TeaModel):
    def __init__(
        self,
        dump_id: int = None,
        dump_size: int = None,
        expect_expire_time: str = None,
        expect_expire_type: str = None,
    ):
        self.dump_id = dump_id
        self.dump_size = dump_size
        self.expect_expire_time = expect_expire_time
        self.expect_expire_type = expect_expire_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dump_id is not None:
            result['DumpId'] = self.dump_id
        if self.dump_size is not None:
            result['DumpSize'] = self.dump_size
        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time
        if self.expect_expire_type is not None:
            result['expectExpireType'] = self.expect_expire_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DumpId') is not None:
            self.dump_id = m.get('DumpId')
        if m.get('DumpSize') is not None:
            self.dump_size = m.get('DumpSize')
        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')
        if m.get('expectExpireType') is not None:
            self.expect_expire_type = m.get('expectExpireType')
        return self


class DescribeBackupDataListResponseBodyDataContent(TeaModel):
    def __init__(
        self,
        backup_download_url: str = None,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_intranet_download_url: str = None,
        backup_location: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_name: str = None,
        backup_scale: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        checksum: str = None,
        consistent_time: int = None,
        encryption: str = None,
        engine: str = None,
        engine_version: str = None,
        expect_expire_time: str = None,
        expect_expire_type: str = None,
        instance_name: str = None,
        is_avail: int = None,
        polar_snapshot: DescribeBackupDataListResponseBodyDataContentPolarSnapshot = None,
        support_deletion: int = None,
    ):
        self.backup_download_url = backup_download_url
        self.backup_end_time = backup_end_time
        self.backup_id = backup_id
        self.backup_intranet_download_url = backup_intranet_download_url
        self.backup_location = backup_location
        self.backup_method = backup_method
        self.backup_mode = backup_mode
        self.backup_name = backup_name
        self.backup_scale = backup_scale
        self.backup_size = backup_size
        self.backup_start_time = backup_start_time
        self.backup_status = backup_status
        self.backup_type = backup_type
        self.checksum = checksum
        self.consistent_time = consistent_time
        self.encryption = encryption
        self.engine = engine
        self.engine_version = engine_version
        self.expect_expire_time = expect_expire_time
        self.expect_expire_type = expect_expire_type
        self.instance_name = instance_name
        self.is_avail = is_avail
        self.polar_snapshot = polar_snapshot
        self.support_deletion = support_deletion

    def validate(self):
        if self.polar_snapshot:
            self.polar_snapshot.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url
        if self.backup_location is not None:
            result['BackupLocation'] = self.backup_location
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_name is not None:
            result['BackupName'] = self.backup_name
        if self.backup_scale is not None:
            result['BackupScale'] = self.backup_scale
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.checksum is not None:
            result['Checksum'] = self.checksum
        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time
        if self.expect_expire_type is not None:
            result['ExpectExpireType'] = self.expect_expire_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail
        if self.polar_snapshot is not None:
            result['PolarSnapshot'] = self.polar_snapshot.to_map()
        if self.support_deletion is not None:
            result['SupportDeletion'] = self.support_deletion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')
        if m.get('BackupLocation') is not None:
            self.backup_location = m.get('BackupLocation')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupName') is not None:
            self.backup_name = m.get('BackupName')
        if m.get('BackupScale') is not None:
            self.backup_scale = m.get('BackupScale')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')
        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')
        if m.get('ExpectExpireType') is not None:
            self.expect_expire_type = m.get('ExpectExpireType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')
        if m.get('PolarSnapshot') is not None:
            temp_model = DescribeBackupDataListResponseBodyDataContentPolarSnapshot()
            self.polar_snapshot = temp_model.from_map(m['PolarSnapshot'])
        if m.get('SupportDeletion') is not None:
            self.support_deletion = m.get('SupportDeletion')
        return self


class DescribeBackupDataListResponseBodyData(TeaModel):
    def __init__(
        self,
        content: List[DescribeBackupDataListResponseBodyDataContent] = None,
        extra: str = None,
        page_number: int = None,
        page_size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.content = content
        self.extra = extra
        self.page_number = page_number
        self.page_size = page_size
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
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
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = DescribeBackupDataListResponseBodyDataContent()
                self.content.append(temp_model.from_map(k))
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


class DescribeBackupDataListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeBackupDataListResponseBodyData = None,
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
            temp_model = DescribeBackupDataListResponseBodyData()
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


class DescribeBackupDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupDataListResponseBody = None,
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
            temp_model = DescribeBackupDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_code: str = None,
    ):
        self.instance_name = instance_name
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


class DescribeBackupPolicyResponseBodyDataAdvanceDataPolicies(TeaModel):
    def __init__(
        self,
        auto_created: bool = None,
        bak_type: str = None,
        dest_region: str = None,
        dest_type: str = None,
        dump_action: str = None,
        filter_key: str = None,
        filter_type: str = None,
        filter_value: str = None,
        policy_id: str = None,
        retention_type: str = None,
        retention_value: str = None,
        src_region: str = None,
        src_type: str = None,
        strategy_id: str = None,
    ):
        self.auto_created = auto_created
        self.bak_type = bak_type
        self.dest_region = dest_region
        self.dest_type = dest_type
        self.dump_action = dump_action
        self.filter_key = filter_key
        self.filter_type = filter_type
        self.filter_value = filter_value
        self.policy_id = policy_id
        self.retention_type = retention_type
        self.retention_value = retention_value
        self.src_region = src_region
        self.src_type = src_type
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_created is not None:
            result['AutoCreated'] = self.auto_created
        if self.bak_type is not None:
            result['BakType'] = self.bak_type
        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region
        if self.dest_type is not None:
            result['DestType'] = self.dest_type
        if self.dump_action is not None:
            result['DumpAction'] = self.dump_action
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.retention_type is not None:
            result['RetentionType'] = self.retention_type
        if self.retention_value is not None:
            result['RetentionValue'] = self.retention_value
        if self.src_region is not None:
            result['SrcRegion'] = self.src_region
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreated') is not None:
            self.auto_created = m.get('AutoCreated')
        if m.get('BakType') is not None:
            self.bak_type = m.get('BakType')
        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')
        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')
        if m.get('DumpAction') is not None:
            self.dump_action = m.get('DumpAction')
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RetentionType') is not None:
            self.retention_type = m.get('RetentionType')
        if m.get('RetentionValue') is not None:
            self.retention_value = m.get('RetentionValue')
        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DescribeBackupPolicyResponseBodyDataAdvanceLogPolicies(TeaModel):
    def __init__(
        self,
        dest_region: str = None,
        dest_type: str = None,
        enable_log_backup: bool = None,
        log_retention_type: str = None,
        log_retention_value: str = None,
        src_region: str = None,
        src_type: str = None,
        strategy_id: str = None,
    ):
        self.dest_region = dest_region
        self.dest_type = dest_type
        self.enable_log_backup = enable_log_backup
        self.log_retention_type = log_retention_type
        self.log_retention_value = log_retention_value
        self.src_region = src_region
        self.src_type = src_type
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region
        if self.dest_type is not None:
            result['DestType'] = self.dest_type
        if self.enable_log_backup is not None:
            result['EnableLogBackup'] = self.enable_log_backup
        if self.log_retention_type is not None:
            result['LogRetentionType'] = self.log_retention_type
        if self.log_retention_value is not None:
            result['LogRetentionValue'] = self.log_retention_value
        if self.src_region is not None:
            result['SrcRegion'] = self.src_region
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')
        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')
        if m.get('EnableLogBackup') is not None:
            self.enable_log_backup = m.get('EnableLogBackup')
        if m.get('LogRetentionType') is not None:
            self.log_retention_type = m.get('LogRetentionType')
        if m.get('LogRetentionValue') is not None:
            self.log_retention_value = m.get('LogRetentionValue')
        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        return self


class DescribeBackupPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        advance_data_policies: List[DescribeBackupPolicyResponseBodyDataAdvanceDataPolicies] = None,
        advance_log_policies: List[DescribeBackupPolicyResponseBodyDataAdvanceLogPolicies] = None,
        backup_method: str = None,
        backup_priority: int = None,
        backup_retention_period: int = None,
        backup_retention_policy_on_cluster_deletion: str = None,
        category: str = None,
        enable_backup: int = None,
        enable_inc_backup: int = None,
        enable_log_backup: int = None,
        high_frequency_bak_interval: int = None,
        high_space_usage_protection: str = None,
        inc_backup_interval: int = None,
        local_log_retention_space: int = None,
        log_backup_local_retention_number: str = None,
        log_backup_retention: int = None,
        preferred_backup_date: str = None,
        preferred_backup_window: str = None,
        preferred_backup_window_begin: str = None,
    ):
        self.advance_data_policies = advance_data_policies
        self.advance_log_policies = advance_log_policies
        self.backup_method = backup_method
        self.backup_priority = backup_priority
        self.backup_retention_period = backup_retention_period
        self.backup_retention_policy_on_cluster_deletion = backup_retention_policy_on_cluster_deletion
        self.category = category
        self.enable_backup = enable_backup
        self.enable_inc_backup = enable_inc_backup
        self.enable_log_backup = enable_log_backup
        self.high_frequency_bak_interval = high_frequency_bak_interval
        self.high_space_usage_protection = high_space_usage_protection
        self.inc_backup_interval = inc_backup_interval
        self.local_log_retention_space = local_log_retention_space
        self.log_backup_local_retention_number = log_backup_local_retention_number
        self.log_backup_retention = log_backup_retention
        self.preferred_backup_date = preferred_backup_date
        self.preferred_backup_window = preferred_backup_window
        self.preferred_backup_window_begin = preferred_backup_window_begin

    def validate(self):
        if self.advance_data_policies:
            for k in self.advance_data_policies:
                if k:
                    k.validate()
        if self.advance_log_policies:
            for k in self.advance_log_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdvanceDataPolicies'] = []
        if self.advance_data_policies is not None:
            for k in self.advance_data_policies:
                result['AdvanceDataPolicies'].append(k.to_map() if k else None)
        result['AdvanceLogPolicies'] = []
        if self.advance_log_policies is not None:
            for k in self.advance_log_policies:
                result['AdvanceLogPolicies'].append(k.to_map() if k else None)
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        if self.backup_priority is not None:
            result['BackupPriority'] = self.backup_priority
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        if self.backup_retention_policy_on_cluster_deletion is not None:
            result['BackupRetentionPolicyOnClusterDeletion'] = self.backup_retention_policy_on_cluster_deletion
        if self.category is not None:
            result['Category'] = self.category
        if self.enable_backup is not None:
            result['EnableBackup'] = self.enable_backup
        if self.enable_inc_backup is not None:
            result['EnableIncBackup'] = self.enable_inc_backup
        if self.enable_log_backup is not None:
            result['EnableLogBackup'] = self.enable_log_backup
        if self.high_frequency_bak_interval is not None:
            result['HighFrequencyBakInterval'] = self.high_frequency_bak_interval
        if self.high_space_usage_protection is not None:
            result['HighSpaceUsageProtection'] = self.high_space_usage_protection
        if self.inc_backup_interval is not None:
            result['IncBackupInterval'] = self.inc_backup_interval
        if self.local_log_retention_space is not None:
            result['LocalLogRetentionSpace'] = self.local_log_retention_space
        if self.log_backup_local_retention_number is not None:
            result['LogBackupLocalRetentionNumber'] = self.log_backup_local_retention_number
        if self.log_backup_retention is not None:
            result['LogBackupRetention'] = self.log_backup_retention
        if self.preferred_backup_date is not None:
            result['PreferredBackupDate'] = self.preferred_backup_date
        if self.preferred_backup_window is not None:
            result['PreferredBackupWindow'] = self.preferred_backup_window
        if self.preferred_backup_window_begin is not None:
            result['PreferredBackupWindowBegin'] = self.preferred_backup_window_begin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advance_data_policies = []
        if m.get('AdvanceDataPolicies') is not None:
            for k in m.get('AdvanceDataPolicies'):
                temp_model = DescribeBackupPolicyResponseBodyDataAdvanceDataPolicies()
                self.advance_data_policies.append(temp_model.from_map(k))
        self.advance_log_policies = []
        if m.get('AdvanceLogPolicies') is not None:
            for k in m.get('AdvanceLogPolicies'):
                temp_model = DescribeBackupPolicyResponseBodyDataAdvanceLogPolicies()
                self.advance_log_policies.append(temp_model.from_map(k))
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        if m.get('BackupPriority') is not None:
            self.backup_priority = m.get('BackupPriority')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        if m.get('BackupRetentionPolicyOnClusterDeletion') is not None:
            self.backup_retention_policy_on_cluster_deletion = m.get('BackupRetentionPolicyOnClusterDeletion')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EnableBackup') is not None:
            self.enable_backup = m.get('EnableBackup')
        if m.get('EnableIncBackup') is not None:
            self.enable_inc_backup = m.get('EnableIncBackup')
        if m.get('EnableLogBackup') is not None:
            self.enable_log_backup = m.get('EnableLogBackup')
        if m.get('HighFrequencyBakInterval') is not None:
            self.high_frequency_bak_interval = m.get('HighFrequencyBakInterval')
        if m.get('HighSpaceUsageProtection') is not None:
            self.high_space_usage_protection = m.get('HighSpaceUsageProtection')
        if m.get('IncBackupInterval') is not None:
            self.inc_backup_interval = m.get('IncBackupInterval')
        if m.get('LocalLogRetentionSpace') is not None:
            self.local_log_retention_space = m.get('LocalLogRetentionSpace')
        if m.get('LogBackupLocalRetentionNumber') is not None:
            self.log_backup_local_retention_number = m.get('LogBackupLocalRetentionNumber')
        if m.get('LogBackupRetention') is not None:
            self.log_backup_retention = m.get('LogBackupRetention')
        if m.get('PreferredBackupDate') is not None:
            self.preferred_backup_date = m.get('PreferredBackupDate')
        if m.get('PreferredBackupWindow') is not None:
            self.preferred_backup_window = m.get('PreferredBackupWindow')
        if m.get('PreferredBackupWindowBegin') is not None:
            self.preferred_backup_window_begin = m.get('PreferredBackupWindowBegin')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeBackupPolicyResponseBodyData = None,
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
            temp_model = DescribeBackupPolicyResponseBodyData()
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


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPolicyResponseBody = None,
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBTablesRecoveryBackupSetRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_code: str = None,
    ):
        self.instance_id = instance_id
        self.region_code = region_code

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
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
    ):
        self.instance_id = instance_id
        self.region_code = region_code

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
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
    ):
        self.instance_id = instance_id
        self.region_code = region_code

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
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
        # The validity period of the URL that is used as the download destination. Take note of the following items:
        # 
        # *   Default value: 7200. This means that the URL is valid for 2 hours by default.
        # *   Valid values: 300 to 86400. Unit: seconds. This means that you can specify a validity period in the range of 5 minutes to 1 day.
        # *   Before you specify this parameter, convert the validity period to seconds. For example, if you want to set the validity period of the URL to 5 minutes, enter 300.
        # 
        # This parameter is required.
        self.duration = duration
        # The ID of the instance.
        # 
        # > The **BackupSetId** parameter is required if you specify the **InstanceName** parameter.
        self.instance_name = instance_name
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/26231.html) operation to query the region ID of the instance.
        # 
        # This parameter is required.
        self.region_code = region_code
        # The download task ID.
        # 
        # *   The **BackupSetId** and **InstanceName** parameters are required if you do not specify the **TaskId** parameter.
        # *   To view the download task ID, go to the instance details page in the console and click **Backup and Restoration** in the left-side navigation pane. On the **Backup Download** tab, view the task ID.
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
        # The validity period of the URL.
        # 
        # > This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
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
        # The error code returned if the request failed.
        self.code = code
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The error message returned if the request failed.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
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
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/26231.html) operation to query the region ID of the instance.
        # 
        # This parameter is required.
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
        # The error code returned if the request failed.
        self.code = code
        # Indicates whether the advanced download feature is supported. Valid values:
        # 
        # *   **true**: The advanced download feature is supported.
        # *   **false**: The advanced download feature is not supported.
        self.data = data
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The error message returned if the request failed.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
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
        # The ID of the backup set generated when you create a download task. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the ID.
        self.backup_set_id = backup_set_id
        # The page number of the page to return.
        self.current_page = current_page
        # The ID of the Database Backup (DBS) data source. Specify the parameter in the format of *ds-${Instance ID}_${regionId}*.
        self.datasource_id = datasource_id
        # The end of the time range to query. Specify this parameter as a timestamp of the LONG type. Unit: milliseconds.
        self.end_time = end_time
        # The ID of the instance.
        # 
        # > This parameter is required.
        self.instance_name = instance_name
        # The column based on which the entries are sorted. By default, the entries are sorted by the time when the download task was created. Set the value to **gmt_create**.
        self.order_column = order_column
        # The order in which you want to sort the entries. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order_direct = order_direct
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the region in which the instance resides. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/26231.html) operation to query the region ID of the instance.
        # 
        # This parameter is required.
        self.region_code = region_code
        # The beginning of the time range to query. Specify this parameter as a timestamp of the LONG type. Unit: milliseconds.
        self.start_time = start_time
        # The state of the download task. Valid values:
        # 
        # *   **Initializing**: The download task is being initialized.
        # *   **queueing**: The download task is queuing.
        # *   **running**: The download task is running.
        # *   **failed**: The download task fails.
        # *   **finished**: The download task is complete.
        # *   **expired**: The download task expires.
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
        # The point in time of the backup set if the task is used to download a backup set at a specific point in time. The value is a timestamp of the LONG type. Unit: millisecond.
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
        # The destination path to which the data is downloaded if the value of **TargetType is OSS**.
        self.target_path = target_path
        # The type of the method in which the backup set is downloaded. Valid values:
        # 
        # *   **OSS**\
        # *   **URL**\
        self.target_type = target_type
        # The download task ID.
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
        # The details of the task.
        self.content = content
        # The extra description of the download tasks.
        self.extra = extra
        # The page number of the returned page. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of full backup tasks.
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
        # The error code returned if the request fails.
        self.code = code
        # The details of the tasks.
        self.data = data
        # The error code returned if the request fails.
        self.err_code = err_code
        # The error message returned if the request fails.
        self.err_message = err_message
        # The error message returned if the request fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
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
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/437215.html) operation to query the ID of the backup schedule.
        # 
        # > If your instance is an ApsaraDB RDS for MySQL instance, you can [configure automatic access to a data source](https://help.aliyun.com/document_detail/193091.html) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The ID of the backup set. If this parameter is specified, only the snapshot of the specified backup set is returned. If this parameter is not specified, all the snapshots of the backup schedule are returned.
        self.backup_set_id = backup_set_id
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   30: This is the default value.
        # *   50\\.
        # *   100\\.
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
        # The error code returned if the request failed.
        self.code = code
        # The returned data. The following parameters are contained:
        # 
        # *   **backupSetTime**: the point in time when the snapshot was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        # *   **backupSetId**: the ID of the backup set.
        # *   **backupSetType**: the type of the snapshot. A value of **Full** indicates that the snapshot is a full backup snapshot. A value of **Inc** indicates that the snapshot is an incremental backup snapshot.
        # *   **backupPlanId**: the ID of the backup schedule.
        self.data = data
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The error message returned if the request failed.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/437215.html) operation to obtain the ID of the backup schedule.
        # 
        # > If your instance is an ApsaraDB RDS for MySQL instance, you can [configure automatic access to a data source](https://help.aliyun.com/document_detail/193091.html) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The ID of the sandbox instance. You can call the [CreateSandboxInstance](https://help.aliyun.com/document_detail/437252.html) operation to obtain the ID of the sandbox instance.
        self.instance_id = instance_id
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   30\\. This is the default value.
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
        # The error code returned if the request fails.
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
        # The error code returned if the request fails.
        self.err_code = err_code
        # The error message returned if the request fails.
        self.err_message = err_message
        # The error message returned if the request fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        # The ID of the backup schedule. You can call the [DescribeBackupPlanList](https://help.aliyun.com/document_detail/437215.html) operation to obtain the ID of the backup schedule. If you set this parameter to the backup schedule ID obtained by calling the DescribeBackupPlanList operation, the dbs prefix must be removed. Otherwise, the call fails.
        # 
        # > If your instance is an ApsaraDB RDS for MySQL instance, you can [configure automatic access to a data source](https://help.aliyun.com/document_detail/193091.html) to automatically add the instance to DBS and obtain the ID of the backup schedule.
        # 
        # This parameter is required.
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
        # The error code returned if the request fails.
        self.code = code
        # The response parameters.
        self.data = data
        # The error code returned if the request fails.
        self.err_code = err_code
        # The error message returned if the request fails.
        self.err_message = err_message
        # The error message returned if the request fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        retention: str = None,
    ):
        self.category = category
        self.instance_id = instance_id
        self.region_code = region_code
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
    ):
        self.instance_id = instance_id
        self.region_code = region_code

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
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



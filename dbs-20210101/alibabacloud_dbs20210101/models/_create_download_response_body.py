# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dbs20210101 import models as main_models
from darabonba.model import DaraModel

class CreateDownloadResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateDownloadResponseBodyData = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.CreateDownloadResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

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

class CreateDownloadResponseBodyData(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


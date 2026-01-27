# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20210101 import models as main_models
from darabonba.model import DaraModel

class DescribeDownloadTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeDownloadTaskResponseBodyData = None,
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
            temp_model = main_models.DescribeDownloadTaskResponseBodyData()
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

class DescribeDownloadTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeDownloadTaskResponseBodyDataContent = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.DescribeDownloadTaskResponseBodyDataContent()
            self.content = temp_model.from_map(m.get('Content'))

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

class DescribeDownloadTaskResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        list: List[main_models.DescribeDownloadTaskResponseBodyDataContentList] = None,
    ):
        self.list = list

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeDownloadTaskResponseBodyDataContentList()
                self.list.append(temp_model.from_map(k1))

        return self

class DescribeDownloadTaskResponseBodyDataContentList(DaraModel):
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
        # *   **csv**
        # *   **SQL**
        # *   **Parquet**
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
        # *   **OSS**
        # *   **URL**
        self.target_type = target_type
        # The download task ID.
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


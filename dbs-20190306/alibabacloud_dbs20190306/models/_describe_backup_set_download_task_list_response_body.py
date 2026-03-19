# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupSetDownloadTaskListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: main_models.DescribeBackupSetDownloadTaskListResponseBodyItems = None,
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
        self.items = items
        # The page number.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The total number of download records for backup sets.
        self.total_elements = total_elements
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.DescribeBackupSetDownloadTaskListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

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

class DescribeBackupSetDownloadTaskListResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_set_download_task_detail: List[main_models.DescribeBackupSetDownloadTaskListResponseBodyItemsBackupSetDownloadTaskDetail] = None,
    ):
        self.backup_set_download_task_detail = backup_set_download_task_detail

    def validate(self):
        if self.backup_set_download_task_detail:
            for v1 in self.backup_set_download_task_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupSetDownloadTaskDetail'] = []
        if self.backup_set_download_task_detail is not None:
            for k1 in self.backup_set_download_task_detail:
                result['BackupSetDownloadTaskDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_set_download_task_detail = []
        if m.get('BackupSetDownloadTaskDetail') is not None:
            for k1 in m.get('BackupSetDownloadTaskDetail'):
                temp_model = main_models.DescribeBackupSetDownloadTaskListResponseBodyItemsBackupSetDownloadTaskDetail()
                self.backup_set_download_task_detail.append(temp_model.from_map(k1))

        return self

class DescribeBackupSetDownloadTaskListResponseBodyItemsBackupSetDownloadTaskDetail(DaraModel):
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
        self.backup_gateway_id = backup_gateway_id
        self.backup_plan_id = backup_plan_id
        self.backup_set_code = backup_set_code
        self.backup_set_data_format = backup_set_data_format
        self.backup_set_data_size = backup_set_data_size
        self.backup_set_db_type = backup_set_db_type
        self.backup_set_download_create_time = backup_set_download_create_time
        self.backup_set_download_dir = backup_set_download_dir
        self.backup_set_download_finish_time = backup_set_download_finish_time
        self.backup_set_download_internet_url = backup_set_download_internet_url
        self.backup_set_download_intranet_url = backup_set_download_intranet_url
        self.backup_set_download_status = backup_set_download_status
        self.backup_set_download_target_type = backup_set_download_target_type
        self.backup_set_download_task_id = backup_set_download_task_id
        self.backup_set_download_task_name = backup_set_download_task_name
        self.backup_set_download_way = backup_set_download_way
        self.backup_set_id = backup_set_id
        self.backup_set_job_type = backup_set_job_type
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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


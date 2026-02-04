# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSynchronizationJobStatusListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        synchronization_job_list_status_list: List[main_models.DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList] = None,
        total_record_count: int = None,
    ):
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of data synchronization instances displayed on one page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success
        # The status of the data synchronization tasks.
        self.synchronization_job_list_status_list = synchronization_job_list_status_list
        # The total number of data synchronization instances.
        self.total_record_count = total_record_count

    def validate(self):
        if self.synchronization_job_list_status_list:
            for v1 in self.synchronization_job_list_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['SynchronizationJobListStatusList'] = []
        if self.synchronization_job_list_status_list is not None:
            for k1 in self.synchronization_job_list_status_list:
                result['SynchronizationJobListStatusList'].append(k1.to_map() if k1 else None)

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.synchronization_job_list_status_list = []
        if m.get('SynchronizationJobListStatusList') is not None:
            for k1 in m.get('SynchronizationJobListStatusList'):
                temp_model = main_models.DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList()
                self.synchronization_job_list_status_list.append(temp_model.from_map(k1))

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList(DaraModel):
    def __init__(
        self,
        synchronization_direction_info_list: List[main_models.DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList] = None,
        synchronization_job_id: str = None,
    ):
        # The details of data synchronization tasks in each direction.
        self.synchronization_direction_info_list = synchronization_direction_info_list
        # The ID of the data synchronization instance.
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        if self.synchronization_direction_info_list:
            for v1 in self.synchronization_direction_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SynchronizationDirectionInfoList'] = []
        if self.synchronization_direction_info_list is not None:
            for k1 in self.synchronization_direction_info_list:
                result['SynchronizationDirectionInfoList'].append(k1.to_map() if k1 else None)

        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronization_direction_info_list = []
        if m.get('SynchronizationDirectionInfoList') is not None:
            for k1 in m.get('SynchronizationDirectionInfoList'):
                temp_model = main_models.DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList()
                self.synchronization_direction_info_list.append(temp_model.from_map(k1))

        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')

        return self

class DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        status: str = None,
        synchronization_direction: str = None,
    ):
        # The UNIX timestamp generated when the latest data record was synchronized.
        # 
        # >  You can use a search engine to obtain a UNIX timestamp converter.
        self.checkpoint = checkpoint
        # The status of the data synchronization task in this direction. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is being prechecked.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **Initializing**: The task is performing initial synchronization.
        # *   **InitializeFailed**: Initial synchronization failed.
        # *   **Synchronizing**: The task is synchronizing data.
        # *   **Failed**: The task failed to synchronize data.
        # *   **Suspending**: The task is paused.
        # *   **Modifying**: The objects in the task are being modified.
        # *   **Finished**: The task is completed.
        self.status = status
        # The synchronization direction. Valid values:
        # 
        # *   **Forward**
        # *   **Reverse**
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.status is not None:
            result['Status'] = self.status

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        return self


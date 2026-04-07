# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaTableOutputResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaTableOutputResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMetaTableOutputResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMetaTableOutputResponseBodyData(DaraModel):
    def __init__(
        self,
        data_entity_list: List[main_models.GetMetaTableOutputResponseBodyDataDataEntityList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The partitions.
        self.data_entity_list = data_entity_list
        # The page number. Valid values: 1 to 30. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data_entity_list:
            for v1 in self.data_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k1 in self.data_entity_list:
                result['DataEntityList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_entity_list = []
        if m.get('DataEntityList') is not None:
            for k1 in m.get('DataEntityList'):
                temp_model = main_models.GetMetaTableOutputResponseBodyDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetMetaTableOutputResponseBodyDataDataEntityList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        project_id: int = None,
        start_time: str = None,
        table_guid: str = None,
        task_id: str = None,
        task_instance_id: int = None,
        wait_time: str = None,
    ):
        # The end time.
        self.end_time = end_time
        # The workspace ID.
        self.project_id = project_id
        # The start time.
        self.start_time = start_time
        # The GUID of the MaxCompute table.
        self.table_guid = table_guid
        # The task ID.
        self.task_id = task_id
        # The instance ID.
        self.task_instance_id = task_instance_id
        # The waiting time.
        self.wait_time = wait_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self


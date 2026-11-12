# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeActiveOperationTaskResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeActiveOperationTaskResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of tasks.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeActiveOperationTaskResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeActiveOperationTaskResponseBodyItems(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        db_type: str = None,
        db_version: str = None,
        deadline: str = None,
        id: int = None,
        ins_name: str = None,
        modified_time: str = None,
        prepare_interval: str = None,
        region: str = None,
        result_info: str = None,
        start_time: str = None,
        status: int = None,
        switch_time: str = None,
        task_params: str = None,
        task_type: str = None,
    ):
        # The time when the task was created. The time is displayed in the `yyyy-MM-ddTHH:mmZ` format (UTC).
        self.created_time = created_time
        # The database engine type.
        self.db_type = db_type
        # The database engine version.
        self.db_version = db_version
        # The latest deadline within the adjustable range for task execution time. The time is displayed in the `yyyy-MM-ddTHH:mmZ` format (UTC).
        self.deadline = deadline
        # The task ID.
        self.id = id
        # The cluster name.
        self.ins_name = ins_name
        # The time when the task was modified. The time is displayed in the `yyyy-MM-ddTHH:mmZ` format (UTC).
        self.modified_time = modified_time
        # The preparation time before the transient disconnection. The time is displayed in the `HH:mm:ss` format.
        self.prepare_interval = prepare_interval
        # The region where the task is located.
        self.region = region
        # The task execution result.
        self.result_info = result_info
        # The time when the task is executed in the background. The time is displayed in the `yyyy-MM-ddTHH:mmZ` format (UTC).
        self.start_time = start_time
        # The task status.
        # * If you set `IsHistory` to **0**, the details of the pending task status are returned. Valid values:
        # 
        #     * **2**: Waiting for the user to set the task start time.
        #     * **3**: Waiting to be processed.
        #     * **4**: The task is being processed.
        # 
        # * If you set `IsHistory` to **1**, the details of the historical task status are returned. Valid values:
        #      * **5**: The task is completed and executed successfully.
        #      * **6**: The task is completed but failed.
        #      * **7**: The task is canceled.
        self.status = status
        # The time when the transient disconnection occurs. The time is displayed in the `yyyy-MM-ddTHH:mmZ` format (UTC).
        self.switch_time = switch_time
        # The task parameters.
        self.task_params = task_params
        # The task type.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.deadline is not None:
            result['Deadline'] = self.deadline

        if self.id is not None:
            result['Id'] = self.id

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.prepare_interval is not None:
            result['PrepareInterval'] = self.prepare_interval

        if self.region is not None:
            result['Region'] = self.region

        if self.result_info is not None:
            result['ResultInfo'] = self.result_info

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.task_params is not None:
            result['TaskParams'] = self.task_params

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('PrepareInterval') is not None:
            self.prepare_interval = m.get('PrepareInterval')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResultInfo') is not None:
            self.result_info = m.get('ResultInfo')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self


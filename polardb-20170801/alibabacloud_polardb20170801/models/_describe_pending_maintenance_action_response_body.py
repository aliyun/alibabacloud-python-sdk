# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePendingMaintenanceActionResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribePendingMaintenanceActionResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # Details about tasks.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
                temp_model = main_models.DescribePendingMaintenanceActionResponseBodyItems()
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

class DescribePendingMaintenanceActionResponseBodyItems(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        dbcluster_id: str = None,
        dbtype: str = None,
        dbversion: str = None,
        deadline: str = None,
        id: int = None,
        modified_time: str = None,
        prepare_interval: str = None,
        region: str = None,
        result_info: str = None,
        start_time: str = None,
        status: int = None,
        switch_time: str = None,
        task_type: str = None,
    ):
        # The time when the task was created. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.created_time = created_time
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The type of the database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **PostgreSQL**
        # *   **Oracle**
        self.dbtype = dbtype
        # The version of the database engine.
        # 
        # *   Valid values for the MySQL database engine:
        # 
        #     *   **5.6**
        #     *   **5.7**
        #     *   **8.0**
        # 
        # *   Valid values for the PostgreSQL database engine:
        # 
        #     *   **11**
        #     *   **14**
        # 
        # *   Valid value for the Oracle database engine: **11**
        self.dbversion = dbversion
        # The deadline before which the task can be executed. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.deadline = deadline
        # The ID of the task.
        self.id = id
        # The time when the parameter was modified. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The preparation time that is required before the pending event is switched. The time follows the `HH:mm:ss` format.
        self.prepare_interval = prepare_interval
        # The region ID of the pending event.
        self.region = region
        # The execution result of the task. Valid values:
        # 
        # *   **manualCancel**: The task is manually canceled.
        # *   **paramCheckNotPass**: The task fails to pass the parameter check.
        # 
        # > This parameter is returned only when the value of the `Status` parameter is **6** or **7**. The value 6 indicates that the task is completed but fails to be executed. The value 7 indicates that the task is canceled.
        self.result_info = result_info
        # The time when the task was executed in the background. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.start_time = start_time
        # The status of the pending task.
        # 
        # *   If you set the `IsHistory` parameter to **0**, the status of the pending task is returned. Valid values:
        # 
        #     *   **2**: The start time of the task is to be specified.
        #     *   **3**: The task is pending.
        #     *   **4**: The task is running. In this case, you cannot modify the execution time.
        # 
        # *   If you set the `IsHistory` parameter to **1**, the details of the historical tasks are returned. Valid values:
        # 
        #     *   **5**: The task is completed and executed.
        #     *   **6**: The task is completed but fails to be executed.
        #     *   **7**: The task is canceled.
        self.status = status
        # The time when the pending event was switched. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.switch_time = switch_time
        # The type of the pending event.
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

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.deadline is not None:
            result['Deadline'] = self.deadline

        if self.id is not None:
            result['Id'] = self.id

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

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self


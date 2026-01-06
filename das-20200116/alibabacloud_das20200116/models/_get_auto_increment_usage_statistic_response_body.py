# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetAutoIncrementUsageStatisticResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAutoIncrementUsageStatisticResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # >  If the request is successful, **Successful** is returned. Otherwise, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetAutoIncrementUsageStatisticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAutoIncrementUsageStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_increment_usage_list: List[main_models.GetAutoIncrementUsageStatisticResponseBodyDataAutoIncrementUsageList] = None,
        error_info: str = None,
        finish: bool = None,
        task_status: str = None,
        timestamp: int = None,
    ):
        # The usage details of auto-increment IDs.
        self.auto_increment_usage_list = auto_increment_usage_list
        # The error message returned if the task fails.
        self.error_info = error_info
        # Indicates whether the task is complete. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.finish = finish
        # The task status. Valid values:
        # 
        # *   **INIT**: The task is being initialized.
        # *   **RUNNING**: The task is being executed.
        # *   **SUCCESS**: The task succeeds.
        # *   **FAIL**: The task fails.
        self.task_status = task_status
        # The time when the request was made. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp

    def validate(self):
        if self.auto_increment_usage_list:
            for v1 in self.auto_increment_usage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoIncrementUsageList'] = []
        if self.auto_increment_usage_list is not None:
            for k1 in self.auto_increment_usage_list:
                result['AutoIncrementUsageList'].append(k1.to_map() if k1 else None)

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.finish is not None:
            result['Finish'] = self.finish

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_increment_usage_list = []
        if m.get('AutoIncrementUsageList') is not None:
            for k1 in m.get('AutoIncrementUsageList'):
                temp_model = main_models.GetAutoIncrementUsageStatisticResponseBodyDataAutoIncrementUsageList()
                self.auto_increment_usage_list.append(temp_model.from_map(k1))

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('Finish') is not None:
            self.finish = m.get('Finish')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetAutoIncrementUsageStatisticResponseBodyDataAutoIncrementUsageList(DaraModel):
    def __init__(
        self,
        auto_increment_current_value: int = None,
        auto_increment_ratio: float = None,
        column_name: str = None,
        db_name: str = None,
        maximum_value: int = None,
        table_name: str = None,
    ):
        # The latest auto-increment ID.
        self.auto_increment_current_value = auto_increment_current_value
        # The usage ratio of auto-increment IDs.
        self.auto_increment_ratio = auto_increment_ratio
        # The column name.
        self.column_name = column_name
        # The database name.
        self.db_name = db_name
        # The maximum auto-increment ID that is supported by the current data type.
        self.maximum_value = maximum_value
        # The table name.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_increment_current_value is not None:
            result['AutoIncrementCurrentValue'] = self.auto_increment_current_value

        if self.auto_increment_ratio is not None:
            result['AutoIncrementRatio'] = self.auto_increment_ratio

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.maximum_value is not None:
            result['MaximumValue'] = self.maximum_value

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrementCurrentValue') is not None:
            self.auto_increment_current_value = m.get('AutoIncrementCurrentValue')

        if m.get('AutoIncrementRatio') is not None:
            self.auto_increment_ratio = m.get('AutoIncrementRatio')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('MaximumValue') is not None:
            self.maximum_value = m.get('MaximumValue')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self


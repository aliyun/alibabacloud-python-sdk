# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeModifyParameterLogResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        engine: str = None,
        engine_version: str = None,
        items: main_models.DescribeModifyParameterLogResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The database engine of the instance.
        self.engine = engine
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The log entries.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeModifyParameterLogResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeModifyParameterLogResponseBodyItems(DaraModel):
    def __init__(
        self,
        parameter_change_log: List[main_models.DescribeModifyParameterLogResponseBodyItemsParameterChangeLog] = None,
    ):
        self.parameter_change_log = parameter_change_log

    def validate(self):
        if self.parameter_change_log:
            for v1 in self.parameter_change_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ParameterChangeLog'] = []
        if self.parameter_change_log is not None:
            for k1 in self.parameter_change_log:
                result['ParameterChangeLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter_change_log = []
        if m.get('ParameterChangeLog') is not None:
            for k1 in m.get('ParameterChangeLog'):
                temp_model = main_models.DescribeModifyParameterLogResponseBodyItemsParameterChangeLog()
                self.parameter_change_log.append(temp_model.from_map(k1))

        return self

class DescribeModifyParameterLogResponseBodyItemsParameterChangeLog(DaraModel):
    def __init__(
        self,
        modify_time: str = None,
        new_parameter_value: str = None,
        old_parameter_value: str = None,
        parameter_name: str = None,
        status: str = None,
    ):
        # The time when the parameter was modified. This value is a UNIX timestamp. Unit: milliseconds.
        self.modify_time = modify_time
        # The new value of the parameter.
        self.new_parameter_value = new_parameter_value
        # The original value of the parameter.
        self.old_parameter_value = old_parameter_value
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The status. Valid values:
        # 
        # *   **Applied:** The new value has taken effect.
        # *   **Syncing:** The new value is being applied and has not taken effect.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.new_parameter_value is not None:
            result['NewParameterValue'] = self.new_parameter_value

        if self.old_parameter_value is not None:
            result['OldParameterValue'] = self.old_parameter_value

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NewParameterValue') is not None:
            self.new_parameter_value = m.get('NewParameterValue')

        if m.get('OldParameterValue') is not None:
            self.old_parameter_value = m.get('OldParameterValue')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


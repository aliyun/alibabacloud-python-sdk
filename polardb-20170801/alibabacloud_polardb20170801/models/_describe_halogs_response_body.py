# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeHALogsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dbinstance_type: str = None,
        ha_log_items: List[main_models.DescribeHALogsResponseBodyHaLogItems] = None,
        ha_status: int = None,
        items_numbers: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_records: int = None,
    ):
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The instance type. Valid values:
        # 
        # - **polardb_mysql_rw**: read-write instance.
        # - **polardb_mysql_ro**: read-only instance.
        # - **polardb_mysql_standby**: standby instance.
        self.dbinstance_type = dbinstance_type
        # The list of primary/secondary 这里 AI 机翻使用了 failover，但代码里用了 switch，建议保持一致，都改为 swichover logs.
        self.ha_log_items = ha_log_items
        # Indicates whether primary/secondary switchover records exist. Valid values:
        # 
        # - **1**: No
        # - **0**: Yes
        self.ha_status = ha_status
        # The number of items in the log list on the current page.
        self.items_numbers = items_numbers
        # The page number. The value is greater than 0 and does not exceed the maximum value of the Integer data type. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page. Valid values: 30 to 100. Default value: 30.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_records = total_records

    def validate(self):
        if self.ha_log_items:
            for v1 in self.ha_log_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        result['HaLogItems'] = []
        if self.ha_log_items is not None:
            for k1 in self.ha_log_items:
                result['HaLogItems'].append(k1.to_map() if k1 else None)

        if self.ha_status is not None:
            result['HaStatus'] = self.ha_status

        if self.items_numbers is not None:
            result['ItemsNumbers'] = self.items_numbers

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_records is not None:
            result['TotalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        self.ha_log_items = []
        if m.get('HaLogItems') is not None:
            for k1 in m.get('HaLogItems'):
                temp_model = main_models.DescribeHALogsResponseBodyHaLogItems()
                self.ha_log_items.append(temp_model.from_map(k1))

        if m.get('HaStatus') is not None:
            self.ha_status = m.get('HaStatus')

        if m.get('ItemsNumbers') is not None:
            self.items_numbers = m.get('ItemsNumbers')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')

        return self

class DescribeHALogsResponseBodyHaLogItems(DaraModel):
    def __init__(
        self,
        switch_cause_code: str = None,
        switch_cause_detail: str = None,
        switch_finish_time: str = None,
        switch_id: str = None,
        switch_start_time: str = None,
    ):
        # The cause code of the switchover.
        self.switch_cause_code = switch_cause_code
        # The cause of the switchover.
        self.switch_cause_detail = switch_cause_detail
        # The end time of the switchover.
        self.switch_finish_time = switch_finish_time
        # The ID of the primary/secondary switchover log.
        self.switch_id = switch_id
        # The start time of the switchover.
        self.switch_start_time = switch_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.switch_cause_code is not None:
            result['SwitchCauseCode'] = self.switch_cause_code

        if self.switch_cause_detail is not None:
            result['SwitchCauseDetail'] = self.switch_cause_detail

        if self.switch_finish_time is not None:
            result['SwitchFinishTime'] = self.switch_finish_time

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.switch_start_time is not None:
            result['SwitchStartTime'] = self.switch_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchCauseCode') is not None:
            self.switch_cause_code = m.get('SwitchCauseCode')

        if m.get('SwitchCauseDetail') is not None:
            self.switch_cause_detail = m.get('SwitchCauseDetail')

        if m.get('SwitchFinishTime') is not None:
            self.switch_finish_time = m.get('SwitchFinishTime')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('SwitchStartTime') is not None:
            self.switch_start_time = m.get('SwitchStartTime')

        return self


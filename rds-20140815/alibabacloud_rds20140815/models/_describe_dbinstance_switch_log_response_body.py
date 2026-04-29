# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceSwitchLogResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        items: main_models.DescribeDBInstanceSwitchLogResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

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
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstanceSwitchLogResponseBodyItems()
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

class DescribeDBInstanceSwitchLogResponseBodyItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.DescribeDBInstanceSwitchLogResponseBodyItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.DescribeDBInstanceSwitchLogResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceSwitchLogResponseBodyItemsItem(DaraModel):
    def __init__(
        self,
        affected_sessions: str = None,
        hastatus: str = None,
        switch_cause_code: str = None,
        switch_cause_detail: str = None,
        switch_finish_time: str = None,
        switch_id: str = None,
        switch_start_time: str = None,
        total_sessions: str = None,
    ):
        self.affected_sessions = affected_sessions
        self.hastatus = hastatus
        self.switch_cause_code = switch_cause_code
        self.switch_cause_detail = switch_cause_detail
        self.switch_finish_time = switch_finish_time
        self.switch_id = switch_id
        self.switch_start_time = switch_start_time
        self.total_sessions = total_sessions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_sessions is not None:
            result['AffectedSessions'] = self.affected_sessions

        if self.hastatus is not None:
            result['HAStatus'] = self.hastatus

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

        if self.total_sessions is not None:
            result['TotalSessions'] = self.total_sessions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedSessions') is not None:
            self.affected_sessions = m.get('AffectedSessions')

        if m.get('HAStatus') is not None:
            self.hastatus = m.get('HAStatus')

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

        if m.get('TotalSessions') is not None:
            self.total_sessions = m.get('TotalSessions')

        return self


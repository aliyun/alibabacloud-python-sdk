# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.ListTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        record: List[main_models.ListTaskResponseBodyDataRecord] = None,
        total: int = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.record = record
        self.total = total

    def validate(self):
        if self.record:
            for v1 in self.record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Record'] = []
        if self.record is not None:
            for k1 in self.record:
                result['Record'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.record = []
        if m.get('Record') is not None:
            for k1 in m.get('Record'):
                temp_model = main_models.ListTaskResponseBodyDataRecord()
                self.record.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListTaskResponseBodyDataRecord(DaraModel):
    def __init__(
        self,
        complete_count: int = None,
        fire_time: str = None,
        gmt_create: str = None,
        id: int = None,
        robot_id: int = None,
        robot_name: str = None,
        status: str = None,
        task_name: str = None,
        total_count: int = None,
    ):
        self.complete_count = complete_count
        self.fire_time = fire_time
        self.gmt_create = gmt_create
        self.id = id
        self.robot_id = robot_id
        self.robot_name = robot_name
        self.status = status
        self.task_name = task_name
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_count is not None:
            result['CompleteCount'] = self.complete_count

        if self.fire_time is not None:
            result['FireTime'] = self.fire_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.robot_id is not None:
            result['RobotId'] = self.robot_id

        if self.robot_name is not None:
            result['RobotName'] = self.robot_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteCount') is not None:
            self.complete_count = m.get('CompleteCount')

        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')

        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self


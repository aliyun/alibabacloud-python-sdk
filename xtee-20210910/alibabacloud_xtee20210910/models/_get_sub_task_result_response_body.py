# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class GetSubTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.GetSubTaskResultResponseBodyResultObject = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.GetSubTaskResultResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class GetSubTaskResultResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        config: List[main_models.GetSubTaskResultResponseBodyResultObjectConfig] = None,
        extra_info: str = None,
        file: main_models.GetSubTaskResultResponseBodyResultObjectFile = None,
        file_name: str = None,
        file_type: str = None,
        file_url: str = None,
        is_charge: bool = None,
        log: List[main_models.GetSubTaskResultResponseBodyResultObjectLog] = None,
        reason: str = None,
        result_url: str = None,
        schedule_type: str = None,
        service_code: str = None,
        service_name: str = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        user_id: int = None,
    ):
        self.config = config
        self.extra_info = extra_info
        self.file = file
        self.file_name = file_name
        self.file_type = file_type
        self.file_url = file_url
        self.is_charge = is_charge
        self.log = log
        self.reason = reason
        self.result_url = result_url
        self.schedule_type = schedule_type
        self.service_code = service_code
        self.service_name = service_name
        self.status = status
        self.task_id = task_id
        self.task_name = task_name
        self.user_id = user_id

    def validate(self):
        if self.config:
            for v1 in self.config:
                 if v1:
                    v1.validate()
        if self.file:
            self.file.validate()
        if self.log:
            for v1 in self.log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Config'] = []
        if self.config is not None:
            for k1 in self.config:
                result['Config'].append(k1.to_map() if k1 else None)

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.is_charge is not None:
            result['IsCharge'] = self.is_charge

        result['Log'] = []
        if self.log is not None:
            for k1 in self.log:
                result['Log'].append(k1.to_map() if k1 else None)

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.result_url is not None:
            result['ResultUrl'] = self.result_url

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config = []
        if m.get('Config') is not None:
            for k1 in m.get('Config'):
                temp_model = main_models.GetSubTaskResultResponseBodyResultObjectConfig()
                self.config.append(temp_model.from_map(k1))

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('File') is not None:
            temp_model = main_models.GetSubTaskResultResponseBodyResultObjectFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('IsCharge') is not None:
            self.is_charge = m.get('IsCharge')

        self.log = []
        if m.get('Log') is not None:
            for k1 in m.get('Log'):
                temp_model = main_models.GetSubTaskResultResponseBodyResultObjectLog()
                self.log.append(temp_model.from_map(k1))

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetSubTaskResultResponseBodyResultObjectLog(DaraModel):
    def __init__(
        self,
        operate_type: str = None,
        reason: str = None,
        time: int = None,
    ):
        self.operate_type = operate_type
        self.reason = reason
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class GetSubTaskResultResponseBodyResultObjectFile(DaraModel):
    def __init__(
        self,
        col: List[main_models.GetSubTaskResultResponseBodyResultObjectFileCol] = None,
        title: List[str] = None,
    ):
        self.col = col
        self.title = title

    def validate(self):
        if self.col:
            for v1 in self.col:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Col'] = []
        if self.col is not None:
            for k1 in self.col:
                result['Col'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.col = []
        if m.get('Col') is not None:
            for k1 in m.get('Col'):
                temp_model = main_models.GetSubTaskResultResponseBodyResultObjectFileCol()
                self.col.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetSubTaskResultResponseBodyResultObjectFileCol(DaraModel):
    def __init__(
        self,
        a_0: str = None,
        a_1: str = None,
        a_10: str = None,
        a_11: str = None,
        a_2: str = None,
        a_3: str = None,
        a_4: str = None,
        a_5: str = None,
        a_6: str = None,
        a_7: str = None,
        a_8: str = None,
        a_9: str = None,
    ):
        # A0。
        self.a_0 = a_0
        # A1。
        self.a_1 = a_1
        # A10。
        self.a_10 = a_10
        # A11。
        self.a_11 = a_11
        # A2。
        self.a_2 = a_2
        # A3。
        self.a_3 = a_3
        # A4。
        self.a_4 = a_4
        # A5。
        self.a_5 = a_5
        # A6。
        self.a_6 = a_6
        # A7。
        self.a_7 = a_7
        # A8。
        self.a_8 = a_8
        # A9。
        self.a_9 = a_9

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.a_0 is not None:
            result['A0'] = self.a_0

        if self.a_1 is not None:
            result['A1'] = self.a_1

        if self.a_10 is not None:
            result['A10'] = self.a_10

        if self.a_11 is not None:
            result['A11'] = self.a_11

        if self.a_2 is not None:
            result['A2'] = self.a_2

        if self.a_3 is not None:
            result['A3'] = self.a_3

        if self.a_4 is not None:
            result['A4'] = self.a_4

        if self.a_5 is not None:
            result['A5'] = self.a_5

        if self.a_6 is not None:
            result['A6'] = self.a_6

        if self.a_7 is not None:
            result['A7'] = self.a_7

        if self.a_8 is not None:
            result['A8'] = self.a_8

        if self.a_9 is not None:
            result['A9'] = self.a_9

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('A0') is not None:
            self.a_0 = m.get('A0')

        if m.get('A1') is not None:
            self.a_1 = m.get('A1')

        if m.get('A10') is not None:
            self.a_10 = m.get('A10')

        if m.get('A11') is not None:
            self.a_11 = m.get('A11')

        if m.get('A2') is not None:
            self.a_2 = m.get('A2')

        if m.get('A3') is not None:
            self.a_3 = m.get('A3')

        if m.get('A4') is not None:
            self.a_4 = m.get('A4')

        if m.get('A5') is not None:
            self.a_5 = m.get('A5')

        if m.get('A6') is not None:
            self.a_6 = m.get('A6')

        if m.get('A7') is not None:
            self.a_7 = m.get('A7')

        if m.get('A8') is not None:
            self.a_8 = m.get('A8')

        if m.get('A9') is not None:
            self.a_9 = m.get('A9')

        return self

class GetSubTaskResultResponseBodyResultObjectConfig(DaraModel):
    def __init__(
        self,
        item: str = None,
        item_desc: str = None,
        sample_item: str = None,
        sample_items: List[str] = None,
    ):
        self.item = item
        self.item_desc = item_desc
        self.sample_item = sample_item
        self.sample_items = sample_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item is not None:
            result['Item'] = self.item

        if self.item_desc is not None:
            result['ItemDesc'] = self.item_desc

        if self.sample_item is not None:
            result['SampleItem'] = self.sample_item

        if self.sample_items is not None:
            result['SampleItems'] = self.sample_items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('ItemDesc') is not None:
            self.item_desc = m.get('ItemDesc')

        if m.get('SampleItem') is not None:
            self.sample_item = m.get('SampleItem')

        if m.get('SampleItems') is not None:
            self.sample_items = m.get('SampleItems')

        return self


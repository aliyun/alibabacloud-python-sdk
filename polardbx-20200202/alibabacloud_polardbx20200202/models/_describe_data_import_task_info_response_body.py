# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDataImportTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeDataImportTaskInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
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
            temp_model = main_models.DescribeDataImportTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDataImportTaskInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        data_import_task_detail_info: main_models.DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfo = None,
    ):
        self.data_import_task_detail_info = data_import_task_detail_info

    def validate(self):
        if self.data_import_task_detail_info:
            self.data_import_task_detail_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_import_task_detail_info is not None:
            result['DataImportTaskDetailInfo'] = self.data_import_task_detail_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataImportTaskDetailInfo') is not None:
            temp_model = main_models.DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfo()
            self.data_import_task_detail_info = temp_model.from_map(m.get('DataImportTaskDetailInfo'))

        return self

class DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfo(DaraModel):
    def __init__(
        self,
        fsm_id: int = None,
        fsm_state: str = None,
        fsm_status: str = None,
        service_detail_list: List[main_models.DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfoServiceDetailList] = None,
    ):
        self.fsm_id = fsm_id
        self.fsm_state = fsm_state
        self.fsm_status = fsm_status
        self.service_detail_list = service_detail_list

    def validate(self):
        if self.service_detail_list:
            for v1 in self.service_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fsm_id is not None:
            result['FsmId'] = self.fsm_id

        if self.fsm_state is not None:
            result['FsmState'] = self.fsm_state

        if self.fsm_status is not None:
            result['FsmStatus'] = self.fsm_status

        result['ServiceDetailList'] = []
        if self.service_detail_list is not None:
            for k1 in self.service_detail_list:
                result['ServiceDetailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FsmId') is not None:
            self.fsm_id = m.get('FsmId')

        if m.get('FsmState') is not None:
            self.fsm_state = m.get('FsmState')

        if m.get('FsmStatus') is not None:
            self.fsm_status = m.get('FsmStatus')

        self.service_detail_list = []
        if m.get('ServiceDetailList') is not None:
            for k1 in m.get('ServiceDetailList'):
                temp_model = main_models.DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfoServiceDetailList()
                self.service_detail_list.append(temp_model.from_map(k1))

        return self

class DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfoServiceDetailList(DaraModel):
    def __init__(
        self,
        id: int = None,
        status: str = None,
        task_detail_list: List[main_models.DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfoServiceDetailListTaskDetailList] = None,
        type: str = None,
    ):
        self.id = id
        self.status = status
        self.task_detail_list = task_detail_list
        self.type = type

    def validate(self):
        if self.task_detail_list:
            for v1 in self.task_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        result['TaskDetailList'] = []
        if self.task_detail_list is not None:
            for k1 in self.task_detail_list:
                result['TaskDetailList'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.task_detail_list = []
        if m.get('TaskDetailList') is not None:
            for k1 in m.get('TaskDetailList'):
                temp_model = main_models.DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfoServiceDetailListTaskDetailList()
                self.task_detail_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeDataImportTaskInfoResponseBodyDataDataImportTaskDetailInfoServiceDetailListTaskDetailList(DaraModel):
    def __init__(
        self,
        delay: int = None,
        last_error: str = None,
        physical_db_name: str = None,
        progress: int = None,
        statistics: str = None,
        status: str = None,
        task_id: int = None,
        type: str = None,
    ):
        self.delay = delay
        self.last_error = last_error
        self.physical_db_name = physical_db_name
        self.progress = progress
        self.statistics = statistics
        self.status = status
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay is not None:
            result['Delay'] = self.delay

        if self.last_error is not None:
            result['LastError'] = self.last_error

        if self.physical_db_name is not None:
            result['PhysicalDbName'] = self.physical_db_name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('LastError') is not None:
            self.last_error = m.get('LastError')

        if m.get('PhysicalDbName') is not None:
            self.physical_db_name = m.get('PhysicalDbName')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


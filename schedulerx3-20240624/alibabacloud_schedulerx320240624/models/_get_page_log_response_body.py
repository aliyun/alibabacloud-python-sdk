# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class GetPageLogResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetPageLogResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = main_models.GetPageLogResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPageLogResponseBodyData(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        records: List[main_models.GetPageLogResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        # -
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.GetPageLogResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetPageLogResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        job_execution_id: str = None,
        job_name: str = None,
        log: str = None,
        time: str = None,
        user_id: str = None,
        worker_addr: str = None,
    ):
        self.app_name = app_name
        self.job_execution_id = job_execution_id
        self.job_name = job_name
        self.log = log
        self.time = time
        self.user_id = user_id
        self.worker_addr = worker_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.log is not None:
            result['Log'] = self.log

        if self.time is not None:
            result['Time'] = self.time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Log') is not None:
            self.log = m.get('Log')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')

        return self


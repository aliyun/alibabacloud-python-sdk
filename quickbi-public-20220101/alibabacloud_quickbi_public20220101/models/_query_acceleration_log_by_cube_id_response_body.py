# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryAccelerationLogByCubeIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryAccelerationLogByCubeIdResponseBodyResult = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryAccelerationLogByCubeIdResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAccelerationLogByCubeIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryAccelerationLogByCubeIdResponseBodyResultData] = None,
        next: int = None,
        page_num: int = None,
        page_size: int = None,
        pre: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        self.data = data
        self.next = next
        self.page_num = page_num
        self.page_size = page_size
        self.pre = pre
        self.total_num = total_num
        self.total_pages = total_pages

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next is not None:
            result['Next'] = self.next

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre is not None:
            result['Pre'] = self.pre

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryAccelerationLogByCubeIdResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            self.next = m.get('Next')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pre') is not None:
            self.pre = m.get('Pre')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class QueryAccelerationLogByCubeIdResponseBodyResultData(DaraModel):
    def __init__(
        self,
        duration: str = None,
        job_history_id: str = None,
        job_id: str = None,
        job_status: str = None,
        jon_start_date: str = None,
        log: str = None,
    ):
        self.duration = duration
        self.job_history_id = job_history_id
        self.job_id = job_id
        self.job_status = job_status
        self.jon_start_date = jon_start_date
        self.log = log

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.job_history_id is not None:
            result['JobHistoryId'] = self.job_history_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.jon_start_date is not None:
            result['JonStartDate'] = self.jon_start_date

        if self.log is not None:
            result['Log'] = self.log

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('JobHistoryId') is not None:
            self.job_history_id = m.get('JobHistoryId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('JonStartDate') is not None:
            self.jon_start_date = m.get('JonStartDate')

        if m.get('Log') is not None:
            self.log = m.get('Log')

        return self


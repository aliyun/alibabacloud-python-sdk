# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetPhysicalInstanceLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        taskrun_log_list: List[main_models.GetPhysicalInstanceLogResponseBodyTaskrunLogList] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.taskrun_log_list = taskrun_log_list

    def validate(self):
        if self.taskrun_log_list:
            for v1 in self.taskrun_log_list:
                 if v1:
                    v1.validate()

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

        if self.success is not None:
            result['Success'] = self.success

        result['TaskrunLogList'] = []
        if self.taskrun_log_list is not None:
            for k1 in self.taskrun_log_list:
                result['TaskrunLogList'].append(k1.to_map() if k1 else None)

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

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.taskrun_log_list = []
        if m.get('TaskrunLogList') is not None:
            for k1 in m.get('TaskrunLogList'):
                temp_model = main_models.GetPhysicalInstanceLogResponseBodyTaskrunLogList()
                self.taskrun_log_list.append(temp_model.from_map(k1))

        return self

class GetPhysicalInstanceLogResponseBodyTaskrunLogList(DaraModel):
    def __init__(
        self,
        duration: str = None,
        end_time: str = None,
        log_content: str = None,
        start_time: str = None,
        status: str = None,
        taskrun_id: str = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.log_content = log_content
        self.start_time = start_time
        self.status = status
        self.taskrun_id = taskrun_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log_content is not None:
            result['LogContent'] = self.log_content

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.taskrun_id is not None:
            result['TaskrunId'] = self.taskrun_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskrunId') is not None:
            self.taskrun_id = m.get('TaskrunId')

        return self


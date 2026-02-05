# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class CreateBatchRepeatJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        job_group: main_models.CreateBatchRepeatJobResponseBodyJobGroup = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.job_group = job_group
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.job_group:
            self.job_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.job_group is not None:
            result['JobGroup'] = self.job_group.to_map()

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('JobGroup') is not None:
            temp_model = main_models.CreateBatchRepeatJobResponseBodyJobGroup()
            self.job_group = temp_model.from_map(m.get('JobGroup'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateBatchRepeatJobResponseBodyJobGroup(DaraModel):
    def __init__(
        self,
        id: str = None,
        min_concurrency: int = None,
        priority: str = None,
        ringing_duration: int = None,
    ):
        self.id = id
        self.min_concurrency = min_concurrency
        self.priority = priority
        self.ringing_duration = ringing_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.min_concurrency is not None:
            result['MinConcurrency'] = self.min_concurrency

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.ringing_duration is not None:
            result['RingingDuration'] = self.ringing_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MinConcurrency') is not None:
            self.min_concurrency = m.get('MinConcurrency')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RingingDuration') is not None:
            self.ringing_duration = m.get('RingingDuration')

        return self


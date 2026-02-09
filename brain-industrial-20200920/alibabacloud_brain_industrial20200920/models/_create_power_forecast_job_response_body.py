# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_brain_industrial20200920 import models as main_models
from darabonba.model import DaraModel

class CreatePowerForecastJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreatePowerForecastJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
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
            temp_model = main_models.CreatePowerForecastJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreatePowerForecastJobResponseBodyData(DaraModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: main_models.CreatePowerForecastJobResponseBodyDataResponse = None,
        status: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.job_id = job_id
        self.progress = progress
        self.response = response
        self.status = status

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed is not None:
            result['Completed'] = self.completed

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error is not None:
            result['Error'] = self.error

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.response is not None:
            result['Response'] = self.response.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Response') is not None:
            temp_model = main_models.CreatePowerForecastJobResponseBodyDataResponse()
            self.response = temp_model.from_map(m.get('Response'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CreatePowerForecastJobResponseBodyDataResponse(DaraModel):
    def __init__(
        self,
        debug_info: Any = None,
        job_type: str = None,
        result: Any = None,
    ):
        self.debug_info = debug_info
        self.job_type = job_type
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class ListJobStepResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        job_steps: List[main_models.ListJobStepResponseBodyJobSteps] = None,
        request_id: str = None,
        success: bool = None,
        use_v2api: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.job_steps = job_steps
        self.request_id = request_id
        self.success = success
        self.use_v2api = use_v2api

    def validate(self):
        if self.job_steps:
            for v1 in self.job_steps:
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

        result['JobSteps'] = []
        if self.job_steps is not None:
            for k1 in self.job_steps:
                result['JobSteps'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.use_v2api is not None:
            result['UseV2API'] = self.use_v2api

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.job_steps = []
        if m.get('JobSteps') is not None:
            for k1 in m.get('JobSteps'):
                temp_model = main_models.ListJobStepResponseBodyJobSteps()
                self.job_steps.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UseV2API') is not None:
            self.use_v2api = m.get('UseV2API')

        return self

class ListJobStepResponseBodyJobSteps(DaraModel):
    def __init__(
        self,
        boot_time: str = None,
        code: str = None,
        create_time: str = None,
        err_msg: str = None,
        error_details: List[main_models.ListJobStepResponseBodyJobStepsErrorDetails] = None,
        finish_time: str = None,
        inc_latency_milliseconds: int = None,
        inc_latency_seconds: int = None,
        job_step_id: str = None,
        job_step_name: str = None,
        modify_time: str = None,
        need_acceleration: bool = None,
        progress: int = None,
        serial: int = None,
        state: str = None,
        sub_job_count: int = None,
        sub_job_steps: List[main_models.ListJobStepResponseBodyJobStepsSubJobSteps] = None,
        redis_phase_type: str = None,
    ):
        self.boot_time = boot_time
        self.code = code
        self.create_time = create_time
        self.err_msg = err_msg
        self.error_details = error_details
        self.finish_time = finish_time
        self.inc_latency_milliseconds = inc_latency_milliseconds
        self.inc_latency_seconds = inc_latency_seconds
        self.job_step_id = job_step_id
        self.job_step_name = job_step_name
        self.modify_time = modify_time
        self.need_acceleration = need_acceleration
        self.progress = progress
        self.serial = serial
        self.state = state
        self.sub_job_count = sub_job_count
        self.sub_job_steps = sub_job_steps
        self.redis_phase_type = redis_phase_type

    def validate(self):
        if self.error_details:
            for v1 in self.error_details:
                 if v1:
                    v1.validate()
        if self.sub_job_steps:
            for v1 in self.sub_job_steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time

        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k1 in self.error_details:
                result['ErrorDetails'].append(k1.to_map() if k1 else None)

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.inc_latency_milliseconds is not None:
            result['IncLatencyMilliseconds'] = self.inc_latency_milliseconds

        if self.inc_latency_seconds is not None:
            result['IncLatencySeconds'] = self.inc_latency_seconds

        if self.job_step_id is not None:
            result['JobStepId'] = self.job_step_id

        if self.job_step_name is not None:
            result['JobStepName'] = self.job_step_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.need_acceleration is not None:
            result['NeedAcceleration'] = self.need_acceleration

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.serial is not None:
            result['Serial'] = self.serial

        if self.state is not None:
            result['State'] = self.state

        if self.sub_job_count is not None:
            result['SubJobCount'] = self.sub_job_count

        result['SubJobSteps'] = []
        if self.sub_job_steps is not None:
            for k1 in self.sub_job_steps:
                result['SubJobSteps'].append(k1.to_map() if k1 else None)

        if self.redis_phase_type is not None:
            result['redisPhaseType'] = self.redis_phase_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k1 in m.get('ErrorDetails'):
                temp_model = main_models.ListJobStepResponseBodyJobStepsErrorDetails()
                self.error_details.append(temp_model.from_map(k1))

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('IncLatencyMilliseconds') is not None:
            self.inc_latency_milliseconds = m.get('IncLatencyMilliseconds')

        if m.get('IncLatencySeconds') is not None:
            self.inc_latency_seconds = m.get('IncLatencySeconds')

        if m.get('JobStepId') is not None:
            self.job_step_id = m.get('JobStepId')

        if m.get('JobStepName') is not None:
            self.job_step_name = m.get('JobStepName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NeedAcceleration') is not None:
            self.need_acceleration = m.get('NeedAcceleration')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Serial') is not None:
            self.serial = m.get('Serial')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SubJobCount') is not None:
            self.sub_job_count = m.get('SubJobCount')

        self.sub_job_steps = []
        if m.get('SubJobSteps') is not None:
            for k1 in m.get('SubJobSteps'):
                temp_model = main_models.ListJobStepResponseBodyJobStepsSubJobSteps()
                self.sub_job_steps.append(temp_model.from_map(k1))

        if m.get('redisPhaseType') is not None:
            self.redis_phase_type = m.get('redisPhaseType')

        return self

class ListJobStepResponseBodyJobStepsSubJobSteps(DaraModel):
    def __init__(
        self,
        boot_time: str = None,
        code: str = None,
        create_time: str = None,
        err_msg: str = None,
        error_details: List[main_models.ListJobStepResponseBodyJobStepsSubJobStepsErrorDetails] = None,
        finish_time: str = None,
        inc_latency_milliseconds: str = None,
        inc_latency_seconds: int = None,
        job_step_id: str = None,
        job_step_name: str = None,
        modify_time: str = None,
        need_acceleration: bool = None,
        progress: int = None,
        serial: int = None,
        state: str = None,
    ):
        self.boot_time = boot_time
        self.code = code
        self.create_time = create_time
        self.err_msg = err_msg
        self.error_details = error_details
        self.finish_time = finish_time
        self.inc_latency_milliseconds = inc_latency_milliseconds
        self.inc_latency_seconds = inc_latency_seconds
        self.job_step_id = job_step_id
        self.job_step_name = job_step_name
        self.modify_time = modify_time
        self.need_acceleration = need_acceleration
        self.progress = progress
        self.serial = serial
        self.state = state

    def validate(self):
        if self.error_details:
            for v1 in self.error_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time

        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k1 in self.error_details:
                result['ErrorDetails'].append(k1.to_map() if k1 else None)

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.inc_latency_milliseconds is not None:
            result['IncLatencyMilliseconds'] = self.inc_latency_milliseconds

        if self.inc_latency_seconds is not None:
            result['IncLatencySeconds'] = self.inc_latency_seconds

        if self.job_step_id is not None:
            result['JobStepId'] = self.job_step_id

        if self.job_step_name is not None:
            result['JobStepName'] = self.job_step_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.need_acceleration is not None:
            result['NeedAcceleration'] = self.need_acceleration

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.serial is not None:
            result['Serial'] = self.serial

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k1 in m.get('ErrorDetails'):
                temp_model = main_models.ListJobStepResponseBodyJobStepsSubJobStepsErrorDetails()
                self.error_details.append(temp_model.from_map(k1))

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('IncLatencyMilliseconds') is not None:
            self.inc_latency_milliseconds = m.get('IncLatencyMilliseconds')

        if m.get('IncLatencySeconds') is not None:
            self.inc_latency_seconds = m.get('IncLatencySeconds')

        if m.get('JobStepId') is not None:
            self.job_step_id = m.get('JobStepId')

        if m.get('JobStepName') is not None:
            self.job_step_name = m.get('JobStepName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NeedAcceleration') is not None:
            self.need_acceleration = m.get('NeedAcceleration')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Serial') is not None:
            self.serial = m.get('Serial')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class ListJobStepResponseBodyJobStepsSubJobStepsErrorDetails(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        help_url: str = None,
    ):
        self.error_code = error_code
        self.help_url = help_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.help_url is not None:
            result['HelpUrl'] = self.help_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HelpUrl') is not None:
            self.help_url = m.get('HelpUrl')

        return self

class ListJobStepResponseBodyJobStepsErrorDetails(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        help_url: str = None,
    ):
        self.error_code = error_code
        self.help_url = help_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.help_url is not None:
            result['HelpUrl'] = self.help_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HelpUrl') is not None:
            self.help_url = m.get('HelpUrl')

        return self


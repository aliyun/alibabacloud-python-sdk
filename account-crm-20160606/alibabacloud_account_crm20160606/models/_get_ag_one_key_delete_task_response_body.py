# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class GetAgOneKeyDeleteTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_dto: main_models.GetAgOneKeyDeleteTaskResponseBodyTaskDto = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_dto = task_dto

    def validate(self):
        if self.task_dto:
            self.task_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_dto is not None:
            result['TaskDto'] = self.task_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskDto') is not None:
            temp_model = main_models.GetAgOneKeyDeleteTaskResponseBodyTaskDto()
            self.task_dto = temp_model.from_map(m.get('TaskDto'))

        return self

class GetAgOneKeyDeleteTaskResponseBodyTaskDto(DaraModel):
    def __init__(
        self,
        delete_status: str = None,
        exist_quiet_period: bool = None,
        quiet_period_end_time: str = None,
    ):
        self.delete_status = delete_status
        self.exist_quiet_period = exist_quiet_period
        self.quiet_period_end_time = quiet_period_end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_status is not None:
            result['DeleteStatus'] = self.delete_status

        if self.exist_quiet_period is not None:
            result['ExistQuietPeriod'] = self.exist_quiet_period

        if self.quiet_period_end_time is not None:
            result['QuietPeriodEndTime'] = self.quiet_period_end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteStatus') is not None:
            self.delete_status = m.get('DeleteStatus')

        if m.get('ExistQuietPeriod') is not None:
            self.exist_quiet_period = m.get('ExistQuietPeriod')

        if m.get('QuietPeriodEndTime') is not None:
            self.quiet_period_end_time = m.get('QuietPeriodEndTime')

        return self


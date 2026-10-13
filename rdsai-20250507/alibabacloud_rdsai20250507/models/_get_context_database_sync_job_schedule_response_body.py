# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetContextDatabaseSyncJobScheduleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetContextDatabaseSyncJobScheduleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetContextDatabaseSyncJobScheduleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetContextDatabaseSyncJobScheduleResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_pause_reason: str = None,
        auto_paused: bool = None,
        daily_times: List[str] = None,
        interval_minutes: int = None,
        missed_policy: str = None,
        next_run_at: str = None,
        timezone: str = None,
        type: str = None,
        updated_at: str = None,
    ):
        # The reason for the automatic pause.
        self.auto_pause_reason = auto_pause_reason
        # Indicates whether the task is automatically paused.
        self.auto_paused = auto_paused
        # The list of daily trigger times for daily-times scheduling in the HH:mm 24-hour format. The number of times ranges from 1 to 6.
        self.daily_times = daily_times
        # The interval in minutes for interval scheduling. The minimum value is 10.
        self.interval_minutes = interval_minutes
        # The processing policy for missed schedules. Valid values: skip and catch-up.
        self.missed_policy = missed_policy
        # The next run time.
        self.next_run_at = next_run_at
        # The time zone.
        self.timezone = timezone
        # The scheduling type. Valid values: interval and daily-times.
        self.type = type
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pause_reason is not None:
            result['AutoPauseReason'] = self.auto_pause_reason

        if self.auto_paused is not None:
            result['AutoPaused'] = self.auto_paused

        if self.daily_times is not None:
            result['DailyTimes'] = self.daily_times

        if self.interval_minutes is not None:
            result['IntervalMinutes'] = self.interval_minutes

        if self.missed_policy is not None:
            result['MissedPolicy'] = self.missed_policy

        if self.next_run_at is not None:
            result['NextRunAt'] = self.next_run_at

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.type is not None:
            result['Type'] = self.type

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPauseReason') is not None:
            self.auto_pause_reason = m.get('AutoPauseReason')

        if m.get('AutoPaused') is not None:
            self.auto_paused = m.get('AutoPaused')

        if m.get('DailyTimes') is not None:
            self.daily_times = m.get('DailyTimes')

        if m.get('IntervalMinutes') is not None:
            self.interval_minutes = m.get('IntervalMinutes')

        if m.get('MissedPolicy') is not None:
            self.missed_policy = m.get('MissedPolicy')

        if m.get('NextRunAt') is not None:
            self.next_run_at = m.get('NextRunAt')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self


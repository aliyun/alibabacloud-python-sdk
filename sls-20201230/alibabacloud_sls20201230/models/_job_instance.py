# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobInstance(DaraModel):
    def __init__(
        self,
        begin_time_in_millis: int = None,
        create_time_in_millis: int = None,
        description: str = None,
        display_name: str = None,
        error_code: str = None,
        error_message: str = None,
        instance_id: str = None,
        job_name: str = None,
        job_schedule_id: str = None,
        result: str = None,
        schedule_time_in_millis: int = None,
        state: str = None,
        summary: str = None,
        update_time_in_millis: int = None,
    ):
        # The start time.
        self.begin_time_in_millis = begin_time_in_millis
        # The creation time.
        self.create_time_in_millis = create_time_in_millis
        # The description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The instance ID.
        self.instance_id = instance_id
        # The task name.
        self.job_name = job_name
        # The scheduled task ID.
        self.job_schedule_id = job_schedule_id
        # The returned result.
        self.result = result
        # The scheduled time.
        self.schedule_time_in_millis = schedule_time_in_millis
        # The current execution status.
        self.state = state
        # The schedule title.
        self.summary = summary
        # The update time.
        self.update_time_in_millis = update_time_in_millis

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time_in_millis is not None:
            result['beginTimeInMillis'] = self.begin_time_in_millis

        if self.create_time_in_millis is not None:
            result['createTimeInMillis'] = self.create_time_in_millis

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.job_name is not None:
            result['jobName'] = self.job_name

        if self.job_schedule_id is not None:
            result['jobScheduleId'] = self.job_schedule_id

        if self.result is not None:
            result['result'] = self.result

        if self.schedule_time_in_millis is not None:
            result['scheduleTimeInMillis'] = self.schedule_time_in_millis

        if self.state is not None:
            result['state'] = self.state

        if self.summary is not None:
            result['summary'] = self.summary

        if self.update_time_in_millis is not None:
            result['updateTimeInMillis'] = self.update_time_in_millis

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTimeInMillis') is not None:
            self.begin_time_in_millis = m.get('beginTimeInMillis')

        if m.get('createTimeInMillis') is not None:
            self.create_time_in_millis = m.get('createTimeInMillis')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')

        if m.get('jobScheduleId') is not None:
            self.job_schedule_id = m.get('jobScheduleId')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('scheduleTimeInMillis') is not None:
            self.schedule_time_in_millis = m.get('scheduleTimeInMillis')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('updateTimeInMillis') is not None:
            self.update_time_in_millis = m.get('updateTimeInMillis')

        return self


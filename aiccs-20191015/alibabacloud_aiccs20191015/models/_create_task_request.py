# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTaskRequest(DaraModel):
    def __init__(
        self,
        call_string: str = None,
        call_string_type: str = None,
        caller: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retry_count: int = None,
        retry_flag: int = None,
        retry_interval: int = None,
        retry_status_code: str = None,
        robot_id: str = None,
        seat_count: str = None,
        start_now: bool = None,
        task_name: str = None,
        work_day: str = None,
        work_time_list: str = None,
    ):
        self.call_string = call_string
        # This parameter is required.
        self.call_string_type = call_string_type
        # This parameter is required.
        self.caller = caller
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.retry_count = retry_count
        self.retry_flag = retry_flag
        self.retry_interval = retry_interval
        self.retry_status_code = retry_status_code
        # This parameter is required.
        self.robot_id = robot_id
        # This parameter is required.
        self.seat_count = seat_count
        self.start_now = start_now
        # This parameter is required.
        self.task_name = task_name
        # This parameter is required.
        self.work_day = work_day
        # This parameter is required.
        self.work_time_list = work_time_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_string is not None:
            result['CallString'] = self.call_string

        if self.call_string_type is not None:
            result['CallStringType'] = self.call_string_type

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count

        if self.retry_flag is not None:
            result['RetryFlag'] = self.retry_flag

        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval

        if self.retry_status_code is not None:
            result['RetryStatusCode'] = self.retry_status_code

        if self.robot_id is not None:
            result['RobotId'] = self.robot_id

        if self.seat_count is not None:
            result['SeatCount'] = self.seat_count

        if self.start_now is not None:
            result['StartNow'] = self.start_now

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.work_day is not None:
            result['WorkDay'] = self.work_day

        if self.work_time_list is not None:
            result['WorkTimeList'] = self.work_time_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallString') is not None:
            self.call_string = m.get('CallString')

        if m.get('CallStringType') is not None:
            self.call_string_type = m.get('CallStringType')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        if m.get('RetryFlag') is not None:
            self.retry_flag = m.get('RetryFlag')

        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')

        if m.get('RetryStatusCode') is not None:
            self.retry_status_code = m.get('RetryStatusCode')

        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')

        if m.get('SeatCount') is not None:
            self.seat_count = m.get('SeatCount')

        if m.get('StartNow') is not None:
            self.start_now = m.get('StartNow')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('WorkDay') is not None:
            self.work_day = m.get('WorkDay')

        if m.get('WorkTimeList') is not None:
            self.work_time_list = m.get('WorkTimeList')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssignJobsRequest(DaraModel):
    def __init__(
        self,
        calling_number: List[str] = None,
        instance_id: str = None,
        is_asynchrony: bool = None,
        job_data_parsing_task_id: str = None,
        job_group_id: str = None,
        jobs_json: List[str] = None,
        roster_type: str = None,
        strategy_json: str = None,
    ):
        # These numbers are displayed as the caller ID to the contact.
        # 
        # > If unspecified, all available calling numbers are used.
        self.calling_number = calling_number
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the task is asynchronous.
        # 
        # You can omit this parameter if you create jobs by calling this API. The default value is `false`.
        self.is_asynchrony = is_asynchrony
        # The ID of the data parsing task for the outbound call job.
        # 
        # You can omit this parameter if you create jobs by calling this API.
        # 
        # > If you create jobs by uploading a file, you must call the `CreateJobDataParsingTask` operation to obtain a value for this parameter.
        self.job_data_parsing_task_id = job_data_parsing_task_id
        # The job group ID.
        # 
        # This parameter is required.
        self.job_group_id = job_group_id
        # >Notice: 
        # 
        # This parameter is required.
        # 
        # 
        # 
        # The job data, a JSON array where each object represents a contact. For formatting details, see the example.
        # 
        # The array can contain up to 99 elements.
        self.jobs_json = jobs_json
        # The roster type.
        # 
        # If you create jobs by calling this API, you can omit this parameter. The default value is `json`. If you upload a contact list file, set this parameter to `excel`.
        self.roster_type = roster_type
        # The execution strategy for the job group.
        # 
        # - `repeatBy`: The recurrence type. Valid values: `Once` (runs once), `Day` (repeats daily), `Week` (repeats weekly), and `Month` (repeats monthly).
        # 
        # - `startTime`: The start time of the strategy.
        # 
        # - `endTime`: The end time of the strategy.
        # 
        # - `workingTime`: The time windows during which calls can be made.
        # 
        # - `maxAttemptsPerDay`: The maximum daily call attempts per phone number.
        # 
        # - `minAttemptInterval`: The minimum interval between call retries, in minutes.
        # 
        # - `routingStrategy`: The number routing strategy. Valid values: `None` (no preference), `LocalFirst` (prioritizes numbers in the same city), and `LocalProvinceFirst` (prioritizes numbers in the same province).
        # 
        # - `repeatDays`: The specific days on which the job runs, based on the `repeatBy` type. If `repeatBy` is set to `Week`, `0` represents Sunday, and `1` through `6` represent Monday through Saturday. If `repeatBy` is set to `Month`, values from `1` to `31` represent the days of the month. If a month does not have a specified day (for example, February 30), the job is skipped for that month.
        # 
        # - `repeatable`: Specifies whether the job is recurring. Valid values are `true` and `false`.
        self.strategy_json = strategy_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_asynchrony is not None:
            result['IsAsynchrony'] = self.is_asynchrony

        if self.job_data_parsing_task_id is not None:
            result['JobDataParsingTaskId'] = self.job_data_parsing_task_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.jobs_json is not None:
            result['JobsJson'] = self.jobs_json

        if self.roster_type is not None:
            result['RosterType'] = self.roster_type

        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsAsynchrony') is not None:
            self.is_asynchrony = m.get('IsAsynchrony')

        if m.get('JobDataParsingTaskId') is not None:
            self.job_data_parsing_task_id = m.get('JobDataParsingTaskId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobsJson') is not None:
            self.jobs_json = m.get('JobsJson')

        if m.get('RosterType') is not None:
            self.roster_type = m.get('RosterType')

        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')

        return self


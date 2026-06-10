# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssignJobsAsyncShrinkRequest(DaraModel):
    def __init__(
        self,
        calling_number_shrink: str = None,
        instance_id: str = None,
        job_group_id: str = None,
        jobs_json_shrink: str = None,
        strategy_json: str = None,
    ):
        # The list of calling numbers to be displayed to callees.
        # 
        # > If you omit this parameter, the system uses all available calling numbers by default.
        self.calling_number_shrink = calling_number_shrink
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the job group.
        # 
        # This parameter is required.
        self.job_group_id = job_group_id
        # A JSON array containing job data. For the required format, see the example.
        # 
        # Each JSON object in the array represents a job for a single contact.
        self.jobs_json_shrink = jobs_json_shrink
        # A JSON string that defines the job group execution strategy. This object has the following properties:
        # 
        # - `repeatBy`
        # 
        # Specifies the repetition frequency. Valid values include `Once` (does not repeat), `Day` (repeats daily), `Week` (repeats weekly), and `Month` (repeats monthly).
        # 
        # - `startTime`
        # 
        # The start time of the execution strategy.
        # 
        # - `endTime`
        # 
        # The end time of the execution strategy.
        # 
        # - `workingTime`
        # 
        # The time range during which outbound calls can be made.
        # 
        # - `maxAttemptsPerDay`
        # 
        # The maximum number of daily call attempts for a single phone number.
        # 
        # - `minAttemptInterval`
        # 
        # The minimum interval between retry attempts, in minutes.
        # 
        # - `routingStrategy`
        # 
        # The routing strategy for calling numbers. Valid values: `None` (not specified), `LocalFirst` (prioritizes numbers in the same city), and `LocalProvinceFirst` (prioritizes numbers in the same province).
        # 
        # - `repeatDays`
        # 
        # The days on which the job repeats. If `repeatBy` is set to `Week`, valid values are `0` for Sunday and `1` to `6` for Monday to Saturday. If `repeatBy` is set to `Month`, valid values are `1` to `31`. If a specified day does not exist in a given month (e.g., February 30), the job is skipped for that month.
        # 
        # - `repeatable`
        # 
        # Specifies whether to enable recurring jobs. Valid values: `true` and `false`.
        self.strategy_json = strategy_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_number_shrink is not None:
            result['CallingNumber'] = self.calling_number_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.jobs_json_shrink is not None:
            result['JobsJson'] = self.jobs_json_shrink

        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumber') is not None:
            self.calling_number_shrink = m.get('CallingNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobsJson') is not None:
            self.jobs_json_shrink = m.get('JobsJson')

        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')

        return self


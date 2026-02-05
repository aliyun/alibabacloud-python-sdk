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
        self.calling_number_shrink = calling_number_shrink
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_group_id = job_group_id
        self.jobs_json_shrink = jobs_json_shrink
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


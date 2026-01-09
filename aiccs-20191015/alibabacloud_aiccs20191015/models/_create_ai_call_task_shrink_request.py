# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAiCallTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        call_day_shrink: str = None,
        call_retry_interval: int = None,
        call_retry_reason_shrink: str = None,
        call_retry_times: int = None,
        call_time_shrink: str = None,
        miss_call_retry: bool = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_type: str = None,
        task_cps: int = None,
        task_name: str = None,
        task_start_time: int = None,
        virtual_number: str = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        # This parameter is required.
        self.call_day_shrink = call_day_shrink
        self.call_retry_interval = call_retry_interval
        self.call_retry_reason_shrink = call_retry_reason_shrink
        self.call_retry_times = call_retry_times
        # This parameter is required.
        self.call_time_shrink = call_time_shrink
        self.miss_call_retry = miss_call_retry
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.start_type = start_type
        self.task_cps = task_cps
        # This parameter is required.
        self.task_name = task_name
        self.task_start_time = task_start_time
        # This parameter is required.
        self.virtual_number = virtual_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.call_day_shrink is not None:
            result['CallDay'] = self.call_day_shrink

        if self.call_retry_interval is not None:
            result['CallRetryInterval'] = self.call_retry_interval

        if self.call_retry_reason_shrink is not None:
            result['CallRetryReason'] = self.call_retry_reason_shrink

        if self.call_retry_times is not None:
            result['CallRetryTimes'] = self.call_retry_times

        if self.call_time_shrink is not None:
            result['CallTime'] = self.call_time_shrink

        if self.miss_call_retry is not None:
            result['MissCallRetry'] = self.miss_call_retry

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_type is not None:
            result['StartType'] = self.start_type

        if self.task_cps is not None:
            result['TaskCps'] = self.task_cps

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        if self.virtual_number is not None:
            result['VirtualNumber'] = self.virtual_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('CallDay') is not None:
            self.call_day_shrink = m.get('CallDay')

        if m.get('CallRetryInterval') is not None:
            self.call_retry_interval = m.get('CallRetryInterval')

        if m.get('CallRetryReason') is not None:
            self.call_retry_reason_shrink = m.get('CallRetryReason')

        if m.get('CallRetryTimes') is not None:
            self.call_retry_times = m.get('CallRetryTimes')

        if m.get('CallTime') is not None:
            self.call_time_shrink = m.get('CallTime')

        if m.get('MissCallRetry') is not None:
            self.miss_call_retry = m.get('MissCallRetry')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartType') is not None:
            self.start_type = m.get('StartType')

        if m.get('TaskCps') is not None:
            self.task_cps = m.get('TaskCps')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        if m.get('VirtualNumber') is not None:
            self.virtual_number = m.get('VirtualNumber')

        return self


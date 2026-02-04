# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAiCallTaskRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_code: str = None,
        application_name: str = None,
        call_day: List[str] = None,
        call_retry_interval: int = None,
        call_retry_reason: List[str] = None,
        call_retry_times: int = None,
        call_time: List[str] = None,
        line_encoding: str = None,
        line_phone_num: str = None,
        miss_call_retry: bool = None,
        owner_id: int = None,
        phone_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source: int = None,
        start_type: str = None,
        task_cps: int = None,
        task_name: str = None,
        task_start_time: int = None,
        virtual_number: str = None,
    ):
        self.agent_id = agent_id
        self.application_code = application_code
        self.application_name = application_name
        # This parameter is required.
        self.call_day = call_day
        self.call_retry_interval = call_retry_interval
        self.call_retry_reason = call_retry_reason
        self.call_retry_times = call_retry_times
        # This parameter is required.
        self.call_time = call_time
        self.line_encoding = line_encoding
        self.line_phone_num = line_phone_num
        self.miss_call_retry = miss_call_retry
        self.owner_id = owner_id
        self.phone_type = phone_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.source = source
        # This parameter is required.
        self.start_type = start_type
        self.task_cps = task_cps
        # This parameter is required.
        self.task_name = task_name
        self.task_start_time = task_start_time
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

        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.call_day is not None:
            result['CallDay'] = self.call_day

        if self.call_retry_interval is not None:
            result['CallRetryInterval'] = self.call_retry_interval

        if self.call_retry_reason is not None:
            result['CallRetryReason'] = self.call_retry_reason

        if self.call_retry_times is not None:
            result['CallRetryTimes'] = self.call_retry_times

        if self.call_time is not None:
            result['CallTime'] = self.call_time

        if self.line_encoding is not None:
            result['LineEncoding'] = self.line_encoding

        if self.line_phone_num is not None:
            result['LinePhoneNum'] = self.line_phone_num

        if self.miss_call_retry is not None:
            result['MissCallRetry'] = self.miss_call_retry

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_type is not None:
            result['PhoneType'] = self.phone_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source is not None:
            result['Source'] = self.source

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

        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CallDay') is not None:
            self.call_day = m.get('CallDay')

        if m.get('CallRetryInterval') is not None:
            self.call_retry_interval = m.get('CallRetryInterval')

        if m.get('CallRetryReason') is not None:
            self.call_retry_reason = m.get('CallRetryReason')

        if m.get('CallRetryTimes') is not None:
            self.call_retry_times = m.get('CallRetryTimes')

        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        if m.get('LineEncoding') is not None:
            self.line_encoding = m.get('LineEncoding')

        if m.get('LinePhoneNum') is not None:
            self.line_phone_num = m.get('LinePhoneNum')

        if m.get('MissCallRetry') is not None:
            self.miss_call_retry = m.get('MissCallRetry')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneType') is not None:
            self.phone_type = m.get('PhoneType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

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


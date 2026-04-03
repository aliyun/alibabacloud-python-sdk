# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AIAgentCallInfo(DaraModel):
    def __init__(
        self,
        call_duration: int = None,
        call_end_time: str = None,
        call_start_time: str = None,
        callee_number: str = None,
        caller_number: str = None,
        hangup_role: int = None,
        status: str = None,
    ):
        self.call_duration = call_duration
        self.call_end_time = call_end_time
        self.call_start_time = call_start_time
        self.callee_number = callee_number
        self.caller_number = caller_number
        self.hangup_role = hangup_role
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_duration is not None:
            result['CallDuration'] = self.call_duration

        if self.call_end_time is not None:
            result['CallEndTime'] = self.call_end_time

        if self.call_start_time is not None:
            result['CallStartTime'] = self.call_start_time

        if self.callee_number is not None:
            result['CalleeNumber'] = self.callee_number

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.hangup_role is not None:
            result['HangupRole'] = self.hangup_role

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallDuration') is not None:
            self.call_duration = m.get('CallDuration')

        if m.get('CallEndTime') is not None:
            self.call_end_time = m.get('CallEndTime')

        if m.get('CallStartTime') is not None:
            self.call_start_time = m.get('CallStartTime')

        if m.get('CalleeNumber') is not None:
            self.callee_number = m.get('CalleeNumber')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('HangupRole') is not None:
            self.hangup_role = m.get('HangupRole')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExportConversationDetailsRequest(DaraModel):
    def __init__(
        self,
        begin_time_left_range: int = None,
        begin_time_right_range: int = None,
        calling_number: str = None,
        debug_conversation: int = None,
        instance_id: str = None,
        options: List[str] = None,
        result: int = None,
        rounds_left_range: int = None,
        rounds_right_range: int = None,
    ):
        self.begin_time_left_range = begin_time_left_range
        self.begin_time_right_range = begin_time_right_range
        self.calling_number = calling_number
        self.debug_conversation = debug_conversation
        # This parameter is required.
        self.instance_id = instance_id
        self.options = options
        self.result = result
        self.rounds_left_range = rounds_left_range
        self.rounds_right_range = rounds_right_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time_left_range is not None:
            result['BeginTimeLeftRange'] = self.begin_time_left_range

        if self.begin_time_right_range is not None:
            result['BeginTimeRightRange'] = self.begin_time_right_range

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.debug_conversation is not None:
            result['DebugConversation'] = self.debug_conversation

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.options is not None:
            result['Options'] = self.options

        if self.result is not None:
            result['Result'] = self.result

        if self.rounds_left_range is not None:
            result['RoundsLeftRange'] = self.rounds_left_range

        if self.rounds_right_range is not None:
            result['RoundsRightRange'] = self.rounds_right_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimeLeftRange') is not None:
            self.begin_time_left_range = m.get('BeginTimeLeftRange')

        if m.get('BeginTimeRightRange') is not None:
            self.begin_time_right_range = m.get('BeginTimeRightRange')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('DebugConversation') is not None:
            self.debug_conversation = m.get('DebugConversation')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('RoundsLeftRange') is not None:
            self.rounds_left_range = m.get('RoundsLeftRange')

        if m.get('RoundsRightRange') is not None:
            self.rounds_right_range = m.get('RoundsRightRange')

        return self


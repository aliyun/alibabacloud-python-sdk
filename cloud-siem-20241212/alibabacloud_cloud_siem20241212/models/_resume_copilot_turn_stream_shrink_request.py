# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResumeCopilotTurnStreamShrinkRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        cursor_by_run_shrink: str = None,
        lang: str = None,
        region_id: str = None,
        trace_id: str = None,
        turn_id: str = None,
    ):
        # The conversation ID. This parameter is required for the second and subsequent turns in a multi-turn conversation.
        # 
        # This parameter is required.
        self.conversation_id = conversation_id
        # The native run cursor mapping.
        # 
        # This parameter is required.
        self.cursor_by_run_shrink = cursor_by_run_shrink
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The region where the data management center for threat analysis is located. You need to select the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: The asset belongs to the Chinese mainland and China (Hong Kong).
        # - ap-southeast-1: The asset belongs to a region outside the Chinese mainland.
        self.region_id = region_id
        # The trace ID.
        self.trace_id = trace_id
        # The primary key ID.
        # 
        # This parameter is required.
        self.turn_id = turn_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.cursor_by_run_shrink is not None:
            result['CursorByRun'] = self.cursor_by_run_shrink

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.turn_id is not None:
            result['TurnId'] = self.turn_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CursorByRun') is not None:
            self.cursor_by_run_shrink = m.get('CursorByRun')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('TurnId') is not None:
            self.turn_id = m.get('TurnId')

        return self


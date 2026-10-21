# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCopilotTurnRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        lang: str = None,
        region_id: str = None,
        trace_id: str = None,
        turn_id: str = None,
    ):
        # The conversation ID.
        # 
        # This parameter is required.
        self.conversation_id = conversation_id
        # The language of the returned messages. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The region of the data management center for threat analysis. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located outside China.
        self.region_id = region_id
        # The trace ID used to accurately query call information.
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

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('TurnId') is not None:
            self.turn_id = m.get('TurnId')

        return self


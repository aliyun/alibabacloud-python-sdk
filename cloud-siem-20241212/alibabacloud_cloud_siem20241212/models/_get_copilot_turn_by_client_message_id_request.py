# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCopilotTurnByClientMessageIdRequest(DaraModel):
    def __init__(
        self,
        client_message_id: str = None,
        conversation_id: str = None,
        lang: str = None,
        region_id: str = None,
        trace_id: str = None,
    ):
        # The client message ID.
        # 
        # This parameter is required.
        self.client_message_id = client_message_id
        # The conversation ID.
        # 
        # This parameter is required.
        self.conversation_id = conversation_id
        # The language of the returned message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The region of the data management center for threat analysis. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Select this value if your assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Select this value if your assets are located outside China.
        self.region_id = region_id
        # The trace ID used to track the service request.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_message_id is not None:
            result['ClientMessageId'] = self.client_message_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientMessageId') is not None:
            self.client_message_id = m.get('ClientMessageId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self


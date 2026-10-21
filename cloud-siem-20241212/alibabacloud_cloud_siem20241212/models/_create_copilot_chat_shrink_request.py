# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCopilotChatShrinkRequest(DaraModel):
    def __init__(
        self,
        client_conversation_id: str = None,
        client_message_id: str = None,
        conversation_id: str = None,
        create_conversation_shrink: str = None,
        lang: str = None,
        messages_shrink: str = None,
        model: str = None,
        plan_mode: str = None,
        project_id: str = None,
        region_id: str = None,
        replace_turn_id: str = None,
        route_target: str = None,
        source: str = None,
        stream: bool = None,
        thinking_mode: str = None,
        trace_id: str = None,
    ):
        # The client conversation ID.
        self.client_conversation_id = client_conversation_id
        # The client message ID.
        # 
        # This parameter is required.
        self.client_message_id = client_message_id
        # The conversation ID.
        self.conversation_id = conversation_id
        # The conversation creation configuration.
        self.create_conversation_shrink = create_conversation_shrink
        # The language of the returned messages. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The list of messages.
        # 
        # This parameter is required.
        self.messages_shrink = messages_shrink
        # The model identifier.
        self.model = model
        # The planning configuration.
        self.plan_mode = plan_mode
        # The security project ID.
        self.project_id = project_id
        # The region of the data management center for threat analysis. Specify the management center based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside in regions outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the conversation turn to replace.
        self.replace_turn_id = replace_turn_id
        # The route target identifier.
        self.route_target = route_target
        # The request source.
        self.source = source
        # Specifies whether to enable streaming responses.
        self.stream = stream
        # The deep thinking configuration.
        self.thinking_mode = thinking_mode
        # The trace ID, which is used to query specific call information.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_conversation_id is not None:
            result['ClientConversationId'] = self.client_conversation_id

        if self.client_message_id is not None:
            result['ClientMessageId'] = self.client_message_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.create_conversation_shrink is not None:
            result['CreateConversation'] = self.create_conversation_shrink

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.messages_shrink is not None:
            result['Messages'] = self.messages_shrink

        if self.model is not None:
            result['Model'] = self.model

        if self.plan_mode is not None:
            result['PlanMode'] = self.plan_mode

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replace_turn_id is not None:
            result['ReplaceTurnId'] = self.replace_turn_id

        if self.route_target is not None:
            result['RouteTarget'] = self.route_target

        if self.source is not None:
            result['Source'] = self.source

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.thinking_mode is not None:
            result['ThinkingMode'] = self.thinking_mode

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientConversationId') is not None:
            self.client_conversation_id = m.get('ClientConversationId')

        if m.get('ClientMessageId') is not None:
            self.client_message_id = m.get('ClientMessageId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CreateConversation') is not None:
            self.create_conversation_shrink = m.get('CreateConversation')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Messages') is not None:
            self.messages_shrink = m.get('Messages')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('PlanMode') is not None:
            self.plan_mode = m.get('PlanMode')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplaceTurnId') is not None:
            self.replace_turn_id = m.get('ReplaceTurnId')

        if m.get('RouteTarget') is not None:
            self.route_target = m.get('RouteTarget')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('ThinkingMode') is not None:
            self.thinking_mode = m.get('ThinkingMode')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self


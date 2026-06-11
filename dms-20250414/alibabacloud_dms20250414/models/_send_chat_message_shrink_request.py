# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendChatMessageShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        dmsunit: str = None,
        data_source_shrink: str = None,
        data_sources_shrink: str = None,
        message: str = None,
        message_type: str = None,
        parent_session_id: str = None,
        question: str = None,
        quoted_message: str = None,
        reply_to: str = None,
        session_config_shrink: str = None,
        session_id: str = None,
    ):
        # The agent ID. This parameter is required. You can obtain this ID from the response of the `CreateAgentSession` operation. An agent has a lifecycle, so its ID may change with each request.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The DMS unit where your DMS instance is located. This information is used to connect to your DMS instance for database analysis. You can find this value in the DMS console. For users on the Alibaba Cloud China site, you can enter `cn-hangzhou`.
        self.dmsunit = dmsunit
        # The data source information. Optional.
        self.data_source_shrink = data_source_shrink
        # A list of data sources. Optional.
        self.data_sources_shrink = data_sources_shrink
        # The content of the message to send to the agent.
        # 
        # This parameter is required.
        self.message = message
        # The message type. The default value is `primary`. Set this parameter to `additional` when responding to a human-in-the-loop question from the agent. Set it to `cancel` to cancel the current session.
        self.message_type = message_type
        # The parent session ID.
        self.parent_session_id = parent_session_id
        # This parameter is required if the `MessageType` is `additional`. It contains the specific question asked by the agent during the human-in-the-loop process.
        self.question = question
        # The quoted content. This parameter is typically used when interacting with the agent.
        self.quoted_message = quoted_message
        # This parameter specifies the agent message to which this message is a response, enabling message deduplication. Set this to the highest checkpoint sequence number you have received. For the first message, use 0.
        self.reply_to = reply_to
        # Session-specific configurations. These apply only if provided in the first `SendMessage` request of the session.
        self.session_config_shrink = session_config_shrink
        # The session ID. This parameter is required. You can obtain the session ID by calling the `CreateAgentSession` operation.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.data_source_shrink is not None:
            result['DataSource'] = self.data_source_shrink

        if self.data_sources_shrink is not None:
            result['DataSources'] = self.data_sources_shrink

        if self.message is not None:
            result['Message'] = self.message

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.parent_session_id is not None:
            result['ParentSessionId'] = self.parent_session_id

        if self.question is not None:
            result['Question'] = self.question

        if self.quoted_message is not None:
            result['QuotedMessage'] = self.quoted_message

        if self.reply_to is not None:
            result['ReplyTo'] = self.reply_to

        if self.session_config_shrink is not None:
            result['SessionConfig'] = self.session_config_shrink

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('DataSource') is not None:
            self.data_source_shrink = m.get('DataSource')

        if m.get('DataSources') is not None:
            self.data_sources_shrink = m.get('DataSources')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('ParentSessionId') is not None:
            self.parent_session_id = m.get('ParentSessionId')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('QuotedMessage') is not None:
            self.quoted_message = m.get('QuotedMessage')

        if m.get('ReplyTo') is not None:
            self.reply_to = m.get('ReplyTo')

        if m.get('SessionConfig') is not None:
            self.session_config_shrink = m.get('SessionConfig')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self


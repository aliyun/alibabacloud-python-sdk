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
        task_config_shrink: str = None,
        workspace_id: str = None,
    ):
        # The agent ID. This is a required field. You can obtain the current AgentId from the return value of the CreateAgentSession operation. Agent resources have a lifecycle, so the AgentId you need to pass in each request may change.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The DMS unit you are currently in. If you choose to analyze a database, this information will be used to correctly connect to your DMS instance through DMS. You can go to the DMS console to check your current DMS unit. If you are a China site user of Alibaba Cloud, you can directly enter cn-hangzhou.
        self.dmsunit = dmsunit
        # The data source information. This parameter can be left empty. Only one data source can be passed in through this parameter. We recommend that you use the DataSources parameter instead.
        self.data_source_shrink = data_source_shrink
        # The detailed data source information. This parameter can be left empty.
        self.data_sources_shrink = data_sources_shrink
        # The content of the message to be sent to the Agent.
        # 
        # This parameter is required.
        self.message = message
        # The message type. Default value: `[primary]`.
        # 
        # - In normal cases, when interacting with the Agent, the message type is `[primary]`.
        # 
        # - When the message is a response to the Agent\\"s Human-in-Loop question, the type should be `[additional]`.
        # 
        # - When the message is intended to trigger a report generation, the type should be `[report]`.
        # 
        # - When the message is intended to cancel the current session, the type should be `[cancel]`.
        self.message_type = message_type
        # The parent session ID.
        self.parent_session_id = parent_session_id
        # This field is required when the message type is `additional`. Pass in the specific question that the Agent asked the user through Human-in-Loop.
        self.question = question
        # Pass in the current quoted content, typically used when interacting with the Agent.
        self.quoted_message = quoted_message
        # **Important**
        # 
        # When this message is a reply to an Agent message (for example, when the Agent asks for clarification through ASK_HUMAN), reply_to must be set to the exact Checkpoint number carried in that Agent message. If this message is not a specific reply, such as requesting the Agent for further in-depth analysis after analysis is completed, reply_to can be left empty or set to "0".
        # 
        # This field affects how the Agent decides to process the message. Passing an incorrect value may lead to analysis results that do not meet expectations.
        self.reply_to = reply_to
        # The special configuration for this session. For the same session, only the configuration passed in the first SendMessage call takes effect.
        self.session_config_shrink = session_config_shrink
        # The session ID. This is a required field. You can obtain the SessionId by calling CreateAgentSession.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The configuration items that only affect the current task.
        self.task_config_shrink = task_config_shrink
        self.workspace_id = workspace_id

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

        if self.task_config_shrink is not None:
            result['TaskConfig'] = self.task_config_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

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

        if m.get('TaskConfig') is not None:
            self.task_config_shrink = m.get('TaskConfig')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self


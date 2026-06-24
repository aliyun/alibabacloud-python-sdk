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
    ):
        # The agent ID. This is a required field. You can obtain the current AgentId from the response of the CreateAgentSession operation. Agent resources have a lifecycle, so the AgentId you need to specify may change with each request.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The Data Management unit you are currently in. If you choose to analyze a database, this information is used to correctly connect to your Data Management instance. You can check your current Data Management unit in the Data Management console. If you are a user of Alibaba Cloud China Website (www.aliyun.com), set this parameter to ap-southeast-1.
        self.dmsunit = dmsunit
        # The data source information. This parameter can be left empty. This parameter supports only a single data source. Use the DataSources parameter instead.
        self.data_source_shrink = data_source_shrink
        # The detailed data source information. This parameter can be left empty.
        self.data_sources_shrink = data_sources_shrink
        # The message content to send to the Agent in this request.
        # 
        # This parameter is required.
        self.message = message
        # The message type. Default value: `[primary]`.  
        # 
        # - For regular interactions with the Agent, set the message type to `[primary]`.
        # 
        # - When the message is a response to the Agent\\"s Human-in-Loop question, set the type to `[additional]`.
        # 
        # - When the message is intended to trigger report generation, set the type to `[report]`.
        # 
        # - When the message is intended to cancel the current session, set the type to `[cancel]`.
        self.message_type = message_type
        # The parent session ID.
        self.parent_session_id = parent_session_id
        # This field is required when the message type is `additional`. Specify the specific question that the Agent asks the user through Human-in-Loop.
        self.question = question
        # The quoted content to pass in. This is typically used during interactions with the Agent.
        self.quoted_message = quoted_message
        # **Important**
        # 
        # When this message is a reply to an Agent message (for example, the Agent asks a clarifying question through ASK_HUMAN), set reply_to to the exact Checkpoint sequence number carried by that Agent message. If this message is not a targeted reply, such as requesting further in-depth analysis after analysis is complete, leave reply_to empty or set it to "0".  
        # 
        # This field affects how the Agent decides to process the message. Passing an incorrect value may lead to analysis results that do not meet expectations.
        self.reply_to = reply_to
        # The special configuration for this session. For the same session, only the configuration passed with the first SendMessage call takes effect.
        self.session_config_shrink = session_config_shrink
        # The session ID. This is a required field. You can obtain the SessionId by calling the CreateAgentSession operation.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The configuration items that affect only the current task.
        self.task_config_shrink = task_config_shrink

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

        return self


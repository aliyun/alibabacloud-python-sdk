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
        user_oss_bucket: str = None,
        workspace_id: str = None,
    ):
        # **[Optimized]** This field is now automatically obtained by the backend. You do not need to specify this field.
        self.agent_id = agent_id
        # **[Optimized]** This field is now automatically obtained by the backend. You do not need to specify this field when calling the API.
        self.dmsunit = dmsunit
        # The data source information. This parameter can be left empty. This parameter supports only one data source. Use the DataSources parameter instead.
        self.data_source_shrink = data_source_shrink
        # The detailed data source information. This parameter can be left empty.
        self.data_sources_shrink = data_sources_shrink
        # The message content to send to the Agent.
        # 
        # This parameter is required.
        self.message = message
        # The message type. Default value: `[primary]`.  
        # 
        # - For regular interactions with the Agent, the message type is `[primary]`.
        # 
        # - When the message is a response to the Agent\\"s Human-in-Loop question, the type should be `[additional]`.
        # 
        # - When the message is intended to trigger a report generation, the type should be `[report]`.
        # 
        # - When the message is intended to cancel the current session, the type should be `[cancel]`.
        self.message_type = message_type
        # The parent session ID.
        self.parent_session_id = parent_session_id
        # This field is required when the message type is `additional`. Specify the specific question that the Agent asks the user through Human-in-Loop.
        self.question = question
        # The quoted content. This is typically used during interactions with the Agent.
        self.quoted_message = quoted_message
        # **Important**
        # 
        # When this message is a reply to an Agent message (for example, the Agent asks a clarification question through ASK_HUMAN), reply_to must be set to the exact Checkpoint sequence number carried in that Agent message. If this message is not a targeted reply, such as requesting the Agent to perform further in-depth analysis after the analysis is complete, reply_to can be left empty or set to "0".  
        # 
        # This field affects how the Agent decides to process the message. Passing an incorrect value may result in analysis results that do not meet expectations.
        self.reply_to = reply_to
        # The special configuration for the current session. For the same session, only the configuration included in the first SendMessage call takes effect.
        self.session_config_shrink = session_config_shrink
        # The session ID. This is an optional field used for multi-turn conversations.
        # - You can start a conversation without specifying this field. The response includes the SessionID for the current session.
        # - You can also manually create a session ID by calling the CreateDataAgentSession operation and include the ID when initiating a conversation.
        # - If you need multi-turn conversations (such as follow-up questions or confirming execution plans), include the SessionID returned by the previous SendChatMessage call.
        self.session_id = session_id
        # The configuration items that affect only the current task.
        self.task_config_shrink = task_config_shrink
        # The user\\"s OSS bucket. If this field is left empty, the analysis results are securely stored in the built-in storage.
        self.user_oss_bucket = user_oss_bucket
        # The workspace ID.
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

        if self.user_oss_bucket is not None:
            result['UserOssBucket'] = self.user_oss_bucket

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

        if m.get('UserOssBucket') is not None:
            self.user_oss_bucket = m.get('UserOssBucket')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self


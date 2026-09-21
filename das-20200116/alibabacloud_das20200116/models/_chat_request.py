# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        message: str = None,
        resume: str = None,
        session_id: str = None,
        summary: str = None,
    ):
        # The agent ID used for the service. This parameter is optional. You can specify an agent generated after DAS Agent is enabled or an agent that you manually created. If this parameter is not specified, the default agent is used.
        self.agent_id = agent_id
        # The message.
        self.message = message
        # The user interaction feedback.
        self.resume = resume
        # The session ID in UUID string format. This parameter is optional. If this parameter is not specified, a new session is created by default. To maintain context across conversations, use the same session ID.
        self.session_id = session_id
        # Specifies whether to output summary information.
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.message is not None:
            result['Message'] = self.message

        if self.resume is not None:
            result['Resume'] = self.resume

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Resume') is not None:
            self.resume = m.get('Resume')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FeedbackRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        feedback: str = None,
        feedback_content: str = None,
        instance_id: str = None,
        message_id: str = None,
        session_id: str = None,
    ):
        self.agent_key = agent_key
        self.feedback = feedback
        self.feedback_content = feedback_content
        self.instance_id = instance_id
        self.message_id = message_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.feedback_content is not None:
            result['FeedbackContent'] = self.feedback_content

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('FeedbackContent') is not None:
            self.feedback_content = m.get('FeedbackContent')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self


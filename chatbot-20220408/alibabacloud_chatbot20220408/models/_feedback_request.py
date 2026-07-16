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
        # The key for the business space. If this parameter is not set, the system uses the default business space. You can obtain the key from the business management page of your primary account.
        self.agent_key = agent_key
        # The feedback rating for the response. This parameter corresponds to `FeedbackType` in the session history API.
        # 
        # Enumerated values: \\"good\\" (a positive rating) and \\"bad\\" (a negative rating).
        self.feedback = feedback
        # The detailed feedback content. You can provide this as a raw string or as a JSON string. If you use a JSON string, the \\"content\\" field corresponds to \\"FeedbackUserInfo\\" and the \\"feedbackLabels\\" field corresponds to \\"FeedbackLabels\\" in the session history.
        self.feedback_content = feedback_content
        # The unique identifier of the chatbot instance.
        self.instance_id = instance_id
        # The unique identifier of a single message within the session.
        self.message_id = message_id
        # The unique identifier for the session. The instant messaging (IM) system uses this ID to track the conversation.
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


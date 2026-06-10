# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssociateRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        perspective: List[str] = None,
        recommend_num: int = None,
        session_id: str = None,
        utterance: str = None,
    ):
        # The workspace key. If this parameter is not specified, the service uses the default workspace. You can obtain the key from the workspace management page of your Alibaba Cloud account.
        self.agent_key = agent_key
        # The instance ID.
        self.instance_id = instance_id
        # The code for a perspective. Use this to retrieve answers from different perspectives that share the same knowledge title. When constructing the request, pass the value in the "Perspective={perspective_code}" format, for example, \\&Perspective=["FZJBY3raWr"]. If you use an SDK, pass the parameter as defined by the SDK. You can specify only one perspective in each request.
        self.perspective = perspective
        # The number of recommended FAQs to return. The value must be an integer from 1 to 10. This parameter takes effect only when recommendations are generated. The number of FAQs returned is less than or equal to the value you specify.
        self.recommend_num = recommend_num
        # The session ID that identifies a conversation and maintains context. For the first request from a new user, you can omit this parameter. The service automatically starts a session and returns a session ID in the response. To continue the conversation, you must include the session ID in subsequent requests.
        self.session_id = session_id
        # The user\\"s utterance.
        self.utterance = utterance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.perspective is not None:
            result['Perspective'] = self.perspective

        if self.recommend_num is not None:
            result['RecommendNum'] = self.recommend_num

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Perspective') is not None:
            self.perspective = m.get('Perspective')

        if m.get('RecommendNum') is not None:
            self.recommend_num = m.get('RecommendNum')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        return self


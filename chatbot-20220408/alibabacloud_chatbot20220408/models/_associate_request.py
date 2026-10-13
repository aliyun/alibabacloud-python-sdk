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
        # The business space key. If not specified, the default business space is accessed. Obtain the key value from the business management page of the primary account.
        self.agent_key = agent_key
        # The unique identifier of the robot.
        self.instance_id = instance_id
        # The perspective code, which is used to call answers from different perspectives under the same knowledge title. When assembling request parameters, pass the parameter in the format Perspective={perspective code}. For example: &Perspective=["FZJBY3raWr"]. When using the SDK, use the parameters defined in the SDK. Currently, only one perspective answer can be called.
        self.perspective = perspective
        # The number of recommended questions, ranging from 1 to 10. This parameter takes effect only when recommendations are returned. The number of returned recommended questions is less than or equal to RecommendNum.
        self.recommend_num = recommend_num
        # The session ID, which is used to identify a visitor\\"s session and maintain context information. For a new visitor, you do not need to pass this field when calling the Chat operation for the first time. The robot starts a session and returns the SessionId of the session in the response of the Chat operation. For subsequent conversation turns of the visitor, pass the SessionId of the current session when calling the Chat operation so that the robot can continue the conversation based on the SessionId.
        self.session_id = session_id
        # The user utterance.
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        intent_name: str = None,
        knowledge_id: str = None,
        perspective_shrink: str = None,
        sand_box: bool = None,
        sender_id: str = None,
        sender_nick: str = None,
        session_id: str = None,
        utterance: str = None,
        vendor_param: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.intent_name = intent_name
        self.knowledge_id = knowledge_id
        self.perspective_shrink = perspective_shrink
        self.sand_box = sand_box
        self.sender_id = sender_id
        self.sender_nick = sender_nick
        self.session_id = session_id
        self.utterance = utterance
        self.vendor_param = vendor_param

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

        if self.intent_name is not None:
            result['IntentName'] = self.intent_name

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.perspective_shrink is not None:
            result['Perspective'] = self.perspective_shrink

        if self.sand_box is not None:
            result['SandBox'] = self.sand_box

        if self.sender_id is not None:
            result['SenderId'] = self.sender_id

        if self.sender_nick is not None:
            result['SenderNick'] = self.sender_nick

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('Perspective') is not None:
            self.perspective_shrink = m.get('Perspective')

        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')

        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')

        if m.get('SenderNick') is not None:
            self.sender_nick = m.get('SenderNick')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')

        return self


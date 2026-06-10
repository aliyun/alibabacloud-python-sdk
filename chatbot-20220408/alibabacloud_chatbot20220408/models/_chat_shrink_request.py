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
        # The key for the business space. If omitted, the request is routed to the default business space. You can get this key from the **Business Management** page of your main account.
        self.agent_key = agent_key
        # The unique ID of the chatbot instance. To get this ID, log in to the Alibaba Cloud Chatbot console and go to **Chatbot Details** > **Session API**.
        self.instance_id = instance_id
        # The name of an intent within a dialog flow. If specified, the chatbot directly activates this intent to process the user\\"s request.
        self.intent_name = intent_name
        # The ID of an entry in the knowledge base. If you specify this ID, the chatbot directly returns the corresponding answer.
        self.knowledge_id = knowledge_id
        # An array of perspective codes. Use these codes to retrieve answers from different perspectives for the same knowledge entry. Example: `Perspective=["FZJBY3raWr"]`. When using an SDK, refer to its parameter definitions.
        self.perspective_shrink = perspective_shrink
        # Specifies the environment to use. The default value is `false`, which indicates the production environment.
        # 
        # - `true`: The test environment. This environment is for testing only. Do not use it in production due to potential instability and QPS limitations.
        # 
        # - `false`: The production environment.
        self.sand_box = sand_box
        # The unique ID of the user in the current session.
        self.sender_id = sender_id
        # The nickname of the user in the current session.
        self.sender_nick = sender_nick
        # The session ID, used to identify a user session and maintain context. For a new user, omit this parameter in the first call to the `Chat` API. The chatbot automatically starts a session and returns the `SessionId` in the response. To continue the conversation, include this `SessionId` in all subsequent requests. The maximum length is 64 characters.
        self.session_id = session_id
        # The user\\"s input text.
        self.utterance = utterance
        # A JSON-formatted string containing custom parameters to pass to various dialog engines.
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


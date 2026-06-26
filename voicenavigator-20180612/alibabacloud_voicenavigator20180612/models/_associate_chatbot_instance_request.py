# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateChatbotInstanceRequest(DaraModel):
    def __init__(
        self,
        chatbot_instance_id: str = None,
        chatbot_name: str = None,
        instance_id: str = None,
        nlu_service_params_json: str = None,
        nlu_service_type: str = None,
        union_source: str = None,
    ):
        # The chatbot ID.
        self.chatbot_instance_id = chatbot_instance_id
        # The name of the chatbot.
        self.chatbot_name = chatbot_name
        # The navigation instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.nlu_service_params_json = nlu_service_params_json
        self.nlu_service_type = nlu_service_type
        self.union_source = union_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chatbot_instance_id is not None:
            result['ChatbotInstanceId'] = self.chatbot_instance_id

        if self.chatbot_name is not None:
            result['ChatbotName'] = self.chatbot_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nlu_service_params_json is not None:
            result['NluServiceParamsJson'] = self.nlu_service_params_json

        if self.nlu_service_type is not None:
            result['NluServiceType'] = self.nlu_service_type

        if self.union_source is not None:
            result['UnionSource'] = self.union_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatbotInstanceId') is not None:
            self.chatbot_instance_id = m.get('ChatbotInstanceId')

        if m.get('ChatbotName') is not None:
            self.chatbot_name = m.get('ChatbotName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NluServiceParamsJson') is not None:
            self.nlu_service_params_json = m.get('NluServiceParamsJson')

        if m.get('NluServiceType') is not None:
            self.nlu_service_type = m.get('NluServiceType')

        if m.get('UnionSource') is not None:
            self.union_source = m.get('UnionSource')

        return self


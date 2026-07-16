# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        introduction: str = None,
        name: str = None,
    ):
        # The workspace key. If you omit this parameter, the default workspace is used. You can get this key from the Business Management page in your Alibaba Cloud account.
        self.agent_key = agent_key
        # The unique ID of the chatbot instance.
        self.instance_id = instance_id
        # The new description of the chatbot.
        self.introduction = introduction
        # The new name of the chatbot. The maximum length is 50 characters.
        self.name = name

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

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


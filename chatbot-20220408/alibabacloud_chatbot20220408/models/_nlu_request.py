# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NluRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        utterance: str = None,
    ):
        # The agent key. If not specified, the default agent is used. Find the key on the Business Management page of your Alibaba Cloud account.
        self.agent_key = agent_key
        # The unique identifier of the bot instance.
        self.instance_id = instance_id
        # The user\\"s text input.
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

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        return self


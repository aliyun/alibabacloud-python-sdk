# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMultiChannelRecordingsRequest(DaraModel):
    def __init__(
        self,
        agent_channel_id: str = None,
        agent_id: str = None,
        contact_id: str = None,
        instance_id: str = None,
    ):
        self.agent_channel_id = agent_channel_id
        self.agent_id = agent_id
        # This parameter is required.
        self.contact_id = contact_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_channel_id is not None:
            result['AgentChannelId'] = self.agent_channel_id

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentChannelId') is not None:
            self.agent_channel_id = m.get('AgentChannelId')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


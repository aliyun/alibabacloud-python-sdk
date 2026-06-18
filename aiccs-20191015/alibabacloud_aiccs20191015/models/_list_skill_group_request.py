# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillGroupRequest(DaraModel):
    def __init__(
        self,
        channel_type: int = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # The skill group channel type. Valid values:
        # - **0**: Returns all skill groups.
        # - **1**: Voice skill group.
        # - **2**: Chat skill group.
        # - **3**: Chat and voice skill group.
        # - **4**: Ticket skill group.
        # - **5**: Voice and ticket skill group.
        # - **6**: Chat and ticket skill group.
        # - **7**: Chat, voice, and ticket skill group.
        self.channel_type = channel_type
        # Unique ID of the customer request. Used for idempotency validation. You can generate it using UUID.
        self.client_token = client_token
        # Artificial Intelligence Cloud Call Service (AICCS) instance ID.  
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


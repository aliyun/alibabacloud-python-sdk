# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDepGroupTreeDataRequest(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        instance_id: str = None,
    ):
        # The agent ID.
        # You can invoke the [GetAgent](https://help.aliyun.com/zh/aiccs/developer-reference/api-aiccs-2019-10-15-getagent) API and view the **AgentId** parameter in the response to obtain the agent ID.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The Artificial Intelligence Cloud Call Service (AICCS) instance ID.
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
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


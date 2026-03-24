# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BeginSessionRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        sand_box: bool = None,
        session_id: str = None,
        vendor_param: str = None,
    ):
        self.agent_key = agent_key
        self.instance_id = instance_id
        self.sand_box = sand_box
        self.session_id = session_id
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

        if self.sand_box is not None:
            result['SandBox'] = self.sand_box

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.vendor_param is not None:
            result['VendorParam'] = self.vendor_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SandBox') is not None:
            self.sand_box = m.get('SandBox')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('VendorParam') is not None:
            self.vendor_param = m.get('VendorParam')

        return self


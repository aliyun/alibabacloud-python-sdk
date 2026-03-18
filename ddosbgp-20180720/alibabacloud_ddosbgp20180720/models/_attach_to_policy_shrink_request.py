# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachToPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        ip_port_protocol_list_shrink: str = None,
        policy_id: str = None,
        port_version: str = None,
    ):
        # The protected objects.
        # 
        # This parameter is required.
        self.ip_port_protocol_list_shrink = ip_port_protocol_list_shrink
        # The policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        self.port_version = port_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_port_protocol_list_shrink is not None:
            result['IpPortProtocolList'] = self.ip_port_protocol_list_shrink

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.port_version is not None:
            result['PortVersion'] = self.port_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPortProtocolList') is not None:
            self.ip_port_protocol_list_shrink = m.get('IpPortProtocolList')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PortVersion') is not None:
            self.port_version = m.get('PortVersion')

        return self


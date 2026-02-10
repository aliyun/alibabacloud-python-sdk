# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateHoneypotNodeRequest(DaraModel):
    def __init__(
        self,
        allow_honeypot_access_internet: bool = None,
        available_probe_num: int = None,
        node_name: str = None,
        security_group_probe_ip_list: List[str] = None,
    ):
        # Specifies whether to allow honeypots to access the Internet. Valid values:
        # 
        # *   **true**: allows honeypots to access the Internet.
        # *   **false**: does not allow honeypots to access the Internet.
        self.allow_honeypot_access_internet = allow_honeypot_access_internet
        # The number of available probes.
        self.available_probe_num = available_probe_num
        # The name of the management node.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The CIDR blocks that are allowed to access the management node.
        self.security_group_probe_ip_list = security_group_probe_ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_honeypot_access_internet is not None:
            result['AllowHoneypotAccessInternet'] = self.allow_honeypot_access_internet

        if self.available_probe_num is not None:
            result['AvailableProbeNum'] = self.available_probe_num

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.security_group_probe_ip_list is not None:
            result['SecurityGroupProbeIpList'] = self.security_group_probe_ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowHoneypotAccessInternet') is not None:
            self.allow_honeypot_access_internet = m.get('AllowHoneypotAccessInternet')

        if m.get('AvailableProbeNum') is not None:
            self.available_probe_num = m.get('AvailableProbeNum')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('SecurityGroupProbeIpList') is not None:
            self.security_group_probe_ip_list = m.get('SecurityGroupProbeIpList')

        return self


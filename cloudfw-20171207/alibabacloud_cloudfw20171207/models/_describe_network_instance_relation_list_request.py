# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkInstanceRelationListRequest(DaraModel):
    def __init__(
        self,
        connect_type: str = None,
        firewall_configure_status: str = None,
        lang: str = None,
        network_instance_id: str = None,
        peer_network_instance_id: str = None,
    ):
        self.connect_type = connect_type
        self.firewall_configure_status = firewall_configure_status
        self.lang = lang
        self.network_instance_id = network_instance_id
        self.peer_network_instance_id = peer_network_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.firewall_configure_status is not None:
            result['FirewallConfigureStatus'] = self.firewall_configure_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.peer_network_instance_id is not None:
            result['PeerNetworkInstanceId'] = self.peer_network_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('FirewallConfigureStatus') is not None:
            self.firewall_configure_status = m.get('FirewallConfigureStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('PeerNetworkInstanceId') is not None:
            self.peer_network_instance_id = m.get('PeerNetworkInstanceId')

        return self


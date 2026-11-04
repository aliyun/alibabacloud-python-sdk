# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindNlbRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        app_id: str = None,
        listeners: str = None,
        nlb_id: str = None,
        zone_mappings: str = None,
    ):
        # The address type. Valid values:
        # - Internet: public network address.
        # - Intranet: private network address.
        self.address_type = address_type
        # The ID of the application.
        self.app_id = app_id
        # The JSON array string of the listeners to be configured. The structure of each listener is as follows:
        # 
        # - **Port**: Integer type, required. The load balancing listener port. Valid values: 0 to 65535.
        # 
        # - **TargetPort**: Integer type, required. The listening port of the container in the instance. Valid values: 0 to 65535.
        # 
        # - **Protocol**: String type, required. The listening protocol. Valid values: TCP, UDP, and TCPSSL.
        # 
        # - **CertIds**: String type, optional. The list of server certificates. This parameter takes effect only for TCPSSL listeners.
        self.listeners = listeners
        # The ID of the NLB instance.
        self.nlb_id = nlb_id
        # The JSON string of the zone and vSwitch mapping list. You can add up to 10 zones. If the current region supports two or more zones, you must add at least two zones. The structure of a ZoneMapping is as follows:
        # 
        # - VSwitchId: String type. The vSwitch corresponding to the zone. Each zone can use only one vSwitch and one subnet.
        # 
        # - ZoneId: String type. The zone ID of the Network Load Balancer (NLB) instance.
        self.zone_mappings = zone_mappings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.listeners is not None:
            result['Listeners'] = self.listeners

        if self.nlb_id is not None:
            result['NlbId'] = self.nlb_id

        if self.zone_mappings is not None:
            result['ZoneMappings'] = self.zone_mappings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')

        if m.get('NlbId') is not None:
            self.nlb_id = m.get('NlbId')

        if m.get('ZoneMappings') is not None:
            self.zone_mappings = m.get('ZoneMappings')

        return self


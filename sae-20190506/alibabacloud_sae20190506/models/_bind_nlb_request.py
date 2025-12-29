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
        # The type of the IP addresses. Valid values:
        # 
        # *   Internet: public endpoint.
        # *   Intranet: private endpoint.
        self.address_type = address_type
        # The ID of the application to which the NLB instance is bound.
        self.app_id = app_id
        # The listener that you want to manage. The value is a string that consists of JSON arrays. Each listener contains the following fields:
        # 
        # *   **port**: the port number of the NLB listener. This field is required. Data type: integer. Valid values: 0 to 65535.
        # *   **TargetPort**: the port number of the container listener. This field is required. Data type: integer. Valid values: 0 to 65535.
        # *   **Protocol**: the listener protocol. This field is required. Data type: string. Valid values: TCP, UDP, and TCPSSL.
        # *   **CertIds**: the IDs of the server certificates. This field is optional. Data type: string. This field is supported only by TCPSSL listeners.
        self.listeners = listeners
        # The ID of the NLB instance.
        self.nlb_id = nlb_id
        # The mappings between zones and vSwitches. The value is a JSON string. You can specify at most 10 zones. If the region supports two or more zones, specify at least two zones. A ZoneMapping contains the following fields:
        # 
        # *   The ID of the vSwitch in the zone. Each zone can contain only one vSwitch and one subnet. Data type: string.
        # *   The zone ID of the NLB instance. Data type: string.
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


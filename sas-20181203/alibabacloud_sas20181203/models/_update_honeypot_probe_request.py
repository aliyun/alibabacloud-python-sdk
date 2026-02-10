# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateHoneypotProbeRequest(DaraModel):
    def __init__(
        self,
        arp: bool = None,
        display_name: str = None,
        lang: str = None,
        ping: bool = None,
        probe_id: str = None,
        service_ip_list: List[str] = None,
    ):
        # Specifies whether address resolution protocol (ARP) is enabled for the check type.
        self.arp = arp
        # The name of the probe.
        self.display_name = display_name
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # Specifies whether ping is enabled for the check type.
        self.ping = ping
        # The ID of the probe.
        # 
        # > You can call the [ListHoneypotProbe](~~ListHoneypotProbe~~) operation to query the IDs of probes.
        # 
        # This parameter is required.
        self.probe_id = probe_id
        # The IP addresses that are monitored.
        self.service_ip_list = service_ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arp is not None:
            result['Arp'] = self.arp

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.ping is not None:
            result['Ping'] = self.ping

        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        if self.service_ip_list is not None:
            result['ServiceIpList'] = self.service_ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arp') is not None:
            self.arp = m.get('Arp')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Ping') is not None:
            self.ping = m.get('Ping')

        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        if m.get('ServiceIpList') is not None:
            self.service_ip_list = m.get('ServiceIpList')

        return self


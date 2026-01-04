# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySnatEntryRequest(DaraModel):
    def __init__(
        self,
        eip_affinity: bool = None,
        isp_affinity: bool = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
    ):
        # Specifies whether to enable IP affinity. Default value: true. Valid values:
        # 
        # *   **false**
        # *   **true**
        # 
        # >  Description After you enable IP affinity, if multiple EIPs are associated with an SNAT entry, one client uses the same EIP to for communication. If IP affinity is disabled, the client uses a random EIP for communication.
        self.eip_affinity = eip_affinity
        self.isp_affinity = isp_affinity
        # This parameter is required.
        self.snat_entry_id = snat_entry_id
        self.snat_entry_name = snat_entry_name
        # Separate multiple EIPs in the SNAT entry with commas (,).
        self.snat_ip = snat_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_affinity is not None:
            result['EipAffinity'] = self.eip_affinity

        if self.isp_affinity is not None:
            result['IspAffinity'] = self.isp_affinity

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAffinity') is not None:
            self.eip_affinity = m.get('EipAffinity')

        if m.get('IspAffinity') is not None:
            self.isp_affinity = m.get('IspAffinity')

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        return self


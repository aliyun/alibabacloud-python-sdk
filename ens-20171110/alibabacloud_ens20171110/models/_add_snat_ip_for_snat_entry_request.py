# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSnatIpForSnatEntryRequest(DaraModel):
    def __init__(
        self,
        snat_entry_id: str = None,
        snat_ip: str = None,
    ):
        # The ID of the SNAT entry.
        # 
        # This parameter is required.
        self.snat_entry_id = snat_entry_id
        # The EIP specified in the SNAT entry.
        # 
        # This parameter is required.
        self.snat_ip = snat_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        return self


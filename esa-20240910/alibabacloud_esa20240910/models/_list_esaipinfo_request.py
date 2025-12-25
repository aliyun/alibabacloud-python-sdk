# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListESAIPInfoRequest(DaraModel):
    def __init__(
        self,
        vip_info: str = None,
    ):
        # You can enter IPv4 or IPv6 addresses. Separate multiple IP addresses with commas (,). You can enter up to 20 IP addresses at a time.
        # 
        # This parameter is required.
        self.vip_info = vip_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vip_info is not None:
            result['VipInfo'] = self.vip_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VipInfo') is not None:
            self.vip_info = m.get('VipInfo')

        return self


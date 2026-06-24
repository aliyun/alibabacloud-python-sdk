# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class WhiteIpGroup(DaraModel):
    def __init__(
        self,
        white_ip_type: str = None,
        group_name: str = None,
        ips: List[str] = None,
    ):
        # The type of the IP address whitelist. Valid values:
        # 
        # - PRIVATE_ES: Elasticsearch private network access whitelist
        # - PUBLIC_ES: Elasticsearch public network access whitelist
        # - PRIVATE_KIBANA: Kibana private network access whitelist
        # - PUBLIC_KIBANA: Kibana public network access whitelist.
        self.white_ip_type = white_ip_type
        # The name of the IP address whitelist group.
        self.group_name = group_name
        # The list of IP addresses in the whitelist group.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.white_ip_type is not None:
            result['WhiteIpType'] = self.white_ip_type

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.ips is not None:
            result['ips'] = self.ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteIpType') is not None:
            self.white_ip_type = m.get('WhiteIpType')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('ips') is not None:
            self.ips = m.get('ips')

        return self


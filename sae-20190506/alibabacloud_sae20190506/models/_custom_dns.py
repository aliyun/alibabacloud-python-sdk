# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CustomDNS(DaraModel):
    def __init__(
        self,
        dns_options: List[main_models.DNSOption] = None,
        name_servers: List[str] = None,
        searches: List[str] = None,
    ):
        self.dns_options = dns_options
        self.name_servers = name_servers
        self.searches = searches

    def validate(self):
        if self.dns_options:
            for v1 in self.dns_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dnsOptions'] = []
        if self.dns_options is not None:
            for k1 in self.dns_options:
                result['dnsOptions'].append(k1.to_map() if k1 else None)

        if self.name_servers is not None:
            result['nameServers'] = self.name_servers

        if self.searches is not None:
            result['searches'] = self.searches

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dns_options = []
        if m.get('dnsOptions') is not None:
            for k1 in m.get('dnsOptions'):
                temp_model = main_models.DNSOption()
                self.dns_options.append(temp_model.from_map(k1))

        if m.get('nameServers') is not None:
            self.name_servers = m.get('nameServers')

        if m.get('searches') is not None:
            self.searches = m.get('searches')

        return self


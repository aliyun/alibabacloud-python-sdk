# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HiMarketDomain(DaraModel):
    def __init__(
        self,
        domain: str = None,
        network_type: str = None,
        port: int = None,
        protocol: str = None,
    ):
        # The custom domain name. This must be a valid DNS hostname.
        self.domain = domain
        # The network type of the endpoint. For example, `VPC` for an internal network or `INTERNET` for a public network.
        self.network_type = network_type
        # The port number for the endpoint. For example, `80` for HTTP or `443` for HTTPS.
        self.port = port
        # The communication protocol. Valid values include `HTTP` and `HTTPS`.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigL7UsKeepaliveRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        downstream_keepalive: str = None,
        upstream_keepalive: str = None,
    ):
        # The domain name of the website service.
        # > The domain name must have a website service forwarding rule configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        self.domain = domain
        # The idle timeout period of the persistent connection between the client and Anti-DDoS Proxy.
        self.downstream_keepalive = downstream_keepalive
        # The persistent connection settings for back-to-origin requests of Anti-DDoS Proxy. The value is a string that represents a JSON struct. The JSON struct contains the following fields:
        # 
        # - **enabled**: Boolean | Required | Specifies whether to enable persistent connections for back-to-origin requests.
        # - **keepalive_requests**: Integer | Required | The number of requests that can be sent over a persistent connection.
        # - **keepalive_timeout**: Integer | Required | The idle timeout period of a persistent connection.
        # 
        # This parameter is required.
        self.upstream_keepalive = upstream_keepalive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.downstream_keepalive is not None:
            result['DownstreamKeepalive'] = self.downstream_keepalive

        if self.upstream_keepalive is not None:
            result['UpstreamKeepalive'] = self.upstream_keepalive

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DownstreamKeepalive') is not None:
            self.downstream_keepalive = m.get('DownstreamKeepalive')

        if m.get('UpstreamKeepalive') is not None:
            self.upstream_keepalive = m.get('UpstreamKeepalive')

        return self


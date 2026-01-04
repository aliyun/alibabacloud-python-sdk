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
        # The domain name of the website.
        # 
        # >  A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        self.domain = domain
        self.downstream_keepalive = downstream_keepalive
        # The settings for back-to-origin persistent connections. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **enabled**: the switch for back-to-origin persistent connections. This field is required, and the value is of the Boolean type.
        # *   **keepalive_requests**: the number of requests that reuse a persistent connection. This field is required, and the value is of the integer type.
        # *   **keepalive_timeout**: the timeout period for an idle persistent connection. This field is required, and the value is of the integer type.
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


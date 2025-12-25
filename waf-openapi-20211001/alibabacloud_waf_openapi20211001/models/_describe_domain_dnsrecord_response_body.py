# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainDNSRecordResponseBody(DaraModel):
    def __init__(
        self,
        dnsstatus: str = None,
        request_id: str = None,
    ):
        # The status of the DNS settings. Valid values:
        # 
        # *   **cnameMatched**: The DNS settings are properly configured.
        # *   **vipMatched**: An A record maps the domain name to the WAF virtual IP address (VIP).
        # *   **wafVip**: An A record maps the domain name to another WAF VIP.
        # *   **unRecord**: The domain name does not have a DNS record.
        # *   **unUsed**: The domain name is not pointed to WAF.
        # *   **checkTimeout**: The check times out.
        self.dnsstatus = dnsstatus
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dnsstatus is not None:
            result['DNSStatus'] = self.dnsstatus

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNSStatus') is not None:
            self.dnsstatus = m.get('DNSStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


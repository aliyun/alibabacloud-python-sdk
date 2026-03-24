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
        # The DNS status. Valid values:
        # 
        # - **cnameMatched**: The DNS record is normal.
        # 
        # - **vipMatched**: The domain name is mapped to an A record.
        # 
        # - **wafVip**: The domain name is mapped to the virtual IP address (VIP) of another WAF instance.
        # 
        # - **unRecord**: No DNS record is configured.
        # 
        # - **unUsed**: Traffic is not forwarded to WAF.
        # 
        # - **checkTimeout**: The check timed out.
        self.dnsstatus = dnsstatus
        # The ID of the request.
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


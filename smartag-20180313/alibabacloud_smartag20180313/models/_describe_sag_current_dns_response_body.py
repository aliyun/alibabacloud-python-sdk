# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSagCurrentDnsResponseBody(DaraModel):
    def __init__(
        self,
        master_dns: str = None,
        request_id: str = None,
        slave_dns: str = None,
    ):
        # The IP address of the primary DNS server.
        self.master_dns = master_dns
        # The ID of the request.
        self.request_id = request_id
        # The IP address of the secondary DNS server.
        self.slave_dns = slave_dns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_dns is not None:
            result['MasterDns'] = self.master_dns

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slave_dns is not None:
            result['SlaveDns'] = self.slave_dns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterDns') is not None:
            self.master_dns = m.get('MasterDns')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlaveDns') is not None:
            self.slave_dns = m.get('SlaveDns')

        return self


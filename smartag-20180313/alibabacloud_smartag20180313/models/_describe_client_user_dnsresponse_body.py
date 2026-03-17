# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeClientUserDNSResponseBody(DaraModel):
    def __init__(
        self,
        app_dns: List[str] = None,
        recovered_dns: List[str] = None,
        request_id: str = None,
    ):
        # The active and standby DNS servers that the SAG app instance uses when it connects to private networks.
        self.app_dns = app_dns
        # The active and standby DNS servers that the SAG app instance uses when it disconnects from private networks.
        self.recovered_dns = recovered_dns
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_dns is not None:
            result['AppDNS'] = self.app_dns

        if self.recovered_dns is not None:
            result['RecoveredDNS'] = self.recovered_dns

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDNS') is not None:
            self.app_dns = m.get('AppDNS')

        if m.get('RecoveredDNS') is not None:
            self.recovered_dns = m.get('RecoveredDNS')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


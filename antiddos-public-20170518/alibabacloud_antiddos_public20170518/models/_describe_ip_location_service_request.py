# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIpLocationServiceRequest(DaraModel):
    def __init__(
        self,
        internet_ip: str = None,
    ):
        # The IP address of the asset to query.
        # 
        # This parameter is required.
        self.internet_ip = internet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        return self


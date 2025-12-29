# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOssStatusV2Request(DaraModel):
    def __init__(
        self,
        service_code: str = None,
        source_ip: str = None,
    ):
        # ServiceCode for Real Person Cloud products:
        # - **antcloudauth**: Financial-grade real person authentication
        # - **cloudauthst (discontinued)**: Enhanced real person authentication
        self.service_code = service_code
        # Visitor\\"s source IP address.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


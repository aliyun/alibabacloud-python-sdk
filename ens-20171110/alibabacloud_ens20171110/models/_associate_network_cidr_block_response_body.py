# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateNetworkCidrBlockResponseBody(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        ip_version: str = None,
        request_id: str = None,
    ):
        # The allocated secondary CIDR block.
        self.cidr_block = cidr_block
        # The IP address type of the secondary CIDR block. Valid values:
        # - IPV4: IPv4 address.
        # - IPV6: IPv6 address.
        self.ip_version = ip_version
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


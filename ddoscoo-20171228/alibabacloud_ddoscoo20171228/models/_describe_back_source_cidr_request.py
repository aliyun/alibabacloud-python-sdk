# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackSourceCidrRequest(DaraModel):
    def __init__(
        self,
        ip_version: str = None,
        line: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.ip_version = ip_version
        self.line = line
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.line is not None:
            result['Line'] = self.line

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


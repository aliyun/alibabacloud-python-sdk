# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFirewallDropStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        acl_drop_cnt: int = None,
        ips_drop_cnt: int = None,
        request_id: str = None,
        total_drop_cnt: int = None,
        vuln_drop_cnt: int = None,
    ):
        self.acl_drop_cnt = acl_drop_cnt
        self.ips_drop_cnt = ips_drop_cnt
        self.request_id = request_id
        self.total_drop_cnt = total_drop_cnt
        self.vuln_drop_cnt = vuln_drop_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_drop_cnt is not None:
            result['AclDropCnt'] = self.acl_drop_cnt

        if self.ips_drop_cnt is not None:
            result['IpsDropCnt'] = self.ips_drop_cnt

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_drop_cnt is not None:
            result['TotalDropCnt'] = self.total_drop_cnt

        if self.vuln_drop_cnt is not None:
            result['VulnDropCnt'] = self.vuln_drop_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclDropCnt') is not None:
            self.acl_drop_cnt = m.get('AclDropCnt')

        if m.get('IpsDropCnt') is not None:
            self.ips_drop_cnt = m.get('IpsDropCnt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalDropCnt') is not None:
            self.total_drop_cnt = m.get('TotalDropCnt')

        if m.get('VulnDropCnt') is not None:
            self.vuln_drop_cnt = m.get('VulnDropCnt')

        return self


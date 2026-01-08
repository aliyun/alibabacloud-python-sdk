# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAclRuleCountResponseBody(DaraModel):
    def __init__(
        self,
        internet_in_acl_count: int = None,
        internet_out_acl_count: int = None,
        nat_in_acl_count: int = None,
        nat_out_acl_count: int = None,
        request_id: str = None,
        total_acl_count: int = None,
        vpc_acl_count: int = None,
    ):
        self.internet_in_acl_count = internet_in_acl_count
        self.internet_out_acl_count = internet_out_acl_count
        self.nat_in_acl_count = nat_in_acl_count
        self.nat_out_acl_count = nat_out_acl_count
        self.request_id = request_id
        self.total_acl_count = total_acl_count
        self.vpc_acl_count = vpc_acl_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_in_acl_count is not None:
            result['InternetInAclCount'] = self.internet_in_acl_count

        if self.internet_out_acl_count is not None:
            result['InternetOutAclCount'] = self.internet_out_acl_count

        if self.nat_in_acl_count is not None:
            result['NatInAclCount'] = self.nat_in_acl_count

        if self.nat_out_acl_count is not None:
            result['NatOutAclCount'] = self.nat_out_acl_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_acl_count is not None:
            result['TotalAclCount'] = self.total_acl_count

        if self.vpc_acl_count is not None:
            result['VpcAclCount'] = self.vpc_acl_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetInAclCount') is not None:
            self.internet_in_acl_count = m.get('InternetInAclCount')

        if m.get('InternetOutAclCount') is not None:
            self.internet_out_acl_count = m.get('InternetOutAclCount')

        if m.get('NatInAclCount') is not None:
            self.nat_in_acl_count = m.get('NatInAclCount')

        if m.get('NatOutAclCount') is not None:
            self.nat_out_acl_count = m.get('NatOutAclCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalAclCount') is not None:
            self.total_acl_count = m.get('TotalAclCount')

        if m.get('VpcAclCount') is not None:
            self.vpc_acl_count = m.get('VpcAclCount')

        return self


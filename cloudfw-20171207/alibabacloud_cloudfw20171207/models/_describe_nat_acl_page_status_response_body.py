# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNatAclPageStatusResponseBody(DaraModel):
    def __init__(
        self,
        detail: str = None,
        nat_acl_page_enable: bool = None,
        request_id: str = None,
    ):
        # Extra error information.
        self.detail = detail
        # Indicates whether pagination for access control policies for NAT firewalls is supported.
        self.nat_acl_page_enable = nat_acl_page_enable
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.nat_acl_page_enable is not None:
            result['NatAclPageEnable'] = self.nat_acl_page_enable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('NatAclPageEnable') is not None:
            self.nat_acl_page_enable = m.get('NatAclPageEnable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


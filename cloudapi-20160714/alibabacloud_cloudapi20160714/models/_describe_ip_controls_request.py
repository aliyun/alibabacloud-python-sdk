# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIpControlsRequest(DaraModel):
    def __init__(
        self,
        ip_control_id: str = None,
        ip_control_name: str = None,
        ip_control_type: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        # The ID of the ACL. The ID is unique.
        self.ip_control_id = ip_control_id
        # The name of the ACL.
        self.ip_control_name = ip_control_name
        # The type of the ACL. Valid values:
        # 
        # *   **ALLOW**: a whitelist
        # *   **REFUSE**: a blacklist
        self.ip_control_type = ip_control_type
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id

        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name

        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')

        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')

        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallAclGroupListRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        firewall_configure_status: str = None,
        firewall_id: str = None,
        lang: str = None,
        page_size: str = None,
    ):
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # Specifies whether VPC firewalls are configured. Valid values:
        # 
        # *   **notconfigured**: VPC firewalls are not configured.
        # *   **configured**: VPC firewalls are configured.
        # *   If you do not specify this parameter, the access control policies of all VPC firewalls are queried.
        self.firewall_configure_status = firewall_configure_status
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Maximum value: 50.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.firewall_configure_status is not None:
            result['FirewallConfigureStatus'] = self.firewall_configure_status

        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FirewallConfigureStatus') is not None:
            self.firewall_configure_status = m.get('FirewallConfigureStatus')

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


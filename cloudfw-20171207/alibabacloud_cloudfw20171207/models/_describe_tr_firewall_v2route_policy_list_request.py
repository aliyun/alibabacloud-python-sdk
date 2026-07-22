# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrFirewallV2RoutePolicyListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        firewall_id: str = None,
        lang: str = None,
        page_size: int = None,
        policy_id: str = None,
    ):
        # The page number in a paged query. Default value: 1. For more information about paging, see the corresponding parameter descriptions.
        self.current_page = current_page
        # The instance ID of the virtual private cloud (VPC) firewall.
        # 
        # > FirewallId is required. If this parameter is not specified, the ErrorParameters (400) error is returned. You can call DescribeTrFirewallsV2List to obtain the FirewallId. Prerequisites: CEN Enterprise Edition with a transit router and VPC mount are configured, and the FirewallId is obtained by calling DescribeTrFirewallsV2List.
        self.firewall_id = firewall_id
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The maximum number of entries per page in a paged query. Default value: 10. For more information about paging, see the corresponding parameter descriptions.
        self.page_size = page_size
        # The ID of the firewall routing policy.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self


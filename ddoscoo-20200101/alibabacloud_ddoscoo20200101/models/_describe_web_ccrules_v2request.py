# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebCCRulesV2Request(DaraModel):
    def __init__(
        self,
        domain: str = None,
        offset: str = None,
        owner: str = None,
        page_size: str = None,
    ):
        # The domain name of the website that you want to add to the Anti-DDoS Proxy instance for protection.
        self.domain = domain
        # The number of entries that you want the system to skip before the system returns entries. Default value: **0**.
        self.offset = offset
        # The method used to create the rule. Valid values:
        # 
        # *   **manual** (default): manually created.
        # *   **clover**: automatically created.
        self.owner = owner
        # The number of entries per page. Maximum value: **20**. Default value: **20**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


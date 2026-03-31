# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCompliancePacksShrinkRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        risk_level: int = None,
        status: str = None,
        tag_shrink: str = None,
    ):
        # The page number.
        # 
        # Pages start from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size
        self.risk_level = risk_level
        # The status of the compliance package to be queried. Valid values:
        # 
        # *   ACTIVE: The compliance package is active.
        # *   CREATING: The compliance package is being created.
        self.status = status
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self


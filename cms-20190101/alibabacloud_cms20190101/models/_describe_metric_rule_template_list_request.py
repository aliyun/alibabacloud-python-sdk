# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricRuleTemplateListRequest(DaraModel):
    def __init__(
        self,
        history: bool = None,
        keyword: str = None,
        name: str = None,
        order: bool = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        template_id: int = None,
    ):
        # Specifies whether to display the history of applying the alert templates to application groups. Valid values:
        # 
        # *   true
        # *   false (default)
        self.history = history
        # The keyword of the alert template name.
        self.keyword = keyword
        # The name of the alert template.
        self.name = name
        # The sorting order. Valid values:
        # 
        # *   true (default): ascending order
        # *   false: descending order
        self.order = order
        # The sorting basis. Valid values:
        # 
        # *   gmtMotified: sorts alert templates by modification time
        # *   gmtCreate (default): sorts alert templates by creation time
        self.order_by = order_by
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the alert template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.history is not None:
            result['History'] = self.history

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('History') is not None:
            self.history = m.get('History')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self


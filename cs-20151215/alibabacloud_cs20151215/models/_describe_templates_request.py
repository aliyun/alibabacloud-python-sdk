# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTemplatesRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        template_type: str = None,
    ):
        # The page number of the returned results.
        # 
        # Default value: 1.
        self.page_num = page_num
        # The number of entries to return on each page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The templatetype. Valid values:
        # 
        # - `kubernetes`: The template is displayed on the Orchestration Templates page in the console.
        # 
        # - If this parameter is left empty or set to other values: The template is not displayed on the Orchestration Templates page in the console.
        # 
        # Recommended settings: `kubernetes`.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['page_num'] = self.page_num

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.template_type is not None:
            result['template_type'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_num') is not None:
            self.page_num = m.get('page_num')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')

        return self


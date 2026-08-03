# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAdvancedQueryTemplateRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        template_name: str = None,
    ):
        # The page number. The value starts from 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The maximum number of results to return.
        # Default value: 20.
        self.page_size = page_size
        # The name of the template. This operation performs a case-insensitive, fuzzy match. If you do not specify a name, all templates are returned.
        # 
        # For example, if you specify `a`, templates named `a1` and `a2` are returned. If you leave this parameter empty, templates named `a1`, `a2`, `b1`, and `c1` are returned.
        self.template_name = template_name

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

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDistillationTemplatesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        template_id: str = None,
    ):
        # The template category for scenario-specific template filtering.
        self.category = category
        # The search keyword for cross-language substring matching against template names, descriptions, and other text fields. If this parameter is left empty, no keyword filtering is applied.
        self.keyword = keyword
        # The page number, starting from 1. If this parameter is not specified or is invalid, the default value 1 is used.
        self.page_number = page_number
        # The number of entries per page. If this parameter is not specified or is invalid, the default value is used. If the value exceeds the upper limit, the upper limit is used.
        self.page_size = page_size
        # The template ID for exact filtering. If this parameter is left empty, no filtering by ID is applied.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self


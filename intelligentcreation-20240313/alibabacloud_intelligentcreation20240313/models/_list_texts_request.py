# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTextsRequest(DaraModel):
    def __init__(
        self,
        generation_source: str = None,
        industry: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        publish_status: str = None,
        text_style_type: str = None,
        text_theme: str = None,
    ):
        self.generation_source = generation_source
        self.industry = industry
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.publish_status = publish_status
        self.text_style_type = text_style_type
        self.text_theme = text_theme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generation_source is not None:
            result['generationSource'] = self.generation_source

        if self.industry is not None:
            result['industry'] = self.industry

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.publish_status is not None:
            result['publishStatus'] = self.publish_status

        if self.text_style_type is not None:
            result['textStyleType'] = self.text_style_type

        if self.text_theme is not None:
            result['textTheme'] = self.text_theme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generationSource') is not None:
            self.generation_source = m.get('generationSource')

        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('publishStatus') is not None:
            self.publish_status = m.get('publishStatus')

        if m.get('textStyleType') is not None:
            self.text_style_type = m.get('textStyleType')

        if m.get('textTheme') is not None:
            self.text_theme = m.get('textTheme')

        return self


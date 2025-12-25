# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OutlineWritingArticle(DaraModel):
    def __init__(
        self,
        content: str = None,
        outline: str = None,
        primary_outline: str = None,
        pub_time: str = None,
        search_source: str = None,
        search_source_name: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.outline = outline
        self.primary_outline = primary_outline
        self.pub_time = pub_time
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.outline is not None:
            result['Outline'] = self.outline

        if self.primary_outline is not None:
            result['PrimaryOutline'] = self.primary_outline

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.search_source is not None:
            result['SearchSource'] = self.search_source

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('PrimaryOutline') is not None:
            self.primary_outline = m.get('PrimaryOutline')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self


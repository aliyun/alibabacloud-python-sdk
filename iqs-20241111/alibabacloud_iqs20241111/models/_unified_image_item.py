# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnifiedImageItem(DaraModel):
    def __init__(
        self,
        height: int = None,
        host_page_url: str = None,
        image_url: str = None,
        published_time: str = None,
        title: str = None,
        width: int = None,
    ):
        self.height = height
        self.host_page_url = host_page_url
        self.image_url = image_url
        self.published_time = published_time
        self.title = title
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['height'] = self.height

        if self.host_page_url is not None:
            result['hostPageUrl'] = self.host_page_url

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.published_time is not None:
            result['publishedTime'] = self.published_time

        if self.title is not None:
            result['title'] = self.title

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('hostPageUrl') is not None:
            self.host_page_url = m.get('hostPageUrl')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('publishedTime') is not None:
            self.published_time = m.get('publishedTime')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self


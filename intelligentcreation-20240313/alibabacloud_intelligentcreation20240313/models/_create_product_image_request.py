# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProductImageRequest(DaraModel):
    def __init__(
        self,
        background_description: str = None,
        background_priority: int = None,
        background_url: str = None,
        highlight_text: str = None,
        image_count: int = None,
        image_url: str = None,
        sub_title: str = None,
        title: str = None,
    ):
        self.background_description = background_description
        self.background_priority = background_priority
        self.background_url = background_url
        self.highlight_text = highlight_text
        self.image_count = image_count
        self.image_url = image_url
        self.sub_title = sub_title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_description is not None:
            result['backgroundDescription'] = self.background_description

        if self.background_priority is not None:
            result['backgroundPriority'] = self.background_priority

        if self.background_url is not None:
            result['backgroundUrl'] = self.background_url

        if self.highlight_text is not None:
            result['highlightText'] = self.highlight_text

        if self.image_count is not None:
            result['imageCount'] = self.image_count

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.sub_title is not None:
            result['subTitle'] = self.sub_title

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backgroundDescription') is not None:
            self.background_description = m.get('backgroundDescription')

        if m.get('backgroundPriority') is not None:
            self.background_priority = m.get('backgroundPriority')

        if m.get('backgroundUrl') is not None:
            self.background_url = m.get('backgroundUrl')

        if m.get('highlightText') is not None:
            self.highlight_text = m.get('highlightText')

        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('subTitle') is not None:
            self.sub_title = m.get('subTitle')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self


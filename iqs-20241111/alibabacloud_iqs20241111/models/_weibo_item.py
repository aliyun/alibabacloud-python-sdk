# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class WeiboItem(DaraModel):
    def __init__(
        self,
        card_type: str = None,
        homepage_link: str = None,
        html_snippet: str = None,
        images: List[str] = None,
        link: str = None,
        publish_display_time: str = None,
        username: str = None,
    ):
        # This parameter is required.
        self.card_type = card_type
        self.homepage_link = homepage_link
        # This parameter is required.
        self.html_snippet = html_snippet
        self.images = images
        # This parameter is required.
        self.link = link
        # This parameter is required.
        self.publish_display_time = publish_display_time
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_type is not None:
            result['cardType'] = self.card_type

        if self.homepage_link is not None:
            result['homepageLink'] = self.homepage_link

        if self.html_snippet is not None:
            result['htmlSnippet'] = self.html_snippet

        if self.images is not None:
            result['images'] = self.images

        if self.link is not None:
            result['link'] = self.link

        if self.publish_display_time is not None:
            result['publishDisplayTime'] = self.publish_display_time

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardType') is not None:
            self.card_type = m.get('cardType')

        if m.get('homepageLink') is not None:
            self.homepage_link = m.get('homepageLink')

        if m.get('htmlSnippet') is not None:
            self.html_snippet = m.get('htmlSnippet')

        if m.get('images') is not None:
            self.images = m.get('images')

        if m.get('link') is not None:
            self.link = m.get('link')

        if m.get('publishDisplayTime') is not None:
            self.publish_display_time = m.get('publishDisplayTime')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HarmonyBody(DaraModel):
    def __init__(
        self,
        action: str = None,
        add_badge: int = None,
        after_open: str = None,
        big_body: str = None,
        custom: str = None,
        img: str = None,
        large_icon: str = None,
        text: str = None,
        title: str = None,
        uri: str = None,
    ):
        self.action = action
        self.add_badge = add_badge
        self.after_open = after_open
        self.big_body = big_body
        self.custom = custom
        self.img = img
        self.large_icon = large_icon
        self.text = text
        self.title = title
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.add_badge is not None:
            result['addBadge'] = self.add_badge

        if self.after_open is not None:
            result['afterOpen'] = self.after_open

        if self.big_body is not None:
            result['bigBody'] = self.big_body

        if self.custom is not None:
            result['custom'] = self.custom

        if self.img is not None:
            result['img'] = self.img

        if self.large_icon is not None:
            result['largeIcon'] = self.large_icon

        if self.text is not None:
            result['text'] = self.text

        if self.title is not None:
            result['title'] = self.title

        if self.uri is not None:
            result['uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('addBadge') is not None:
            self.add_badge = m.get('addBadge')

        if m.get('afterOpen') is not None:
            self.after_open = m.get('afterOpen')

        if m.get('bigBody') is not None:
            self.big_body = m.get('bigBody')

        if m.get('custom') is not None:
            self.custom = m.get('custom')

        if m.get('img') is not None:
            self.img = m.get('img')

        if m.get('largeIcon') is not None:
            self.large_icon = m.get('largeIcon')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('uri') is not None:
            self.uri = m.get('uri')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Message2ThirdChannel(DaraModel):
    def __init__(
        self,
        set_badge: int = None,
        add_badge: int = None,
        big_body: str = None,
        big_title: str = None,
        expand_image: str = None,
        img: str = None,
        sound: str = None,
        text: str = None,
        title: str = None,
    ):
        self.set_badge = set_badge
        self.add_badge = add_badge
        self.big_body = big_body
        self.big_title = big_title
        self.expand_image = expand_image
        self.img = img
        self.sound = sound
        self.text = text
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.set_badge is not None:
            result['SetBadge'] = self.set_badge

        if self.add_badge is not None:
            result['addBadge'] = self.add_badge

        if self.big_body is not None:
            result['bigBody'] = self.big_body

        if self.big_title is not None:
            result['bigTitle'] = self.big_title

        if self.expand_image is not None:
            result['expandImage'] = self.expand_image

        if self.img is not None:
            result['img'] = self.img

        if self.sound is not None:
            result['sound'] = self.sound

        if self.text is not None:
            result['text'] = self.text

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetBadge') is not None:
            self.set_badge = m.get('SetBadge')

        if m.get('addBadge') is not None:
            self.add_badge = m.get('addBadge')

        if m.get('bigBody') is not None:
            self.big_body = m.get('bigBody')

        if m.get('bigTitle') is not None:
            self.big_title = m.get('bigTitle')

        if m.get('expandImage') is not None:
            self.expand_image = m.get('expandImage')

        if m.get('img') is not None:
            self.img = m.get('img')

        if m.get('sound') is not None:
            self.sound = m.get('sound')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self


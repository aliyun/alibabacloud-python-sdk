# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Body(DaraModel):
    def __init__(
        self,
        activity: str = None,
        add_badge: int = None,
        after_open: str = None,
        builder_id: int = None,
        custom: str = None,
        expand_image: str = None,
        icon: str = None,
        img: str = None,
        play_lights: bool = None,
        play_sound: bool = None,
        play_vibrate: bool = None,
        re_pop: int = None,
        set_badge: int = None,
        sound: str = None,
        text: str = None,
        title: str = None,
        url: str = None,
    ):
        self.activity = activity
        self.add_badge = add_badge
        self.after_open = after_open
        self.builder_id = builder_id
        self.custom = custom
        self.expand_image = expand_image
        self.icon = icon
        self.img = img
        self.play_lights = play_lights
        self.play_sound = play_sound
        self.play_vibrate = play_vibrate
        self.re_pop = re_pop
        self.set_badge = set_badge
        self.sound = sound
        self.text = text
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity is not None:
            result['activity'] = self.activity

        if self.add_badge is not None:
            result['addBadge'] = self.add_badge

        if self.after_open is not None:
            result['afterOpen'] = self.after_open

        if self.builder_id is not None:
            result['builderId'] = self.builder_id

        if self.custom is not None:
            result['custom'] = self.custom

        if self.expand_image is not None:
            result['expandImage'] = self.expand_image

        if self.icon is not None:
            result['icon'] = self.icon

        if self.img is not None:
            result['img'] = self.img

        if self.play_lights is not None:
            result['playLights'] = self.play_lights

        if self.play_sound is not None:
            result['playSound'] = self.play_sound

        if self.play_vibrate is not None:
            result['playVibrate'] = self.play_vibrate

        if self.re_pop is not None:
            result['rePop'] = self.re_pop

        if self.set_badge is not None:
            result['setBadge'] = self.set_badge

        if self.sound is not None:
            result['sound'] = self.sound

        if self.text is not None:
            result['text'] = self.text

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activity') is not None:
            self.activity = m.get('activity')

        if m.get('addBadge') is not None:
            self.add_badge = m.get('addBadge')

        if m.get('afterOpen') is not None:
            self.after_open = m.get('afterOpen')

        if m.get('builderId') is not None:
            self.builder_id = m.get('builderId')

        if m.get('custom') is not None:
            self.custom = m.get('custom')

        if m.get('expandImage') is not None:
            self.expand_image = m.get('expandImage')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('img') is not None:
            self.img = m.get('img')

        if m.get('playLights') is not None:
            self.play_lights = m.get('playLights')

        if m.get('playSound') is not None:
            self.play_sound = m.get('playSound')

        if m.get('playVibrate') is not None:
            self.play_vibrate = m.get('playVibrate')

        if m.get('rePop') is not None:
            self.re_pop = m.get('rePop')

        if m.get('setBadge') is not None:
            self.set_badge = m.get('setBadge')

        if m.get('sound') is not None:
            self.sound = m.get('sound')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self


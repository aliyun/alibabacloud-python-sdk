# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddOrUpdateWelcomeTextRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        music_url: str = None,
        welcome_text: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.music_url = music_url
        # This parameter is required.
        self.welcome_text = welcome_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.music_url is not None:
            result['MusicUrl'] = self.music_url

        if self.welcome_text is not None:
            result['WelcomeText'] = self.welcome_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')

        if m.get('WelcomeText') is not None:
            self.welcome_text = m.get('WelcomeText')

        return self


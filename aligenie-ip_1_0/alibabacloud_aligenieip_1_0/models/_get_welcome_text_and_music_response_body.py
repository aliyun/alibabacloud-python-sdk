# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetWelcomeTextAndMusicResponseBody(DaraModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetWelcomeTextAndMusicResponseBodyResult = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extentions is not None:
            result['Extentions'] = self.extentions

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetWelcomeTextAndMusicResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class GetWelcomeTextAndMusicResponseBodyResult(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        music_url: str = None,
        text: str = None,
    ):
        self.hotel_id = hotel_id
        self.music_url = music_url
        self.text = text

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

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetDeviceStatusDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetDeviceStatusDetailResponseBodyResult = None,
    ):
        # Returned error code. 200 indicates that the invocation succeeded.
        self.code = code
        # Return Result of invoking this API.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned detailed information.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetDeviceStatusDetailResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetDeviceStatusDetailResponseBodyResult(DaraModel):
    def __init__(
        self,
        player: main_models.GetDeviceStatusDetailResponseBodyResultPlayer = None,
        power: main_models.GetDeviceStatusDetailResponseBodyResultPower = None,
        speaker: main_models.GetDeviceStatusDetailResponseBodyResultSpeaker = None,
    ):
        # Player information
        self.player = player
        # Battery information
        self.power = power
        # Volume information
        self.speaker = speaker

    def validate(self):
        if self.player:
            self.player.validate()
        if self.power:
            self.power.validate()
        if self.speaker:
            self.speaker.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.player is not None:
            result['Player'] = self.player.to_map()

        if self.power is not None:
            result['Power'] = self.power.to_map()

        if self.speaker is not None:
            result['Speaker'] = self.speaker.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Player') is not None:
            temp_model = main_models.GetDeviceStatusDetailResponseBodyResultPlayer()
            self.player = temp_model.from_map(m.get('Player'))

        if m.get('Power') is not None:
            temp_model = main_models.GetDeviceStatusDetailResponseBodyResultPower()
            self.power = temp_model.from_map(m.get('Power'))

        if m.get('Speaker') is not None:
            temp_model = main_models.GetDeviceStatusDetailResponseBodyResultSpeaker()
            self.speaker = temp_model.from_map(m.get('Speaker'))

        return self

class GetDeviceStatusDetailResponseBodyResultSpeaker(DaraModel):
    def __init__(
        self,
        muted: bool = None,
        volume: int = None,
    ):
        # Is muted
        self.muted = muted
        # Current volume value
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.muted is not None:
            result['Muted'] = self.muted

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Muted') is not None:
            self.muted = m.get('Muted')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class GetDeviceStatusDetailResponseBodyResultPower(DaraModel):
    def __init__(
        self,
        quantity: int = None,
        status: str = None,
    ):
        # Battery value
        self.quantity = quantity
        # Power status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetDeviceStatusDetailResponseBodyResultPlayer(DaraModel):
    def __init__(
        self,
        audio_album: str = None,
        audio_anchor: str = None,
        audio_ext: str = None,
        audio_id: str = None,
        audio_length: str = None,
        audio_name: str = None,
        audio_source: str = None,
        audio_url: str = None,
        format: str = None,
        progress: str = None,
        source: str = None,
        status: str = None,
        timestamp: str = None,
    ):
        # Song Album
        self.audio_album = audio_album
        # Artist
        self.audio_anchor = audio_anchor
        # Extension Information
        self.audio_ext = audio_ext
        # Audio ID
        self.audio_id = audio_id
        # Song length, in seconds
        self.audio_length = audio_length
        # Song Name
        self.audio_name = audio_name
        # Song Source (xiami)
        self.audio_source = audio_source
        # Song URL
        self.audio_url = audio_url
        # Song Type (mp3)
        self.format = format
        # Playback progress
        self.progress = progress
        # Playback Source (cloud)
        self.source = source
        # Playback status, pause
        self.status = status
        # Reporting Time
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_album is not None:
            result['AudioAlbum'] = self.audio_album

        if self.audio_anchor is not None:
            result['AudioAnchor'] = self.audio_anchor

        if self.audio_ext is not None:
            result['AudioExt'] = self.audio_ext

        if self.audio_id is not None:
            result['AudioId'] = self.audio_id

        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length

        if self.audio_name is not None:
            result['AudioName'] = self.audio_name

        if self.audio_source is not None:
            result['AudioSource'] = self.audio_source

        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url

        if self.format is not None:
            result['Format'] = self.format

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioAlbum') is not None:
            self.audio_album = m.get('AudioAlbum')

        if m.get('AudioAnchor') is not None:
            self.audio_anchor = m.get('AudioAnchor')

        if m.get('AudioExt') is not None:
            self.audio_ext = m.get('AudioExt')

        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')

        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')

        if m.get('AudioName') is not None:
            self.audio_name = m.get('AudioName')

        if m.get('AudioSource') is not None:
            self.audio_source = m.get('AudioSource')

        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self


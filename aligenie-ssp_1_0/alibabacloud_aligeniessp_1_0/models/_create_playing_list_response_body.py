# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class CreatePlayingListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CreatePlayingListResponseBodyResult = None,
        success: str = None,
    ):
        # Return code of the invocation
        self.code = code
        # Additional information, typically used to briefly describe a failed invocation to help the caller troubleshoot the issue.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Actual return result of the service
        self.result = result
        # Indicates whether the invocation succeeded. true indicates success, and false indicates failure. When the value is false, check the Message field for details.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

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
            temp_model = main_models.CreatePlayingListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreatePlayingListResponseBodyResult(DaraModel):
    def __init__(
        self,
        album_name: str = None,
        album_raw_id: str = None,
        audio_length: int = None,
        copyright: int = None,
        cover: main_models.CreatePlayingListResponseBodyResultCover = None,
        default_play_order: int = None,
        item_url: str = None,
        liked: bool = None,
        lyric_url: str = None,
        play_mode: str = None,
        pos: int = None,
        progress: int = None,
        raw_id: str = None,
        singer: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        # Third-party album name
        self.album_name = album_name
        # Third-party album ID
        self.album_raw_id = album_raw_id
        # Length
        self.audio_length = audio_length
        # The copyright field is upgraded to indicate whether the content is playable: 0 means playable, 1 or 2 means not playable.
        self.copyright = copyright
        # thumbnail image object
        self.cover = cover
        # Default playback order of the package: 0 for sequential, 1 for reverse.
        self.default_play_order = default_play_order
        # Playback URL
        self.item_url = item_url
        # is collected
        self.liked = liked
        # Lyrics URL
        self.lyric_url = lyric_url
        # Playback pattern (Repeat, Shuffle, RepeatOne, Normal)
        self.play_mode = play_mode
        # Position of the item in the playlist
        self.pos = pos
        # Playback progress of the song
        self.progress = progress
        # third-party ID
        self.raw_id = raw_id
        # Author
        self.singer = singer
        # Source
        self.source = source
        # title
        self.title = title
        # type (such as music, program, joke, news, children_song, radio, etc.)
        self.type = type
        # Playback availability: VALID(10), UNKNOWN(20), NOT_VALID(30)
        self.valid = valid

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.album_name is not None:
            result['AlbumName'] = self.album_name

        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id

        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length

        if self.copyright is not None:
            result['Copyright'] = self.copyright

        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order

        if self.item_url is not None:
            result['ItemUrl'] = self.item_url

        if self.liked is not None:
            result['Liked'] = self.liked

        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url

        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode

        if self.pos is not None:
            result['Pos'] = self.pos

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.raw_id is not None:
            result['RawId'] = self.raw_id

        if self.singer is not None:
            result['Singer'] = self.singer

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        if self.valid is not None:
            result['Valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')

        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')

        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')

        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')

        if m.get('Cover') is not None:
            temp_model = main_models.CreatePlayingListResponseBodyResultCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')

        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')

        if m.get('Liked') is not None:
            self.liked = m.get('Liked')

        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')

        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')

        if m.get('Pos') is not None:
            self.pos = m.get('Pos')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')

        if m.get('Singer') is not None:
            self.singer = m.get('Singer')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        return self

class CreatePlayingListResponseBodyResultCover(DaraModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        # Indicates whether OSS rules can be used for cropping.
        self.can_resize = can_resize
        # default image
        self.img = img
        # Large image
        self.large = large
        # Medium image
        self.mediam = mediam
        # medium image
        self.medium = medium
        # small image
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize

        if self.img is not None:
            result['Img'] = self.img

        if self.large is not None:
            result['Large'] = self.large

        if self.mediam is not None:
            result['Mediam'] = self.mediam

        if self.medium is not None:
            result['Medium'] = self.medium

        if self.small is not None:
            result['Small'] = self.small

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')

        if m.get('Img') is not None:
            self.img = m.get('Img')

        if m.get('Large') is not None:
            self.large = m.get('Large')

        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        if m.get('Small') is not None:
            self.small = m.get('Small')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GenerateVideoPlaylistResponseBody(DaraModel):
    def __init__(
        self,
        audio_playlist: List[main_models.GenerateVideoPlaylistResponseBodyAudioPlaylist] = None,
        duration: float = None,
        master_uri: str = None,
        request_id: str = None,
        subtitle_playlist: List[main_models.GenerateVideoPlaylistResponseBodySubtitlePlaylist] = None,
        token: str = None,
        video_playlist: List[main_models.GenerateVideoPlaylistResponseBodyVideoPlaylist] = None,
    ):
        # The audio media playlist files.
        self.audio_playlist = audio_playlist
        # The total duration of the generated video.
        self.duration = duration
        # The OSS path of the master playlist.
        self.master_uri = master_uri
        # The request ID.
        self.request_id = request_id
        # The subtitle media playlist files.
        self.subtitle_playlist = subtitle_playlist
        # The token of the master playlist.
        self.token = token
        # The video media playlist files.
        self.video_playlist = video_playlist

    def validate(self):
        if self.audio_playlist:
            for v1 in self.audio_playlist:
                 if v1:
                    v1.validate()
        if self.subtitle_playlist:
            for v1 in self.subtitle_playlist:
                 if v1:
                    v1.validate()
        if self.video_playlist:
            for v1 in self.video_playlist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioPlaylist'] = []
        if self.audio_playlist is not None:
            for k1 in self.audio_playlist:
                result['AudioPlaylist'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.master_uri is not None:
            result['MasterURI'] = self.master_uri

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SubtitlePlaylist'] = []
        if self.subtitle_playlist is not None:
            for k1 in self.subtitle_playlist:
                result['SubtitlePlaylist'].append(k1.to_map() if k1 else None)

        if self.token is not None:
            result['Token'] = self.token

        result['VideoPlaylist'] = []
        if self.video_playlist is not None:
            for k1 in self.video_playlist:
                result['VideoPlaylist'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_playlist = []
        if m.get('AudioPlaylist') is not None:
            for k1 in m.get('AudioPlaylist'):
                temp_model = main_models.GenerateVideoPlaylistResponseBodyAudioPlaylist()
                self.audio_playlist.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MasterURI') is not None:
            self.master_uri = m.get('MasterURI')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.subtitle_playlist = []
        if m.get('SubtitlePlaylist') is not None:
            for k1 in m.get('SubtitlePlaylist'):
                temp_model = main_models.GenerateVideoPlaylistResponseBodySubtitlePlaylist()
                self.subtitle_playlist.append(temp_model.from_map(k1))

        if m.get('Token') is not None:
            self.token = m.get('Token')

        self.video_playlist = []
        if m.get('VideoPlaylist') is not None:
            for k1 in m.get('VideoPlaylist'):
                temp_model = main_models.GenerateVideoPlaylistResponseBodyVideoPlaylist()
                self.video_playlist.append(temp_model.from_map(k1))

        return self

class GenerateVideoPlaylistResponseBodyVideoPlaylist(DaraModel):
    def __init__(
        self,
        frame_rate: str = None,
        resolution: str = None,
        token: str = None,
        uri: str = None,
    ):
        # The video frame rate.
        self.frame_rate = frame_rate
        # The video resolution.
        self.resolution = resolution
        # The token of the video media playlist. You can use this parameter to generate the path of a TS file.
        # 
        # >  You can generate the path of a transcoded TS file based on the value of this parameter. The path must be in the oss://${Bucket}/${Object}-${Token}-${Index}.ts format. oss://${Bucket}/${Object} specifies the URI specified by input parameters for output files. ${Token} specifies the returned token, and ${Index} specifies the serial number of a TS file.
        self.token = token
        # The OSS path of the video media playlist.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.token is not None:
            result['Token'] = self.token

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

class GenerateVideoPlaylistResponseBodySubtitlePlaylist(DaraModel):
    def __init__(
        self,
        index: int = None,
        language: str = None,
        token: str = None,
        uri: str = None,
    ):
        # The serial number of the subtitle stream. The value starts from 0.
        self.index = index
        # The language of the subtitle stream.
        # 
        # >  The language is derived from the subtitle stream information in the OSS path specified by the SourceURI parameter for a source video. If no language information exists in the source video, null is returned.
        self.language = language
        # The token of the subtitle media playlist. You can use this parameter to generate the path of a subtitle file.
        # 
        # >  You can generate the path of a transcoded subtitle file based on the returned token value. The path must be in the oss://${Bucket}/${Object}-${Token}_${Index}.ts format. oss://${Bucket}/${Object} specifies the URI specified by input parameters for output files. ${Token} specifies the returned token value, and ${Index} specifies the serial number of a subtitle file.
        self.token = token
        # The OSS path of the subtitle media playlist.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.language is not None:
            result['Language'] = self.language

        if self.token is not None:
            result['Token'] = self.token

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

class GenerateVideoPlaylistResponseBodyAudioPlaylist(DaraModel):
    def __init__(
        self,
        channels: int = None,
        token: str = None,
        uri: str = None,
    ):
        # The number of audio channels.
        self.channels = channels
        # The token of the audio media playlist. You can use this parameter to generate the path of a TS file.
        self.token = token
        # The OSS path of the audio media playlist.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels

        if self.token is not None:
            result['Token'] = self.token

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self


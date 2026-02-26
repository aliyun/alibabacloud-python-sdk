# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DetectMediaMetaResponseBody(DaraModel):
    def __init__(
        self,
        addresses: List[main_models.Address] = None,
        album: str = None,
        album_artist: str = None,
        artist: str = None,
        audio_streams: List[main_models.AudioStream] = None,
        bitrate: int = None,
        composer: str = None,
        duration: float = None,
        format_long_name: str = None,
        format_name: str = None,
        language: str = None,
        lat_long: str = None,
        performer: str = None,
        produce_time: str = None,
        program_count: int = None,
        request_id: str = None,
        size: int = None,
        start_time: float = None,
        stream_count: int = None,
        subtitles: List[main_models.SubtitleStream] = None,
        title: str = None,
        video_height: int = None,
        video_streams: List[main_models.VideoStream] = None,
        video_width: int = None,
    ):
        # The addresses.
        # 
        # This parameter is returned only when address information is detected.
        self.addresses = addresses
        # The album.
        self.album = album
        # The album artist.
        self.album_artist = album_artist
        # The artist.
        self.artist = artist
        # The audio streams.
        self.audio_streams = audio_streams
        # The bitrate. Unit: bit/s.
        self.bitrate = bitrate
        # The composer.
        self.composer = composer
        # The total duration of the video. Unit: seconds.
        self.duration = duration
        # The full format name.
        self.format_long_name = format_long_name
        # The abbreviated format name.
        self.format_name = format_name
        # The language of the content. For more information, see the ISO 639-2 Alpha-3 codes for the representation of names of languages.
        self.language = language
        # The coordinate pair of the central point. The coordinate pair consists of latitude and longitude values. This parameter value must be in the "latitude,longitude" format. Valid values of the latitude: [-90,+90]. Valid values of the longitude: [-180,+180].
        self.lat_long = lat_long
        # The performer.
        self.performer = performer
        # The time of recording. For more information about the time formats, see the RFC3339 Nano standard.
        self.produce_time = produce_time
        # The number of programs.
        self.program_count = program_count
        # The request ID.
        self.request_id = request_id
        # The size of the media object. Unit: bytes.
        self.size = size
        # The initial playback time.
        self.start_time = start_time
        # The number of media streams.
        self.stream_count = stream_count
        # The subtitle streams.
        self.subtitles = subtitles
        # The title of the media object.
        self.title = title
        # The video height in pixels.
        self.video_height = video_height
        # The video streams.
        self.video_streams = video_streams
        # The video width in pixels.
        self.video_width = video_width

    def validate(self):
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()
        if self.audio_streams:
            for v1 in self.audio_streams:
                 if v1:
                    v1.validate()
        if self.subtitles:
            for v1 in self.subtitles:
                 if v1:
                    v1.validate()
        if self.video_streams:
            for v1 in self.video_streams:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addresses'] = []
        if self.addresses is not None:
            for k1 in self.addresses:
                result['Addresses'].append(k1.to_map() if k1 else None)

        if self.album is not None:
            result['Album'] = self.album

        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist

        if self.artist is not None:
            result['Artist'] = self.artist

        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k1 in self.audio_streams:
                result['AudioStreams'].append(k1.to_map() if k1 else None)

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.composer is not None:
            result['Composer'] = self.composer

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name

        if self.format_name is not None:
            result['FormatName'] = self.format_name

        if self.language is not None:
            result['Language'] = self.language

        if self.lat_long is not None:
            result['LatLong'] = self.lat_long

        if self.performer is not None:
            result['Performer'] = self.performer

        if self.produce_time is not None:
            result['ProduceTime'] = self.produce_time

        if self.program_count is not None:
            result['ProgramCount'] = self.program_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count

        result['Subtitles'] = []
        if self.subtitles is not None:
            for k1 in self.subtitles:
                result['Subtitles'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        if self.video_height is not None:
            result['VideoHeight'] = self.video_height

        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k1 in self.video_streams:
                result['VideoStreams'].append(k1.to_map() if k1 else None)

        if self.video_width is not None:
            result['VideoWidth'] = self.video_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k1 in m.get('Addresses'):
                temp_model = main_models.Address()
                self.addresses.append(temp_model.from_map(k1))

        if m.get('Album') is not None:
            self.album = m.get('Album')

        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')

        if m.get('Artist') is not None:
            self.artist = m.get('Artist')

        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k1 in m.get('AudioStreams'):
                temp_model = main_models.AudioStream()
                self.audio_streams.append(temp_model.from_map(k1))

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Composer') is not None:
            self.composer = m.get('Composer')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')

        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LatLong') is not None:
            self.lat_long = m.get('LatLong')

        if m.get('Performer') is not None:
            self.performer = m.get('Performer')

        if m.get('ProduceTime') is not None:
            self.produce_time = m.get('ProduceTime')

        if m.get('ProgramCount') is not None:
            self.program_count = m.get('ProgramCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')

        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.SubtitleStream()
                self.subtitles.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')

        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k1 in m.get('VideoStreams'):
                temp_model = main_models.VideoStream()
                self.video_streams.append(temp_model.from_map(k1))

        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')

        return self


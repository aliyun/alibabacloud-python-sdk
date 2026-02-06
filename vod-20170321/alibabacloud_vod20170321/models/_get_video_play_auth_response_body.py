# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetVideoPlayAuthResponseBody(DaraModel):
    def __init__(
        self,
        play_auth: str = None,
        request_id: str = None,
        video_meta: main_models.GetVideoPlayAuthResponseBodyVideoMeta = None,
    ):
        # The credential for media playback.
        self.play_auth = play_auth
        # The ID of the request.
        self.request_id = request_id
        # The metadata of the audio or video file.
        self.video_meta = video_meta

    def validate(self):
        if self.video_meta:
            self.video_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.play_auth is not None:
            result['PlayAuth'] = self.play_auth

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.video_meta is not None:
            result['VideoMeta'] = self.video_meta.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlayAuth') is not None:
            self.play_auth = m.get('PlayAuth')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VideoMeta') is not None:
            temp_model = main_models.GetVideoPlayAuthResponseBodyVideoMeta()
            self.video_meta = temp_model.from_map(m.get('VideoMeta'))

        return self

class GetVideoPlayAuthResponseBodyVideoMeta(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        duration: float = None,
        status: str = None,
        title: str = None,
        video_id: str = None,
    ):
        # The thumbnail URL of the media file.
        self.cover_url = cover_url
        # The duration of the media file. Unit: seconds.
        self.duration = duration
        # The status of the media file. For more information about the value range and description, see [Status: the status of a video](~~52839#title-vqg-8cz-7p8~~).
        self.status = status
        # The title of the media file.
        self.title = title
        # The ID of the media file.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self


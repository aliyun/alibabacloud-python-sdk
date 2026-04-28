# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStoryRequest(DaraModel):
    def __init__(
        self,
        cover_image_thumbnail_process: str = None,
        cover_video_thumbnail_process: str = None,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        story_id: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        self.cover_image_thumbnail_process = cover_image_thumbnail_process
        self.cover_video_thumbnail_process = cover_video_thumbnail_process
        # This parameter is required.
        self.drive_id = drive_id
        self.image_thumbnail_process = image_thumbnail_process
        self.image_url_process = image_url_process
        # This parameter is required.
        self.story_id = story_id
        self.url_expire_sec = url_expire_sec
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_image_thumbnail_process is not None:
            result['cover_image_thumbnail_process'] = self.cover_image_thumbnail_process

        if self.cover_video_thumbnail_process is not None:
            result['cover_video_thumbnail_process'] = self.cover_video_thumbnail_process

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process

        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process

        if self.story_id is not None:
            result['story_id'] = self.story_id

        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec

        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_image_thumbnail_process') is not None:
            self.cover_image_thumbnail_process = m.get('cover_image_thumbnail_process')

        if m.get('cover_video_thumbnail_process') is not None:
            self.cover_video_thumbnail_process = m.get('cover_video_thumbnail_process')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')

        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')

        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')

        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')

        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')

        return self


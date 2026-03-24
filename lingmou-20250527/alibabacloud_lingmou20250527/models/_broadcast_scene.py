# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BroadcastScene(DaraModel):
    def __init__(
        self,
        clip_info: str = None,
        cover_url: str = None,
        create_time: str = None,
        download_url: str = None,
        id: str = None,
        modified_time: str = None,
        name: str = None,
        preview_url: str = None,
        ratio: str = None,
        remain_seconds: int = None,
        short_video_url: str = None,
        status: str = None,
        thumbnail_url: str = None,
        version: int = None,
    ):
        self.clip_info = clip_info
        self.cover_url = cover_url
        self.create_time = create_time
        self.download_url = download_url
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.preview_url = preview_url
        self.ratio = ratio
        self.remain_seconds = remain_seconds
        self.short_video_url = short_video_url
        self.status = status
        self.thumbnail_url = thumbnail_url
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clip_info is not None:
            result['clipInfo'] = self.clip_info

        if self.cover_url is not None:
            result['coverURL'] = self.cover_url

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.download_url is not None:
            result['downloadURL'] = self.download_url

        if self.id is not None:
            result['id'] = self.id

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.name is not None:
            result['name'] = self.name

        if self.preview_url is not None:
            result['previewURL'] = self.preview_url

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.remain_seconds is not None:
            result['remainSeconds'] = self.remain_seconds

        if self.short_video_url is not None:
            result['shortVideoURL'] = self.short_video_url

        if self.status is not None:
            result['status'] = self.status

        if self.thumbnail_url is not None:
            result['thumbnailURL'] = self.thumbnail_url

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clipInfo') is not None:
            self.clip_info = m.get('clipInfo')

        if m.get('coverURL') is not None:
            self.cover_url = m.get('coverURL')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('downloadURL') is not None:
            self.download_url = m.get('downloadURL')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('previewURL') is not None:
            self.preview_url = m.get('previewURL')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('remainSeconds') is not None:
            self.remain_seconds = m.get('remainSeconds')

        if m.get('shortVideoURL') is not None:
            self.short_video_url = m.get('shortVideoURL')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('thumbnailURL') is not None:
            self.thumbnail_url = m.get('thumbnailURL')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self


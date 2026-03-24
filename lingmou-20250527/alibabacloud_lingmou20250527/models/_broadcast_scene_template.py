# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BroadcastSceneTemplate(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        create_time: str = None,
        desc: str = None,
        id: str = None,
        modified_time: str = None,
        name: str = None,
        preview_url: str = None,
        ratio: str = None,
        short_video_url: str = None,
        tags: List[str] = None,
        thumbnail_url: str = None,
    ):
        self.cover_url = cover_url
        self.create_time = create_time
        self.desc = desc
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.preview_url = preview_url
        self.ratio = ratio
        self.short_video_url = short_video_url
        self.tags = tags
        self.thumbnail_url = thumbnail_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['coverURL'] = self.cover_url

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.desc is not None:
            result['desc'] = self.desc

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

        if self.short_video_url is not None:
            result['shortVideoURL'] = self.short_video_url

        if self.tags is not None:
            result['tags'] = self.tags

        if self.thumbnail_url is not None:
            result['thumbnailURL'] = self.thumbnail_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('coverURL') is not None:
            self.cover_url = m.get('coverURL')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

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

        if m.get('shortVideoURL') is not None:
            self.short_video_url = m.get('shortVideoURL')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('thumbnailURL') is not None:
            self.thumbnail_url = m.get('thumbnailURL')

        return self


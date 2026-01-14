# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InteractTextResponseBody(DaraModel):
    def __init__(
        self,
        end: bool = None,
        index: int = None,
        message: str = None,
        related_images: List[str] = None,
        related_videos: List[str] = None,
        session_id: str = None,
        type: int = None,
    ):
        self.end = end
        self.index = index
        self.message = message
        self.related_images = related_images
        self.related_videos = related_videos
        self.session_id = session_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['end'] = self.end

        if self.index is not None:
            result['index'] = self.index

        if self.message is not None:
            result['message'] = self.message

        if self.related_images is not None:
            result['relatedImages'] = self.related_images

        if self.related_videos is not None:
            result['relatedVideos'] = self.related_videos

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('relatedImages') is not None:
            self.related_images = m.get('relatedImages')

        if m.get('relatedVideos') is not None:
            self.related_videos = m.get('relatedVideos')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


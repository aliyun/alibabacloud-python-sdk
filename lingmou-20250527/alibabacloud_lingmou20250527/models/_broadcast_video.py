# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BroadcastVideo(DaraModel):
    def __init__(
        self,
        alignment_file_url: str = None,
        caption_url: str = None,
        cover_url: str = None,
        create_time: str = None,
        id: str = None,
        modified_time: str = None,
        name: str = None,
        status: str = None,
        video_url: str = None,
    ):
        self.alignment_file_url = alignment_file_url
        self.caption_url = caption_url
        self.cover_url = cover_url
        self.create_time = create_time
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.status = status
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alignment_file_url is not None:
            result['alignmentFileURL'] = self.alignment_file_url

        if self.caption_url is not None:
            result['captionURL'] = self.caption_url

        if self.cover_url is not None:
            result['coverURL'] = self.cover_url

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.id is not None:
            result['id'] = self.id

        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        if self.video_url is not None:
            result['videoURL'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignmentFileURL') is not None:
            self.alignment_file_url = m.get('alignmentFileURL')

        if m.get('captionURL') is not None:
            self.caption_url = m.get('captionURL')

        if m.get('coverURL') is not None:
            self.cover_url = m.get('coverURL')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('videoURL') is not None:
            self.video_url = m.get('videoURL')

        return self


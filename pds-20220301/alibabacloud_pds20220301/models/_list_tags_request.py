# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagsRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        video_thumbnail_process: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The method that is used to generate the thumbnail of an image.
        self.image_thumbnail_process = image_thumbnail_process
        # The method that is used to generate the thumbnail of a video.
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process

        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')

        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')

        return self


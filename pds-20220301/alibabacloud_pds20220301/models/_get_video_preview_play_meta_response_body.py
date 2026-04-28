# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class GetVideoPreviewPlayMetaResponseBody(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
        video_preview_play_meta: main_models.VideoPreviewPlayMeta = None,
    ):
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        self.file_id = file_id
        # The share ID.
        self.share_id = share_id
        # The preview metadata of the video.
        self.video_preview_play_meta = video_preview_play_meta

    def validate(self):
        if self.video_preview_play_meta:
            self.video_preview_play_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.video_preview_play_meta is not None:
            result['video_preview_play_meta'] = self.video_preview_play_meta.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('video_preview_play_meta') is not None:
            temp_model = main_models.VideoPreviewPlayMeta()
            self.video_preview_play_meta = temp_model.from_map(m.get('video_preview_play_meta'))

        return self


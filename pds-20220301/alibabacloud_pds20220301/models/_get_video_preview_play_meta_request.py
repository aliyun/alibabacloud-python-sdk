# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoPreviewPlayMetaRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
    ):
        # The preview type. You must enable the corresponding video transcoding feature. Valid values:
        # 
        # *   live_transcoding: previews a live stream while transcoding is in progress.
        # *   quick_video: previews a video while transcoding is in progress.
        # *   offline_audio: previews a piece of audio after the audio is transcoded offline.
        # *   offline_video: previews a video after the video is transcoded offline.
        # 
        # This parameter is required.
        self.category = category
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The share ID. If you want to manage a file by using a sharing link, carry the `x-share-token` header in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify at least either `share_id` or `drive_id`.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.share_id is not None:
            result['share_id'] = self.share_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        return self


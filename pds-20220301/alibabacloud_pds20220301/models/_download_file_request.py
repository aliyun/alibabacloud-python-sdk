# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadFileRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        image_thumbnail_process: str = None,
        office_thumbnail_process: str = None,
        share_id: str = None,
        video_thumbnail_process: str = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The method used to generate the thumbnail of an image. If this parameter is specified, you are redirected to the URL of the generated thumbnail.
        self.image_thumbnail_process = image_thumbnail_process
        # The method used to generate the thumbnail of a document. If this parameter is specified, you are redirected to the URL of the generated thumbnail.
        self.office_thumbnail_process = office_thumbnail_process
        # The share ID. If you want to manage a file by using a share link, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # The method used to generate the thumbnail of a video. If this parameter is specified, you are redirected to the URL of the generated thumbnail.
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

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process

        if self.office_thumbnail_process is not None:
            result['office_thumbnail_process'] = self.office_thumbnail_process

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')

        if m.get('office_thumbnail_process') is not None:
            self.office_thumbnail_process = m.get('office_thumbnail_process')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')

        return self

